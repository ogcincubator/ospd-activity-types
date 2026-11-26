
# OSPD specific activity types: earth observation (Model)

`ogc.register.ospd.specific.earth-observation` *v0.1*

Activity types contributed by OSPD participants that specialise the generic types of earth observation (ogc.register.ospd.generic.earth-observation).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD specific activity types: earth observation

Activity types contributed by OSPD participants that specialise the generic types of earth observation (ogc.register.ospd.generic.earth-observation).

This block has 2 specific activity types, each the specialisation (`skos:broader`) of a generic type of
[Earth observation](https://w3id.org/ogc/ospd/activity-type/families/earth-observation). It is a profile of that family's block, whose
shapes it inherits, and adds a warning for a type without a generic parent. Its data resource (`data.ttl`) is uploaded to
the OSPD Prez instance when the register is built.

## Activity types

- [Multi-sensor observation matching](https://w3id.org/ogc/ospd/activity-type/lightning2earthcare-observation-matching) (`lightning2earthcare-observation-matching`) -- no generic parent yet
- [Storm characterisation](https://w3id.org/ogc/ospd/activity-type/lightning2earthcare-storm-characterisation) (`lightning2earthcare-storm-characterisation`) -- no generic parent yet

## Examples

### Multi-sensor observation matching
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

ospd:lightning2earthcare-observation-matching a skos:Concept,
        acttype:ActivityType ;
    dcterms:source <https://github.com/sunnydean/lightning2earthcare/blob/be63866b12733db5ef7349205d36d8af8ea937f1/cwl/ospd2026/registry/geoprocessing-activities.jsonld#L18> ;
    rdfs:subClassOf acttype:ActivityType ;
    skos:closeMatch ospd:GA047 ;
    skos:definition "Matches lightning observations to EarthCARE observations by location and acquisition time, accounting for parallax offsets."@en ;
    skos:inScheme ospd-specific:earth-observation ;
    skos:notation "collocation" ;
    skos:note "Contributed to OSPD 2026 by lightning2earthcare (sunnydean); defined here (decision of 26 Nov 2026). No tool-neutral generic parent yet: open question. Evidence in dcterms:source."@en ;
    skos:prefLabel "Multi-sensor observation matching"@en ;
    skos:topConceptOf ospd-specific:earth-observation ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/lightning2earthcare-observation-matching"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/specific-activity-types/earth-observation> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/specific/earth-observation`

