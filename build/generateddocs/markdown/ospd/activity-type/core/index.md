
# OSPD Activity Types Register (Model)

`ogc.ospd.activity-type.core` *v0.1*

The catalog of the OSPD-specific activity types: tool- and example-specific specialisations of the generic activity types of the Activity Types Register.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD Activity Types Register

Activity types specific to the OGC Open Science Persistent Demonstrator (OSPD), under stable URIs of the form
`https://w3id.org/ogc/ospd/activity-type/<slug>`: tool- and example-specific types, each specialising a generic activity type (`skos:broader`) of the
[Activity Types Register](https://ogcincubator.github.io/activity-type-register/).

This block holds the catalog (`https://w3id.org/ogc/ospd/catalog`). The concept scheme and the activity types are in the `specific` block
(`ogc.ospd.activity-type.specific`), a profile of this one.

## Examples

### Catalog with the OSPD concept scheme
#### turtle
```turtle
@prefix dcat: <http://www.w3.org/ns/dcat#> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

<https://w3id.org/ogc/ospd/catalog> a dcat:Catalog ;
    dcterms:title "OSPD Activity Types Register"@en ;
    dcterms:hasPart <https://w3id.org/ogc/ospd/specific-activity-types> .

<https://w3id.org/ogc/ospd/specific-activity-types> a skos:ConceptScheme ;
    skos:prefLabel "OSPD specific activity types"@en .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/core`

