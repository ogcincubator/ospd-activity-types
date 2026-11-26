# OSPD Activity Types Register

The activity types of the OGC Open Science Persistent Demonstrator (OSPD), published as an
[OGC Building Blocks](https://ogcincubator.github.io/bblocks-docs/) register: the **generic activity types**, grouped into
families, and the model they are described with: the activity type profiles of the Registered Item Model
(`_sources/profiles/`). It supersedes the [Activity Type Register](https://github.com/ogcincubator/activity-type-register).

- Persistent URIs: `https://w3id.org/ogc/ospd/activity-type/<slug>`
- Blocks: *OSPD Activity Types Register* (`_sources/core/`: the OSPD catalog and the catalog of the generic types) and one
  block per family (`_sources/generic/<family>/`: its concept scheme and types, as Turtle), including *SQL/MM spatial operations*
- Specific types (a tool, product or workflow) are defined by the participant registers, forked into ogcincubator and loaded
  from there; an OSPD-specific type with no participant register goes in `_sources/specific/<family>/`
- Data: uploaded to the OSPD Prez instance on build
- Review tables: [`docs/analysis`](docs/analysis)
- Guide to the layers, new projects and promotion: [`docs/activity-type-registers.md`](docs/activity-type-registers.md)

See `SECURITY.md` and `USAGE.md` (from the bblock-template) for build and viewing instructions.
