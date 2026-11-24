
# Workflow and scoring (Model)

`ogc.ospd.activity-type.workflow-and-scoring` *v0.1*

Workflow runs and scoring or classification activities used in the model-of-models and workflow examples.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Workflow and scoring

Workflow runs and scoring or classification activities used in the model-of-models and workflow examples.

This family has 3 activity types. It is a profile of the OSPD Activity Type core block and its data resource
(`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Scoring and progress tracking](https://w3id.org/ogc/ospd/activity-type/ScoringAndProgressTracking) (`ScoringAndProgressTracking`)
- [Weighted scoring and classification](https://w3id.org/ogc/ospd/activity-type/WeightedScoringAndClassification) (`WeightedScoringAndClassification`)
- [Workflow run](https://w3id.org/ogc/ospd/activity-type/WorkflowRun) (`WorkflowRun`)

## Examples

### Scoring and progress tracking
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ospd: a skos:ConceptScheme .

ospd:ScoringAndProgressTracking a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://example.org/ospd/process-types/ScoringAndProgressTracking> ;
    rdfs:seeAlso <https://example.org/ospd/process-types/scoring-and-progress-tracking> ;
    skos:definition "Combines the scores of several sources into one result per zone and tracks its status against the previous result (New, Continued, Upgraded, Downgraded)."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/workflow-and-scoring> ;
    skos:prefLabel "Scoring and progress tracking"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/workflow-and-scoring> .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/workflow-and-scoring`

