#!/usr/bin/env python3
"""Create the block metadata for the core block and the family blocks.

Always (re)written: description.md and examples.yaml (generated from <block>/data.ttl).
Written only if missing (hand edits survive): bblock.json and, for core, shapes.shacl.
Run scripts/generate.py first so each block has its data.ttl.
"""
import json, os
from rdflib import Graph, RDF, Namespace
from rdflib.namespace import SKOS

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "..", "_sources")
BASE = "https://w3id.org/ogc/ospd/activity-type/"
ADDED = "2026-11-23T00:00:00Z"
FAMILIES = {
    "vector-geometry-processing": ("Vector geometry processing",
        "Operations and tests on vector geometries: buffers, hulls, envelopes, set operations, spatial predicates and extents (including the SQL/MM implementations)."),
    "raster-coverage-processing": ("Raster and coverage processing",
        "Operations on rasters and coverages: reprojection, resampling, cropping, mosaicking, format conversion, rendering, band math, spectral indices and zonal analysis."),
    "earth-observation": ("Earth observation",
        "Earth-observation data access and applications: Sentinel-2 band retrieval and product selection, cloud and best-available-pixel handling, and the water-bodies, algae-bloom and mangrove-biomass workflows."),
    "terrain-and-hydrology": ("Terrain and hydrology",
        "Terrain derivatives (slope, hillshading, ruggedness and position indices) and hydrological analysis (flow direction and accumulation, watersheds, stream networks, wetness index)."),
    "spatial-indexing": ("Spatial indexing",
        "Discrete global grid system (DGGS) indexing and conversion of geometries to grid cells."),
    "point-cloud-processing": ("Point-cloud processing",
        "Point-cloud thinning, gridding and conversion to shapes."),
    "ml-and-statistical-modeling": ("Machine learning and statistical modeling",
        "Machine-learning and statistical activities: regression, climate-variable downscaling, super-resolution and trend analysis, and inference executions."),
    "information-extraction-and-retrieval": ("Information extraction and retrieval",
        "Source acquisition, text metadata enrichment (entity extraction, geotagging, classification, normalization) and retrieval-augmented generation."),
    "workflow-and-scoring": ("Workflow and scoring",
        "Workflow runs and scoring or classification activities used in the model-of-models and workflow examples."),
}

def concepts(path):
    g = Graph(); g.parse(path, format="turtle")
    out = []
    for s in g.subjects(RDF.type, SKOS.Concept):
        label = g.value(s, SKOS.prefLabel)
        out.append((str(s), str(label) if label else str(s)))
    return sorted(out, key=lambda x: x[1].lower())

def example_for(path, iri):
    """A self-contained Turtle snippet for one concept (its own triples, with prefixes)."""
    g = Graph(); g.parse(path, format="turtle")
    sub = Graph()
    for p, n in g.namespaces(): sub.bind(p, n)
    from rdflib import URIRef, BNode
    def walk(node):
        for p, o in g.predicate_objects(node):
            sub.add((node, p, o))
            if isinstance(o, BNode): walk(o)
    walk(URIRef(iri))
    sub.add((URIRef(BASE), RDF.type, SKOS.ConceptScheme))
    return sub.serialize(format="turtle")

def write_if_missing(path, text):
    if not os.path.exists(path):
        open(path, "w").write(text)

def yaml_block(snips):
    out = ["examples:"]
    for title, code in snips:
        out += [f"  - title: {title}", "    snippets:", "      - language: turtle", "        code: |"]
        out += ["          " + l if l.strip() else "" for l in code.rstrip().splitlines()]
    return "\n".join(out) + "\n"

# ---- core
core = os.path.join(SRC, "core")
fam_list = "\n".join(f"- **{n}** (`ogc.ospd.activity-type.{k}`): {a}" for k, (n, a) in FAMILIES.items())
write_if_missing(os.path.join(core, "bblock.json"), json.dumps({
    "name": "OSPD Activity Type",
    "abstract": "Root of the OSPD activity types: the catalog listing one concept scheme per family, under https://w3id.org/ogc/ospd/activity-type/.",
    "status": "under-development", "dateTimeAddition": ADDED, "itemClass": "model", "version": "0.1",
    "tags": ["ospd", "activity-type", "provenance"],
    "group": "OSPD Activity Types",
    "isProfileOf": "bblocks://ogc.rim.activity-type",
    "shaclShapes": ["shapes.shacl"],
    "resources": [{"role": "data", "ref": "data.ttl", "format": "text/turtle",
                   "title": "OSPD activity types catalog"}],
}, indent=2) + "\n")
write_if_missing(os.path.join(core, "shapes.shacl"), '''@prefix sh:      <http://www.w3.org/ns/shacl#> .
@prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix ospd:    <https://w3id.org/ogc/ospd/activity-type/> .
@prefix ex:      <https://w3id.org/ogc/ospd/shapes/> .

ex:ActivityTypeShape a sh:NodeShape ;
    sh:targetClass acttype:ActivityType ;
    sh:property [
        sh:path skos:prefLabel ;
        sh:minCount 1 ;
        sh:message "An activity type needs a skos:prefLabel."
    ] ;
    sh:property [
        sh:path skos:inScheme ;
        sh:class skos:ConceptScheme ;
        sh:minCount 1 ;
        sh:message "An activity type must be in a concept scheme (its family)."
    ] ;
    sh:property [
        sh:path skos:definition ;
        sh:minCount 1 ;
        sh:severity sh:Warning ;
        sh:message "An activity type should have a skos:definition."
    ] .
''')
cg = concepts(os.path.join(core, "data.ttl"))
open(os.path.join(core, "description.md"), "w").write(f"""# OSPD Activity Type

Activity types used across the OGC Open Science Persistent Demonstrator (OSPD), consolidated under stable URIs of the
form `https://w3id.org/ogc/ospd/activity-type/<slug>`.

This block holds the catalog (`{BASE}catalog`), which lists one `skos:ConceptScheme` per family of related activity types.
Each family is a building block that profiles this one and carries its concept scheme and the Turtle definitions of its activity types.

Every activity type is a `skos:Concept` and an `acttype:ActivityType` (Registered Item Model), has a `skos:prefLabel`, and
records the IRIs it replaces (`dcterms:replaces`), equivalent aliases (`skos:exactMatch`) and likely duplicates
(`skos:closeMatch`).

## Families

{fam_list}
""")
open(os.path.join(core, "examples.yaml"), "w").write(yaml_block([(
    "Catalog with a family concept scheme",
    f"""@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<{BASE}catalog> a dcat:Catalog ;
    dcterms:title "OSPD Activity Types"@en ;
    dcterms:hasPart <{BASE}families/vector-geometry-processing> .

<{BASE}families/vector-geometry-processing> a skos:ConceptScheme ;
    skos:prefLabel "Vector geometry processing"@en .
""")]))

# ---- families
for key, (name, abstract) in FAMILIES.items():
    d = os.path.join(SRC, key)
    cs = concepts(os.path.join(d, "data.ttl"))
    write_if_missing(os.path.join(d, "bblock.json"), json.dumps({
        "name": name,
        "abstract": abstract,
        "status": "under-development", "dateTimeAddition": ADDED, "itemClass": "model", "version": "0.1",
        "tags": ["ospd", "activity-type", key],
        "group": "OSPD Activity Types",
        "isProfileOf": "bblocks://ogc.ospd.activity-type.core",
        "resources": [{"role": "data", "ref": "data.ttl", "format": "text/turtle",
                       "title": f"{name}: activity type definitions"}],
    }, indent=2) + "\n")
    lines = "\n".join(f"- [{l}]({i}) (`{i.rsplit('/', 1)[1]}`)" for i, l in cs)
    open(os.path.join(d, "description.md"), "w").write(f"""# {name}

{abstract}

This family has {len(cs)} activity types. It is a profile of the OSPD Activity Type core block and its data resource
(`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

{lines}
""")
    first_iri = cs[0][0]
    open(os.path.join(d, "examples.yaml"), "w").write(yaml_block([(
        f"{cs[0][1]}", example_for(os.path.join(d, "data.ttl"), first_iri))]))
print("blocks written:", 1 + len(FAMILIES))
