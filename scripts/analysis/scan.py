#!/usr/bin/env python3
"""Scan cloned OSPD repos (Turtle only) for activity-type definitions and references."""
import csv, os, re, sys, json
from collections import defaultdict
from rdflib import Graph, URIRef, Literal, BNode, RDF, RDFS, OWL, Namespace
from rdflib.namespace import SKOS

ROOT = sys.argv[1]
OUT = sys.argv[2]
os.makedirs(OUT, exist_ok=True)

PROV = Namespace("http://www.w3.org/ns/prov#")
SH = Namespace("http://www.w3.org/ns/shacl#")
SCHEMA = Namespace("https://schema.org/")
ACTTYPE_CLASS = URIRef("https://w3id.org/ogc/rim/activity-type/ActivityType")
PROV_BUILTIN_RANGE_ACTIVITY = {PROV.wasGeneratedBy, PROV.wasInvalidatedBy, PROV.wasInformedBy,
                               PROV.activity, PROV.hadActivity}
IGNORED_TYPE_NS = ("http://www.w3.org/ns/prov#", "http://www.w3.org/2002/07/owl#",
                   "http://www.w3.org/2000/01/rdf-schema#", "http://www.w3.org/ns/shacl#",
                   "http://www.w3.org/2004/02/skos/core#")
KNOWN_SCHEMES = re.compile(
    r"(example\.org/ospd/process-types/[^/#]+$|"
    r"w3id\.org/geolabs/ospd/process-profiles/process-type/(?!.*/actions/)[^#]+$|"
    r"crim-ca\.github\.io/[^>\s]*/activity-type/[^/#]+$|"
    r"geolabs\.github\.io/bblocks-process-profiles/def/process-type/|"
    r"voyager\.ogc/prov/activity/|hartis\.org/ospd2026/activity-type/|"
    r"w3id\.org/ogc/rim/activity-type/[^/#]+$|w3id\.org/ogc/ospd/activity-type/|"
    r"http://ospd/demo/GA|demo:GA\d+)")

files = []
for dp, dn, fn in os.walk(ROOT):
    dn[:] = [d for d in dn if d != ".git"]
    for f in fn:
        if f.endswith(".ttl"):
            files.append(os.path.join(dp, f))
files.sort()

def repo_of(path):
    return os.path.relpath(path, ROOT).split(os.sep)[0]

def rel(path):
    return os.path.relpath(path, ROOT)

# ---- pass 1: parse and collect global schema information
subclass = defaultdict(set)
subprop = defaultdict(set)
range_decl = defaultdict(set)      # property -> ranges
types_of = defaultdict(set)        # subject -> types
failed = []
graphs = {}
for p in files:
    g = Graph()
    try:
        g.parse(p, format="turtle")
    except Exception as e:
        failed.append((rel(p), str(e)[:120]))
        continue
    graphs[p] = g
    for s, o in g.subject_objects(RDFS.subClassOf):
        if isinstance(s, URIRef) and isinstance(o, URIRef):
            subclass[s].add(o)
    for s, o in g.subject_objects(RDFS.subPropertyOf):
        if isinstance(s, URIRef) and isinstance(o, URIRef):
            subprop[s].add(o)
    for s, o in g.subject_objects(RDFS.range):
        if isinstance(s, URIRef) and isinstance(o, URIRef):
            range_decl[s].add(o)
    # SHACL property shapes: sh:path + sh:class
    for ps in g.subjects(SH["class"], None):
        for path in g.objects(ps, SH.path):
            if isinstance(path, URIRef):
                for c in g.objects(ps, SH["class"]):
                    if isinstance(c, URIRef):
                        range_decl[path].add(c)
    for s, o in g.subject_objects(RDF.type):
        if isinstance(s, URIRef) and isinstance(o, URIRef):
            types_of[s].add(o)

def closure_up(start, rel_map):
    seen = {start}
    stack = [start]
    while stack:
        x = stack.pop()
        for y in rel_map.get(x, ()):
            if y not in seen:
                seen.add(y)
                stack.append(y)
    return seen

# classes that are (transitively) subclasses of prov:Activity
activity_classes = {PROV.Activity}
changed = True
while changed:
    changed = False
    for c, sups in subclass.items():
        if c not in activity_classes and sups & activity_classes:
            activity_classes.add(c)
            changed = True
activity_like_ranges = activity_classes | {ACTTYPE_CLASS}

# classes that are (transitively) subclasses of acttype:ActivityType
type_classes = {ACTTYPE_CLASS}
changed = True
while changed:
    changed = False
    for c, sups in subclass.items():
        if c not in type_classes and sups & type_classes:
            type_classes.add(c)
            changed = True

def props_with_range(ranges, builtin=()):
    out = set(builtin)
    for prop in set(range_decl) | set(subprop):
        for anc in closure_up(prop, subprop):
            if range_decl.get(anc, set()) & ranges:
                out.add(prop)
                break
    return out

instance_range_props = props_with_range(activity_classes, PROV_BUILTIN_RANGE_ACTIVITY)
type_range_props = props_with_range(type_classes)
PROV_BUILTIN_DOMAIN_ACTIVITY = {PROV[x] for x in (
    "used", "generated", "invalidated", "startedAtTime", "endedAtTime", "wasStartedBy", "wasEndedBy",
    "wasAssociatedWith", "qualifiedAssociation", "qualifiedStart", "qualifiedEnd", "qualifiedUsage",
    "qualifiedCommunication", "wasInformedBy")}
domain_decl = defaultdict(set)
for g_ in graphs.values():
    for s_, o_ in g_.subject_objects(RDFS.domain):
        if isinstance(s_, URIRef) and isinstance(o_, URIRef):
            domain_decl[s_].add(o_)
domain_props = set(PROV_BUILTIN_DOMAIN_ACTIVITY)
for prop in set(domain_decl) | set(subprop):
    for anc in closure_up(prop, subprop):
        if domain_decl.get(anc, set()) & activity_classes:
            domain_props.add(prop)
            break
range_props = instance_range_props | type_range_props

# ---- pass 2: collect
recs = defaultdict(lambda: {"methods": set(), "repos": set(), "files": set(),
                            "is_def": False, "props": defaultdict(set)})
def note(iri, method, path):
    r = recs[str(iri)]
    r["methods"].add(method)
    r["repos"].add(repo_of(path))
    r["files"].add(rel(path))
    return r

untyped = {}
activity_instance = {s for s, ts in types_of.items() if ts & activity_classes}
# indirect: objects of activity-range props, subjects of activity-domain props
for g_ in graphs.values():
    for pred in instance_range_props:
        for o_ in g_.objects(None, pred):
            if isinstance(o_, (URIRef, BNode)):
                activity_instance.add(o_)
    for pred in domain_props:
        for s_ in g_.subjects(pred, None):
            if isinstance(s_, (URIRef, BNode)):
                activity_instance.add(s_)
for p, g in graphs.items():
    # definitions: acttype class items and subclasses of prov:Activity
    for s in set(g.subjects(RDF.type, ACTTYPE_CLASS)):
        if isinstance(s, URIRef):
            r = note(s, "def:acttype", p)
            r["is_def"] = True
            for pred, obj in g.predicate_objects(s):
                if pred in (SCHEMA.name, RDFS.label, SKOS.prefLabel, SCHEMA.description, RDFS.comment,
                            SKOS.definition, SCHEMA.version, SCHEMA.citation, SCHEMA.url):
                    r["props"][str(pred)].add(str(obj))
                elif pred in (SKOS.broader, SKOS.narrower, SKOS.related, SKOS.exactMatch,
                              SKOS.closeMatch, RDFS.subClassOf):
                    r["props"][str(pred)].add(str(obj))
                elif str(pred) == "https://w3id.org/ogc/rim/inRegister":
                    r["props"]["inRegister"].add(str(obj))
    for s, o in g.subject_objects(RDFS.subClassOf):
        if isinstance(s, URIRef) and s in activity_classes and s != PROV.Activity \
                and not str(s).startswith(IGNORED_TYPE_NS):
            r = note(s, "def:subclass-of-activity", p)
            r["is_def"] = True
            for pred in (RDFS.label, SKOS.prefLabel, RDFS.comment, SKOS.definition, SCHEMA.description):
                for obj in g.objects(s, pred):
                    r["props"][str(pred)].add(str(obj))
            r["props"][str(RDFS.subClassOf)].add(str(o))
    # references via rdf:type on activity instances
    for s, o in g.subject_objects(RDF.type):
        if isinstance(o, URIRef) and s in activity_instance and not str(o).startswith(IGNORED_TYPE_NS) \
                and o not in (ACTTYPE_CLASS,) and not (isinstance(s, URIRef) and s in activity_classes):
            note(o, "ref:type-on-activity", p)
    # references as objects of properties whose range is an activity type (class-valued)
    for pred in type_range_props:
        for s_, o in g.subject_objects(pred):
            if isinstance(o, URIRef):
                note(o, "ref:type-range-object", p)
    # activity instances referenced through activity-range props but with no type at all
    for pred in instance_range_props:
        for s_, o in g.subject_objects(pred):
            if isinstance(o, URIRef) and not types_of.get(o):
                untyped.setdefault(str(o), set()).add(rel(p))
    # cross-check: any IRI matching known schemes
    for t in g:
        for x in t:
            if isinstance(x, URIRef) and KNOWN_SCHEMES.search(str(x)):
                note(x, "xchk:known-scheme", p)

# ---- write outputs
def join(s):
    return " | ".join(sorted(s))

with open(os.path.join(OUT, "activity-types.csv"), "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["iri", "is_definition", "methods", "n_repos", "repos", "n_files", "example_file",
                "name", "description", "broader", "related", "version", "citation", "url", "in_register", "all_files"])
    for iri in sorted(recs):
        r = recs[iri]
        pr = r["props"]
        name = pr.get(str(SCHEMA.name)) or pr.get(str(RDFS.label)) or pr.get(str(SKOS.prefLabel)) or set()
        desc = pr.get(str(SCHEMA.description)) or pr.get(str(RDFS.comment)) or pr.get(str(SKOS.definition)) or set()
        broader = pr.get(str(SKOS.broader), set()) | pr.get(str(RDFS.subClassOf), set())
        w.writerow([iri, r["is_def"], join(r["methods"]), len(r["repos"]), join(r["repos"]),
                    len(r["files"]), sorted(r["files"])[0], join(name), join(desc), join(broader),
                    join(pr.get(str(SKOS.related), set())), join(pr.get(str(SCHEMA.version), set())),
                    join(pr.get(str(SCHEMA.citation), set())), join(pr.get(str(SCHEMA.url), set())),
                    join(pr.get("inRegister", set())), join(r["files"])])

with open(os.path.join(OUT, "range-properties.txt"), "w") as f:
    for p in sorted(map(str, instance_range_props)):
        f.write("instance-range\t" + p + "\n")
    for p in sorted(map(str, type_range_props)):
        f.write("type-range\t" + p + "\n")
with open(os.path.join(OUT, "untyped-activity-instances.txt"), "w") as f:
    for i in sorted(untyped):
        f.write(i + "\t" + sorted(untyped[i])[0] + "\n")
with open(os.path.join(OUT, "parse-failures.txt"), "w") as f:
    for p, e in failed:
        f.write(f"{p}\t{e}\n")
summary = {
    "ttl_files": len(files), "parsed": len(graphs), "failed": len(failed),
    "activity_classes": len(activity_classes), "instance_range_props": len(instance_range_props), "type_range_props": len(type_range_props), "untyped_activity_instances": len(untyped), "domain_props": len(domain_props), "activity_instances": len(activity_instance),
    "iris": len(recs), "definitions": sum(1 for r in recs.values() if r["is_def"]),
}
print(json.dumps(summary, indent=1))
