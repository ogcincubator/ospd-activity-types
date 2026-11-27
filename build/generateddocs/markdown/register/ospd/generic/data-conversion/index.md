
# Data conversion (Model)

`ogc.register.ospd.generic.data-conversion` *v0.1*

Activities that change the encoding or the spatial model of data without changing the information it carries.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Data conversion

Activities that change the encoding or the spatial model of data without changing the information it carries.

This family has 3 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [COG conversion](https://w3id.org/ogc/ospd/activity-type/cog-conversion) (`cog-conversion`)
- [Encoding conversion](https://w3id.org/ogc/ospd/activity-type/encoding-conversion) (`encoding-conversion`)
- [Spatial model conversion](https://w3id.org/ogc/ospd/activity-type/spatial-model-conversion) (`spatial-model-conversion`)

## Examples

### Encoding conversion
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix geoproc: <https://w3id.org/ogc/rim/geoprocessing/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd:encoding-conversion a skos:Concept,
        acttype:ActivityType ;
    dcterms:source <https://github.com/52North/bblocks-openscience/blob/fe57fc59540ed1d64d18b174529d22add905d66c/_sources/prov-examples/52n-provenance/vegetation-productivity/example.json#L208>,
        <https://github.com/GeoLabs/bblocks-generic-profiles/blob/56fd9896e9e21cbd9d67c1fd3194917a4cc48934/scripts/activity-types.yaml#L753>,
        <https://github.com/geonovum-labs/ospd-dtaas-register/blob/387794d7052af37986cadd791c81afe87acb24f4/_sources/ogcapi/processes/3dgi/convert_format/examples/metadata.json#L1> ;
    rdfs:subClassOf geoproc:GeoprocessingActivityType ;
    skos:altLabel "Format conversion"@en ;
    skos:definition "Re-encodes spatial data in another data format, without changing the information it carries."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/data-conversion> ;
    skos:note "Promoted by the OSPD 2026 activity-type triage (decision of 26 Nov 2026). Evidence in dcterms:source."@en ;
    skos:prefLabel "Encoding conversion"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/data-conversion> ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/encoding-conversion"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/activity-type/families/data-conversion> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/generic/data-conversion`

