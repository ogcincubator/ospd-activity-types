
# OSPD specific activity types: vector geometry processing (Model)

`ogc.register.ospd.specific.vector-geometry-processing` *v0.1*

Activity types contributed by OSPD participants that specialise the generic types of vector geometry processing (ogc.register.ospd.generic.vector-geometry-processing).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD specific activity types: vector geometry processing

Activity types contributed by OSPD participants that specialise the generic types of vector geometry processing (ogc.register.ospd.generic.vector-geometry-processing).

This block has 3 specific activity types, each the specialisation (`skos:broader`) of a generic type of
[Vector geometry processing](https://w3id.org/ogc/ospd/activity-type/families/vector-geometry-processing). It is a profile of that family's block, whose
shapes it inherits, and adds a warning for a type without a generic parent. Its data resource (`data.ttl`) is uploaded to
the OSPD Prez instance when the register is built.

## Activity types

- [Coastline extraction](https://w3id.org/ogc/ospd/activity-type/cvi-coastline-extraction) (`cvi-coastline-extraction`)
- [Erosion data integration](https://w3id.org/ogc/ospd/activity-type/cvi-erosion-data-integration) (`cvi-erosion-data-integration`) -- no generic parent yet
- [Transect generation](https://w3id.org/ogc/ospd/activity-type/cvi-transect-generation) (`cvi-transect-generation`)

## Examples

### Coastline extraction
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

ospd:cvi-coastline-extraction a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://example.org/ospd/process-types/coastline-extraction> ;
    dcterms:source <https://github.com/hartis-org/cvi-workflow/blob/b6f8e98a07be3320a2a936a23cb427009abd12d0/ospd2026/provenance/cvi_full_workflow_design_runtime_entities.json#L46> ;
    rdfs:subClassOf ospd:GA020 ;
    skos:broader ospd:GA020 ;
    skos:definition "Extracts the coastline of an area of interest from OpenStreetMap Overpass features."@en ;
    skos:inScheme ospd-specific:vector-geometry-processing ;
    skos:note "Contributed to OSPD 2026 by hartis-org (cvi-workflow); defined here (decision of 26 Nov 2026). Evidence in dcterms:source."@en ;
    skos:prefLabel "Coastline extraction"@en ;
    skos:topConceptOf ospd-specific:vector-geometry-processing ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/cvi-coastline-extraction"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/specific-activity-types/vector-geometry-processing> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/specific/vector-geometry-processing`

