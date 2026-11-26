
# OSPD specific activity types: raster and coverage processing (Model)

`ogc.register.ospd.specific.raster-coverage-processing` *v0.1*

Activity types contributed by OSPD participants that specialise the generic types of raster and coverage processing (ogc.register.ospd.generic.raster-coverage-processing).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD specific activity types: raster and coverage processing

Activity types contributed by OSPD participants that specialise the generic types of raster and coverage processing (ogc.register.ospd.generic.raster-coverage-processing).

This block has 2 specific activity types, each the specialisation (`skos:broader`) of a generic type of
[Raster and coverage processing](https://w3id.org/ogc/ospd/activity-type/families/raster-coverage-processing). It is a profile of that family's block, whose
shapes it inherits, and adds a warning for a type without a generic parent. Its data resource (`data.ttl`) is uploaded to
the OSPD Prez instance when the register is built.

## Activity types

- [Elevation analysis](https://w3id.org/ogc/ospd/activity-type/cvi-elevation-analysis) (`cvi-elevation-analysis`)
- [Land-cover analysis](https://w3id.org/ogc/ospd/activity-type/cvi-land-cover-analysis) (`cvi-land-cover-analysis`)

## Examples

### Elevation analysis
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

ospd:cvi-elevation-analysis a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://example.org/ospd/process-types/elevation-analysis> ;
    dcterms:source <https://github.com/hartis-org/cvi-workflow/blob/b6f8e98a07be3320a2a936a23cb427009abd12d0/ospd2026/provenance/cvi_full_workflow_design_runtime_entities.json#L81> ;
    rdfs:subClassOf ospd:GA028 ;
    skos:broader ospd:GA028 ;
    skos:definition "Samples Copernicus DEM elevation along the transects and scores it."@en ;
    skos:inScheme ospd-specific:raster-coverage-processing ;
    skos:note "Contributed to OSPD 2026 by hartis-org (cvi-workflow); defined here (decision of 26 Nov 2026). Evidence in dcterms:source."@en ;
    skos:prefLabel "Elevation analysis"@en ;
    skos:topConceptOf ospd-specific:raster-coverage-processing ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/cvi-elevation-analysis"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/specific-activity-types/raster-coverage-processing> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/specific/raster-coverage-processing`

