
# Spatial indexing (Model)

`ogc.ospd.activity-type.spatial-indexing` *v0.1*

Discrete global grid system (DGGS) indexing and conversion of geometries to grid cells.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Spatial indexing

Discrete global grid system (DGGS) indexing and conversion of geometries to grid cells.

This family has 3 activity types. It is a profile of the OSPD Activity Type core block and its data resource
(`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [DGGS cell indexing](https://w3id.org/ogc/ospd/activity-type/GA029) (`GA029`)
- [Polygon-to-DGGS cell conversion](https://w3id.org/ogc/ospd/activity-type/GA036) (`GA036`)
- [Spatial indexing](https://w3id.org/ogc/ospd/activity-type/GA033) (`GA033`)

## Examples

### DGGS cell indexing
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd: a skos:ConceptScheme .

ospd:GA029 a skos:Concept,
        acttype:ActivityType ;
    dcterms:modified "2026-09-17"^^xsd:date ;
    dcterms:replaces <http://ospd/demo/GA029> ;
    dcterms:source <https://www.ogc.org/standards/dggs/> ;
    owl:versionInfo "2" ;
    skos:broader ospd:GA033 ;
    skos:definition "Quantizes input spatial positions or geometries to cells at a specified resolution in a Discrete Global Grid System and returns the corresponding cell identifiers."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/spatial-indexing> ;
    skos:prefLabel "DGGS cell indexing"@en ;
    skos:related ospd:GA027,
        ospd:GA028 ;
    prov:qualifiedAttribution [ prov:agent <https://hartis.org> ;
            prov:hadRole <https://def.isotc211.org/codeset/RoleCode/custodian> ] ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/GA029"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/spatial-indexing`

