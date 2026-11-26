
# Earth observation (Model)

`ogc.register.ospd.generic.earth-observation` *v0.1*

Earth-observation data access and applications: Sentinel-2 band retrieval and product selection, cloud and best-available-pixel handling. The water-bodies, algae-bloom and mangrove-biomass workflows that use them are defined by the participant registers.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Earth observation

Earth-observation data access and applications: Sentinel-2 band retrieval and product selection, cloud and best-available-pixel handling. The water-bodies, algae-bloom and mangrove-biomass workflows that use them are defined by the participant registers.

This family has 5 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Band retrieval](https://w3id.org/ogc/ospd/activity-type/band-retrieval) (`band-retrieval`)
- [Best available pixel (BAP)](https://w3id.org/ogc/ospd/activity-type/GA016) (`GA016`)
- [Cloud cover](https://w3id.org/ogc/ospd/activity-type/GA014) (`GA014`)
- [Cloud mask distance](https://w3id.org/ogc/ospd/activity-type/GA015) (`GA015`)
- [Product selection](https://w3id.org/ogc/ospd/activity-type/product-selection) (`product-selection`)

## Examples

### Band retrieval
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd:band-retrieval a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/band-retrieval> ;
    dcterms:source [ ],
        [ ] ;
    rdfs:subClassOf <https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType> ;
    skos:definition "Retrieves one band, one range component, of an Earth observation product as a raster, over the whole product or over an area of interest, with the values the product provides, possibly converted to physical units by the scale and offset the product declares."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/earth-observation> ;
    skos:prefLabel "Band retrieval"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/earth-observation> ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/band-retrieval"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/activity-type/families/earth-observation> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/generic/earth-observation`

