
# OSPD specific activity types: data conversion (Model)

`ogc.register.ospd.specific.data-conversion` *v0.1*

Activity types contributed by OSPD participants that specialise the generic types of data conversion (ogc.register.ospd.generic.data-conversion).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD specific activity types: data conversion

Activity types contributed by OSPD participants that specialise the generic types of data conversion (ogc.register.ospd.generic.data-conversion).

This block has 2 specific activity types, each the specialisation (`skos:broader`) of a generic type of
[Data conversion](https://w3id.org/ogc/ospd/activity-type/families/data-conversion). It is a profile of that family's block, whose
shapes it inherits, and adds a warning for a type without a generic parent. Its data resource (`data.ttl`) is uploaded to
the OSPD Prez instance when the register is built.

## Activity types

- [Geospatial feature construction](https://w3id.org/ogc/ospd/activity-type/lightning2earthcare-feature-construction) (`lightning2earthcare-feature-construction`)
- [Output export](https://w3id.org/ogc/ospd/activity-type/cool-spots-output-export) (`cool-spots-output-export`) -- no generic parent yet

## Examples

### Geospatial feature construction
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix ospd-specific: <https://w3id.org/ogc/ospd/specific-activity-types/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd:lightning2earthcare-feature-construction a skos:Concept,
        acttype:ActivityType ;
    dcterms:source <https://github.com/sunnydean/lightning2earthcare/blob/be63866b12733db5ef7349205d36d8af8ea937f1/cwl/ospd2026/registry/geoprocessing-activities.jsonld#L43> ;
    rdfs:subClassOf ospd:spatial-model-conversion ;
    skos:broader ospd:spatial-model-conversion ;
    skos:definition "Builds point features with measurements, times and identifiers from NetCDF observations and storm records, and writes them as GeoParquet."@en ;
    skos:inScheme ospd-specific:data-conversion ;
    skos:notation "conversion" ;
    skos:note "Contributed to OSPD 2026 by lightning2earthcare (sunnydean); defined here (decision of 26 Nov 2026). Evidence in dcterms:source."@en ;
    skos:prefLabel "Geospatial feature construction"@en ;
    skos:topConceptOf ospd-specific:data-conversion ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/lightning2earthcare-feature-construction"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/specific-activity-types/data-conversion> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/specific/data-conversion`

