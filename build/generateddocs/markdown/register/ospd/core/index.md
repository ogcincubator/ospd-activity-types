
# OSPD Activity Types Register (Model)

`ogc.register.ospd.core` *v0.1*

The catalogs of the OSPD activity types: the OSPD catalog and, in it, the catalog of the generic activity types, one concept scheme per family. Participant registers specialise the generic types.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD Activity Types Register

The activity types of the OGC Open Science Persistent Demonstrator (OSPD), under stable URIs of the form
`https://w3id.org/ogc/ospd/activity-type/<slug>`.

This block holds two catalogs: the OSPD catalog (`https://w3id.org/ogc/ospd/catalog`) and, in it, the catalog of the generic
activity types (`https://w3id.org/ogc/ospd/activity-type/catalog`), which lists one `skos:ConceptScheme` per family of related
types. Each family is a building block under `generic/` that profiles this one and carries its concept scheme and the Turtle
definitions of its types. This block is a profile of the activity type profile
(`profiles/activity-types`, `ogc.register.ospd.profiles.activity-types`), whose SHACL shapes it inherits; its own shapes
add a label, a concept scheme and (as a warning) a definition.

Every activity type is a `skos:Concept` and an `acttype:ActivityType` (Registered Item Model), has a `skos:prefLabel`, and
records the IRIs it replaces (`dcterms:replaces`), equivalent aliases (`skos:exactMatch`) and likely duplicates
(`skos:closeMatch`).

**Specific types** (a tool, product or workflow) are defined by the participant registers, loaded from their ogcincubator
forks; they point to their generic parent with `skos:broader`, and the parent lists them with `skos:narrower`. They are not
repeated here. Specific types contributed to OSPD directly are in blocks `specific/<family>/`
(`ogc.register.ospd.specific.<family>`), using the same families.

## Families

- **Vector geometry processing** (`ogc.register.ospd.generic.vector-geometry-processing`): Operations and tests on vector geometries: buffers, hulls, envelopes, set operations, spatial predicates and extents. The SQL/MM operations are a block of their own (ogc.register.ospd.generic.sqlmm).
- **SQL/MM spatial operations** (`ogc.register.ospd.generic.sqlmm`): The spatial operations and predicates on geometries defined by ISO/IEC 13249-3 (SQL/MM Spatial) and OGC Simple Features Access: area, buffer, centroid, convex hull, the set operations and the spatial relation tests. Each specialises a grouping type of vector geometry processing.
- **Raster and coverage processing** (`ogc.register.ospd.generic.raster-coverage-processing`): Operations on rasters and coverages: reprojection, resampling, cropping, mosaicking, format conversion, rendering, band math, spectral indices and zonal analysis.
- **Data conversion** (`ogc.register.ospd.generic.data-conversion`): Activities that change the encoding or the spatial model of data without changing the information it carries.
- **Earth observation** (`ogc.register.ospd.generic.earth-observation`): Earth-observation data access and applications: Sentinel-2 band retrieval and product selection, cloud and best-available-pixel handling. The water-bodies, algae-bloom and mangrove-biomass workflows that use them are defined by the participant registers.
- **Terrain and hydrology** (`ogc.register.ospd.generic.terrain-and-hydrology`): Terrain derivatives (slope, hillshading, ruggedness and position indices) and hydrological analysis (flow direction and accumulation, watersheds, stream networks, wetness index).
- **Spatial indexing** (`ogc.register.ospd.generic.spatial-indexing`): Discrete global grid system (DGGS) indexing and conversion of geometries to grid cells.
- **Point-cloud processing** (`ogc.register.ospd.generic.point-cloud-processing`): Point-cloud thinning, gridding and conversion to shapes.
- **Machine learning and statistical modeling** (`ogc.register.ospd.generic.ml-and-statistical-modeling`): Machine-learning and statistical activities: regression, climate-variable downscaling, super-resolution and trend analysis, and inference executions.
- **Information extraction and retrieval** (`ogc.register.ospd.generic.information-extraction-and-retrieval`): Source acquisition, text metadata enrichment (entity extraction, geotagging, classification, normalization) and retrieval-augmented generation.
- **Workflow and scoring** (`ogc.register.ospd.generic.workflow-and-scoring`): Workflow runs and scoring or classification activities used in the model-of-models and workflow examples.

## Specific blocks

Activity types contributed by OSPD participants without a register of their own (Hartis, lightning2earthcare, KindGrove,
Aganitha, 52North),
one block per generic family:

- **OSPD specific activity types: data conversion** (`ogc.register.ospd.specific.data-conversion`): `cool-spots-output-export`, `lightning2earthcare-feature-construction`
- **OSPD specific activity types: earth observation** (`ogc.register.ospd.specific.earth-observation`): `lightning2earthcare-observation-matching`, `lightning2earthcare-storm-characterisation`
- **OSPD specific activity types: information extraction and retrieval** (`ogc.register.ospd.specific.information-extraction-and-retrieval`): `lightning2earthcare-observation-discovery`
- **OSPD specific activity types: machine learning and statistical modeling** (`ogc.register.ospd.specific.ml-and-statistical-modeling`): `aganitha-standardised-index`
- **OSPD specific activity types: raster and coverage processing** (`ogc.register.ospd.specific.raster-coverage-processing`): `cvi-elevation-analysis`, `cvi-land-cover-analysis`
- **OSPD specific activity types: spatial indexing** (`ogc.register.ospd.specific.spatial-indexing`): `kindgrove-stac-fingerprint`
- **OSPD specific activity types: vector geometry processing** (`ogc.register.ospd.specific.vector-geometry-processing`): `cvi-coastline-extraction`, `cvi-erosion-data-integration`, `cvi-transect-generation`
- **OSPD specific activity types: workflow and scoring** (`ogc.register.ospd.specific.workflow-and-scoring`): `aganitha-drought-classification`, `aganitha-index-normalisation`, `cvi-configuration-validation`, `cvi-vulnerability-index-scoring`

## Examples

### OSPD catalog, generic catalog and a family concept scheme
#### turtle
```turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://w3id.org/ogc/ospd/catalog> a dcat:Catalog ;
    dcterms:title "OSPD Activity Types Register"@en ;
    dcterms:hasPart <https://w3id.org/ogc/ospd/activity-type/catalog> .

<https://w3id.org/ogc/ospd/activity-type/catalog> a dcat:Catalog ;
    dcterms:title "Generic activity types"@en ;
    dcterms:hasPart <https://w3id.org/ogc/ospd/activity-type/families/vector-geometry-processing> .

<https://w3id.org/ogc/ospd/activity-type/families/vector-geometry-processing> a skos:ConceptScheme ;
    skos:prefLabel "Vector geometry processing"@en .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/core`

