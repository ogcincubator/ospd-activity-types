
# Workflow and scoring (Model)

`ogc.register.ospd.generic.workflow-and-scoring` *v0.1*

Workflow runs and scoring or classification activities used in the model-of-models and workflow examples.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Workflow and scoring

Workflow runs and scoring or classification activities used in the model-of-models and workflow examples.

This family has 6 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Catalog export](https://w3id.org/ogc/ospd/activity-type/catalog-export) (`catalog-export`)
- [Composite index calculation](https://w3id.org/ogc/ospd/activity-type/index-composition) (`index-composition`)
- [Input validation](https://w3id.org/ogc/ospd/activity-type/input-validation) (`input-validation`)
- [Scoring and progress tracking](https://w3id.org/ogc/ospd/activity-type/ScoringAndProgressTracking) (`ScoringAndProgressTracking`)
- [Weighted scoring and classification](https://w3id.org/ogc/ospd/activity-type/WeightedScoringAndClassification) (`WeightedScoringAndClassification`)
- [Workflow](https://w3id.org/ogc/ospd/activity-type/workflow) (`workflow`)

## Examples

### Catalog export
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd:catalog-export a skos:Concept,
        acttype:ActivityType ;
    rdfs:subClassOf acttype:ActivityType ;
    skos:definition "Assembles the results of an analysis into a catalog of items with their assets, for example a STAC Catalog."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/workflow-and-scoring> ;
    skos:note "Proposed generic type, introduced to give specific types a parent; not derived from a source definition."@en ;
    skos:prefLabel "Catalog export"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/workflow-and-scoring> ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/catalog-export"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/activity-type/families/workflow-and-scoring> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/generic/workflow-and-scoring`

