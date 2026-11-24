
# Vector geometry processing (Model)

`ogc.ospd.activity-type.vector-geometry-processing` *v0.1*

Operations and tests on vector geometries: buffers, hulls, envelopes, set operations, spatial predicates and extents (including the SQL/MM implementations).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Vector geometry processing

Operations and tests on vector geometries: buffers, hulls, envelopes, set operations, spatial predicates and extents (including the SQL/MM implementations).

This family has 42 activity types. It is a profile of the OSPD Activity Type core block and its data resource
(`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Area](https://w3id.org/ogc/ospd/activity-type/area) (`area`)
- [Boundary](https://w3id.org/ogc/ospd/activity-type/GA002) (`GA002`)
- [Bounding Circle](https://w3id.org/ogc/ospd/activity-type/GA004) (`GA004`)
- [Buffer](https://w3id.org/ogc/ospd/activity-type/GA001) (`GA001`)
- [Buffer](https://w3id.org/ogc/ospd/activity-type/buffer) (`buffer`)
- [Centroid](https://w3id.org/ogc/ospd/activity-type/centroid) (`centroid`)
- [Compute convex hull.](https://w3id.org/ogc/ospd/activity-type/sqlmm-convex-hull) (`sqlmm-convex-hull`)
- [Compute difference.](https://w3id.org/ogc/ospd/activity-type/sqlmm-difference) (`sqlmm-difference`)
- [Compute geometry area.](https://w3id.org/ogc/ospd/activity-type/sqlmm-area) (`sqlmm-area`)
- [Compute intersection.](https://w3id.org/ogc/ospd/activity-type/sqlmm-intersection) (`sqlmm-intersection`)
- [Compute intersection.](https://w3id.org/ogc/ospd/activity-type/sqlmm-touches) (`sqlmm-touches`)
- [Compute symmetric difference.](https://w3id.org/ogc/ospd/activity-type/sqlmm-symdifference) (`sqlmm-symdifference`)
- [Compute union.](https://w3id.org/ogc/ospd/activity-type/sqlmm-union) (`sqlmm-union`)
- [Computes the centroid of a polygon.](https://w3id.org/ogc/ospd/activity-type/sqlmm-centroid) (`sqlmm-centroid`)
- [Concave Hull](https://w3id.org/ogc/ospd/activity-type/GA005) (`GA005`)
- [Contains](https://w3id.org/ogc/ospd/activity-type/sqlmm-contains) (`sqlmm-contains`)
- [Contains](https://w3id.org/ogc/ospd/activity-type/contains) (`contains`)
- [Convex Hull](https://w3id.org/ogc/ospd/activity-type/GA006) (`GA006`)
- [Convex hull](https://w3id.org/ogc/ospd/activity-type/convex-hull) (`convex-hull`)
- [Create a buffer around a polygon.](https://w3id.org/ogc/ospd/activity-type/sqlmm-buffer) (`sqlmm-buffer`)
- [Crosses](https://w3id.org/ogc/ospd/activity-type/crosses) (`crosses`)
- [Crosses test](https://w3id.org/ogc/ospd/activity-type/sqlmm-crosses) (`sqlmm-crosses`)
- [Difference](https://w3id.org/ogc/ospd/activity-type/GA019) (`GA019`)
- [Difference](https://w3id.org/ogc/ospd/activity-type/difference) (`difference`)
- [Disjoint](https://w3id.org/ogc/ospd/activity-type/sqlmm-disjoint) (`sqlmm-disjoint`)
- [Disjoint](https://w3id.org/ogc/ospd/activity-type/disjoint) (`disjoint`)
- [Envelope](https://w3id.org/ogc/ospd/activity-type/GA003) (`GA003`)
- [Equals](https://w3id.org/ogc/ospd/activity-type/sqlmm-equals) (`sqlmm-equals`)
- [Equals](https://w3id.org/ogc/ospd/activity-type/equals) (`equals`)
- [Filter geometries](https://w3id.org/ogc/ospd/activity-type/GA020) (`GA020`)
- [Geometry extent](https://w3id.org/ogc/ospd/activity-type/geometry-extent) (`geometry-extent`)
- [Get Shapes Extents](https://w3id.org/ogc/ospd/activity-type/vector-geometry-extent) (`vector-geometry-extent`)
- [Intersection](https://w3id.org/ogc/ospd/activity-type/intersection) (`intersection`)
- [Intersects](https://w3id.org/ogc/ospd/activity-type/intersects) (`intersects`)
- [Intersects test](https://w3id.org/ogc/ospd/activity-type/sqlmm-intersects) (`sqlmm-intersects`)
- [Is simple](https://w3id.org/ogc/ospd/activity-type/is-simple) (`is-simple`)
- [IsSimple test](https://w3id.org/ogc/ospd/activity-type/sqlmm-is-simple) (`sqlmm-is-simple`)
- [Symmetric difference](https://w3id.org/ogc/ospd/activity-type/symdifference) (`symdifference`)
- [Touches](https://w3id.org/ogc/ospd/activity-type/touches) (`touches`)
- [Union](https://w3id.org/ogc/ospd/activity-type/union) (`union`)
- [Within](https://w3id.org/ogc/ospd/activity-type/within) (`within`)
- [Within test](https://w3id.org/ogc/ospd/activity-type/sqlmm-within) (`sqlmm-within`)

## Examples

### Area
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd: a skos:ConceptScheme .

ospd:area a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/area> ;
    dcterms:source [ ],
        [ ] ;
    rdfs:subClassOf <https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType> ;
    skos:definition "The area of this Surface, as measured in the spatial reference system of this Surface."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/vector-geometry-processing> ;
    skos:prefLabel "Area"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/vector-geometry-processing> ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/area"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/vector-geometry-processing`

