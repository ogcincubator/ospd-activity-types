
# OSPD specific activity types: workflow and scoring (Model)

`ogc.register.ospd.specific.workflow-and-scoring` *v0.1*

Activity types contributed by OSPD participants that specialise the generic types of workflow and scoring (ogc.register.ospd.generic.workflow-and-scoring).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD specific activity types: workflow and scoring

Activity types contributed by OSPD participants that specialise the generic types of workflow and scoring (ogc.register.ospd.generic.workflow-and-scoring).

This block has 4 specific activity types, each the specialisation (`skos:broader`) of a generic type of
[Workflow and scoring](https://w3id.org/ogc/ospd/activity-type/families/workflow-and-scoring). It is a profile of that family's block, whose
shapes it inherits, and adds a warning for a type without a generic parent. Its data resource (`data.ttl`) is uploaded to
the OSPD Prez instance when the register is built.

## Activity types

- [Configuration validation](https://w3id.org/ogc/ospd/activity-type/cvi-configuration-validation) (`cvi-configuration-validation`)
- [Drought severity classification](https://w3id.org/ogc/ospd/activity-type/aganitha-drought-classification) (`aganitha-drought-classification`) -- no generic parent yet
- [Indicator normalisation](https://w3id.org/ogc/ospd/activity-type/aganitha-index-normalisation) (`aganitha-index-normalisation`) -- no generic parent yet
- [Vulnerability index scoring](https://w3id.org/ogc/ospd/activity-type/cvi-vulnerability-index-scoring) (`cvi-vulnerability-index-scoring`)

## Examples

### Configuration validation
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

ospd:cvi-configuration-validation a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://example.org/ospd/process-types/configuration-validation> ;
    dcterms:source <https://github.com/hartis-org/cvi-workflow/blob/b6f8e98a07be3320a2a936a23cb427009abd12d0/ospd2026/provenance/cvi_full_workflow_design_runtime_entities.json#L39> ;
    rdfs:subClassOf ospd:input-validation ;
    skos:broader ospd:input-validation ;
    skos:definition "Validates the CVI scoring configuration (thresholds, weights) before a run."@en ;
    skos:inScheme ospd-specific:workflow-and-scoring ;
    skos:note "Contributed to OSPD 2026 by hartis-org (cvi-workflow); defined here (decision of 26 Nov 2026). Evidence in dcterms:source."@en ;
    skos:prefLabel "Configuration validation"@en ;
    skos:topConceptOf ospd-specific:workflow-and-scoring ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/cvi-configuration-validation"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/specific-activity-types/workflow-and-scoring> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/specific/workflow-and-scoring`

