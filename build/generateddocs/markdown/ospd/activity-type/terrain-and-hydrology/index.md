
# Terrain and hydrology (Model)

`ogc.ospd.activity-type.terrain-and-hydrology` *v0.1*

Terrain derivatives (slope, hillshading, ruggedness and position indices) and hydrological analysis (flow direction and accumulation, watersheds, stream networks, wetness index).

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Terrain and hydrology

Terrain derivatives (slope, hillshading, ruggedness and position indices) and hydrological analysis (flow direction and accumulation, watersheds, stream networks, wetness index).

This family has 17 activity types. It is a profile of the OSPD Activity Type core block and its data resource
(`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Analytical Hillshading](https://w3id.org/ogc/ospd/activity-type/hillshading) (`hillshading`)
- [Analytical hillshading](https://w3id.org/ogc/ospd/activity-type/analytical-hillshading) (`analytical-hillshading`)
- [D8 flow-accumulation derivation](https://w3id.org/ogc/ospd/activity-type/GA023) (`GA023`)
- [D8 flow-direction derivation](https://w3id.org/ogc/ospd/activity-type/GA022) (`GA022`)
- [Hydrological analysis](https://w3id.org/ogc/ospd/activity-type/GA031) (`GA031`)
- [Hydrological DEM conditioning](https://w3id.org/ogc/ospd/activity-type/GA034) (`GA034`)
- [Slope](https://w3id.org/ogc/ospd/activity-type/slope) (`slope`)
- [Slope derivation](https://w3id.org/ogc/ospd/activity-type/GA021) (`GA021`)
- [Slope, Aspect, Curvature](https://w3id.org/ogc/ospd/activity-type/terrain-slope) (`terrain-slope`)
- [Stream-network extraction](https://w3id.org/ogc/ospd/activity-type/GA025) (`GA025`)
- [Terrain analysis](https://w3id.org/ogc/ospd/activity-type/GA030) (`GA030`)
- [Terrain ruggedness index](https://w3id.org/ogc/ospd/activity-type/terrain-ruggedness-index) (`terrain-ruggedness-index`)
- [Terrain Ruggedness Index (TRI)](https://w3id.org/ogc/ospd/activity-type/terrain-terrain-ruggedness-index) (`terrain-terrain-ruggedness-index`)
- [Topographic position index](https://w3id.org/ogc/ospd/activity-type/topographic-position-index) (`topographic-position-index`)
- [Topographic Position Index (TPI)](https://w3id.org/ogc/ospd/activity-type/terrain-topographic-position-index) (`terrain-topographic-position-index`)
- [Topographic Wetness Index calculation](https://w3id.org/ogc/ospd/activity-type/GA035) (`GA035`)
- [Watershed/catchment delineation](https://w3id.org/ogc/ospd/activity-type/GA024) (`GA024`)

## Examples

### Analytical Hillshading
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix rim: <https://w3id.org/ogc/rim/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .
@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .

ospd: a skos:ConceptScheme .

ospd:hillshading a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://w3id.org/geolabs/ospd/process-profiles/process-type/terrain/hillshading> ;
    skos:broader ospd:analytical-hillshading ;
    skos:definition "This tool performs an analytical hillshade computation for an elevation grid. The 'Standard' method simply calculates the angle at which light coming from the position of the light source would hit the surface. This method can produce angles greater than 90 degree. With the second method all values are kept within the range of 0-90 degree. It can be enhanced with shadowing effects, where shadowed cells will be marked with a value of exactly 90 degree. 'Shadows Only' creates a mask for the shadowed areas and sets all other cells to no-data. 'Combined Shading' takes the values of the standard method and multiplies these with the normalized slope. 'Ambient Occlusion' is based on the concepts of Tarini et al. (2006), but only the northern half-space is considered here."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/terrain-and-hydrology> ;
    skos:prefLabel "Analytical Hillshading"@en ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/hillshading"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/terrain-and-hydrology`

