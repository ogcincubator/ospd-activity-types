# Duplicate detection prompt (OSPD activity types), v2

Input: `definitions.csv` (157 rows, one per defined activity type: iri, name, description, broader, related, version, citation, url, in_register, repos).
Task: find activity types that describe the same or near-same concept under different IRIs, and clusters of closely related types.
Distinguish two relations, because GeoLabs uses three tiers:
 - `duplicate`: same concept, different IRIs, same level (e.g. GA register item vs GA register item, CRIM vs GeoLabs snapshot, openscience vs GA).
 - `implements`: an implementation-level type (GeoLabs `process-profiles/process-type/<group>/<slug>`, tool-specific) realizes a generic type (GeoLabs `generic-profiles/activity-type/<slug>`) or a GA register item. This is NOT a duplicate; record it as role `implements` pointing at the generic/GA canonical.
Output: `duplicates.csv` with columns group_id, iri, role (canonical|duplicate|implements|related), confidence (high|medium|low), rationale.
Rules: flag, never force a merge; use only name/description/broader/related/citation as evidence; prefer the richest definition as canonical; uncertain pairs are `related` with low confidence; one row per IRI per group; groups of size >= 2.
Known issues to keep out of the groups (record in notes instead): GeoLabs `sqlmm/touches` has intersection metadata (copy-paste error); `raster/band-math` and `raster/band-math-multiband` have identical descriptions.
