
# Machine learning and statistical modeling (Model)

`ogc.register.ospd.generic.ml-and-statistical-modeling` *v0.1*

Machine-learning and statistical activities: regression, climate-variable downscaling, super-resolution and trend analysis, and inference executions.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Machine learning and statistical modeling

Machine-learning and statistical activities: regression, climate-variable downscaling, super-resolution and trend analysis, and inference executions.

This family has 5 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [ML Climate Variable Downscaling](https://w3id.org/ogc/ospd/activity-type/GA009) (`GA009`)
- [Model inference](https://w3id.org/ogc/ospd/activity-type/model-inference) (`model-inference`)
- [Model training](https://w3id.org/ogc/ospd/activity-type/model-training) (`model-training`)
- [Regression](https://w3id.org/ogc/ospd/activity-type/GA007) (`GA007`)
- [Seasonal Sen’s Slope](https://w3id.org/ogc/ospd/activity-type/GA017) (`GA017`)

## Examples

### ML Climate Variable Downscaling
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd:GA009 a skos:Concept,
        acttype:ActivityType ;
    dcterms:modified "2026-10-09"^^xsd:date ;
    dcterms:replaces <http://ospd/demo/GA009> ;
    rdfs:seeAlso <https://hirondelle.crim.ca/weaver/processes/ogc-ospd2026-downscaling-unet> ;
    rdfs:subClassOf acttype:ActivityType ;
    owl:versionInfo "0.1.3.dev10" ;
    skos:definition "Performs climate variable downscaling used to transform coarse-scale climate model outputs into high-resolution, locally relevant climate data, using a machine learning algorithm described through STAC MLM."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/ml-and-statistical-modeling> ;
    skos:prefLabel "ML Climate Variable Downscaling"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/ml-and-statistical-modeling> ;
    prov:qualifiedAttribution [ prov:agent <https://www.crim.ca> ;
            prov:hadRole <https://def.isotc211.org/codeset/RoleCode/custodian> ] ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/GA009"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/activity-type/families/ml-and-statistical-modeling> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/generic/ml-and-statistical-modeling`

