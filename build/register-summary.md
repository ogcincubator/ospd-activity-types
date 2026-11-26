# OSPD Activity Types Register

The activity types of the OGC Open Science Persistent Demonstrator (OSPD), under stable
`https://w3id.org/ogc/ospd/activity-type/` URIs: the generic activity types, grouped into families.


The activity types of OSPD and the model they are described with: the activity type, geoprocessing and
machine learning profiles of the Registered Item Model (`profiles/`), the catalogs (`core/`) and the generic
activity types, one block and one concept scheme per family (`generic/<family>`). Specific types are defined
by the participant registers, loaded from their ogcincubator forks, and point to a generic type with
`skos:broader`. This register supersedes the [Activity Type Register](https://ogcincubator.github.io/activity-type-register/).


## Building Blocks

### `ogc.register.ospd.profiles.activity-types` — Activity Types Register Profile

**Type:** model

A profile of the Registered Item Model for governed activity type records in the acttype:ActivityType hierarchy, with related PROV object types and an optional plan.

### `ogc.register.ospd.core` — OSPD Activity Types Register

**Type:** model

The catalogs of the OSPD activity types: the OSPD catalog and, in it, the catalog of the generic activity types, one concept scheme per family. Participant registers specialise the generic types.

### `ogc.register.ospd.profiles.geoprocessing-activity-types` — Geoprocessing Activity Types Profile

**Type:** model

A profile of the Activity Type Register Profile for geoprocessing activity types: registered sub-classes of geoproc:GeoprocessingActivityType, each required to use or generate at least one GeoSPARQL spatial data type.

### `ogc.register.ospd.generic.data-conversion` — Data conversion

**Type:** model

Activities that change the encoding or the spatial model of data without changing the information it carries.

### `ogc.register.ospd.generic.earth-observation` — Earth observation

**Type:** model

Earth-observation data access and applications: Sentinel-2 band retrieval and product selection, cloud and best-available-pixel handling. The water-bodies, algae-bloom and mangrove-biomass workflows that use them are defined by the participant registers.

### `ogc.register.ospd.generic.information-extraction-and-retrieval` — Information extraction and retrieval

**Type:** model

Source acquisition, text metadata enrichment (entity extraction, geotagging, classification, normalization) and retrieval-augmented generation.

### `ogc.register.ospd.generic.ml-and-statistical-modeling` — Machine learning and statistical modeling

**Type:** model

Machine-learning and statistical activities: regression, climate-variable downscaling, super-resolution and trend analysis, and inference executions.

### `ogc.register.ospd.generic.point-cloud-processing` — Point-cloud processing

**Type:** model

Point-cloud thinning, gridding and conversion to shapes.

### `ogc.register.ospd.generic.raster-coverage-processing` — Raster and coverage processing

**Type:** model

Operations on rasters and coverages: reprojection, resampling, cropping, mosaicking, format conversion, rendering, band math, spectral indices and zonal analysis.

### `ogc.register.ospd.generic.spatial-indexing` — Spatial indexing

**Type:** model

Discrete global grid system (DGGS) indexing and conversion of geometries to grid cells.

### `ogc.register.ospd.generic.sqlmm` — SQL/MM spatial operations

**Type:** model

The spatial operations and predicates on geometries defined by ISO/IEC 13249-3 (SQL/MM Spatial) and OGC Simple Features Access: area, buffer, centroid, convex hull, the set operations and the spatial relation tests. Each specialises a grouping type of vector geometry processing.

### `ogc.register.ospd.generic.terrain-and-hydrology` — Terrain and hydrology

**Type:** model

Terrain derivatives (slope, hillshading, ruggedness and position indices) and hydrological analysis (flow direction and accumulation, watersheds, stream networks, wetness index).

### `ogc.register.ospd.generic.vector-geometry-processing` — Vector geometry processing

**Type:** model

Operations and tests on vector geometries: buffers, hulls, envelopes, set operations, spatial predicates and extents. The SQL/MM operations are a block of their own (ogc.register.ospd.generic.sqlmm).

### `ogc.register.ospd.generic.workflow-and-scoring` — Workflow and scoring

**Type:** model

Workflow runs and scoring or classification activities used in the model-of-models and workflow examples.

### `ogc.register.ospd.profiles.st-ml-activity-types` — SpatioTemporal ML Activity Types Profile

**Type:** model

A profile of the SpatioTemporal Machine learning Activity Types Profile describing spatiotemporal machine learning training and inference runs, and registrable ML activity types, using the STAC MLM extension's task, framework/accelerator and input/output vocabulary.

### `ogc.register.ospd.profiles.schemas.activity-types-schema` — Activity Types Register Profile Schema

**Type:** schema

This is a schema representation of the ogc.register.ospd.profiles.activity-types model

### `ogc.register.ospd.specific.data-conversion` — OSPD specific activity types: data conversion

**Type:** model

Activity types contributed by OSPD participants that specialise the generic types of data conversion (ogc.register.ospd.generic.data-conversion).

### `ogc.register.ospd.specific.earth-observation` — OSPD specific activity types: earth observation

**Type:** model

Activity types contributed by OSPD participants that specialise the generic types of earth observation (ogc.register.ospd.generic.earth-observation).

### `ogc.register.ospd.specific.information-extraction-and-retrieval` — OSPD specific activity types: information extraction and retrieval

**Type:** model

Activity types contributed by OSPD participants that specialise the generic types of information extraction and retrieval (ogc.register.ospd.generic.information-extraction-and-retrieval).

### `ogc.register.ospd.specific.ml-and-statistical-modeling` — OSPD specific activity types: machine learning and statistical modeling

**Type:** model

Activity types contributed by OSPD participants that specialise the generic types of machine learning and statistical modeling (ogc.register.ospd.generic.ml-and-statistical-modeling).

### `ogc.register.ospd.specific.raster-coverage-processing` — OSPD specific activity types: raster and coverage processing

**Type:** model

Activity types contributed by OSPD participants that specialise the generic types of raster and coverage processing (ogc.register.ospd.generic.raster-coverage-processing).

### `ogc.register.ospd.specific.spatial-indexing` — OSPD specific activity types: spatial indexing

**Type:** model

Activity types contributed by OSPD participants that specialise the generic types of spatial indexing (ogc.register.ospd.generic.spatial-indexing).

### `ogc.register.ospd.specific.vector-geometry-processing` — OSPD specific activity types: vector geometry processing

**Type:** model

Activity types contributed by OSPD participants that specialise the generic types of vector geometry processing (ogc.register.ospd.generic.vector-geometry-processing).

### `ogc.register.ospd.specific.workflow-and-scoring` — OSPD specific activity types: workflow and scoring

**Type:** model

Activity types contributed by OSPD participants that specialise the generic types of workflow and scoring (ogc.register.ospd.generic.workflow-and-scoring).

### `ogc.register.ospd.profiles.schemas.geoprocessing-activity-types-schema` — Geoprocessing Activity Types Profile Schema

**Type:** schema

This is a schema representation of the ogc.register.ospd.profiles.geoprocessing-activity-types model

### `ogc.register.ospd.profiles.schemas.st-ml-activity-types-schema` — SpatioTemporal ML Activity Types Profile Schema

**Type:** schema

This is a schema representation of the ogc.register.ospd.profiles.st-ml-activity-types model

