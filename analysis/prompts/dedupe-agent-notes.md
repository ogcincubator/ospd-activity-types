# Dedupe notes (v2 run)

Output: `duplicates.csv`, 110 rows in 28 groups.

Counts by role: related 66, implements 18, canonical 15, duplicate 11.
Counts by confidence: high 23, medium 64, low 23.
By role and confidence: canonical high 9 / medium 6; duplicate high 4 / medium 7; implements high 10 / medium 6 / low 2; related medium 45 / low 21.

## Patterns
- Cross-scheme GA vs generic: GA001 Buffer, GA006 Convex Hull (high); GA019 Difference, GA021 Slope, GA008 Band Calculation, GA003 Envelope vs geometry-extent (medium). The generic is canonical because its definition is richer; GA items are the duplicates.
- GA018 Reproject is only `related` to raster-reprojection (data type unspecified). GA012 SAVI and GA013 NDVI are `related` to generic radiometric-index (they are single indices it names).
- `implements` is recorded only where a GA/generic group exists or where it clarifies siblings (sqlmm buffer, convex-hull, difference; raster/band-math; Sentinel-2 download/selection impls).
- Same-level duplicates found only in GeoLabs impls (kindgrove parse-aoi vs parse-aoi-steps; water-bodies vs detect-water-body; mangrove workflow vs steps) and GA027 vs openscience ZonalStatistics. GA009 vs CRIM climate-downscaling is medium.
- Clusters (no canonical, all `related`): terrain, hydrology (GA022-25, 31, 34, 35), raster analysis, DGGS, BAP, geometry envelopes, set operations, spatial predicates, point cloud, algae-bloom workflows.

## Needs a human decision
- GA003 Envelope vs generic geometry-extent: GA003 speaks of one geometry, generic of a set of geometries.
- GA039 Geolocate vs GA041 Geotag: likely overlapping functions in two pipelines.
- GA036 Polygon-to-DGGS vs GA029 DGGS cell indexing: GA036 has no description.
- `algae-bloom/reproject-image` has broader raster-resampling, probably should be raster-reprojection.
- `kindgrove-steps/reproject-band` broader includes invalid `https://example.org/not-an-activity-type`.
- GA009 vs CRIM climate-downscaling: CRIM has no description; GA009 is ML-specific. CRIM `climate-downscaling-inference` linked as `implements` with low confidence.
- GA010 SEN2SR vs raster-resampling: low-confidence relation only.

## Known issues kept out of groups
- `sqlmm/touches` has intersection metadata (copy-paste); it is not grouped.
- `raster/band-math` and `raster/band-math-multiband` have identical impl descriptions; the multiband generic is only listed as `related`.
- The sqlmm/intersection and sqlmm/touches name "Compute intersection." collision is part of the touches issue.

## Not analyzed
- No names or descriptions, so no grouping: Geonovum roofer/planspace process URLs (4), `example.org/test/*` (2), GA014/GA015/GA030-035 (empty; grouped only by their `related`/`broader` links), `rss-hydro.lu/.../WorkflowRun` and CRIM `InferenceExecution` (no counterpart).
- No stale CRIM GeoLabs snapshot rows were present in definitions.csv (only 3 CRIM rows), so no CRIM-vs-GeoLabs duplicates were found.
- No GA counterparts found for GA002, GA004, GA007, GA011, GA020 Filter, GA037/38, GA040, GA042-46.
- I used only definitions.csv fields; Turtle files were not consulted.
