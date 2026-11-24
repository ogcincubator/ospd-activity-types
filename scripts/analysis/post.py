#!/usr/bin/env python3
"""Inline analysis steps that sit between scan.py and the generator.

  post.py definitions <dir>   build definitions.csv from activity-types.csv
                              (definitions only; drops fixtures and rim:RegisterAction)
  post.py merge-dups <dir>    add the dup_groups column to mapping.csv from duplicates.csv
"""
import csv, collections, sys
mode, D = sys.argv[1], sys.argv[2]
if mode == "definitions":
    rows = [r for r in csv.DictReader(open(f"{D}/activity-types.csv")) if r["is_definition"] == "True"]
    keep = [r for r in rows if "fixture" not in r["iri"].lower() and not r["iri"].endswith("/rim/RegisterAction")]
    cols = ["iri", "name", "description", "broader", "related", "version", "citation", "url", "in_register", "repos"]
    w = csv.writer(open(f"{D}/definitions.csv", "w", newline=""))
    w.writerow(cols)
    for r in sorted(keep, key=lambda r: r["iri"]):
        w.writerow([r[c] for c in cols])
    print(len(rows), "definitions,", len(keep), "after exclusions")
elif mode == "merge-dups":
    m = list(csv.DictReader(open(f"{D}/mapping.csv")))
    d = collections.defaultdict(list)
    for r in csv.DictReader(open(f"{D}/duplicates.csv")):
        d[r["iri"]].append(r)
    cols = [c for c in m[0].keys() if c != "dup_groups"] + ["dup_groups"]
    for r in m:
        r["dup_groups"] = " ; ".join(f"{x['group_id']}:{x['role']}:{x['confidence']}" for x in d.get(r["old_iri"], []))
    w = csv.DictWriter(open(f"{D}/mapping.csv", "w", newline=""), fieldnames=cols)
    w.writeheader(); w.writerows(m)
