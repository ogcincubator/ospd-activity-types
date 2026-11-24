# Duplicate detection prompt (OSPD activity types)

Input: `definitions.csv` (one row per defined activity type: iri, name, description, broader, related, version, citation, url, in_register, repos).
Task: find activity types that describe the same or near-same concept under different IRIs, and groups of types that overlap.
Output: `duplicates.csv` with columns group_id, iri, role (canonical|duplicate|related), confidence (high|medium|low), rationale.
Rules: flag, never force a merge; use only name/description/broader/related/citation as evidence; prefer the richest definition as canonical; list uncertain pairs as `related` with low confidence; note scheme differences (GAnnn items, GeoLabs process-type, CRIM activity-type, example.org process-types, Geonovum process endpoints).
