
# Point-cloud processing (Model)

`ogc.register.ospd.generic.point-cloud-processing` *v0.1*

Point-cloud thinning, gridding and conversion to shapes.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Point-cloud processing

Point-cloud thinning, gridding and conversion to shapes.

This family has 4 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Point cloud filtering](https://w3id.org/ogc/ospd/activity-type/point-cloud-filtering) (`point-cloud-filtering`)
- [Point cloud thinning (simple)](https://w3id.org/ogc/ospd/activity-type/point-cloud-thinning) (`point-cloud-thinning`)
- [Point cloud to grid](https://w3id.org/ogc/ospd/activity-type/point-cloud-to-grid) (`point-cloud-to-grid`)
- [Point cloud to shapes](https://w3id.org/ogc/ospd/activity-type/point-cloud-to-shapes) (`point-cloud-to-shapes`)

## Examples

### Point cloud thinning (simple)
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd:point-cloud-thinning a skos:Concept,
        acttype:ActivityType ;
    rdfs:subClassOf <https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType> ;
    skos:definition "Reduces the number of points to the given percentage by sequential point removal, which suits points stored in chronological order best."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/point-cloud-processing> ;
    skos:prefLabel "Point cloud thinning (simple)"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/point-cloud-processing> ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/point-cloud-thinning"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/activity-type/families/point-cloud-processing> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/generic/point-cloud-processing`

