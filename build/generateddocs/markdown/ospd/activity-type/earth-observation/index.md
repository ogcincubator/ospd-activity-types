
# Earth observation (Model)

`ogc.ospd.activity-type.earth-observation` *v0.1*

Earth-observation data access and applications: Sentinel-2 band retrieval and product selection, cloud and best-available-pixel handling, and the water-bodies, algae-bloom and mangrove-biomass workflows.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Earth observation

Earth-observation data access and applications: Sentinel-2 band retrieval and product selection, cloud and best-available-pixel handling, and the water-bodies, algae-bloom and mangrove-biomass workflows.

This family has 25 activity types. It is a profile of the OSPD Activity Type core block and its data resource
(`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.](https://w3id.org/ogc/ospd/activity-type/workflow-copernicus) (`workflow-copernicus`)
- [Algae bloom for water quality assessment on Sentinel-2 L2A imagery offered by Earth-Search platform.](https://w3id.org/ogc/ospd/activity-type/workflow-earth-search) (`workflow-earth-search`)
- [Assemble a STAC catalog of detected water bodies](https://w3id.org/ogc/ospd/activity-type/stac) (`stac`)
- [Band retrieval](https://w3id.org/ogc/ospd/activity-type/band-retrieval) (`band-retrieval`)
- [Best available pixel (BAP)](https://w3id.org/ogc/ospd/activity-type/GA016) (`GA016`)
- [Cloud cover](https://w3id.org/ogc/ospd/activity-type/GA014) (`GA014`)
- [Cloud mask distance](https://w3id.org/ogc/ospd/activity-type/GA015) (`GA015`)
- [Crop a Sentinel-2 COG band to an area of interest](https://w3id.org/ogc/ospd/activity-type/crop) (`crop`)
- [Download one Sentinel-2 band over a bounding box](https://w3id.org/ogc/ospd/activity-type/download-band) (`download-band`)
- [Downloads Copernicus products.](https://w3id.org/ogc/ospd/activity-type/download-band-sentinel2-product-safe) (`download-band-sentinel2-product-safe`)
- [Downloads Sentinel-2 GeoTiff from STAC Item.](https://w3id.org/ogc/ospd/activity-type/download-band-sentinel2-stac-item) (`download-band-sentinel2-stac-item`)
- [Mangrove biomass and carbon estimation](https://w3id.org/ogc/ospd/activity-type/mangrove) (`mangrove`)
- [Mangrove Biomass Workflow](https://w3id.org/ogc/ospd/activity-type/mangrove-workflow) (`mangrove-workflow`)
- [Mangrove Biomass Workflow (step notebooks)](https://w3id.org/ogc/ospd/activity-type/mangrove-workflow-steps) (`mangrove-workflow-steps`)
- [Mangrove detection, allometric biomass and IPCC carbon stock](https://w3id.org/ogc/ospd/activity-type/estimate-biomass) (`estimate-biomass`)
- [Parse area of interest](https://w3id.org/ogc/ospd/activity-type/parse-aoi-steps) (`parse-aoi-steps`)
- [Parse area of interest](https://w3id.org/ogc/ospd/activity-type/parse-aoi) (`parse-aoi`)
- [Plot the biomass map and export a STAC catalog](https://w3id.org/ogc/ospd/activity-type/export-stac) (`export-stac`)
- [Processing on Sentinel-2 bands to evaluate algae bloom.](https://w3id.org/ogc/ospd/activity-type/workflow-copernicus-process) (`workflow-copernicus-process`)
- [Processing on Sentinel-2 L2A bands to evaluate algae bloom.](https://w3id.org/ogc/ospd/activity-type/workflow-earth-search-process) (`workflow-earth-search-process`)
- [Product selection](https://w3id.org/ogc/ospd/activity-type/product-selection) (`product-selection`)
- [Searches the specified catalog for Sentinel-2 products matching filtering criteria.](https://w3id.org/ogc/ospd/activity-type/select-products-sentinel2) (`select-products-sentinel2`)
- [Select the least cloudy Sentinel-2 L2A scene](https://w3id.org/ogc/ospd/activity-type/select-scene) (`select-scene`)
- [Water bodies detection based on NDWI and otsu threshold](https://w3id.org/ogc/ospd/activity-type/water-bodies) (`water-bodies`)
- [Water body detection based on NDWI and otsu threshold](https://w3id.org/ogc/ospd/activity-type/detect-water-body) (`detect-water-body`)

## Examples

### Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform.
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ospd:workflow-copernicus a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://w3id.org/geolabs/ospd/process-profiles/process-type/algae-bloom/workflow-copernicus> ;
    skos:definition "Finds Sentinel-2 products on Copernicus using filtering parameters and performs band calculation on retrieved Sentinel-2 products to evaluate algae bloom for water quality assessment."@en ;
    skos:exactMatch <https://geolabs.github.io/bblocks-process-profiles/def/process-type/algae-bloom/workflow-copernicus> ;
    skos:inScheme ospd: ;
    skos:prefLabel "Algae bloom for water quality assessment on Sentinel-2 imagery offered by Copernicus platform."@en .

ospd: a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/earth-observation`

