---
title: "Activity type registers: layers, new projects and promotion"
subtitle: "Draft of 2026-11-26 for discussion"
---

Provenance traces only work as linked data if the activity types they cite resolve to descriptions. This note explains how the activity type registers are layered, how a new project adds its own types, and how a project-specific type becomes a generic one.

# 1. The three layers

![The three layers and how they refer to each other](img/layers.png){ width=95% }

All repositories are under `github.com/ogcincubator`.

| Layer | Repository and block ids | What it holds |
|:------|:-------------------------|:--------------|
| **RIM** | `registered-item-model` (`ogc.rim.*`) | The Registered Item Model (ISO 19135:2026): registers, register items, statuses, governance. No activity types. Catalog: `w3id.org/ogc/rim/catalog`. |
| **Activity type profiles** | `ospd-activity-types`, `_sources/profiles/` (`ogc.register.ospd.profiles.*`) | The activity type profiles of the RIM (`acttype:ActivityType`, geoprocessing and ML profiles, JSON schemas). No activity types. Until 26 Nov 2026 in `activity-type-register`, which this register supersedes. |
| **Generic activity types** | `ospd-activity-types`, `_sources/core/` and `_sources/generic/` (`ogc.register.ospd.*`) | The **generic activity types**, grouped into **families**: one block and one `skos:ConceptScheme` per family (`generic/<family>`), among them the SQL/MM spatial operations. |
| **Specific activity types** | one register per participant, e.g. the GeoLabs process profiles or the Geonovum DTaaS register, loaded from forks in `ogcincubator`; so far only the GeoLabs one exists (`geolabs-bblocks-process-profiles`, see the worked example in section 2) | The types of one participant: tool- or example-specific **specialisations** of generic types. They are loaded from the forks and not repeated in `ospd-activity-types`. |

**How they interact**

- *Building blocks:* a participant register imports the OSPD activity types register (the profiles and the generic types), which imports the RIM (`imports` in `bblocks-config.yaml`). Its root block is `isProfileOf bblocks://ogc.register.ospd.profiles.activity-types`, so the shapes of the activity type profile apply to every type it defines.
- *Linked data:* every type is a `skos:Concept` **and** an `acttype:ActivityType` (a `rim:RegisterItem`). A specific type points to its generic parent with `skos:broader`; the parent lives in another register and is resolved by IRI.
- *Hierarchy of abstraction:* two views of one tree. For browsing, `skos:broader` goes family (concept scheme) → generic type → specific type. For reasoning, `rdfs:subClassOf` goes `acttype:ActivityType` → `geoproc:GeoprocessingActivityType` (each profile adds constraints) → generic type → specific type, so a trace typed with a specific type is also an instance of its generic parent. Not every generic type is geoprocessing: the information-extraction, workflow and ML families specialise `acttype:ActivityType` directly for now. Generic types state *what* is done, independent of tools (`buffer`, `raster-reprojection`, `workflow`); specific types name a tool, product or workflow that does it (`cvi-coastline-extraction`, `aganitha-standardised-index`) and stay as evidence of relevance for the generic one.
- *Repository layout:* `ospd-activity-types` holds the model in `_sources/profiles/` (the three profile blocks and their JSON schemas, ids `ogc.register.ospd.profiles.*`) and the content: `_sources/core/` (the catalogs, `ogc.register.ospd.core`) and `_sources/generic/<family>/` (`ogc.register.ospd.generic.<family>`); an OSPD-specific type with no participant register would go in `_sources/specific/<family>/`, using the same families. A participant register has `_sources/core/` and `_sources/specific/`, so its specific block is always `<prefix>specific`.
- *Publication:* each repository builds to GitHub Pages and uploads its ontologies and data to the shared triplestore behind the OSPD Prez instance, one graph per block, replaced on every build. The Prez shows the RIM catalog and the *OSPD Activity Types Register*, to which the participant registers belong (`dcterms:isPartOf`), and the catalog of the generic activity types, which is a catalog of its own and not part of the OSPD one.
- *Traces:* a `prov:Activity` is typed with the IRI of the most specific type that applies (`rdf:type`); queries can climb to the generic type through `skos:broader`.

**URIs.** Types are minted under `https://w3id.org/ogc/ospd/activity-type/<slug>`; generic and OSPD-specific types share this namespace for now, so a type keeps its IRI if it is promoted (section 3). Whether generic types should later move to a neutral namespace is open.

**Source of truth.** The current `data.ttl` files were generated once from the consolidation tables, which are published as snapshots in [`docs/analysis`](https://github.com/ogcincubator/ospd-activity-types/tree/main/docs/analysis) of `ospd-activity-types`. From now on they are edited **by hand**; do not regenerate them from the tables.

# 2. How a new project declares its own activity types

Example: project *Acme* defines `acme-flood-extent`.

1. **Create the register.** Use the OGC [`bblock-template`](https://github.com/opengeospatial/bblock-template) ("Use this template", not fork). Set `identifier-prefix: ogc.acme.activity-type.` and the imports:

   ```yaml
   imports:
     - default
     - https://ogcincubator.github.io/registered-item-model/build/register.json
     - https://ogcincubator.github.io/ospd-activity-types/build/register.json
   ```

   To publish into the shared Prez, add the `sparql:` section (push endpoint, an own `graph`, `resources.data: true`) and the `sparql_username`/`sparql_password` secrets.
2. **Add a root block** (`_sources/core/`) with `isProfileOf: bblocks://ogc.register.ospd.profiles.activity-types`, a `data.ttl` with the register catalog, and, only if it needs more than the profile's, SHACL shapes of its own: the profile's shapes are inherited through `isProfileOf`. Add a second block (`_sources/specific/`, `isProfileOf` the root) for the concept scheme and the types.
3. **Pick the generic parent** of each type: browse the generic register in the Prez, or its families in `ospd-activity-types/_sources/generic/<family>/data.ttl`. Prefer the narrowest generic type that is still tool-neutral. If none fits, either leave the type without parent (the shapes only warn) and open a promotion request (section 3), or propose a new generic type.
4. **Define the type** in `data.ttl`:

   ```turtle
   @prefix skos:    <http://www.w3.org/2004/02/skos/core#> .
   @prefix rdfs:    <http://www.w3.org/2000/01/rdf-schema#> .
   @prefix rim:     <https://w3id.org/ogc/rim/> .
   @prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
   @prefix xsd:     <http://www.w3.org/2001/XMLSchema#> .
   @prefix acme:    <https://w3id.org/ogc/acme/activity-type/> .
   @prefix ospd:    <https://w3id.org/ogc/ospd/activity-type/> .

   acme:flood-extent a skos:Concept, acttype:ActivityType ;
       skos:inScheme acme:scheme ;
       skos:prefLabel "Flood extent"@en ;
       skos:definition "Delineates the flooded area from a SAR scene."@en ;
       skos:broader ospd:GA032 ;                    # generic parent: "Raster analysis"
       rdfs:subClassOf ospd:GA032 ;                 # same parent, for reasoning
       rim:itemClass acttype:activityTypeItemClass ;
       rim:objectIdentifier "https://w3id.org/ogc/acme/activity-type/flood-extent"^^xsd:anyURI ;
       rim:validityStatus rim:valid ;
       rim:publicationStatus rim:published .
   ```

   Required: the two types, `rim:itemClass`, `rim:objectIdentifier` and the two statuses (RIM shapes), `skos:prefLabel` and `skos:inScheme`. Recommended: `skos:definition`, and `skos:broader` plus `rdfs:subClassOf` to the generic parent. Optional: `dcterms:source`, `rdfs:seeAlso`, `prov:qualifiedAttribution`, `skos:closeMatch` to similar types elsewhere.
5. **Choose the URI namespace.** Use the project's own w3id prefix (a pull request to `perma-id/w3id.org`, as done for `/ogc/ospd`). OSPD participants adding types to the OSPD register keep `.../ogc/ospd/activity-type/<slug>`.
6. **Build and publish.** `./build.sh`, fix validation errors, push to `main`: CI validates, deploys Pages and uploads the data. Cite the new IRI as the `rdf:type` of your `prov:Activity` instances.

**Worked example: GeoLabs.** `ogcincubator/geolabs-bblocks-process-profiles` is a fork of `GeoLabs/bblocks-process-profiles` that acts as a downstream register of this one.

- *Namespace:* `https://w3id.org/ogc/ospd/geolabs/` is used as if GeoLabs controlled it (a pretence for the demonstrator).
- *What it defines:* only what is specific to GeoLabs, the 58 process types (`activity-type/<group>-<slug>`, e.g. `sqlmm-contains`), in one concept scheme and one `dcat:Catalog` (`.../geolabs/catalog`, `dcterms:isPartOf` the OSPD catalog). The generic types GeoLabs used to define are not repeated: every reference to them points at the OSPD IRI.
- *Links point upwards:* each process type has `skos:broadMatch` (another concept scheme) and `rdfs:subClassOf` to its OSPD parent, and no `skos:broader`. This register does not point at the downstream one, so the old `dcterms:replaces` and `skos:*Match` statements to GeoLabs IRIs were removed from it.
- *Publication:* the fork has its own `sparql:` section (own graph, same Fuseki) and CI, with the secrets `sparql_username` and `sparql_password`. On a new fork, enable Actions and run the workflow once with *Run workflow*: the first push run is skipped by the template guard.
- *Alternative:* to define the remapped generic types in the participant register too, bind each to its OSPD type with `skos:closeMatch` or `skos:broadMatch`; the fork's `alignment/` has the data and the instructions.

# 3. Promoting a specific type to a generic one

*Proposed process, for Rob's review.* A type is a candidate when it is tool-neutral and used, or clearly needed, by more than one project or tool.

1. **Request.** Open an issue or pull request in `ospd-activity-types` naming the type, its definition, the family it belongs to, and the evidence (the specific types and traces that use it).
2. **Move it, do not copy it.** Add the concept to `_sources/generic/<family>/data.ttl` and **remove it from the project's `data.ttl`**: one IRI must have one definition.
   - *Same namespace* (OSPD): the IRI does not change, so existing traces and `skos:broader` links keep working.
   - *Own namespace* (e.g. `acme:`): mint `.../ogc/ospd/activity-type/<slug>` for the generic type, record the old IRI with `dcterms:replaces` and `skos:exactMatch`, and let the project type specialise it (`skos:broader`) or retire it.
   - Drop project-specific detail from the definition; keep the originals as evidence (`dcterms:source`, `skos:narrower` or `skos:closeMatch`).
3. **New family, if needed.** Create `_sources/generic/<new-family>/` with a `bblock.json` (`isProfileOf: bblocks://ogc.register.ospd.core`, a data resource `data.ttl`), a `data.ttl` that defines the `skos:ConceptScheme` `.../activity-type/families/<new-family>` (with `skos:hasTopConcept` / `skos:topConceptOf`) and the concepts, a `description.md` and an `examples.yaml`. Add the scheme to `dcterms:hasPart` of the generic catalog in `_sources/core/data.ttl`.
4. **Merge order.** Generic register first, then the project register, so that `skos:broader` links resolve when both are uploaded. Each upload replaces its graphs, so the removal from the project graph needs no extra step.
5. **Check.** Both builds pass; the type shows in the new family in the Prez and its former specific siblings link to it.

**Open points:** who decides a promotion (suggestion: the maintainers of the generic register, with the proposing project's agreement); whether generic types get their own namespace; whether generic types should also carry the PROV constraints of the profile (`acttype:usedEntityType`, `acttype:generatedEntityType`, ...), which today only the profile blocks define.
