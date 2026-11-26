
# Terrain and hydrology (Model)

`ogc.register.ospd.generic.terrain-and-hydrology` *v0.1*

Terrain derivatives (slope, hillshading, ruggedness and position indices) and hydrological analysis (flow direction and accumulation, watersheds, stream networks, wetness index).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Terrain and hydrology

Terrain derivatives (slope, hillshading, ruggedness and position indices) and hydrological analysis (flow direction and accumulation, watersheds, stream networks, wetness index).

This family has 13 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Analytical hillshading](https://w3id.org/ogc/ospd/activity-type/analytical-hillshading) (`analytical-hillshading`)
- [D8 flow-accumulation derivation](https://w3id.org/ogc/ospd/activity-type/GA023) (`GA023`)
- [D8 flow-direction derivation](https://w3id.org/ogc/ospd/activity-type/GA022) (`GA022`)
- [Hydrological analysis](https://w3id.org/ogc/ospd/activity-type/GA031) (`GA031`)
- [Hydrological DEM conditioning](https://w3id.org/ogc/ospd/activity-type/GA034) (`GA034`)
- [Slope](https://w3id.org/ogc/ospd/activity-type/slope) (`slope`)
- [Slope derivation](https://w3id.org/ogc/ospd/activity-type/GA021) (`GA021`)
- [Stream-network extraction](https://w3id.org/ogc/ospd/activity-type/GA025) (`GA025`)
- [Terrain analysis](https://w3id.org/ogc/ospd/activity-type/GA030) (`GA030`)
- [Terrain ruggedness index](https://w3id.org/ogc/ospd/activity-type/terrain-ruggedness-index) (`terrain-ruggedness-index`)
- [Topographic position index](https://w3id.org/ogc/ospd/activity-type/topographic-position-index) (`topographic-position-index`)
- [Topographic Wetness Index calculation](https://w3id.org/ogc/ospd/activity-type/GA035) (`GA035`)
- [Watershed/catchment delineation](https://w3id.org/ogc/ospd/activity-type/GA024) (`GA024`)

## Examples

### Analytical hillshading
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd:analytical-hillshading a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://w3id.org/geolabs/ospd/generic-profiles/activity-type/analytical-hillshading> ;
    rdfs:subClassOf <https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType> ;
    skos:definition "For each cell, the angle at which light coming from the position of the light source hits the terrain surface."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/terrain-and-hydrology> ;
    skos:prefLabel "Analytical hillshading"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/terrain-and-hydrology> ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/analytical-hillshading"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/activity-type/families/terrain-and-hydrology> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/generic/terrain-and-hydrology`

