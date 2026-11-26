
# OSPD specific activity types: spatial indexing (Model)

`ogc.register.ospd.specific.spatial-indexing` *v0.1*

Activity types contributed by OSPD participants that specialise the generic types of spatial indexing (ogc.register.ospd.generic.spatial-indexing).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# OSPD specific activity types: spatial indexing

Activity types contributed by OSPD participants that specialise the generic types of spatial indexing (ogc.register.ospd.generic.spatial-indexing).

This block has 1 specific activity types, each the specialisation (`skos:broader`) of a generic type of
[Spatial indexing](https://w3id.org/ogc/ospd/activity-type/families/spatial-indexing). It is a profile of that family's block, whose
shapes it inherits, and adds a warning for a type without a generic parent. Its data resource (`data.ttl`) is uploaded to
the OSPD Prez instance when the register is built.

## Activity types

- [STAC fingerprinting](https://w3id.org/ogc/ospd/activity-type/kindgrove-stac-fingerprint) (`kindgrove-stac-fingerprint`)

## Examples

### STAC fingerprinting
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

ospd:kindgrove-stac-fingerprint a skos:Concept,
        acttype:ActivityType ;
    dcterms:source <https://github.com/starling-foundries/KindGrove/blob/6e3872eb82c5574744b682f13cf5cda14e7132a3/scripts/provenance.py#L119> ;
    rdfs:subClassOf ospd:GA029 ;
    skos:broader ospd:GA029 ;
    skos:definition "Writes the STAC Fingerprint extension into a STAC catalog: for every item, the SHA-256 root of the compact rHEALPix DGGS zone list of its geometry at a refinement level."@en ;
    skos:inScheme ospd-specific:spatial-indexing ;
    skos:notation "identification" ;
    skos:note "Contributed to OSPD 2026 by KindGrove (starling-foundries); defined here (decision of 26 Nov 2026). Evidence in dcterms:source."@en ;
    skos:prefLabel "STAC fingerprinting"@en ;
    skos:topConceptOf ospd-specific:spatial-indexing ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/kindgrove-stac-fingerprint"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/specific-activity-types/spatial-indexing> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/specific/spatial-indexing`

