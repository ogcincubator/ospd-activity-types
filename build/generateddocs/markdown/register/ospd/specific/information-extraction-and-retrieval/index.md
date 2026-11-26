
# OSPD specific activity types: information extraction and retrieval (Model)

`ogc.register.ospd.specific.information-extraction-and-retrieval` *v0.1*

Activity types contributed by OSPD participants that specialise the generic types of information extraction and retrieval (ogc.register.ospd.generic.information-extraction-and-retrieval).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD specific activity types: information extraction and retrieval

Activity types contributed by OSPD participants that specialise the generic types of information extraction and retrieval (ogc.register.ospd.generic.information-extraction-and-retrieval).

This block has 1 specific activity types, each the specialisation (`skos:broader`) of a generic type of
[Information extraction and retrieval](https://w3id.org/ogc/ospd/activity-type/families/information-extraction-and-retrieval). It is a profile of that family's block, whose
shapes it inherits, and adds a warning for a type without a generic parent. Its data resource (`data.ttl`) is uploaded to
the OSPD Prez instance when the register is built.

## Activity types

- [Satellite observation discovery](https://w3id.org/ogc/ospd/activity-type/lightning2earthcare-observation-discovery) (`lightning2earthcare-observation-discovery`)

## Examples

### Satellite observation discovery
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

ospd:lightning2earthcare-observation-discovery a skos:Concept,
        acttype:ActivityType ;
    dcterms:source <https://github.com/sunnydean/lightning2earthcare/blob/be63866b12733db5ef7349205d36d8af8ea937f1/cwl/ospd2026/registry/geoprocessing-activities.jsonld#L34> ;
    rdfs:subClassOf ospd:catalogue-search ;
    skos:broader ospd:catalogue-search ;
    skos:definition "Finds EarthCARE products and lightning sources that meet the time, coverage and product requirements of a run."@en ;
    skos:inScheme ospd-specific:information-extraction-and-retrieval ;
    skos:notation "selection" ;
    skos:note "Contributed to OSPD 2026 by lightning2earthcare (sunnydean); defined here (decision of 26 Nov 2026). Evidence in dcterms:source."@en ;
    skos:prefLabel "Satellite observation discovery"@en ;
    skos:topConceptOf ospd-specific:information-extraction-and-retrieval ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/lightning2earthcare-observation-discovery"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/specific-activity-types/information-extraction-and-retrieval> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/specific/information-extraction-and-retrieval`

