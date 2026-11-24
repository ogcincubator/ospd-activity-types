# OSPD activity types: consolidation summary for discussion

*Draft of 2026-11-24, for discussion between Rob Atkinson and Alejandro Villar. Numbers in this document are generated from the analysis tables in the `ospd-activity-types` repository.*

## 1. Purpose and status

Provenance traces should work as linked data: the activity types they cite must resolve to descriptions. The plan is to gather every activity type used across the OSPD material, rebase them onto stable `https://w3id.org/ogc/ospd/activity-type/<slug>` URIs, deduplicate them, package them as building blocks per family, and publish them from the OSPD-only Prez instance (`defs-hosted.opengis.net/prez-ospd`).

Done so far: a scan of 33 repositories (Turtle only), a deduplication pass, a draft family structure, a mapping table of every old IRI to its new IRI, a building blocks register (`ospd-activity-types`, 10 blocks, validating cleanly), published at <https://github.com/ogcincubator/ospd-activity-types> with its data uploaded to the OSPD Prez, the w3id.org redirects (perma-id/w3id.org#7269, merged; #7280 is a small follow-up for `/ogc/rim/`), and the three RIM profile blocks, restored in `registered-item-model` (so `core` is now a profile of `ogc.rim.activity-type`). Not done: per-repository PRs and the non-Turtle sources (JSON/JSON-LD examples are covered, since the build uplifts them to Turtle).

## 2. What we scanned and found

The scan parsed 1,555 of 1,556 Turtle files in the 33 repositories (one Geonovum RML example has an unbound prefix). Non-Turtle sources (JSON/YAML examples, the Voyager TypeScript/Python definitions, HARTIS, Lampata, Starling) are not covered yet.

An activity type is detected structurally: as a definition (typed `acttype:ActivityType` or a subclass of `prov:Activity`) or as a reference (an extra `rdf:type` on a `prov:Activity` instance, including activities recognised only through the range or domain of PROV properties such as `prov:wasGeneratedBy` or `prov:used`). Known URI schemes are only a cross-check.

**157 definitions** (test fixtures and `rim:RegisterAction` excluded), by origin:

| Origin | Definitions |
|---|---|
| GeoLabs implementation | 58 |
| ospd-data register item | 49 |
| GeoLabs generic type | 36 |
| openscience | 5 |
| Geonovum process endpoint | 4 |
| CRIM | 3 |
| test fixture | 2 |

GeoLabs uses three tiers: concepts, generic activity types (`bblocks-generic-profiles`) and tool-specific implementation process types that specialise a generic type. We include all tiers as register items, with implementations under their generic type via `skos:broader`.

**Referenced but not defined:** 64 IRIs: 33 are aliases of existing definitions (27 CRIM snapshot IRIs of GeoLabs types and 6 Kurrawong catalog URLs for GA001 and GA016-GA020), 8 are real gaps (the 7 `example.org/ospd/process-types/*` types used in the examples, and `rim/activity-type/WorkflowRun`; the RIM class `rim/activity-type/ActivityType` itself is classed as external), 11 are types local to an example (for instance `example.org/cool-spots#...`), and 12 are external vocabulary (Wf4ever, GeoJSON, FOAF) that we do not map. Full lists in appendix C.

17 activity instances have no type beyond `prov:Activity` (among them the 8 HARTIS CVI run activities). They will show as unmapped in a trace viewer.

## 3. URI scheme and the RIM namespace

- **Activity types:** `https://w3id.org/ogc/ospd/activity-type/<slug>`. Slugs reuse each source's own slug (`GA001`, GeoLabs slugs, ...). Where a generic and an implementation type collide, the generic keeps the bare slug and the implementation gets a group prefix (for example `sqlmm-buffer`). 24 slugs were renamed this way. Every old IRI, new IRI and reason is recorded in `analysis/mapping.csv`, so any choice can be rebound later.
- **Slug style:** left as the sources have it (CamelCase and kebab-case coexist). The mapping table makes a later normalisation cheap if we change our minds.
- **Registers (`http://w3id.org/ogc/reg/<id>`):** not part of this change. If we revisit them, the idea is to move them to `https://w3id.org/ogc/ospd/register/<id>`, fixing the `ogcactivites` typo.
- **RIM (`https://w3id.org/ogc/rim/`):** we propose to keep it where it is. It is the Registered Item Model (ISO 19135:2026), and its README says the prefix is designed to stay stable. The `/ogc/rim` redirects to the OSPD Prez are live (#7269; #7280 makes `/ogc/rim/` resolve to the ontology itself), and `registered-item-model` now publishes its ontology and a top-level catalog (`https://w3id.org/ogc/rim/catalog`) to the same instance through the bblocks SPARQL data loading. `rim:` terms in our data are left unchanged.
- **RIM profile blocks:** the README of `registered-item-model` describes `activity-type`, `geoprocessing-activity-types` and `ml-activity-types` profile blocks. They existed on the `pre-geonovum-refactor` branch but were dropped from `master` by the refactor. We restored them (identifiers moved to `ogc.rim.*`; one example fixed for the updated MLM shapes). Our `core` block is a profile of `ogc.rim.activity-type`.
- **Register item metadata and default statuses:** profiling the RIM activity-type block makes every activity type a `rim:RegisterItem`, which requires `rim:itemClass` (`acttype:activityTypeItemClass`), `rim:objectIdentifier` (its own IRI), `rim:validityStatus` and `rim:publicationStatus`. We set **`rim:valid` and `rim:published` on every type as defaults**; this is a governance statement that should be confirmed (one line in `scripts/generate.py`).
- **Vocabulary of the generated data:** SKOS (`skos:prefLabel`, `skos:definition`, `skos:broader`, `skos:related`), `owl:versionInfo`, `dcterms:modified`/`source`/`replaces`, `rdfs:seeAlso`, `prov:qualifiedAttribution` with agents that are either a real IRI or a blank node with a `foaf:name` (no e-mail addresses). Aliases are `skos:exactMatch`, probable duplicates `skos:closeMatch`.

## 4. Families and building blocks

The register `ogc.ospd.activity-type.` has a `core` block (the `dcat:Catalog`, which lists the families) and one leaf block per family, each a profile of `core`. Each family block carries its own `skos:ConceptScheme` (`.../activity-type/families/<slug>`) and its activity types as `skos:Concept`s in it, as a Turtle data resource that the build uploads to Prez. Concepts with no broader concept in the family are marked as top concepts (`skos:topConceptOf` / `skos:hasTopConcept`), which Prez uses as entry points. The previous single scheme for all types was dropped.

| Family block | Types | Scope |
|---|---|---|
| `vector-geometry-processing` | 42 | buffers, hulls, envelopes, set operations, spatial predicates, extents (incl. SQL/MM) |
| `raster-coverage-processing` | 35 | reprojection, resampling, crop, mosaic, format conversion, rendering, band math, spectral indices, zonal analysis |
| `earth-observation` | 25 | Sentinel-2 data access, cloud/best-available-pixel, water-bodies, algae-bloom and mangrove workflows |
| `terrain-and-hydrology` | 17 | terrain derivatives and hydrological analysis |
| `information-extraction-and-retrieval` | 13 | source acquisition, text metadata enrichment, retrieval-augmented generation |
| `ml-and-statistical-modeling` | 6 | regression, downscaling, trend analysis, inference executions |
| `point-cloud-processing` | 6 | thinning, gridding, conversion to shapes |
| `spatial-indexing` | 3 | DGGS indexing and conversion |
| `workflow-and-scoring` | 3 | workflow runs, scoring and classification |
| (unassigned) | 7 | openscience `Geoprocessing` root, two `example.org/test/*` types, four Geonovum process-endpoint URLs |

Families were built from the existing `skos:broader` structure, GeoLabs' concepts and the names and descriptions. The one-family rule holds for the current assignment: no type has parents in two families, no child sits in a different family from its parent, and no duplicate or implementation group spans families. Judgement calls (marked as manual in `family-assignment.csv`): GA010 SEN2SR is in raster processing because its description speaks of spatial resolution of raster imagery; GA017 Seasonal Sen's Slope is in ML and statistics as a time-series trend test. The earth-observation family is partly an application bucket; workflow-level types are thin (3) and may be better folded elsewhere.

## 5. Deduplication

An LLM-assisted pass over names, descriptions, broader links and citations produced 28 groups (110 rows: 66 related, 18 implements, 15 canonical, 11 duplicate; confidence 64 medium, 23 high, 23 low). Prompts and the agent's notes are in `analysis/prompts/`. Groups are flagged, never merged: duplicates are recorded as `skos:closeMatch` to the proposed canonical type, and `implements` marks a GeoLabs implementation realising a generic or register type. The same-level duplicates found:

| Group | Duplicate | Canonical | Confidence |
|---|---|---|---|
| buffer | GA001 | GLgen:buffer | high |
| convex-hull | GA006 | GLgen:convex-hull | high |
| geometry-difference | GA019 | GLgen:difference | medium |
| geometry-extent | GA003 | GLgen:geometry-extent | medium |
| band-math | GA008 | GLgen:raster-band-math | medium |
| slope | GA021 | GLgen:slope | medium |
| zonal-statistics | OS:ZonalStatistics | GA027 | medium |
| climate-downscaling | CRIM:activity-type/climate-downscaling | GA009 | medium |
| parse-aoi | GL:kindgrove-steps/parse-aoi-steps | GL:kindgrove/parse-aoi | high |
| mangrove-workflow | GL:kindgrove-steps/mangrove-workflow-steps | GL:kindgrove/mangrove-workflow | medium |
| water-bodies-detection | GL:water-bodies/detect-water-body | GL:water-bodies/water-bodies | high |

Open calls for a human, each with our suggestion (for Rob to confirm or overrule):

| Case | What differs | Suggestion |
|---|---|---|
| GA003 Envelope vs `geometry-extent` | GA003 returns the bounding rectangle of one geometry; `geometry-extent` computes it for a set of geometries | Keep both, as `skos:related` (currently flagged as a duplicate, medium) |
| GA039 Geolocate vs GA041 Geotag | Both resolve place names against a gazetteer; GA039 takes a country or place name and is the terminal step of the connector chain, GA041 resolves place mentions produced by entity extraction | Keep both, as related; merge only if Rob sees them as the same operation |
| GA009 vs CRIM climate-downscaling | CRIM's type has no description, so it can't be told apart from GA009 (ML climate downscaling) | Keep the `skos:closeMatch` for now and ask CRIM for a description; then decide between exact match and separate types |
| GA029 vs GA036 | GA036 (polygon to DGGS cells) has no description; GA029 indexes positions or geometries to DGGS cells | Keep both: GA036 looks like a more specific case of GA029; ask HARTIS for a definition |
| Workflow-level types | Same workflow realised by different tools or steps | Keep as related, not duplicates |

Full groups in appendix B.

## 6. Potential errors in the source data

- GeoLabs `sqlmm/touches` is named "Compute intersection." with an intersection description: probable copy-paste error (not merged with `sqlmm/intersection`).
- GeoLabs `raster/band-math` and `raster/band-math-multiband` have identical descriptions.
- GeoLabs `algae-bloom/reproject-image` has broader `raster-resampling`, probably `raster-reprojection`; `kindgrove-steps/reproject-band` has the invalid broader `https://example.org/not-an-activity-type`.
- ospd-data hierarchy gaps: GA034, GA035 and GA036 have no broader; the hulls GA005 and GA006 are not under GA002 Boundary. GA014, GA015 and GA030-GA036 have no description.
- ospd-data register typo `ogcactivites` (live; some items use `ogcactivities`) and typos in descriptions ("vertecies", "interoir").
- openscience: the examples reference lowercase kebab slugs (`process-types/classification`, `ingest`, `model-training`, ...) while the ontology defines CamelCase terms (`Geoprocessing`, `ScoringAndProgressTracking`): references and definitions do not match.
- `rim/activity-type/WorkflowRun` is referenced but defined nowhere; rss-hydro `mom/WorkflowRun` looks like the same concept.
- Katerina's examples cite GA001 and GA016-GA020 by Kurrawong catalog URLs instead of `http://ospd/demo/GAnnn`.
- Geonovum uses process-endpoint URLs as activity types, with no names or descriptions. Its `ldv-prov.rml.ttl` example does not parse (prefix `rdfs:` unbound).
- CRIM's `geolabs.github.io/.../process-type/...` IRIs are a stale snapshot of GeoLabs, and its climate-downscaling types have no descriptions.
- The attribution data in ospd-data points to agent IRIs under `http://ospd/demo/` (one contributor, on nine types) that do not resolve; the generated data keeps the name only, as a blank node.

## 7. Remapping plan

- **Mapping table:** `analysis/mapping.csv` is the record (old IRI, new IRI, kind: kept / renamed-collision / alias / gap / review / external, canonical, confidence, duplicate groups). A rewrite script applies it; rerun it whenever the table changes.
- **Per-repository PRs** (drafts, for review): rewrite old IRIs in `_sources` to the new ones and rebuild, since `build/` is committed in these repositories. Candidates, from the scan: bblocks-openscience (the `example.org/ospd/process-types/*` and Kurrawong catalog references), GeoLabs process-profiles and generic-profiles, CRIM, ospd-data and ospd-regcat-profile, Geonovum ospd-dtaas-register, HARTIS cvi-workflow, Voyager. Repositories that need no change: prov-cwl, bblocks-cwl, bblocks-eoap-cct, bblocks-examples*, bblocks-ogcapi-processes, topo-feature, KindGrove, gen-ogc-apppackage, bblocks-demo-register.
- **Source-data fixes** as separate PRs (section 6), not mixed with the IRI rewrite.
- **Gaps:** define the 7 openscience process types and `rim/activity-type/WorkflowRun` (or map them to existing definitions); decide what to do with example-local types; fill the missing descriptions.
- **Publishing:** the register's build uploads each block's `data.ttl` to the OSPD Prez (the bblocks `sparql.resources.data` setting; each rebuild replaces that graph). The w3id.org redirects then resolve each URI through `prez-ospd-b/object`.
- **RIM:** done: the three profile blocks are restored, the model's ontology and a catalog are published to the same Prez, and our core block is a profile of `ogc.rim.activity-type`.
- **Later:** the vocabulary validator that checks activity-type markers in uplifted resources resolve to definitions (Katerina's `unknown-activity-type-fail` test is a starting point), and a smoke test of a trace in the viewer.

## 8. Questions for discussion

- Keep `rim:` as is and register `/ogc/rim` (our proposal), or move the model terms under `ogc/ospd`?
- The three RIM profile blocks were restored from `pre-geonovum-refactor`: was their removal from `master` deliberate?
- Are `rim:valid` and `rim:published` the right default statuses for the consolidated types?
- Slug style: we keep each source's own for now (CamelCase and kebab-case coexist); do you want them normalised to kebab-case?
- IRIs for the families (`.../activity-type/families/<slug>`) and the catalog (`.../activity-type/catalog`) are our proposal and render well in Prez as catalog and concept schemes: acceptable?
- GeoLabs implementation types and generic types are both register items. Is the generic/implementation tier distinction something Prez or the register should expose, or is `skos:broader` enough?
- Are the family boundaries right, in particular earth-observation and workflow-and-scoring?
- Do you agree with our suggestions for the open duplicate calls in section 5?
- Terminology: process type vs activity type, and the "registered term" wording in Katerina's register.

## 9. Artifacts

Everything is in the `ospd-activity-types` repository (<https://github.com/ogcincubator/ospd-activity-types>): `analysis/` (CSV tables, prompts), `scripts/` (scan, mapping, family, generation and block scripts; run order in `scripts/analysis/README.md`), `_sources/` (the building blocks), `docs/` (the notes of the 2026-11-20 call and this summary).

## Appendix A. All activity types by family

Abbreviations for old IRIs: `GL:` = `https://w3id.org/geolabs/ospd/process-profiles/process-type/`; `GLgen:` = `https://w3id.org/geolabs/ospd/generic-profiles/activity-type/`; `OS:` = `https://example.org/ospd/process-types/`; `CRIM:` = `https://crim-ca.github.io/bblocks-process-profiles/def/`; `CRIMsnap:` = `https://geolabs.github.io/bblocks-process-profiles/def/process-type/`; `KW:` = `https://catalog.ospd.dev.kurrawong.ai/catalogs/demo:geoacs/collections/demo:ospd-geoacs/items/`; `RH:` = `https://rss-hydro.lu/ns/mom/`; `ospd:` = `https://w3id.org/ogc/ospd/activity-type/`; a bare `GAnnn` is `http://ospd/demo/GAnnn`.

### vector-geometry-processing (42)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `GA001` | Buffer | ospd-data register item | GA001 |
| `GA002` | Boundary | ospd-data register item | GA002 |
| `GA003` | Envelope | ospd-data register item | GA003 |
| `GA004` | Bounding Circle | ospd-data register item | GA004 |
| `GA005` | Concave Hull | ospd-data register item | GA005 |
| `GA006` | Convex Hull | ospd-data register item | GA006 |
| `GA019` | Difference | ospd-data register item | GA019 |
| `GA020` | Filter geometries | ospd-data register item | GA020 |
| `area` | Area | GeoLabs generic type | GLgen:area |
| `buffer` | Buffer | GeoLabs generic type | GLgen:buffer |
| `centroid` | Centroid | GeoLabs generic type | GLgen:centroid |
| `contains` | Contains | GeoLabs generic type | GLgen:contains |
| `convex-hull` | Convex hull | GeoLabs generic type | GLgen:convex-hull |
| `crosses` | Crosses | GeoLabs generic type | GLgen:crosses |
| `difference` | Difference | GeoLabs generic type | GLgen:difference |
| `disjoint` | Disjoint | GeoLabs generic type | GLgen:disjoint |
| `equals` | Equals | GeoLabs generic type | GLgen:equals |
| `geometry-extent` | Geometry extent | GeoLabs generic type | GLgen:geometry-extent |
| `intersection` | Intersection | GeoLabs generic type | GLgen:intersection |
| `intersects` | Intersects | GeoLabs generic type | GLgen:intersects |
| `is-simple` | Is simple | GeoLabs generic type | GLgen:is-simple |
| `sqlmm-area` | Compute geometry area. | GeoLabs implementation (sqlmm) | GL:sqlmm/area |
| `sqlmm-buffer` | Create a buffer around a polygon. | GeoLabs implementation (sqlmm) | GL:sqlmm/buffer |
| `sqlmm-centroid` | Computes the centroid of a polygon. | GeoLabs implementation (sqlmm) | GL:sqlmm/centroid |
| `sqlmm-contains` | Contains | GeoLabs implementation (sqlmm) | GL:sqlmm/contains |
| `sqlmm-convex-hull` | Compute convex hull. | GeoLabs implementation (sqlmm) | GL:sqlmm/convex-hull |
| `sqlmm-crosses` | Crosses test | GeoLabs implementation (sqlmm) | GL:sqlmm/crosses |
| `sqlmm-difference` | Compute difference. | GeoLabs implementation (sqlmm) | GL:sqlmm/difference |
| `sqlmm-disjoint` | Disjoint | GeoLabs implementation (sqlmm) | GL:sqlmm/disjoint |
| `sqlmm-equals` | Equals | GeoLabs implementation (sqlmm) | GL:sqlmm/equals |
| `sqlmm-intersection` | Compute intersection. | GeoLabs implementation (sqlmm) | GL:sqlmm/intersection |
| `sqlmm-intersects` | Intersects test | GeoLabs implementation (sqlmm) | GL:sqlmm/intersects |
| `sqlmm-is-simple` | IsSimple test | GeoLabs implementation (sqlmm) | GL:sqlmm/is-simple |
| `sqlmm-symdifference` | Compute symmetric difference. | GeoLabs implementation (sqlmm) | GL:sqlmm/symdifference |
| `sqlmm-touches` | Compute intersection. | GeoLabs implementation (sqlmm) | GL:sqlmm/touches |
| `sqlmm-union` | Compute union. | GeoLabs implementation (sqlmm) | GL:sqlmm/union |
| `sqlmm-within` | Within test | GeoLabs implementation (sqlmm) | GL:sqlmm/within |
| `symdifference` | Symmetric difference | GeoLabs generic type | GLgen:symdifference |
| `touches` | Touches | GeoLabs generic type | GLgen:touches |
| `union` | Union | GeoLabs generic type | GLgen:union |
| `vector-geometry-extent` | Get Shapes Extents | GeoLabs implementation (vector) | GL:vector/geometry-extent |
| `within` | Within | GeoLabs generic type | GLgen:within |

### raster-coverage-processing (35)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `GA008` | Band Calculation | ospd-data register item | GA008 |
| `GA010` | SEN2SR | ospd-data register item | GA010 |
| `GA011` | Mosaic | ospd-data register item | GA011 |
| `GA012` | Soil-adjusted vegetation index (SAVI) | ospd-data register item | GA012 |
| `GA013` | NDVI | ospd-data register item | GA013 |
| `GA018` | Reproject | ospd-data register item | GA018 |
| `GA026` | Distance-to-feature calculation | ospd-data register item | GA026 |
| `GA027` | Zonal raster statistics | ospd-data register item | GA027 |
| `GA028` | Raster sampling at points | ospd-data register item | GA028 |
| `GA032` | Raster analysis | ospd-data register item | GA032 |
| `ZonalStatistics` | Zonal statistics | openscience (Katerina) | OS:ZonalStatistics |
| `band-math` | Outputs a monoband image which is the result of a mathematic | GeoLabs implementation (raster) | GL:raster/band-math |
| `band-math-multiband` | This application performs mathematical operations on several | GeoLabs implementation (raster) | GL:raster/band-math-multiband |
| `calculate-band` | Performs a calculation with bands. | GeoLabs implementation (algae-bloom) | GL:algae-bloom/calculate-band |
| `calculate-indices` | Compute NDVI, NDWI and SAVI | GeoLabs implementation (kindgrove-steps) | GL:kindgrove-steps/calculate-indices |
| `extent` | Extracts an image envelope. | GeoLabs implementation (raster) | GL:raster/extent |
| `extract-roi` | Extract a ROI defined by the user. | GeoLabs implementation (raster) | GL:raster/extract-roi |
| `format-conversion` | Convert raster data from one format to another. | GeoLabs implementation (raster) | GL:raster/format-conversion |
| `norm-diff` | Normalized difference between two rasters | GeoLabs implementation (water-bodies) | GL:water-bodies/norm-diff |
| `otsu` | Otsu binary threshold | GeoLabs implementation (water-bodies) | GL:water-bodies/otsu |
| `otsu-thresholding` | Otsu thresholding | GeoLabs generic type | GLgen:otsu-thresholding |
| `plot-image` | Plots an image with colors. | GeoLabs implementation (algae-bloom) | GL:algae-bloom/plot-image |
| `radiometric-index` | Radiometric index | GeoLabs generic type | GLgen:radiometric-index |
| `raster-band-math` | Raster band math | GeoLabs generic type | GLgen:raster-band-math |
| `raster-band-math-multiband` | Raster band math (multi-band output) | GeoLabs generic type | GLgen:raster-band-math-multiband |
| `raster-crop` | Raster crop | GeoLabs generic type | GLgen:raster-crop |
| `raster-extent` | Raster extent | GeoLabs generic type | GLgen:raster-extent |
| `raster-format-conversion` | Raster format conversion | GeoLabs generic type | GLgen:raster-format-conversion |
| `raster-radiometric-index` | Compute radiometric indices. | GeoLabs implementation (raster) | GL:raster/radiometric-index |
| `raster-rendering` | Raster rendering | GeoLabs generic type | GLgen:raster-rendering |
| `raster-reprojection` | Raster reprojection | GeoLabs generic type | GLgen:raster-reprojection |
| `raster-resampling` | Raster resampling | GeoLabs generic type | GLgen:raster-resampling |
| `reproject-band` | Reproject a raster onto a regular grid | GeoLabs implementation (kindgrove-steps) | GL:kindgrove-steps/reproject-band |
| `reproject-image` | Performs image reprojection. | GeoLabs implementation (algae-bloom) | GL:algae-bloom/reproject-image |
| `reprojection` | GDAL Warp Tool | GeoLabs implementation (raster) | GL:raster/reprojection |

### earth-observation (25)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `GA014` | Cloud cover | ospd-data register item | GA014 |
| `GA015` | Cloud mask distance | ospd-data register item | GA015 |
| `GA016` | Best available pixel (BAP) | ospd-data register item | GA016 |
| `band-retrieval` | Band retrieval | GeoLabs generic type | GLgen:band-retrieval |
| `crop` | Crop a Sentinel-2 COG band to an area of interest | GeoLabs implementation (water-bodies) | GL:water-bodies/crop |
| `detect-water-body` | Water body detection based on NDWI and otsu threshold | GeoLabs implementation (water-bodies) | GL:water-bodies/detect-water-body |
| `download-band` | Download one Sentinel-2 band over a bounding box | GeoLabs implementation (kindgrove-steps) | GL:kindgrove-steps/download-band |
| `download-band-sentinel2-product-safe` | Downloads Copernicus products. | GeoLabs implementation (algae-bloom) | GL:algae-bloom/download-band-sentinel2-product-safe |
| `download-band-sentinel2-stac-item` | Downloads Sentinel-2 GeoTiff from STAC Item. | GeoLabs implementation (algae-bloom) | GL:algae-bloom/download-band-sentinel2-stac-item |
| `estimate-biomass` | Mangrove detection, allometric biomass and IPCC carbon stock | GeoLabs implementation (kindgrove-steps) | GL:kindgrove-steps/estimate-biomass |
| `export-stac` | Plot the biomass map and export a STAC catalog | GeoLabs implementation (kindgrove-steps) | GL:kindgrove-steps/export-stac |
| `mangrove` | Mangrove biomass and carbon estimation | GeoLabs implementation (kindgrove) | GL:kindgrove/mangrove |
| `mangrove-workflow` | Mangrove Biomass Workflow | GeoLabs implementation (kindgrove) | GL:kindgrove/mangrove-workflow |
| `mangrove-workflow-steps` | Mangrove Biomass Workflow (step notebooks) | GeoLabs implementation (kindgrove-steps) | GL:kindgrove-steps/mangrove-workflow-steps |
| `parse-aoi` | Parse area of interest | GeoLabs implementation (kindgrove) | GL:kindgrove/parse-aoi |
| `parse-aoi-steps` | Parse area of interest | GeoLabs implementation (kindgrove-steps) | GL:kindgrove-steps/parse-aoi-steps |
| `product-selection` | Product selection | GeoLabs generic type | GLgen:product-selection |
| `select-products-sentinel2` | Searches the specified catalog for Sentinel-2 products match | GeoLabs implementation (algae-bloom) | GL:algae-bloom/select-products-sentinel2 |
| `select-scene` | Select the least cloudy Sentinel-2 L2A scene | GeoLabs implementation (kindgrove-steps) | GL:kindgrove-steps/select-scene |
| `stac` | Assemble a STAC catalog of detected water bodies | GeoLabs implementation (water-bodies) | GL:water-bodies/stac |
| `water-bodies` | Water bodies detection based on NDWI and otsu threshold | GeoLabs implementation (water-bodies) | GL:water-bodies/water-bodies |
| `workflow-copernicus` | Algae bloom for water quality assessment on Sentinel-2 image | GeoLabs implementation (algae-bloom) | GL:algae-bloom/workflow-copernicus |
| `workflow-copernicus-process` | Processing on Sentinel-2 bands to evaluate algae bloom. | GeoLabs implementation (algae-bloom) | GL:algae-bloom/workflow-copernicus-process |
| `workflow-earth-search` | Algae bloom for water quality assessment on Sentinel-2 L2A i | GeoLabs implementation (algae-bloom) | GL:algae-bloom/workflow-earth-search |
| `workflow-earth-search-process` | Processing on Sentinel-2 L2A bands to evaluate algae bloom. | GeoLabs implementation (algae-bloom) | GL:algae-bloom/workflow-earth-search-process |

### terrain-and-hydrology (17)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `GA021` | Slope derivation | ospd-data register item | GA021 |
| `GA022` | D8 flow-direction derivation | ospd-data register item | GA022 |
| `GA023` | D8 flow-accumulation derivation | ospd-data register item | GA023 |
| `GA024` | Watershed/catchment delineation | ospd-data register item | GA024 |
| `GA025` | Stream-network extraction | ospd-data register item | GA025 |
| `GA030` | Terrain analysis | ospd-data register item | GA030 |
| `GA031` | Hydrological analysis | ospd-data register item | GA031 |
| `GA034` | Hydrological DEM conditioning | ospd-data register item | GA034 |
| `GA035` | Topographic Wetness Index calculation | ospd-data register item | GA035 |
| `analytical-hillshading` | Analytical hillshading | GeoLabs generic type | GLgen:analytical-hillshading |
| `hillshading` | Analytical Hillshading | GeoLabs implementation (terrain) | GL:terrain/hillshading |
| `slope` | Slope | GeoLabs generic type | GLgen:slope |
| `terrain-ruggedness-index` | Terrain ruggedness index | GeoLabs generic type | GLgen:terrain-ruggedness-index |
| `terrain-slope` | Slope, Aspect, Curvature | GeoLabs implementation (terrain) | GL:terrain/slope |
| `terrain-terrain-ruggedness-index` | Terrain Ruggedness Index (TRI) | GeoLabs implementation (terrain) | GL:terrain/terrain-ruggedness-index |
| `terrain-topographic-position-index` | Topographic Position Index (TPI) | GeoLabs implementation (terrain) | GL:terrain/topographic-position-index |
| `topographic-position-index` | Topographic position index | GeoLabs generic type | GLgen:topographic-position-index |

### information-extraction-and-retrieval (13)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `GA037` | FAS Source Fetch | ospd-data register item | GA037 |
| `GA038` | FAS Code Decode | ospd-data register item | GA038 |
| `GA039` | FAS Geolocate | ospd-data register item | GA039 |
| `GA040` | NLP Entity Extraction | ospd-data register item | GA040 |
| `GA041` | Geotag | ospd-data register item | GA041 |
| `GA042` | Commodity Classification | ospd-data register item | GA042 |
| `GA043` | Region Classification | ospd-data register item | GA043 |
| `GA044` | Field Normalization | ospd-data register item | GA044 |
| `GA045` | Retrieve | ospd-data register item | GA045 |
| `GA046` | Generate | ospd-data register item | GA046 |
| `GA047` | Data Acquisition | ospd-data register item | GA047 |
| `GA048` | Text Metadata Enrichment | ospd-data register item | GA048 |
| `GA049` | Retrieval-Augmented Generation | ospd-data register item | GA049 |

### ml-and-statistical-modeling (6)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `GA007` | Regression | ospd-data register item | GA007 |
| `GA009` | ML Climate Variable Downscaling | ospd-data register item | GA009 |
| `GA017` | Seasonal Sen’s Slope | ospd-data register item | GA017 |
| `InferenceExecution` | Inference execution without an asserted register action | CRIM | CRIM:InferenceExecution |
| `climate-downscaling` | Climate-variable downscaling | CRIM | CRIM:activity-type/climate-downscaling |
| `climate-downscaling-inference` | U-Net RDPS-to-HRDPS downscaling inference | CRIM | CRIM:activity-type/climate-downscaling-inference |

### point-cloud-processing (6)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `point-cloud-thinning` | Point cloud thinning (simple) | GeoLabs generic type | GLgen:point-cloud-thinning |
| `point-cloud-to-grid` | Point cloud to grid | GeoLabs generic type | GLgen:point-cloud-to-grid |
| `point-cloud-to-shapes` | Point cloud to shapes | GeoLabs generic type | GLgen:point-cloud-to-shapes |
| `pointcloud-point-cloud-thinning` | Point Cloud Thinning (Simple) | GeoLabs implementation (pointcloud) | GL:pointcloud/point-cloud-thinning |
| `pointcloud-point-cloud-to-grid` | Point Cloud to Grid | GeoLabs implementation (pointcloud) | GL:pointcloud/point-cloud-to-grid |
| `pointcloud-point-cloud-to-shapes` | Point Cloud to Shapes | GeoLabs implementation (pointcloud) | GL:pointcloud/point-cloud-to-shapes |

### spatial-indexing (3)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `GA029` | DGGS cell indexing | ospd-data register item | GA029 |
| `GA033` | Spatial indexing | ospd-data register item | GA033 |
| `GA036` | Polygon-to-DGGS cell conversion | ospd-data register item | GA036 |

### workflow-and-scoring (3)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `ScoringAndProgressTracking` | Scoring and progress tracking | openscience (Katerina) | OS:ScoringAndProgressTracking |
| `WeightedScoringAndClassification` | Weighted scoring and classification | openscience (Katerina) | OS:WeightedScoringAndClassification |
| `WorkflowRun` | Workflow run | openscience (rss-hydro) | RH:WorkflowRun |

### unassigned (7)

| New slug | Name | Origin | Old IRI |
|---|---|---|---|
| `Geoprocessing` | Geoprocessing | openscience (Katerina) | OS:Geoprocessing |
| `MissingOutput` |  | test fixture | https://example.org/test/MissingOutput |
| `NonSpatial` |  | test fixture | https://example.org/test/NonSpatial |
| `roofer-convert-format-v1` |  | Geonovum process endpoint | https://processes.staging.roofer-online.nl/ogcapi/processes/roofer:con |
| `roofer-reconstruct-buildings-v1` |  | Geonovum process endpoint | https://processes.staging.roofer-online.nl/ogcapi/processes/roofer:rec |
| `roofer-validate-point-cloud-v1` |  | Geonovum process endpoint | https://processes.staging.roofer-online.nl/ogcapi/processes/roofer:val |
| `subsidence-subsidence` |  | Geonovum process endpoint | https://registry.playground.planspace.nl/processes/subsidence_subsiden |

## Appendix B. Duplicate groups

| Group | Role | Conf. | IRI | Rationale |
|---|---|---|---|---|
| buffer | canonical | high | GLgen:buffer | Generic buffer: "all points whose distance from this geometric object is less than or equal to" a distance; richest definition. |
| buffer | duplicate | high | GA001 | GA001 Buffer: "creates a zone of a specified distance around or inside an input geometry"; same operation as generic buffer, different scheme. |
| buffer | implements | high | GL:sqlmm/buffer | "return a feature collection representing the buffer of geometry InputPolygon at distance"; broader is generic buffer. |
| convex-hull | canonical | high | GLgen:convex-hull | Generic: "convex hull of this Geometry". |
| convex-hull | duplicate | high | GA006 | GA006 Convex Hull: "smallest convex polygon containing all the vertecies"; same concept. |
| convex-hull | implements | high | GL:sqlmm/convex-hull | "feature collection that represents the convex hull of geometry InputPolygon"; broader is generic convex-hull. |
| convex-hull | related | medium | GA005 | GA005 Concave Hull lists GA006 as related; sibling operation, not the same. |
| geometry-difference | canonical | high | GLgen:difference | Generic: "point set difference of this geometric object with anotherGeometry". |
| geometry-difference | duplicate | medium | GA019 | GA019 Difference: "difference between two geometries"; terse, but same operation name and operands. |
| geometry-difference | implements | high | GL:sqlmm/difference | "closure of the set difference between the..."; broader is generic difference. |
| geometry-extent | canonical | medium | GLgen:geometry-extent | Generic: "minimum bounding rectangle of a set of input geometries, as a geometry". |
| geometry-extent | duplicate | medium | GA003 | GA003 Envelope: "smallest rectangle with sides parallel to the coordinate axes that contains all the vertecies"; describes the axis-aligned bounding b |
| geometry-extent | implements | high | GL:vector/geometry-extent | "Get Shapes Extents"; broader is generic geometry-extent. |
| geometry-extent | related | low | GLgen:raster-extent | "bounding envelope of a raster coverage, as a vector polygon"; same output idea but raster input. |
| reprojection | canonical | high | GLgen:raster-reprojection | Generic: "Reprojects a raster coverage to another coordinate reference system, resampling pixel values". |
| reprojection | related | medium | GA018 | GA018 Reproject: "Reproject data from one CRS to another"; same operation but data type unspecified (more general than raster). |
| reprojection | implements | high | GL:raster/reprojection | "gdalwarp ... can reproject to any"; broader is generic raster-reprojection. |
| reprojection | implements | medium | GL:kindgrove-steps/reproject-band | "Reprojects a raster onto a regular grid covering a bounding box"; its broader lists raster-reprojection plus an invalid https://example.org/not-an-ac |
| reprojection | related | medium | GL:algae-bloom/reproject-image | "Performs a reprojection over image bands"; but its broader is raster-resampling, which looks mismatched with the name and text; human decision. |
| band-math | canonical | high | GLgen:raster-band-math | Generic: "mathematical expression per pixel across one or more input rasters". |
| band-math | duplicate | medium | GA008 | GA008 Band Calculation: "calculation over imagery bands ... using the specified band arithmetic"; same idea, imagery-specific wording. |
| band-math | implements | high | GL:raster/band-math | "mathematical operation on several multi-band images"; broader is generic raster-band-math. |
| band-math | implements | high | GL:algae-bloom/calculate-band | "Performs a calculation over JPEG bands and returns the resulting GeoTiff"; broader is raster-band-math. |
| band-math | related | medium | GLgen:raster-band-math-multiband | Vector-valued variant of band math (multi-band output). |
| radiometric-index | canonical | high | GLgen:radiometric-index | Generic: "one or more named radiometric indices (e.g. NDVI, NDWI, SAVI)". |
| radiometric-index | related | medium | GA013 | GA013 NDVI is one specific index named in the generic; narrower, child of GA008. |
| radiometric-index | related | medium | GA012 | GA012 SAVI is one specific index named in the generic; narrower, child of GA008. |
| radiometric-index | implements | high | GL:raster/radiometric-index | "computes radiometric indices using the relevant channels"; broader is radiometric-index. |
| radiometric-index | implements | high | GL:kindgrove-steps/calculate-indices | "Computes NDVI, NDWI and SAVI from Sentinel-2 red, green and NIR bands"; broader is radiometric-index. |
| radiometric-index | implements | medium | GL:water-bodies/norm-diff | "normalized difference index ((A-B)/(A+B))"; broader is radiometric-index. |
| slope | canonical | high | GLgen:slope | Generic: "slope gradient of an elevation model at each cell". |
| slope | duplicate | medium | GA021 | GA021 Slope derivation: "rate of elevation change for each cell in an input elevation raster, expressed as degrees or percent"; same concept (generic  |
| slope | implements | high | GL:terrain/slope | "Slope, Aspect, Curvature"; broader is generic slope; also computes aspect/curvature. |
| terrain-cluster | related | medium | GA030 | GA030 Terrain analysis (no description) is the broader of GA021. |
| terrain-cluster | related | low | GLgen:terrain-ruggedness-index | Terrain index from elevation grids; sibling of slope. |
| terrain-cluster | related | low | GLgen:topographic-position-index | Terrain index from elevation grids; sibling of slope. |
| terrain-cluster | related | low | GLgen:analytical-hillshading | Terrain derivative from elevation grid. |
| terrain-cluster | related | medium | GA021 | Slope derivation, child of GA030. |
| hydrology-cluster | related | medium | GA031 | GA031 Hydrological analysis (no description) is broader of GA022-GA025. |
| hydrology-cluster | related | medium | GA022 | D8 flow direction; broader GA031. |
| hydrology-cluster | related | medium | GA023 | D8 flow accumulation "following an input D8 flow-direction raster"; consumes GA022 output. |
| hydrology-cluster | related | medium | GA024 | Watershed delineation "using a flow-direction or flow-accumulation" raster. |
| hydrology-cluster | related | medium | GA025 | Stream extraction "from a flow-accumulation raster". |
| hydrology-cluster | related | low | GA034 | Hydrological DEM conditioning (no description); name suggests it precedes flow direction. |
| hydrology-cluster | related | low | GA035 | Topographic Wetness Index calculation (no description); hydrology/terrain topic. |
| zonal-statistics | canonical | medium | GA027 | GA027 Zonal raster statistics: "summary statistics ... for raster cells within each input polygon"; richest. |
| zonal-statistics | duplicate | medium | OS:ZonalStatistics | openscience Zonal statistics: "Aggregates a gridded source per zone, skipping nodata cells"; same concept. |
| zonal-statistics | related | low | OS:WeightedScoringAndClassification | Consumes "zonal statistics" as input indicators; a downstream step, not the same. |
| raster-analysis-cluster | related | medium | GA032 | GA032 Raster analysis (no description) broader of GA026-GA028. |
| raster-analysis-cluster | related | medium | GA026 | Distance-to-feature; broader GA032. |
| raster-analysis-cluster | related | medium | GA027 | Zonal stats; broader GA032. |
| raster-analysis-cluster | related | medium | GA028 | Raster sampling at points; broader GA032. |
| dggs-cluster | related | medium | GA033 | GA033 Spatial indexing is broader of GA029. |
| dggs-cluster | related | medium | GA029 | DGGS cell indexing: "Quantizes input spatial positions or geometries to cells". |
| dggs-cluster | related | low | GA036 | Polygon-to-DGGS cell conversion (no description); likely overlaps GA029 for geometries, human check. |
| climate-downscaling | canonical | medium | GA009 | GA009 ML Climate Variable Downscaling has the fuller description. |
| climate-downscaling | duplicate | medium | CRIM:activity-type/climate-downscaling | CRIM "Climate-variable downscaling" (no description); same name concept as GA009, which is ML-specific. |
| climate-downscaling | implements | low | CRIM:activity-type/climate-downscaling-inference | "U-Net RDPS-to-HRDPS downscaling inference"; broader is CRIM climate-downscaling. |
| resolution-enhancement | related | low | GA010 | GA010 SEN2SR: "enhances the spatial resolution of raster imagery". |
| resolution-enhancement | related | low | GLgen:raster-resampling | "Changes the cell size of a raster coverage"; resampling vs super-resolution differ, uncertain. |
| resolution-enhancement | related | low | GA009 | Downscaling also increases resolution, but of climate model output. |
| bap-cluster | related | medium | GA016 | GA016 BAP lists GA012-GA015 as related. |
| bap-cluster | related | medium | GA014 | Cloud cover, related of GA016 (no description). |
| bap-cluster | related | medium | GA015 | Cloud mask distance, related of GA016 (no description). |
| bap-cluster | related | low | GA012 | SAVI, related of GA016. |
| bap-cluster | related | low | GA013 | NDVI, related of GA016. |
| bap-cluster | related | low | GA017 | Seasonal Sen's Slope lists GA016 as related. |
| geometry-envelopes | related | medium | GA002 | GA002 Boundary; GA003/GA004 list it as broader. |
| geometry-envelopes | related | medium | GA003 | Envelope, related GA004. |
| geometry-envelopes | related | medium | GA004 | Bounding Circle, related GA003. |
| geometry-envelopes | related | medium | GA005 | Concave Hull, related GA006. |
| geometry-envelopes | related | medium | GA006 | Convex Hull, related GA005. |
| set-operations | related | medium | GLgen:union | Point set union. |
| set-operations | related | medium | GLgen:intersection | Point set intersection. |
| set-operations | related | medium | GLgen:difference | Point set difference. |
| set-operations | related | medium | GLgen:symdifference | Point set symmetric difference. |
| set-operations | related | low | GA019 | GA019 Difference. |
| spatial-predicates | related | medium | GLgen:contains | Contains; "The converse" of within. |
| spatial-predicates | related | medium | GLgen:within | Within; converse of Contains. |
| spatial-predicates | related | medium | GLgen:disjoint | Disjoint, complementary to intersects. |
| spatial-predicates | related | medium | GLgen:intersects | Intersects. |
| spatial-predicates | related | medium | GLgen:touches | Touches. |
| spatial-predicates | related | medium | GLgen:crosses | Crosses. |
| spatial-predicates | related | medium | GLgen:equals | Equals. |
| point-cloud | related | low | GLgen:point-cloud-thinning | Point cloud processing. |
| point-cloud | related | low | GLgen:point-cloud-to-grid | Point cloud processing. |
| point-cloud | related | low | GLgen:point-cloud-to-shapes | Point cloud processing. |
| s2-band-retrieval-impls | canonical | medium | GLgen:band-retrieval | Generic: "Retrieves one band ... of an Earth observation product as a raster". |
| s2-band-retrieval-impls | implements | medium | GL:algae-bloom/download-band-sentinel2-stac-item | "Downloads the GeoTiff band from the Sentinel-2 product STAC Item"; near-identical to kindgrove-steps/download-band, tool-specific. |
| s2-band-retrieval-impls | implements | medium | GL:kindgrove-steps/download-band | "Downloads one Sentinel-2 band over a bounding box from a STAC Item". |
| s2-band-retrieval-impls | implements | low | GL:water-bodies/crop | "Cloud-native windowed read of one Sentinel-2 COG band asset of a STAC item"; includes cropping. |
| s2-product-selection-impls | canonical | medium | GLgen:product-selection | Generic: selects EO products from a catalogue by footprint. |
| s2-product-selection-impls | implements | medium | GL:algae-bloom/select-products-sentinel2 | "Searches a catalog for Sentinel-2 products"; returns all matches. |
| s2-product-selection-impls | implements | medium | GL:kindgrove-steps/select-scene | "Selects the least cloudy Sentinel-2 L2A scene"; picks one, so narrower than the algae-bloom variant. |
| parse-aoi | canonical | high | GL:kindgrove/parse-aoi | "Unpacks an OGC bounding box (EOAP BBox custom type) into west, south, east and north coordinates." |
| parse-aoi | duplicate | high | GL:kindgrove-steps/parse-aoi-steps | "Splits an OGC bounding box into its west, south, east and north coordinates"; same function in the step-notebook variant. |
| mangrove-workflow | canonical | medium | GL:kindgrove/mangrove-workflow | "Workflow for Mangrove Biomass Analysis"; same-named workflow as the steps variant. |
| mangrove-workflow | duplicate | medium | GL:kindgrove-steps/mangrove-workflow-steps | "Mangrove above-ground biomass and carbon stock estimation from Sentinel-2 L2A, split into one CommandLineTool" per step; same analysis, different pac |
| mangrove-workflow | related | medium | GL:kindgrove/mangrove | "Detects mangroves ... and estimates above-ground biomass"; the same analysis as one tool. |
| mangrove-workflow | related | low | GL:kindgrove-steps/estimate-biomass | "Detects mangrove pixels and estimates above-ground biomass"; the step version of the same analysis. |
| water-bodies-detection | canonical | high | GL:water-bodies/water-bodies | "Water bodies detection based on NDWI and otsu threshold applied to Sentinel-2 COG STAC items"; richest. |
| water-bodies-detection | duplicate | high | GL:water-bodies/detect-water-body | "Water body detection based on NDWI and otsu threshold"; same wording, singular. |
| algae-bloom-workflows | related | medium | GL:algae-bloom/workflow-copernicus | Algae bloom on Copernicus; same analysis, different catalog. |
| algae-bloom-workflows | related | medium | GL:algae-bloom/workflow-earth-search | Algae bloom on Earth-Search; same analysis, different catalog. |
| algae-bloom-workflows | related | medium | GL:algae-bloom/workflow-copernicus-process | Processing step of the Copernicus workflow. |
| algae-bloom-workflows | related | medium | GL:algae-bloom/workflow-earth-search-process | Processing step of the Earth-Search workflow. |
| scoring-openscience | related | low | OS:ScoringAndProgressTracking | Combines scores per zone and tracks status. |
| scoring-openscience | related | low | OS:WeightedScoringAndClassification | Combines weighted indicators into score and level per zone; both "per zone" scoring, overlap uncertain. |
| geolocation | related | medium | GA039 | GA039 Geolocate: "Country / place-name -> GeoJSON geometry lookup via a gazetteer". |
| geolocation | related | medium | GA041 | GA041 Geotag: "Place-name mention -> coordinate lookup"; similar function in a different pipeline; possible duplicate. |

## Appendix C. Aliases, gaps and other references

| Kind | Old IRI | Maps to | Notes |
|---|---|---|---|
| alias | CRIMsnap:algae-bloom/calculate-band | ospd:calculate-band |  |
| alias | CRIMsnap:algae-bloom/download-band-sentinel2-product-safe | ospd:download-band-sentinel2-product-safe |  |
| alias | CRIMsnap:algae-bloom/download-band-sentinel2-stac-item | ospd:download-band-sentinel2-stac-item |  |
| alias | CRIMsnap:algae-bloom/plot-image | ospd:plot-image |  |
| alias | CRIMsnap:algae-bloom/reproject-image | ospd:reproject-image |  |
| alias | CRIMsnap:algae-bloom/select-products-sentinel2 | ospd:select-products-sentinel2 |  |
| alias | CRIMsnap:algae-bloom/workflow-copernicus | ospd:workflow-copernicus |  |
| alias | CRIMsnap:algae-bloom/workflow-copernicus-process | ospd:workflow-copernicus-process |  |
| alias | CRIMsnap:algae-bloom/workflow-earth-search | ospd:workflow-earth-search |  |
| alias | CRIMsnap:algae-bloom/workflow-earth-search-process | ospd:workflow-earth-search-process |  |
| alias | CRIMsnap:kindgrove-steps/calculate-indices | ospd:calculate-indices |  |
| alias | CRIMsnap:kindgrove-steps/download-band | ospd:download-band |  |
| alias | CRIMsnap:kindgrove-steps/estimate-biomass | ospd:estimate-biomass |  |
| alias | CRIMsnap:kindgrove-steps/export-stac | ospd:export-stac |  |
| alias | CRIMsnap:kindgrove-steps/mangrove-workflow-steps | ospd:mangrove-workflow-steps |  |
| alias | CRIMsnap:kindgrove-steps/parse-aoi-steps | ospd:parse-aoi-steps |  |
| alias | CRIMsnap:kindgrove-steps/reproject-band | ospd:reproject-band |  |
| alias | CRIMsnap:kindgrove-steps/select-scene | ospd:select-scene |  |
| alias | CRIMsnap:kindgrove/mangrove | ospd:mangrove |  |
| alias | CRIMsnap:kindgrove/mangrove-workflow | ospd:mangrove-workflow |  |
| alias | CRIMsnap:kindgrove/parse-aoi | ospd:parse-aoi |  |
| alias | CRIMsnap:water-bodies/crop | ospd:crop |  |
| alias | CRIMsnap:water-bodies/detect-water-body | ospd:detect-water-body |  |
| alias | CRIMsnap:water-bodies/norm-diff | ospd:norm-diff |  |
| alias | CRIMsnap:water-bodies/otsu | ospd:otsu |  |
| alias | CRIMsnap:water-bodies/stac | ospd:stac |  |
| alias | CRIMsnap:water-bodies/water-bodies | ospd:water-bodies |  |
| alias | KW:demo:GA001 | ospd:GA001 |  |
| alias | KW:demo:GA016 | ospd:GA016 |  |
| alias | KW:demo:GA017 | ospd:GA017 |  |
| alias | KW:demo:GA018 | ospd:GA018 |  |
| alias | KW:demo:GA019 | ospd:GA019 |  |
| alias | KW:demo:GA020 | ospd:GA020 |  |
| gap | OS:classification | ospd:classification | referenced in examples; no definition |
| gap | OS:index-composition | ospd:index-composition | referenced in examples; no definition |
| gap | OS:index-normalisation | ospd:index-normalisation | referenced in examples; no definition |
| gap | OS:ingest | ospd:ingest | referenced in examples; no definition |
| gap | OS:model-inference | ospd:model-inference | referenced in examples; no definition |
| gap | OS:model-training | ospd:model-training | referenced in examples; no definition |
| gap | OS:standardised-index | ospd:standardised-index | referenced in examples; no definition |
| gap | https://w3id.org/ogc/rim/activity-type/WorkflowRun | ospd:WorkflowRun | no definition; possible alias of https://rss-hydro.lu/ns/mom/WorkflowRun (to rev |
| gap-example-local | http://example.org/myActivityTypes/InitialSurvey |  | type local to an example; decide whether to define or leave |
| gap-example-local | http://example.org/myActivityTypes/Registration |  | type local to an example; decide whether to define or leave |
| gap-example-local | https://example.com/stac/example1/InitialSurvey |  | type local to an example; decide whether to define or leave |
| gap-example-local | https://example.org/cool-spots#acquireData |  | type local to an example; decide whether to define or leave |
| gap-example-local | https://example.org/cool-spots#defineInputs |  | type local to an example; decide whether to define or leave |
| gap-example-local | https://example.org/cool-spots#exportOutputs |  | type local to an example; decide whether to define or leave |
| gap-example-local | https://example.org/cool-spots#geocodeCity |  | type local to an example; decide whether to define or leave |
| gap-example-local | https://example.org/openeo#BatchJob |  | type local to an example; decide whether to define or leave |
| gap-example-local | https://example.org/vegetation-productivity#CogConversion |  | type local to an example; decide whether to define or leave |
| gap-example-local | https://example.org/vegetation-productivity#PostProcessing |  | type local to an example; decide whether to define or leave |
| gap-example-local | https://example.org/vegetation-productivity#StacMetadataCreation |  | type local to an example; decide whether to define or leave |
| external | http://purl.org/wf4ever/wfdesc#Process |  | external vocabulary; not mapped |
| external | http://purl.org/wf4ever/wfdesc#ProcessRun |  | external vocabulary; not mapped |
| external | http://purl.org/wf4ever/wfprov#ProcessRun |  | external vocabulary; not mapped |
| external | http://purl.org/wf4ever/wfprov#WorkflowEngine |  | external vocabulary; not mapped |
| external | http://purl.org/wf4ever/wfprov#WorkflowRun |  | external vocabulary; not mapped |
| external | http://purl.org/wf4ever/wfprov#experiment |  | external vocabulary; not mapped |
| external | http://xmlns.com/foaf/0.1/OnlineAccount |  | external vocabulary; not mapped |
| external | https://purl.org/geojson/vocab#Feature |  | external vocabulary; not mapped |
| external | https://w3id.org/ogc/rim/activity-type/ActivityType |  | external vocabulary; not mapped |
| external | wfprov:ProcessRun |  | external vocabulary; not mapped |
| external | wfprov:WorkflowEngine |  | external vocabulary; not mapped |
| external | wfprov:WorkflowRun |  | external vocabulary; not mapped |
