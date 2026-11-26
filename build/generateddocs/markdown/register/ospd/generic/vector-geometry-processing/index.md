
# Vector geometry processing (Model)

`ogc.register.ospd.generic.vector-geometry-processing` *v0.1*

Operations and tests on vector geometries: buffers, hulls, envelopes, set operations, spatial predicates and extents. The SQL/MM operations are a block of their own (ogc.register.ospd.generic.sqlmm).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Vector geometry processing

Operations and tests on vector geometries: buffers, hulls, envelopes, set operations, spatial predicates and extents. The SQL/MM operations are a block of their own (ogc.register.ospd.generic.sqlmm).

This family has 15 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Boundary](https://w3id.org/ogc/ospd/activity-type/GA002) (`GA002`)
- [Bounding Circle](https://w3id.org/ogc/ospd/activity-type/GA004) (`GA004`)
- [Buffer](https://w3id.org/ogc/ospd/activity-type/GA001) (`GA001`)
- [Concave Hull](https://w3id.org/ogc/ospd/activity-type/GA005) (`GA005`)
- [Convex Hull](https://w3id.org/ogc/ospd/activity-type/GA006) (`GA006`)
- [Difference](https://w3id.org/ogc/ospd/activity-type/GA019) (`GA019`)
- [Envelope](https://w3id.org/ogc/ospd/activity-type/GA003) (`GA003`)
- [Extent computation](https://w3id.org/ogc/ospd/activity-type/extent-computation) (`extent-computation`)
- [Filter geometries](https://w3id.org/ogc/ospd/activity-type/GA020) (`GA020`)
- [Geometry construction](https://w3id.org/ogc/ospd/activity-type/geometry-construction) (`geometry-construction`)
- [Geometry extent](https://w3id.org/ogc/ospd/activity-type/geometry-extent) (`geometry-extent`)
- [Geometry measure](https://w3id.org/ogc/ospd/activity-type/geometry-measure) (`geometry-measure`)
- [Geometry property test](https://w3id.org/ogc/ospd/activity-type/geometry-property-test) (`geometry-property-test`)
- [Set operation on geometries](https://w3id.org/ogc/ospd/activity-type/set-operation) (`set-operation`)
- [Spatial relation test](https://w3id.org/ogc/ospd/activity-type/spatial-relation-test) (`spatial-relation-test`)

## Examples

### Boundary
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd:GA002 a skos:Concept,
        acttype:ActivityType ;
    dcterms:modified "2026-09-17"^^xsd:date ;
    dcterms:replaces <http://ospd/demo/GA002> ;
    dcterms:source <https://geopandas.org/en/latest/docs/reference/api/geopandas.GeoSeries.boundary.html> ;
    rdfs:subClassOf <https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType> ;
    owl:versionInfo "2" ;
    skos:definition "Boundary is a Geoprocessing Activity that returns a polygon containing the vertecies of an input geometry without any interoir rings"@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/vector-geometry-processing> ;
    skos:prefLabel "Boundary"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/vector-geometry-processing> ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/GA002"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/activity-type/families/vector-geometry-processing> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/generic/vector-geometry-processing`

