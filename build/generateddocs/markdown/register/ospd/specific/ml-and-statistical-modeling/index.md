
# OSPD specific activity types: machine learning and statistical modeling (Model)

`ogc.register.ospd.specific.ml-and-statistical-modeling` *v0.1*

Activity types contributed by OSPD participants that specialise the generic types of machine learning and statistical modeling (ogc.register.ospd.generic.ml-and-statistical-modeling).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD specific activity types: machine learning and statistical modeling

Activity types contributed by OSPD participants that specialise the generic types of machine learning and statistical modeling (ogc.register.ospd.generic.ml-and-statistical-modeling).

This block has 1 specific activity types, each the specialisation (`skos:broader`) of a generic type of
[Machine learning and statistical modeling](https://w3id.org/ogc/ospd/activity-type/families/ml-and-statistical-modeling). It is a profile of that family's block, whose
shapes it inherits, and adds a warning for a type without a generic parent. Its data resource (`data.ttl`) is uploaded to
the OSPD Prez instance when the register is built.

## Activity types

- [Standardised precipitation index](https://w3id.org/ogc/ospd/activity-type/aganitha-standardised-index) (`aganitha-standardised-index`) -- no generic parent yet

## Examples

### Standardised precipitation index
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

ospd:aganitha-standardised-index a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://example.org/ospd/process-types/standardised-index> ;
    dcterms:source <https://github.com/ogcincubator/bblocks-openscience/blob/02f6895/_sources/prov-profiles/aganitha-ndvi/examples/spi.json#L4> ;
    rdfs:subClassOf acttype:ActivityType ;
    skos:definition "Computes the standardised precipitation index (SPI): precipitation accumulated over a period, transformed to a standard normal variable against its reference distribution."@en ;
    skos:editorialNote "Definition drafted on 26 Nov 2026 from the label and data of the example step; to be confirmed by the contributor."@en ;
    skos:inScheme ospd-specific:ml-and-statistical-modeling ;
    skos:note "Contributed to OSPD 2026 by Aganitha (bblocks-openscience aganitha-ndvi examples); defined here (decision of 26 Nov 2026). No tool-neutral generic parent yet: open question. Evidence in dcterms:source."@en ;
    skos:prefLabel "Standardised precipitation index"@en ;
    skos:topConceptOf ospd-specific:ml-and-statistical-modeling ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/aganitha-standardised-index"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/specific-activity-types/ml-and-statistical-modeling> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/specific/ml-and-statistical-modeling`

