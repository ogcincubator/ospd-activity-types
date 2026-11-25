# OSPD Activity Types Register

Activity types specific to the OGC Open Science Persistent Demonstrator (OSPD), under stable
`https://w3id.org/ogc/ospd/activity-type/` URIs, each specialising a generic activity type.


The OSPD-specific activity types (tool- and example-specific), as a federated register of the
[Activity Types Register](https://ogcincubator.github.io/activity-type-register/): a root block (catalog)
and a `specific` block carrying the Turtle definitions of the types, whose data is uploaded to the OSPD
Prez instance when the register is built. Each type points to its generic parent with `skos:broader`.


## Building Blocks

### `ogc.ospd.activity-type.core` — OSPD Activity Types Register

**Type:** model

The catalog of the OSPD-specific activity types: tool- and example-specific specialisations of the generic activity types of the Activity Types Register.

### `ogc.ospd.activity-type.specific` — OSPD specific activity types

**Type:** model

Activity types specific to OSPD (tool- and example-specific), each specialising a generic activity type.

