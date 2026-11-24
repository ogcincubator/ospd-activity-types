# OSPD Activity Types

Activity types used across the OGC Open Science Persistent Demonstrator (OSPD), consolidated under
stable `https://w3id.org/ogc/ospd/activity-type/` URIs and grouped into families of related types.


A root *OSPD Activity type* block, a profile of the Registered Item Model's activity-type block, and one
sub-block (profile of the root) per family of related activity types. Each family block carries the Turtle
definitions of its activity types as a data resource, which is uploaded to the OSPD Prez instance when
the register is built.


## Building Blocks

### `ogc.ospd.activity-type.core` — OSPD Activity Type

**Type:** model

Root of the OSPD activity types: the concept scheme, catalog and family collections under https://w3id.org/ogc/ospd/activity-type/.

### `ogc.ospd.activity-type.earth-observation` — Earth observation

**Type:** model

Earth-observation data access and applications: Sentinel-2 band retrieval and product selection, cloud and best-available-pixel handling, and the water-bodies, algae-bloom and mangrove-biomass workflows.

### `ogc.ospd.activity-type.information-extraction-and-retrieval` — Information extraction and retrieval

**Type:** model

Source acquisition, text metadata enrichment (entity extraction, geotagging, classification, normalization) and retrieval-augmented generation.

### `ogc.ospd.activity-type.ml-and-statistical-modeling` — Machine learning and statistical modeling

**Type:** model

Machine-learning and statistical activities: regression, climate-variable downscaling, super-resolution and trend analysis, and inference executions.

### `ogc.ospd.activity-type.point-cloud-processing` — Point-cloud processing

**Type:** model

Point-cloud thinning, gridding and conversion to shapes.

### `ogc.ospd.activity-type.raster-coverage-processing` — Raster and coverage processing

**Type:** model

Operations on rasters and coverages: reprojection, resampling, cropping, mosaicking, format conversion, rendering, band math, spectral indices and zonal analysis.

### `ogc.ospd.activity-type.spatial-indexing` — Spatial indexing

**Type:** model

Discrete global grid system (DGGS) indexing and conversion of geometries to grid cells.

### `ogc.ospd.activity-type.terrain-and-hydrology` — Terrain and hydrology

**Type:** model

Terrain derivatives (slope, hillshading, ruggedness and position indices) and hydrological analysis (flow direction and accumulation, watersheds, stream networks, wetness index).

### `ogc.ospd.activity-type.vector-geometry-processing` — Vector geometry processing

**Type:** model

Operations and tests on vector geometries: buffers, hulls, envelopes, set operations, spatial predicates and extents (including the SQL/MM implementations).

### `ogc.ospd.activity-type.workflow-and-scoring` — Workflow and scoring

**Type:** model

Workflow runs and scoring or classification activities used in the model-of-models and workflow examples.

