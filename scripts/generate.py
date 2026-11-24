#!/usr/bin/env python3
"""Generate the family Turtle data resources and the root concept scheme.

Usage: generate.py <repos-dir> [<analysis-dir>]

Reads the source Turtle files in <repos-dir> (clones of the OSPD repositories) and the analysis tables
(mapping.csv, family-assignment.csv, duplicates.csv) and writes, under _sources/:
  core/data.ttl                    root concept scheme, catalog and family collections
  <family>/data.ttl                one data resource per family

Vocabulary: SKOS (no schema.org). Everything is derived from the tables, so rerun after editing them.
"""
import csv, os, sys, collections
from rdflib import Graph, URIRef, Literal, BNode, Namespace, RDF, RDFS, OWL, XSD
from rdflib.namespace import SKOS, DCTERMS, PROV, FOAF

REPOS = sys.argv[1]
AN = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(__file__), "..", "analysis")
OUT = os.path.join(os.path.dirname(__file__), "..", "_sources")
BASE = "https://w3id.org/ogc/ospd/activity-type/"
SCHEMA = Namespace("https://schema.org/")
ACTTYPE = Namespace("https://w3id.org/ogc/rim/activity-type/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
ROOT = URIRef(BASE)
CATALOG = URIRef(BASE + "catalog")
FAMILY_NS = BASE + "families/"

rd = lambda f: list(csv.DictReader(open(os.path.join(AN, f))))
fam_rows = rd("family-assignment.csv")
mapping = {r["old_iri"]: r for r in rd("mapping.csv")}
dups = rd("duplicates.csv")

# union graph of all source Turtle (fixtures excluded)
g = Graph()
for dp, dn, fn in os.walk(REPOS):
    dn[:] = [d for d in dn if d not in (".git", "_scan")]
    for f in fn:
        if f.endswith(".ttl"):
            try:
                g.parse(os.path.join(dp, f), format="turtle")
            except Exception:
                pass

defs = [r for r in fam_rows if r["kind"] in ("kept", "renamed-collision", "review") and r["family"]]
new_of = {r["old_iri"]: r["new_iri"] for r in fam_rows if r["new_iri"]}
for old, m in mapping.items():  # aliases resolve to the canonical new IRI
    if m["kind"] == "alias" and m["new_iri"]:
        new_of[old] = m["new_iri"]
in_set = {r["old_iri"] for r in defs}
family_of = {r["old_iri"]: r["family"] for r in defs}

def first_node(node, preds):
    for p in preds:
        for v in g.objects(node, p):
            if isinstance(v, Literal):
                return v
    return None

def first(subj, preds):
    for p in preds:
        vals = sorted(g.objects(URIRef(subj), p), key=str)
        vals = [v for v in vals if isinstance(v, Literal) and (v.language in (None, "en"))]
        if vals:
            return vals[0]
    return None

aliases = collections.defaultdict(list)
for old, m in mapping.items():
    if m["kind"] == "alias" and m["canonical_old_iri"]:
        aliases[m["canonical_old_iri"]].append(old)
closematch = collections.defaultdict(set)
by_group = collections.defaultdict(list)
for r in dups:
    by_group[r["group_id"]].append(r)
for gid, rs in by_group.items():
    canon = [r["iri"] for r in rs if r["role"] == "canonical"]
    for r in rs:
        if r["role"] == "duplicate" and r["confidence"] in ("high", "medium") and canon:
            closematch[r["iri"]].add(canon[0])

report = collections.defaultdict(list)
per_family = collections.defaultdict(Graph)

def bind(gr):
    for p, n in (("skos", SKOS), ("dcterms", DCTERMS), ("owl", OWL), ("rdfs", RDFS), ("prov", PROV),
                 ("dcat", DCAT), ("foaf", FOAF), ("acttype", ACTTYPE), ("ospd", Namespace(BASE))):
        gr.bind(p, n)

for r in sorted(defs, key=lambda r: r["new_iri"]):
    old, fam = r["old_iri"], r["family"]
    s = URIRef(r["new_iri"])
    out = per_family[fam]
    out.add((s, RDF.type, SKOS.Concept))
    out.add((s, RDF.type, ACTTYPE.ActivityType))
    out.add((s, SKOS.inScheme, ROOT))
    label = first(old, [SKOS.prefLabel, SCHEMA.name, RDFS.label, DCTERMS.title])
    if label is None:
        label = Literal(r["new_iri"].rsplit("/", 1)[1].replace("-", " "), lang="en")
        report["no label (derived from slug)"].append(old)
    out.add((s, SKOS.prefLabel, Literal(str(label), lang="en")))
    d = first(old, [SKOS.definition, SCHEMA.description, RDFS.comment, DCTERMS.description])
    if d is not None:
        out.add((s, SKOS.definition, Literal(str(d), lang="en")))
    else:
        report["no definition"].append(old)
    v = first(old, [SCHEMA.version, OWL.versionInfo])
    if v is not None: out.add((s, OWL.versionInfo, Literal(str(v))))
    m = first(old, [SCHEMA.dateModified, DCTERMS.modified])
    if m is not None: out.add((s, DCTERMS.modified, Literal(str(m), datatype=XSD.date)))
    for p in (SCHEMA.citation, DCTERMS.source):
        for o in g.objects(URIRef(old), p):
            out.add((s, DCTERMS.source, o))
    for p in (SCHEMA.url, RDFS.seeAlso):
        for o in g.objects(URIRef(old), p):
            out.add((s, RDFS.seeAlso, o))
    seen_attr = set()
    for qa in g.objects(URIRef(old), PROV.qualifiedAttribution):
        agent = g.value(qa, PROV.agent)
        role = g.value(qa, PROV.hadRole)
        if agent is None or role is None:
            continue
        name = None
        if isinstance(agent, BNode):  # agent described inline: keep its name only (no email addresses)
            nm = first_node(agent, [SCHEMA.name, RDFS.label, FOAF.name])
            name = str(nm) if nm is not None else None
        key = (str(agent) if not isinstance(agent, BNode) else name, str(role))
        if key in seen_attr:
            continue
        seen_attr.add(key)
        b = BNode()
        if isinstance(agent, BNode):
            a = BNode()
            if name:
                out.add((a, FOAF.name, Literal(name)))
            out.add((b, PROV.agent, a))
        else:
            out.add((b, PROV.agent, agent))
            if str(agent).startswith("http://ospd/demo/"):
                report["agent IRI under http://ospd/demo/ (unresolvable)"].append(str(agent))
        out.add((b, PROV.hadRole, role))
        out.add((s, PROV.qualifiedAttribution, b))
    # hierarchy: in-set parents -> skos:broader; others kept as rdfs:subClassOf
    parents = set(g.objects(URIRef(old), SKOS.broader)) | set(g.objects(URIRef(old), RDFS.subClassOf))
    for p in sorted(parents, key=str):
        ps = str(p)
        if ps in new_of and ps in in_set:
            out.add((s, SKOS.broader, URIRef(new_of[ps])))
            if family_of.get(ps) != fam:
                report["cross-family broader"].append(f"{old} -> {ps}")
        elif ps in new_of:
            report["broader maps to a non-family item"].append(f"{old} -> {ps}")
        elif ps.startswith(("https://w3id.org/ogc/rim/geoprocessing/", "https://w3id.org/ogc/rim/ml-activity/")):
            out.add((s, RDFS.subClassOf, p))
        else:
            report["dropped parent (not an in-scope type)"].append(f"{old} -> {ps}")
    for p in sorted(g.objects(URIRef(old), SKOS.related), key=str):
        if str(p) in new_of:
            out.add((s, SKOS.related, URIRef(new_of[str(p)])))
    out.add((s, DCTERMS.replaces, URIRef(old)))
    for a in sorted(aliases.get(old, [])):
        out.add((s, SKOS.exactMatch, URIRef(a)))
    for c in sorted(closematch.get(old, [])):
        if c in new_of:
            out.add((s, SKOS.closeMatch, URIRef(new_of[c])))

# root: concept scheme, catalog, family collections
root = Graph(); bind(root)
root.add((ROOT, RDF.type, SKOS.ConceptScheme))
root.add((ROOT, SKOS.prefLabel, Literal("OSPD Activity Types", lang="en")))
root.add((ROOT, SKOS.definition, Literal(
    "Activity types used across the OGC Open Science Persistent Demonstrator (OSPD), consolidated under stable URIs "
    "and grouped into families of related types.", lang="en")))
root.add((CATALOG, RDF.type, DCAT.Catalog))
root.add((CATALOG, DCTERMS.title, Literal("OSPD Activity Types", lang="en")))
root.add((CATALOG, DCTERMS.description, Literal("Catalog of the OSPD activity types and their families.", lang="en")))
root.add((CATALOG, DCTERMS.hasPart, ROOT))
for fam in sorted(per_family):
    c = URIRef(FAMILY_NS + fam)
    root.add((c, RDF.type, SKOS.Collection))
    root.add((c, SKOS.prefLabel, Literal(fam.replace("-", " ").capitalize(), lang="en")))
    root.add((c, SKOS.inScheme, ROOT)) if False else None
    for r in defs:
        if r["family"] == fam:
            root.add((c, SKOS.member, URIRef(r["new_iri"])))
    for r in defs:  # top concepts: no in-scheme parent
        if r["family"] == fam and not any(str(p) in in_set for p in g.objects(URIRef(r["old_iri"]), SKOS.broader)) \
                and not any(str(p) in in_set for p in g.objects(URIRef(r["old_iri"]), RDFS.subClassOf)):
            root.add((ROOT, SKOS.hasTopConcept, URIRef(r["new_iri"])))
            root.add((URIRef(r["new_iri"]), SKOS.topConceptOf, ROOT))

def write(gr, path):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    bind(gr)
    gr.serialize(path, format="turtle")

write(root, os.path.join(OUT, "core", "data.ttl"))
for fam, gr in per_family.items():
    write(gr, os.path.join(OUT, fam, "data.ttl"))
print({f: len(set(gr.subjects(RDF.type, SKOS.Concept))) for f, gr in sorted(per_family.items())})
for k, v in report.items():
    print(f"\n{k}: {len(v)}")
    for x in v[:12]:
        print("  ", x.replace("https://w3id.org/geolabs/ospd/", "GL:").replace("http://ospd/demo/", ""))
