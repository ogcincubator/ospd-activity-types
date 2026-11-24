
# Information extraction and retrieval (Model)

`ogc.ospd.activity-type.information-extraction-and-retrieval` *v0.1*

Source acquisition, text metadata enrichment (entity extraction, geotagging, classification, normalization) and retrieval-augmented generation.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Information extraction and retrieval

Source acquisition, text metadata enrichment (entity extraction, geotagging, classification, normalization) and retrieval-augmented generation.

This family has 13 activity types. It is a profile of the OSPD Activity Type core block and its data resource
(`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Commodity Classification](https://w3id.org/ogc/ospd/activity-type/GA042) (`GA042`)
- [Data Acquisition](https://w3id.org/ogc/ospd/activity-type/GA047) (`GA047`)
- [FAS Code Decode](https://w3id.org/ogc/ospd/activity-type/GA038) (`GA038`)
- [FAS Geolocate](https://w3id.org/ogc/ospd/activity-type/GA039) (`GA039`)
- [FAS Source Fetch](https://w3id.org/ogc/ospd/activity-type/GA037) (`GA037`)
- [Field Normalization](https://w3id.org/ogc/ospd/activity-type/GA044) (`GA044`)
- [Generate](https://w3id.org/ogc/ospd/activity-type/GA046) (`GA046`)
- [Geotag](https://w3id.org/ogc/ospd/activity-type/GA041) (`GA041`)
- [NLP Entity Extraction](https://w3id.org/ogc/ospd/activity-type/GA040) (`GA040`)
- [Region Classification](https://w3id.org/ogc/ospd/activity-type/GA043) (`GA043`)
- [Retrieval-Augmented Generation](https://w3id.org/ogc/ospd/activity-type/GA049) (`GA049`)
- [Retrieve](https://w3id.org/ogc/ospd/activity-type/GA045) (`GA045`)
- [Text Metadata Enrichment](https://w3id.org/ogc/ospd/activity-type/GA048) (`GA048`)

## Examples

### Commodity Classification
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix foaf: <http://xmlns.com/foaf/0.1/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix owl: <http://www.w3.org/2002/07/owl#> .
@prefix prov: <http://www.w3.org/ns/prov#> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd: a skos:ConceptScheme .

ospd:GA042 a skos:Concept,
        acttype:ActivityType ;
    dcterms:modified "2026-09-23"^^xsd:date ;
    dcterms:replaces <http://ospd/demo/GA042> ;
    dcterms:source <https://github.com/voyagersearch/voyager-prov-ts/blob/dev/docs/ospd-register-proposal.md> ;
    rdfs:seeAlso <http://ospd/demo/classify-commodity> ;
    owl:versionInfo "v1" ;
    skos:broader ospd:GA048 ;
    skos:definition "Text → commodity-taxonomy classifier (dictionary matcher over normalized labels). Domain-specific to agricultural / commodity data."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/information-extraction-and-retrieval> ;
    skos:prefLabel "Commodity Classification"@en ;
    skos:related ospd:GA043,
        ospd:GA044 ;
    prov:qualifiedAttribution [ prov:agent [ foaf:name "Alex Bostic" ] ;
            prov:hadRole <https://def.isotc211.org/codeset/RoleCode/pointOfContact> ],
        [ prov:agent [ foaf:name "Voyager Search" ] ;
            prov:hadRole <https://def.isotc211.org/codeset/RoleCode/custodian> ] .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/information-extraction-and-retrieval`

