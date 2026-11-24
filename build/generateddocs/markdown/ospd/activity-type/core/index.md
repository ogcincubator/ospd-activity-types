
# OSPD Activity Type (Model)

`ogc.ospd.activity-type.core` *v0.1*

Root of the OSPD activity types: the concept scheme, catalog and family collections under https://w3id.org/ogc/ospd/activity-type/.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD Activity Type

Activity types used across the OGC Open Science Persistent Demonstrator (OSPD), consolidated under stable URIs of the
form `https://w3id.org/ogc/ospd/activity-type/<slug>`.

This block holds the concept scheme (`https://w3id.org/ogc/ospd/activity-type/`), the catalog and one `skos:Collection` per family of related activity types.
Each family is a building block that profiles this one and carries the Turtle definitions of its activity types.

Every activity type is a `skos:Concept` and an `acttype:ActivityType` (Registered Item Model), has a `skos:prefLabel`, and
records the IRIs it replaces (`dcterms:replaces`), equivalent aliases (`skos:exactMatch`) and likely duplicates
(`skos:closeMatch`).

## Families

- **Vector geometry processing** (`ogc.ospd.activity-type.vector-geometry-processing`): Operations and tests on vector geometries: buffers, hulls, envelopes, set operations, spatial predicates and extents (including the SQL/MM implementations).
- **Raster and coverage processing** (`ogc.ospd.activity-type.raster-coverage-processing`): Operations on rasters and coverages: reprojection, resampling, cropping, mosaicking, format conversion, rendering, band math, spectral indices and zonal analysis.
- **Earth observation** (`ogc.ospd.activity-type.earth-observation`): Earth-observation data access and applications: Sentinel-2 band retrieval and product selection, cloud and best-available-pixel handling, and the water-bodies, algae-bloom and mangrove-biomass workflows.
- **Terrain and hydrology** (`ogc.ospd.activity-type.terrain-and-hydrology`): Terrain derivatives (slope, hillshading, ruggedness and position indices) and hydrological analysis (flow direction and accumulation, watersheds, stream networks, wetness index).
- **Spatial indexing** (`ogc.ospd.activity-type.spatial-indexing`): Discrete global grid system (DGGS) indexing and conversion of geometries to grid cells.
- **Point-cloud processing** (`ogc.ospd.activity-type.point-cloud-processing`): Point-cloud thinning, gridding and conversion to shapes.
- **Machine learning and statistical modeling** (`ogc.ospd.activity-type.ml-and-statistical-modeling`): Machine-learning and statistical activities: regression, climate-variable downscaling, super-resolution and trend analysis, and inference executions.
- **Information extraction and retrieval** (`ogc.ospd.activity-type.information-extraction-and-retrieval`): Source acquisition, text metadata enrichment (entity extraction, geotagging, classification, normalization) and retrieval-augmented generation.
- **Workflow and scoring** (`ogc.ospd.activity-type.workflow-and-scoring`): Workflow runs and scoring or classification activities used in the model-of-models and workflow examples.

## Examples

### Concept scheme with a family collection
#### turtle
```turtle
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .

ospd: a skos:ConceptScheme ;
    skos:prefLabel "OSPD Activity Types"@en .

<https://w3id.org/ogc/ospd/activity-type/families/vector-geometry-processing> a skos:Collection ;
    skos:prefLabel "Vector geometry processing"@en .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/core`

