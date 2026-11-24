
# Machine learning and statistical modeling (Model)

`ogc.ospd.activity-type.ml-and-statistical-modeling` *v0.1*

Machine-learning and statistical activities: regression, climate-variable downscaling, super-resolution and trend analysis, and inference executions.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Machine learning and statistical modeling

Machine-learning and statistical activities: regression, climate-variable downscaling, super-resolution and trend analysis, and inference executions.

This family has 6 activity types. It is a profile of the OSPD Activity Type core block and its data resource
(`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Climate-variable downscaling](https://w3id.org/ogc/ospd/activity-type/climate-downscaling) (`climate-downscaling`)
- [Inference execution without an asserted register action](https://w3id.org/ogc/ospd/activity-type/InferenceExecution) (`InferenceExecution`)
- [ML Climate Variable Downscaling](https://w3id.org/ogc/ospd/activity-type/GA009) (`GA009`)
- [Regression](https://w3id.org/ogc/ospd/activity-type/GA007) (`GA007`)
- [Seasonal Sen’s Slope](https://w3id.org/ogc/ospd/activity-type/GA017) (`GA017`)
- [U-Net RDPS-to-HRDPS downscaling inference](https://w3id.org/ogc/ospd/activity-type/climate-downscaling-inference) (`climate-downscaling-inference`)

## Examples

### Climate-variable downscaling
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd: a skos:ConceptScheme .

ospd:climate-downscaling a skos:Concept,
        acttype:ActivityType ;
    dcterms:modified "2026-10-15"^^xsd:date ;
    dcterms:replaces <https://crim-ca.github.io/bblocks-process-profiles/def/activity-type/climate-downscaling> ;
    rdfs:subClassOf <https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType> ;
    skos:closeMatch ospd:GA009 ;
    skos:definition "Transforms georeferenced climate fields to a finer-resolution target grid."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/ml-and-statistical-modeling> ;
    skos:prefLabel "Climate-variable downscaling"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/ml-and-statistical-modeling> .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/ml-and-statistical-modeling`

