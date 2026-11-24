#!/usr/bin/env python3
"""Generate docs/ospd-activity-types-summary.md from the analysis tables."""
import csv, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
AN = os.path.join(HERE, "..", "analysis")
OUT = os.path.join(HERE, "..", "docs", "ospd-activity-types-summary.md")
rd = lambda f: list(csv.DictReader(open(os.path.join(AN, f))))
defs = {r["iri"]: r for r in rd("definitions.csv")}
fam = rd("family-assignment.csv")
mp = {r["old_iri"]: r for r in rd("mapping.csv")}
dups = rd("duplicates.csv")
und = rd("undefined-references.csv")
GP = "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/"
GL = "https://w3id.org/geolabs/ospd/process-profiles/process-type/"
NEW = "https://w3id.org/ogc/ospd/activity-type/"

def origin(i):
    if i.startswith("http://ospd/demo/"): return "ospd-data register item"
    if i.startswith(GP): return "GeoLabs generic type"
    if i.startswith(GL): return "GeoLabs implementation (" + i[len(GL):].split("/")[0] + ")"
    if "crim-ca.github.io" in i: return "CRIM"
    if "example.org/ospd/process-types" in i: return "openscience (Katerina)"
    if "rss-hydro" in i: return "openscience (rss-hydro)"
    if "roofer-online" in i or "planspace" in i: return "Geonovum process endpoint"
    if "example.org/test" in i: return "test fixture"
    return "other"
def short(i):
    return (i.replace(GL, "GL:").replace(GP, "GLgen:").replace("http://ospd/demo/", "")
             .replace("https://example.org/ospd/process-types/", "OS:").replace(NEW, "ospd:")
             .replace("https://crim-ca.github.io/bblocks-process-profiles/def/", "CRIM:")
             .replace("https://geolabs.github.io/bblocks-process-profiles/def/process-type/", "CRIMsnap:")
             .replace("https://catalog.ospd.dev.kurrawong.ai/catalogs/demo:geoacs/collections/demo:ospd-geoacs/items/", "KW:")
             .replace("https://rss-hydro.lu/ns/mom/", "RH:").replace("http://www.w3.org/ns/prov#", "prov:"))
esc = lambda s: (s or "").replace("|", "/").replace("\n", " ")

assigned = [r for r in fam if r["kind"] in ("kept", "renamed-collision", "review") and r["family"]]
unassigned = [r for r in fam if r["kind"] in ("kept", "renamed-collision", "review") and not r["family"]]
by_family = collections.defaultdict(list)
for r in assigned: by_family[r["family"]].append(r)
by_origin = collections.Counter(origin(i) .split(" (")[0] for i in defs)
renames = sum(1 for r in mp.values() if r["kind"] == "renamed-collision")
aliases = [r for r in mp.values() if r["kind"] == "alias"]
gaps = [r for r in mp.values() if r["kind"] == "gap"]
ex_local = [r for r in mp.values() if r["kind"] == "gap-example-local"]
external = [r for r in mp.values() if r["kind"] == "external"]
roles = collections.Counter(r["role"] for r in dups)
confs = collections.Counter(r["confidence"] for r in dups)
groups = collections.defaultdict(list)
for r in dups: groups[r["group_id"]].append(r)

FAMDESC = {
 "vector-geometry-processing": "buffers, hulls, envelopes, set operations, spatial predicates, extents (incl. SQL/MM)",
 "raster-coverage-processing": "reprojection, resampling, crop, mosaic, format conversion, rendering, band math, spectral indices, zonal analysis",
 "earth-observation": "Sentinel-2 data access, cloud/best-available-pixel, water-bodies, algae-bloom and mangrove workflows",
 "terrain-and-hydrology": "terrain derivatives and hydrological analysis",
 "information-extraction-and-retrieval": "source acquisition, text metadata enrichment, retrieval-augmented generation",
 "ml-and-statistical-modeling": "regression, downscaling, trend analysis, inference executions",
 "point-cloud-processing": "thinning, gridding, conversion to shapes",
 "spatial-indexing": "DGGS indexing and conversion",
 "workflow-and-scoring": "workflow runs, scoring and classification",
}
L = []
w = L.append
w("# OSPD activity types: consolidation summary for discussion")
w("")
w("*Draft of 2026-11-23, for discussion between Rob Atkinson and Alejandro Villar. Numbers in this document are generated from the analysis tables in the `ospd-activity-types` repository.*")
w("")
w("## 1. Purpose and status")
w("")
w("Provenance traces should work as linked data: the activity types they cite must resolve to descriptions. The plan is to gather every activity type used across the OSPD material, rebase them onto stable `https://w3id.org/ogc/ospd/activity-type/<slug>` URIs, deduplicate them, package them as building blocks per family, and publish them from the OSPD-only Prez instance (`defs-hosted.opengis.net/prez-ospd`).")
w("")
w("Done so far: a scan of 33 repositories (Turtle only), a deduplication pass, a draft family structure, a mapping table of every old IRI to its new IRI, a local building blocks register (`ospd-activity-types`, 10 blocks, validating cleanly), and a w3id.org redirect PR (perma-id/w3id.org#7269, awaiting merge). Not done: per-repository PRs, loading the data into Prez, the missing RIM profile blocks, and the non-Turtle sources.")
w("")
w("## 2. What we scanned and found")
w("")
w("The scan parsed 1,555 of 1,556 Turtle files in the 33 repositories (one Geonovum RML example has an unbound prefix). Non-Turtle sources (JSON/YAML examples, the Voyager TypeScript/Python definitions, HARTIS, Lampata, Starling) are not covered yet.")
w("")
w("An activity type is detected structurally: as a definition (typed `acttype:ActivityType` or a subclass of `prov:Activity`) or as a reference (an extra `rdf:type` on a `prov:Activity` instance, including activities recognised only through the range or domain of PROV properties such as `prov:wasGeneratedBy` or `prov:used`). Known URI schemes are only a cross-check.")
w("")
w(f"**{len(defs)} definitions** (test fixtures and `rim:RegisterAction` excluded), by origin:")
w("")
w("| Origin | Definitions |")
w("|---|---|")
for k, v in by_origin.most_common(): w(f"| {k} | {v} |")
w("")
w(f"GeoLabs uses three tiers: concepts, generic activity types (`bblocks-generic-profiles`) and tool-specific implementation process types that specialise a generic type. We include all tiers as register items, with implementations under their generic type via `skos:broader`.")
w("")
w(f"**Referenced but not defined:** {len(und)} IRIs: {len(aliases)} are aliases of existing definitions (27 CRIM snapshot IRIs of GeoLabs types and 6 Kurrawong catalog URLs for GA001 and GA016-GA020), {len(gaps)} are real gaps (the 7 `example.org/ospd/process-types/*` types used in the examples, and `rim/activity-type/WorkflowRun`; the RIM class `rim/activity-type/ActivityType` itself is classed as external), {len(ex_local)} are types local to an example (for instance `example.org/cool-spots#...`), and {len(external)} are external vocabulary (Wf4ever, GeoJSON, FOAF) that we do not map. Full lists in appendix C.")
w("")
w("17 activity instances have no type beyond `prov:Activity` (among them the 8 HARTIS CVI run activities). They will show as unmapped in a trace viewer.")
w("")
w("## 3. URI scheme and the RIM namespace")
w("")
w("- **Activity types:** `https://w3id.org/ogc/ospd/activity-type/<slug>`. Slugs reuse each source's own slug (`GA001`, GeoLabs slugs, ...). Where a generic and an implementation type collide, the generic keeps the bare slug and the implementation gets a group prefix (for example `sqlmm-buffer`). " + f"{renames} slugs were renamed this way. Every old IRI, new IRI and reason is recorded in `analysis/mapping.csv`, so any choice can be rebound later.")
w("- **Registers (`http://w3id.org/ogc/reg/<id>`):** to move to `https://w3id.org/ogc/ospd/register/<id>`, fixing the `ogcactivites` typo.")
w("- **RIM (`https://w3id.org/ogc/rim/`):** we propose to keep it where it is. It is the Registered Item Model (ISO 19135:2026), and its README says the prefix is designed to stay stable. We would add a `/ogc/rim` redirect to the OSPD Prez (already in PR #7269) and retrofit `registered-item-model` to publish its ontology data to the same instance through the new bblocks SPARQL data loading. `rim:` terms in our data are therefore left unchanged.")
w("- **Missing RIM profile blocks:** the README of `registered-item-model` describes `activity-type`, `geoprocessing-activity-types` and `ml-activity-types` profile blocks that are not in the repository's master. The data uses `acttype:ActivityType`, `rim/geoprocessing/GeoprocessingActivityType` and `rim/ml-activity/...`, so these need to exist. We propose to add them by PR, and to make our core block a profile of the `activity-type` one once it is published.")
w("- **Vocabulary of the generated data:** SKOS (`skos:prefLabel`, `skos:definition`, `skos:broader`, `skos:related`), `owl:versionInfo`, `dcterms:modified`/`source`/`replaces`, `rdfs:seeAlso`, `prov:qualifiedAttribution` with `foaf:name` agents (no e-mail addresses). Aliases are `skos:exactMatch`, probable duplicates `skos:closeMatch`.")
w("")
w("## 4. Families and building blocks")
w("")
w("The register `ogc.ospd.activity-type.` has a `core` block (concept scheme, catalog, one `skos:Collection` per family) and one leaf block per family, each a profile of `core` carrying its activity types as a Turtle data resource that the build uploads to Prez.")
w("")
w("| Family block | Types | Scope |")
w("|---|---|---|")
for k, v in sorted(by_family.items(), key=lambda kv: -len(kv[1])):
    w(f"| `{k}` | {len(v)} | {FAMDESC.get(k, '')} |")
w(f"| (unassigned) | {len(unassigned)} | openscience `Geoprocessing` root, two `example.org/test/*` types, four Geonovum process-endpoint URLs |")
w("")
w("Families were built from the existing `skos:broader` structure, GeoLabs' concepts and the names and descriptions. The one-family rule holds for the current assignment: no type has parents in two families, no child sits in a different family from its parent, and no duplicate or implementation group spans families. Judgement calls (marked as manual in `family-assignment.csv`): GA010 SEN2SR is in raster processing because its description speaks of spatial resolution of raster imagery; GA017 Seasonal Sen's Slope is in ML and statistics as a time-series trend test. The earth-observation family is partly an application bucket; workflow-level types are thin (3) and may be better folded elsewhere.")
w("")
w("## 5. Deduplication")
w("")
w(f"An LLM-assisted pass over names, descriptions, broader links and citations produced {len(groups)} groups ({len(dups)} rows: " + ", ".join(f"{v} {k}" for k, v in roles.most_common()) + "; confidence " + ", ".join(f"{v} {k}" for k, v in confs.most_common()) + "). Prompts and the agent's notes are in `analysis/prompts/`. Groups are flagged, never merged: duplicates are recorded as `skos:closeMatch` to the proposed canonical type, and `implements` marks a GeoLabs implementation realising a generic or register type. The same-level duplicates found:")
w("")
w("| Group | Duplicate | Canonical | Confidence |")
w("|---|---|---|---|")
for gid, rs in groups.items():
    canon = [short(r["iri"]) for r in rs if r["role"] == "canonical"]
    for r in rs:
        if r["role"] == "duplicate":
            w(f"| {gid} | {short(r['iri'])} | {canon[0] if canon else ''} | {r['confidence']} |")
w("")
w("Open calls for a human: GA003 Envelope vs generic `geometry-extent` (one geometry vs a set), GA039 Geolocate vs GA041 Geotag, GA009 vs CRIM climate-downscaling (CRIM has no description), GA029 vs GA036 (GA036 has no description), whether workflow-level types are duplicates or related. Full groups in appendix B.")
w("")
w("## 6. Potential errors in the source data")
w("")
for t in [
 "GeoLabs `sqlmm/touches` is named \"Compute intersection.\" with an intersection description: probable copy-paste error (not merged with `sqlmm/intersection`).",
 "GeoLabs `raster/band-math` and `raster/band-math-multiband` have identical descriptions.",
 "GeoLabs `algae-bloom/reproject-image` has broader `raster-resampling`, probably `raster-reprojection`; `kindgrove-steps/reproject-band` has the invalid broader `https://example.org/not-an-activity-type`.",
 "ospd-data hierarchy gaps: GA034, GA035 and GA036 have no broader; the hulls GA005 and GA006 are not under GA002 Boundary. GA014, GA015 and GA030-GA036 have no description.",
 "ospd-data register typo `ogcactivites` (live; some items use `ogcactivities`) and typos in descriptions (\"vertecies\", \"interoir\").",
 "openscience: the examples reference lowercase kebab slugs (`process-types/classification`, `ingest`, `model-training`, ...) while the ontology defines CamelCase terms (`Geoprocessing`, `ScoringAndProgressTracking`): references and definitions do not match.",
 "`rim/activity-type/WorkflowRun` is referenced but defined nowhere; rss-hydro `mom/WorkflowRun` looks like the same concept.",
 "Katerina's examples cite GA001 and GA016-GA020 by Kurrawong catalog URLs instead of `http://ospd/demo/GAnnn`.",
 "Geonovum uses process-endpoint URLs as activity types, with no names or descriptions. Its `ldv-prov.rml.ttl` example does not parse (prefix `rdfs:` unbound).",
 "CRIM's `geolabs.github.io/.../process-type/...` IRIs are a stale snapshot of GeoLabs, and its climate-downscaling types have no descriptions.",
 "The attribution data in ospd-data points to agent IRIs under `http://ospd/demo/` (for example one contributor) that do not resolve; the generated data keeps names only."]:
    w(f"- {t}")
w("")
w("## 7. Remapping plan")
w("")
for t in [
 "**Mapping table:** `analysis/mapping.csv` is the record (old IRI, new IRI, kind: kept / renamed-collision / alias / gap / review / external, canonical, confidence, duplicate groups). A rewrite script applies it; rerun it whenever the table changes.",
 "**Per-repository PRs** (drafts, for review): rewrite old IRIs in `_sources` to the new ones and rebuild, since `build/` is committed in these repositories. Candidates, from the scan: bblocks-openscience (the `example.org/ospd/process-types/*` and Kurrawong catalog references), GeoLabs process-profiles and generic-profiles, CRIM, ospd-data and ospd-regcat-profile, Geonovum ospd-dtaas-register, HARTIS cvi-workflow, Voyager. Repositories that need no change: prov-cwl, bblocks-cwl, bblocks-eoap-cct, bblocks-examples*, bblocks-ogcapi-processes, topo-feature, KindGrove, gen-ogc-apppackage, bblocks-demo-register.",
 "**Source-data fixes** as separate PRs (section 6), not mixed with the IRI rewrite.",
 "**Gaps:** define the 7 openscience process types and `rim/activity-type/WorkflowRun` (or map them to existing definitions); decide what to do with example-local types; fill the missing descriptions.",
 "**Publishing:** the register's build uploads each block's `data.ttl` to the OSPD Prez (the bblocks `sparql.resources.data` setting; each rebuild replaces that graph). The w3id.org redirects then resolve each URI through `prez-ospd-b/object`.",
 "**RIM:** PR to `registered-item-model` adding the three profile blocks and publishing its ontology data to the same Prez; then `isProfileOf` from our core block.",
 "**Later:** the vocabulary validator that checks activity-type markers in uplifted resources resolve to definitions (Katerina's `unknown-activity-type-fail` test is a starting point), and a smoke test of a trace in the viewer."]:
    w(f"- {t}")
w("")
w("## 8. Questions for discussion")
w("")
for t in [
 "Keep `rim:` as is and register `/ogc/rim` (our proposal), or move the model terms under `ogc/ospd`?",
 "Does the `activity-type`, `geoprocessing-activity-types`, `ml-activity-types` chain already exist somewhere unpublished, or should we write the blocks?",
 "Slug style: keep each source's own (CamelCase and kebab-case coexist), or normalise to kebab-case?",
 "IRIs for the families (`.../activity-type/families/<slug>`) and the catalog (`.../activity-type/catalog`) are our proposal: acceptable? What does the OSPD Prez expect for the catalog and concept scheme to render?",
 "GeoLabs implementation types and generic types are both register items. Is the generic/implementation tier distinction something Prez or the register should expose, or is `skos:broader` enough?",
 "Are the family boundaries right, in particular earth-observation and workflow-and-scoring?",
 "Which of the medium and low confidence duplicates should be merged, and which kept as related?",
 "Terminology: process type vs activity type, and the \"registered term\" wording in Katerina's register."]:
    w(f"- {t}")
w("")
w("## 9. Artifacts")
w("")
w("Everything is in the `ospd-activity-types` repository (local, no remote yet): `analysis/` (CSV tables, prompts), `scripts/` (scan, mapping, family, generation and block scripts; run order in `scripts/analysis/README.md`), `_sources/` (the building blocks), `docs/` (the notes of the 2026-11-20 call and this summary).")
w("")
w("## Appendix A. All activity types by family")
w("")
w("Abbreviations for old IRIs: `GL:` = `https://w3id.org/geolabs/ospd/process-profiles/process-type/`; `GLgen:` = `https://w3id.org/geolabs/ospd/generic-profiles/activity-type/`; `OS:` = `https://example.org/ospd/process-types/`; `CRIM:` = `https://crim-ca.github.io/bblocks-process-profiles/def/`; `CRIMsnap:` = `https://geolabs.github.io/bblocks-process-profiles/def/process-type/`; `KW:` = `https://catalog.ospd.dev.kurrawong.ai/catalogs/demo:geoacs/collections/demo:ospd-geoacs/items/`; `RH:` = `https://rss-hydro.lu/ns/mom/`; `ospd:` = `https://w3id.org/ogc/ospd/activity-type/`; a bare `GAnnn` is `http://ospd/demo/GAnnn`.")
w("")
for k in sorted(by_family, key=lambda k: -len(by_family[k])):
    w(f"### {k} ({len(by_family[k])})")
    w("")
    w("| New slug | Name | Origin | Old IRI |")
    w("|---|---|---|---|")
    for r in sorted(by_family[k], key=lambda r: r["new_iri"]):
        w(f"| `{r['new_iri'].rsplit('/', 1)[1]}` | {esc(r['name'])[:60]} | {origin(r['old_iri'])} | {esc(short(r['old_iri']))} |")
    w("")
w(f"### unassigned ({len(unassigned)})")
w("")
w("| New slug | Name | Origin | Old IRI |")
w("|---|---|---|---|")
for r in unassigned:
    w(f"| `{r['new_iri'].rsplit('/', 1)[1]}` | {esc(r['name'])[:60]} | {origin(r['old_iri'])} | {esc(short(r['old_iri']))[:70]} |")
w("")
w("## Appendix B. Duplicate groups")
w("")
w("| Group | Role | Conf. | IRI | Rationale |")
w("|---|---|---|---|---|")
for r in dups:
    w(f"| {r['group_id']} | {r['role']} | {r['confidence']} | {esc(short(r['iri']))} | {esc(r['rationale'])[:150]} |")
w("")
w("## Appendix C. Aliases, gaps and other references")
w("")
w("| Kind | Old IRI | Maps to | Notes |")
w("|---|---|---|---|")
for r in aliases + gaps + ex_local + external:
    w(f"| {r['kind']} | {esc(short(r['old_iri']))[:80]} | {esc(short(r['new_iri']))[:60]} | {esc(r['notes'])[:80]} |")
open(OUT, "w").write("\n".join(L) + "\n")
print(len(L), "lines")
