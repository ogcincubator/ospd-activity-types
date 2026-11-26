
# SQL/MM spatial operations (Model)

`ogc.register.ospd.generic.sqlmm` *v0.1*

The spatial operations and predicates on geometries defined by ISO/IEC 13249-3 (SQL/MM Spatial) and OGC Simple Features Access: area, buffer, centroid, convex hull, the set operations and the spatial relation tests. Each specialises a grouping type of vector geometry processing.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# SQL/MM spatial operations

The spatial operations and predicates on geometries defined by ISO/IEC 13249-3 (SQL/MM Spatial) and OGC Simple Features Access: area, buffer, centroid, convex hull, the set operations and the spatial relation tests. Each specialises a grouping type of vector geometry processing.

This family has 16 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Area](https://w3id.org/ogc/ospd/activity-type/area) (`area`)
- [Buffer](https://w3id.org/ogc/ospd/activity-type/buffer) (`buffer`)
- [Centroid](https://w3id.org/ogc/ospd/activity-type/centroid) (`centroid`)
- [Contains](https://w3id.org/ogc/ospd/activity-type/contains) (`contains`)
- [Convex hull](https://w3id.org/ogc/ospd/activity-type/convex-hull) (`convex-hull`)
- [Crosses](https://w3id.org/ogc/ospd/activity-type/crosses) (`crosses`)
- [Difference](https://w3id.org/ogc/ospd/activity-type/difference) (`difference`)
- [Disjoint](https://w3id.org/ogc/ospd/activity-type/disjoint) (`disjoint`)
- [Equals](https://w3id.org/ogc/ospd/activity-type/equals) (`equals`)
- [Intersection](https://w3id.org/ogc/ospd/activity-type/intersection) (`intersection`)
- [Intersects](https://w3id.org/ogc/ospd/activity-type/intersects) (`intersects`)
- [Is simple](https://w3id.org/ogc/ospd/activity-type/is-simple) (`is-simple`)
- [Symmetric difference](https://w3id.org/ogc/ospd/activity-type/symdifference) (`symdifference`)
- [Touches](https://w3id.org/ogc/ospd/activity-type/touches) (`touches`)
- [Union](https://w3id.org/ogc/ospd/activity-type/union) (`union`)
- [Within](https://w3id.org/ogc/ospd/activity-type/within) (`within`)

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

ospd:area a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/area> ;
    dcterms:source [ ],
        [ ] ;
    rdfs:subClassOf ospd:geometry-measure ;
    skos:broader ospd:geometry-measure ;
    skos:definition "The area of this Surface, as measured in the spatial reference system of this Surface."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/sqlmm> ;
    skos:prefLabel "Area"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/sqlmm> ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/area"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/activity-type/families/sqlmm> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/generic/sqlmm`

