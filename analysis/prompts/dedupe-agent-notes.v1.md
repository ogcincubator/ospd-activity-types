# Dedupe agent notes

Output: `../duplicates.csv` (30 groups, 96 rows). Rows by confidence: high 18, medium 56, low 22. By role: canonical 29, duplicate 18, related 49.

## Patterns
- Cross-scheme overlap is systematic between the ospd-data GAnnn items and GeoLabs types. High-confidence pairs: Buffer, Convex Hull, Difference, Reproject, and Band Calculation (GA vs sqlmm/raster/algae-bloom). GA items are generic and GeoLabs items are tool-specific (OTB, GDAL, SAGA, SQL/MM), so GeoLabs is usually the richer definition, except for the sqlmm geometry operations where the GA text is the cleaner generic one.
- GA012 (SAVI) and GA013 (NDVI) are specific indices, whereas GeoLabs `raster/radiometric-index` is generic. They are flagged `related`, not duplicate.
- CRIM climate-downscaling types have no description. They are matched to GA009 by name only (medium).
- example.org `ZonalStatistics` duplicates GA027 (high). The other example.org scoring types are only `related` to each other.
- Within GeoLabs there are intra-scheme near-duplicates: kindgrove vs kindgrove-steps (parse-aoi, download-band vs algae-bloom, mangrove workflow) and water-bodies/detect-water-body vs water-bodies/water-bodies.
- The GeoLabs `broader` values already point to shared parents (raster-band-math, radiometric-index, band-retrieval, product-selection, raster-reprojection). These parents are not defined rows in the CSV.
- Family clusters (terrain, hydrology, DGGS, topological predicates, overlay ops, hull/boundary) are `related`.

## Left for a human to decide
- `sqlmm/touches` has name "Compute intersection." and an intersection description. This is probably a copy-paste error in the source (a predicate should be a boolean test). It is flagged as a medium duplicate of `sqlmm/intersection`, but the fix is likely to correct the metadata.
- GA039 Geolocate vs GA041 Geotag (low): same gazetteer lookup, but under different umbrellas (GA047 data acquisition vs GA048 enrichment). They may be intentionally distinct.
- Hierarchy gaps: GA034, GA035 (hydrology/terrain) and GA036 (DGGS) have no broader. GA005 and GA006 (hulls) are not under GA002 Boundary.
- Workflow-level types (algae-bloom workflow-*, kindgrove mangrove/workflow) are flagged as related, not duplicates, because the process-versus-workflow distinction is unclear.
- Several IRIs appear in more than one group (sqlmm/difference, sqlmm/intersection, ZonalStatistics, water-bodies/crop, GA003, GA006). Each group is a separate lens (duplicate vs family).
- Not analyzed because there is no name or description: Geonovum roofer/planspace endpoints (only one low-confidence IRI-slug-based link for convert_format), `example.org/test/*`, and the CRIM/openscience PROV classes (`InferenceExecution`, `WorkflowRun`, `Geoprocessing`).
