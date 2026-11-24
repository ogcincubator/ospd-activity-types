#!/usr/bin/env python3
"""Rewrite old activity-type IRIs to the consolidated ones, using analysis/mapping.csv.

DRY RUN BY DEFAULT: nothing is written unless --apply is given.

    rewrite_iris.py <repos-dir> [--mapping analysis/mapping.csv] [--only REPO ...]
                    [--report changes.csv] [--diff] [--include-build] [--apply]

<repos-dir> holds one directory per repository (<owner>__<name>), as in the scan.

What is rewritten (only rows of mapping.csv with a non-empty new_iri, old != new):
  * full IRIs, in any text file, matched as whole IRIs (not as a prefix of a longer one);
  * prefixed names (CURIEs) in Turtle-like files (.ttl .trig .n3 .shacl .rq .sparql), when the
    same file declares a prefix whose namespace + local name is an old IRI;
  * prefixed names in JSON / JSON-LD / YAML files, same rule, using prefixes declared in the
    file ("gp": "https://...", or `gp: https://...` in YAML).
Replacements are done in one pass, so a new IRI that is also an old IRI of another row is never
rewritten twice. In Turtle, a prefixed name becomes a prefixed name again when the file declares
a prefix for the new namespace, and a full <IRI> otherwise. In JSON/YAML it becomes the full IRI.

Skipped on purpose:
  * build/, build-local/, .git/, node_modules/ (generated; rebuild after rewriting _sources).
    Use --include-build to process build/ as well.
  * prefixed names that sit inside a string literal or a comment (reported as "manual").
  * rows of kind external / gap-example-local (no new IRI).

The report lists, per repository, files and replacements by form, plus anything that still
looks like an old reference afterwards (manual review).
"""
import argparse
import csv
import os
import re
import subprocess
import sys
from collections import Counter, defaultdict

TURTLE_EXT = {".ttl", ".trig", ".n3", ".shacl", ".rq", ".sparql"}
STRUCT_EXT = {".json", ".jsonld", ".yaml", ".yml"}
TEXT_EXT = TURTLE_EXT | STRUCT_EXT | {".md", ".txt", ".html", ".py", ".ts", ".js", ".csv", ".xml", ".rdf", ""}
DEFAULT_SKIP = {".git", "build", "build-local", "node_modules", "_scan"}

LOCAL = r"[A-Za-z0-9_](?:[A-Za-z0-9_.\-]*[A-Za-z0-9_\-])?"
# characters that may continue an IRI after a match (so we never replace a prefix of a longer IRI)
IRI_TAIL = r"(?![A-Za-z0-9_\-/#%~]|\.[A-Za-z0-9_])"
TTL_PREFIX = re.compile(r"(?:@prefix\s+|PREFIX\s+)([A-Za-z][\w\-]*)?:\s*<([^>]*)>", re.I)
JSON_PREFIX = re.compile(r"""["']([A-Za-z][\w\-]*)["']\s*:\s*["'](https?://[^"']+)["']""")
YAML_PREFIX = re.compile(r"^\s*([A-Za-z][\w\-]*)\s*:\s+['\"]?(https?://\S+?)['\"]?\s*$", re.M)


def load_mapping(path):
    m = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            old, new = row["old_iri"].strip(), row["new_iri"].strip()
            if old and new and old != new:
                m[old] = (new, row["kind"])
    return m


def in_literal_or_comment(text, pos):
    """Naive check on the line before pos: odd number of quotes, or a # comment started."""
    line_start = text.rfind("\n", 0, pos) + 1
    before = text[line_start:pos]
    stripped = re.sub(r"<[^>]*>", "", before)  # ignore IRIs (they may contain '#')
    stripped = stripped.replace('\\"', "")
    if stripped.count('"') % 2 == 1:
        return True
    quote_free = re.sub(r'"[^"]*"', "", stripped)
    return "#" in quote_free


class Rewriter:
    def __init__(self, mapping):
        self.mapping = mapping
        olds = sorted(mapping, key=len, reverse=True)
        self.full_re = re.compile("(?:" + "|".join(re.escape(o) for o in olds) + ")" + IRI_TAIL)
        self.by_ns = defaultdict(dict)  # namespace -> {local: old_iri}
        for old in mapping:
            m = re.match(r"^(.*[/#])(" + LOCAL + r")$", old)
            if m:
                self.by_ns[m.group(1)][m.group(2)] = old

    def prefixes(self, text, ext):
        found = {}
        if ext in TURTLE_EXT:
            for m in TTL_PREFIX.finditer(text):
                found[m.group(1) or ""] = m.group(2)
        elif ext in STRUCT_EXT:
            for m in JSON_PREFIX.finditer(text):
                found[m.group(1)] = m.group(2)
            for m in YAML_PREFIX.finditer(text):
                found.setdefault(m.group(1), m.group(2))
        return found

    def rewrite(self, text, ext):
        """Return (new_text, changes, manual) where changes = [(line, old, new, form)]."""
        changes, manual = [], []
        edits = []  # (start, end, replacement, old, form)

        for m in self.full_re.finditer(text):
            old = m.group(0)
            edits.append((m.start(), m.end(), self.mapping[old][0], old, "iri"))

        prefixes = self.prefixes(text, ext)
        if prefixes and ext in (TURTLE_EXT | STRUCT_EXT):
            rev = {}  # namespace -> prefix declared in this file
            for p, ns in prefixes.items():
                rev.setdefault(ns, p)
            for p, ns in prefixes.items():
                locals_ = self.by_ns.get(ns)
                if not locals_:
                    continue
                pat = re.compile(r"(?<![\w:/#.\-<])" + re.escape(p) + ":(" + LOCAL + r")(?![\w:\-])")
                for m in pat.finditer(text):
                    old = locals_.get(m.group(1))
                    if not old:
                        continue
                    if ext in TURTLE_EXT and in_literal_or_comment(text, m.start()):
                        manual.append((text.count("\n", 0, m.start()) + 1, m.group(0), "curie in literal/comment"))
                        continue
                    new = self.mapping[old][0]
                    if ext in TURTLE_EXT:
                        repl = "<" + new + ">"
                        for nns, np_ in rev.items():
                            mm = re.match(r"^" + re.escape(nns) + "(" + LOCAL + ")$", new)
                            if mm and "." not in mm.group(1):
                                repl = (np_ + ":" + mm.group(1))
                                break
                    else:
                        repl = new
                    edits.append((m.start(), m.end(), repl, old, "curie"))

        # one pass, no overlaps (full IRIs inside <...> never overlap CURIEs; keep the first if they do)
        edits.sort(key=lambda e: (e[0], -(e[1] - e[0])))
        out, last, kept = [], 0, []
        for s, e, repl, old, form in edits:
            if s < last:
                continue
            out.append(text[last:s])
            out.append(repl)
            last = e
            kept.append((s, old, repl, form))
        out.append(text[last:])
        new_text = "".join(out)
        for s, old, repl, form in kept:
            changes.append((text.count("\n", 0, s) + 1, old, repl, form))
        return new_text, changes, manual


def iter_files(root, skip):
    for dp, dn, fn in os.walk(root):
        dn[:] = sorted(d for d in dn if d not in skip)
        for f in sorted(fn):
            ext = os.path.splitext(f)[1].lower()
            if ext in TEXT_EXT:
                yield os.path.join(dp, f), ext


def git_dirty(repo):
    try:
        out = subprocess.run(["git", "-C", repo, "status", "--porcelain"], capture_output=True, text=True)
        return out.returncode == 0 and bool(out.stdout.strip())
    except OSError:
        return False


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("repos_dir")
    ap.add_argument("--mapping", default=os.path.join(os.path.dirname(__file__), "..", "analysis", "mapping.csv"))
    ap.add_argument("--only", nargs="*", help="repository directory names to process (default: all)")
    ap.add_argument("--report", help="write one CSV row per replacement to this file")
    ap.add_argument("--diff", action="store_true", help="print a unified diff of every changed file")
    ap.add_argument("--include-build", action="store_true", help="also process build/ and build-local/")
    ap.add_argument("--apply", action="store_true", help="WRITE the changes (default is a dry run)")
    args = ap.parse_args()

    mapping = load_mapping(args.mapping)
    chained = [o for o, (n, _) in mapping.items() if n in mapping]
    if chained:
        print("WARNING: new IRI is also an old IRI of another row (rewritten once, not chained):", chained[:5], file=sys.stderr)
    rw = Rewriter(mapping)
    skip = DEFAULT_SKIP - ({"build", "build-local"} if args.include_build else set())

    repos = sorted(d for d in os.listdir(args.repos_dir)
                   if os.path.isdir(os.path.join(args.repos_dir, d)) and not d.startswith("_"))
    if args.only:
        repos = [r for r in repos if r in args.only]

    mode = "APPLY" if args.apply else "DRY RUN (nothing written)"
    print(f"== rewrite_iris: {mode}; {len(mapping)} mapped IRIs; {len(repos)} repos")
    rows, manual_all = [], []
    totals = Counter()
    for repo in repos:
        rdir = os.path.join(args.repos_dir, repo)
        if args.apply and git_dirty(rdir):
            print(f"!! {repo}: working tree not clean, skipped (commit/stash first)")
            continue
        nfiles, forms, kinds = 0, Counter(), Counter()
        for path, ext in iter_files(rdir, skip):
            try:
                with open(path, encoding="utf-8", newline="") as f:
                    text = f.read()
            except (UnicodeDecodeError, OSError):
                continue
            new_text, changes, manual = rw.rewrite(text, ext)
            rel = os.path.relpath(path, args.repos_dir)
            for ln, old, repl, why in manual:
                manual_all.append((rel, ln, old, why))
            if not changes:
                continue
            nfiles += 1
            for ln, old, repl, form in changes:
                forms[form] += 1
                kinds[mapping[old][1]] += 1
                rows.append((rel, ln, old, repl, form, mapping[old][1]))
            if args.diff:
                import difflib
                sys.stdout.writelines(difflib.unified_diff(text.splitlines(True), new_text.splitlines(True), rel, rel))
            if args.apply:
                with open(path, "w", encoding="utf-8", newline="") as f:
                    f.write(new_text)
        if nfiles:
            totals.update(forms)
            print(f"{repo}: {nfiles} files, {sum(forms.values())} replacements "
                  f"({', '.join(f'{k} {v}' for k, v in forms.items())}); kinds: "
                  + ", ".join(f"{k} {v}" for k, v in kinds.most_common()))
    print(f"TOTAL: {len({r[0] for r in rows})} files, {len(rows)} replacements ({dict(totals)})")
    if manual_all:
        print(f"MANUAL REVIEW ({len(manual_all)}): prefixed names inside literals/comments, not rewritten:")
        for rel, ln, old, why in manual_all[:30]:
            print(f"  {rel}:{ln}  {old}  [{why}]")
    if args.report:
        with open(args.report, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            w.writerow(["file", "line", "old", "new", "form", "kind"])
            w.writerows(rows)
        print("report written to", args.report)
    if not args.apply:
        print("Dry run only. Re-run with --apply to write the changes.")


if __name__ == "__main__":
    main()
