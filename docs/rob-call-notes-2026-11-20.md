# OSPD activity-types consolidation

Working document for the OSPD (Open Science Persistent Demonstrator) activity-types consolidation. Status as of 2026-11-23. Origin: the 2026-11-20 call between Rob Atkinson and Alejandro (after Ingo left), plus decisions made since.

## Goal

Rob's thesis: an activity type may need a rich description (inputs, outputs, parameters, dimensions, quality, examples, profile schemas such as one suitable for OGC API Processes). Building blocks are the one packaging mechanism for this, with governance rules expressed in validation. The goal is to gather every activity type used across the OSPD material, rebase them onto stable URIs, deduplicate them, package them as building blocks per family of activity types, and publish them from an OSPD-only Prez instance so the URIs resolve.

## Background

### Sources of activity types

1. Nick's spreadsheet and the Turtle files generated from it. Rebased URIs are already part of Alejandro's plan. The spreadsheet will contain local descriptions people created.
2. Gerald's building blocks, roughly one per activity type. These are the richest and most accurate.
3. Others: ontologies in other blocks (possibly granular, possibly a set of descriptions), activity types implicit in provenance traces (for example a 52°North trace pushed as an example into bblocks-open-science), and IDs with no description.

Katerina's pull request on bblocks-open-science is merged (2026-11-23) and is now the main source of activity-type definitions: an ontology of activity types plus a "model of models" workflow, with examples, tests and a preview register. Her spreadsheet content is duplicated in it, so the spreadsheet entries for these should be deduplicated and the spreadsheet content removed once loaded. Alejandro's JSON-LD fix moved the per-run `run` prefix from the reusable `context.jsonld` to a top-level `prefixes:` key in `examples.yaml`.

### Terminology (Rob)

Activity is the generic concept. A process is a subclass of activity that runs and has an identity. The process type is the code used to invoke a process on an OGC API Processes endpoint (like a SKOS notation), so it is probably an attribute of the term's description. Procedure and observation are separate concepts and overlap only imperfectly.

### Open conceptual points from Katerina's PR

- Subclassing vs. SKOS-style mechanisms (Rob deliberately didn't over-specify; soft point).
- The "registered term" / "process type" wording in the register is confusing and probably wrong.
- Whether activity type vs. processType is a canonical key attribute or a separate implementation profile (Rob commented on the PR).
- The EarthCODE parts are to be pulled out into a separate profile (Rob).

### Expectations

Rob expects duplicates (fine) and gaps (IDs with no description). Gaps are less dangerous than they look: unmapped items still show up in a map or tabular view of a provenance trace, which makes a good smoke test (like looking at a record in pygeoapi).

## Infrastructure decisions

- **Hosting:** the OSPD-only Prez instance is live at `https://defs-hosted.opengis.net/prez-ospd` (human-friendly UI). The backend, which serves `/object`, is at `/prez-ospd-b`. Rob's condition: it can sit on defs-hosted with a different context as long as it isn't presented as hosted content. It is a persistent demonstrator node and not hosted on behalf of anybody.
- **Data loading:** the building block data will be uploaded through the SPARQL upload mechanism in the building blocks themselves.
- **Persistent URIs:** `https://w3id.org/ogc/ospd/...`. A redirect PR is open at https://github.com/perma-id/w3id.org/pull/7269 (branch `ogc-ospd` on the avillar fork). Two commits: (1) add `/ogc/ospd`, where individual URIs get a 303 to `prez-ospd-b/object?uri=https://w3id.org/ogc/ospd/<path>` and the bare root goes to `prez-ospd/`; (2) send the bare `/geopose` and `/hosted` roots to the human-friendly Prez UI (`prez-hosted/catalogs/hosted:geopose` and `prez-hosted/`). The redirects were tested locally and the three UI pages return 200. Not yet checked: what `prez-ospd-b/object` does for a URI that doesn't exist yet (it returned a 307 in a probe).
- **URI policy:** the rebased URIs must stay consistent with D4 (Identifier, Namespace, URL & Redirect Policy). The path layout under `https://w3id.org/ogc/ospd/` is not decided yet. For URI-minting, never say in shared documents or comments that provisional w3id minting needs or skips approval; just describe the two-stage path.

## Plan

1. Characterize how each activity type is defined and what identifies it. Extract metadata from Turtle, blocks or examples, and use an LLM for consolidation.
2. Rebase URIs and deduplicate.
3. Scour the repos for references and open PRs to update them.
4. Create new building blocks per family of activity types (ontology or model type) with the data attached, so the data is pushed into the new Prez/triple store instance. Rob wants these loaded as sub-registers composed into the knowledge graph, and blocks may declare a dependency on a set (for example a STAC MLM ontology with its own governance domain).
5. Host as an OSPD-only instance (done, see above).
6. Optional: a vocabulary validator that finds activity-type markers in uplifted resources and checks that they resolve to proper definitions. Rob built something similar for the 3D cadastre (a CSV mapping that generated SHACL rules automatically). A first cut is doable.

Order of attack: start with the Turtle files, since they are easier than the spreadsheet. Rob offered to review a first cut by the end of Alejandro's day and will probably work over the weekend.

## Task list

Status: Done / Partly settled / Pending / Not started.

### Phase 0: locate and inventory

1. Find the three sources: Nick's spreadsheet, the Turtle files, and Gerald's building blocks. **Pending**
2. Check Katerina's merged blocks in bblocks-open-science as a fourth input. **Pending**
3. List the "other" sources: ontologies in other blocks, activity types implicit in provenance traces, and bare IDs with no description. **Pending**

### Phase 1: characterize and extract (Turtle files first)

4. Document how each source defines an activity type and what identifies it (URI, notation, label). **Pending**
5. Write an extraction script that outputs one flat record per activity type: URI, label, description, parent class, source, and any inputs/outputs/parameters. **Pending**
6. Run it on the Turtle files, then Gerald's blocks, then Katerina's, then the spreadsheet. **Pending**
7. Use Claude for consolidation, and keep the prompts. Rob wants them or a first cut. **Pending**

### Phase 2: rebase and deduplicate

8. Define the rebased URI scheme. The namespace is `https://w3id.org/ogc/ospd/...`; the path layout under it is still to decide and must be checked against D4. **Partly settled**
9. Deduplicate across sources, flagging duplicates rather than forcing a merge, and keep a gap list of IDs with no description. **Pending**
10. Note which spreadsheet entries duplicate Katerina's blocks; once loaded, that spreadsheet content should be removed. **Pending**

### Phase 3: first cut to Rob

11. Send Rob the extraction output, the dedup/gap report and the prompts. **Pending**

### Phase 4: references and PRs

12. Search the repos for references to the old activity-type URIs (for example `w3id.org/ogc/...` variants found by Rob) and for open PRs that need updating. **Pending**

### Phase 5: new blocks and hosting

13. Create new building blocks per family of activity types, with the data attached, as sub-registers composed into the knowledge graph. **Pending**
14. Check free memory on defs-hosted. **Done**
15. Set up the OSPD-only Prez instance. **Done** (live at defs-hosted.opengis.net/prez-ospd, backend at `/prez-ospd-b`)
16. Load the blocks' data through the SPARQL upload mechanism in the blocks themselves. **Pending**, blocked on step 13.
17. Set up the w3id.org redirects. **Done**, PR #7269 awaiting review and merge.

### Phase 6: optional

18. Vocabulary validator for activity-type markers in uplifted resources. **Not started**
19. Smoke test: view a provenance trace in a map or tabular view and confirm unmapped items still show up. **Not started**

## Open points with Rob

- Whether the first cut covers all three sources or only the Turtle files.
- Subclassing vs. SKOS-style mechanisms, and the processType wording.
- The repo harvest that Rob wanted to run an LLM over hasn't been done yet; it overlaps with step 12.
- Checking that `prez-ospd-b/object` behaves sensibly for URIs not yet loaded.

## Suggested next step

Steps 1-3 and 5 on the Turtle files.
