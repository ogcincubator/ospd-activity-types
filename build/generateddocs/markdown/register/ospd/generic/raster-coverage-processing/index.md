
# Raster and coverage processing (Model)

`ogc.register.ospd.generic.raster-coverage-processing` *v0.1*

Operations on rasters and coverages: reprojection, resampling, cropping, mosaicking, format conversion, rendering, band math, spectral indices and zonal analysis.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Raster and coverage processing

Operations on rasters and coverages: reprojection, resampling, cropping, mosaicking, format conversion, rendering, band math, spectral indices and zonal analysis.

This family has 25 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Band Calculation](https://w3id.org/ogc/ospd/activity-type/GA008) (`GA008`)
- [Coverage subsetting](https://w3id.org/ogc/ospd/activity-type/coverage-subsetting) (`coverage-subsetting`)
- [Distance-to-feature calculation](https://w3id.org/ogc/ospd/activity-type/GA026) (`GA026`)
- [Mosaic](https://w3id.org/ogc/ospd/activity-type/GA011) (`GA011`)
- [NDVI](https://w3id.org/ogc/ospd/activity-type/GA013) (`GA013`)
- [Otsu thresholding](https://w3id.org/ogc/ospd/activity-type/otsu-thresholding) (`otsu-thresholding`)
- [Portrayal](https://w3id.org/ogc/ospd/activity-type/portrayal) (`portrayal`)
- [Radiometric index](https://w3id.org/ogc/ospd/activity-type/radiometric-index) (`radiometric-index`)
- [Raster analysis](https://w3id.org/ogc/ospd/activity-type/GA032) (`GA032`)
- [Raster band math](https://w3id.org/ogc/ospd/activity-type/raster-band-math) (`raster-band-math`)
- [Raster band math (multi-band output)](https://w3id.org/ogc/ospd/activity-type/raster-band-math-multiband) (`raster-band-math-multiband`)
- [Raster classification](https://w3id.org/ogc/ospd/activity-type/raster-classification) (`raster-classification`)
- [Raster crop](https://w3id.org/ogc/ospd/activity-type/raster-crop) (`raster-crop`)
- [Raster extent](https://w3id.org/ogc/ospd/activity-type/raster-extent) (`raster-extent`)
- [Raster format conversion](https://w3id.org/ogc/ospd/activity-type/raster-format-conversion) (`raster-format-conversion`)
- [Raster regridding](https://w3id.org/ogc/ospd/activity-type/raster-regridding) (`raster-regridding`)
- [Raster rendering](https://w3id.org/ogc/ospd/activity-type/raster-rendering) (`raster-rendering`)
- [Raster reprojection](https://w3id.org/ogc/ospd/activity-type/raster-reprojection) (`raster-reprojection`)
- [Raster resampling](https://w3id.org/ogc/ospd/activity-type/raster-resampling) (`raster-resampling`)
- [Raster sampling at points](https://w3id.org/ogc/ospd/activity-type/GA028) (`GA028`)
- [Reproject](https://w3id.org/ogc/ospd/activity-type/GA018) (`GA018`)
- [SEN2SR](https://w3id.org/ogc/ospd/activity-type/GA010) (`GA010`)
- [Soil-adjusted vegetation index (SAVI)](https://w3id.org/ogc/ospd/activity-type/GA012) (`GA012`)
- [Zonal raster statistics](https://w3id.org/ogc/ospd/activity-type/GA027) (`GA027`)
- [Zonal statistics](https://w3id.org/ogc/ospd/activity-type/ZonalStatistics) (`ZonalStatistics`)

## Examples

### Band Calculation
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

ospd:GA008 a skos:Concept,
        acttype:ActivityType ;
    dcterms:modified "2026-10-09"^^xsd:date ;
    dcterms:replaces <http://ospd/demo/GA008> ;
    rdfs:seeAlso <https://hirondelle.crim.ca/weaver/processes/calculate-band> ;
    rdfs:subClassOf <https://w3id.org/ogc/rim/geoprocessing/GeoprocessingActivityType> ;
    owl:versionInfo "2" ;
    skos:closeMatch ospd:raster-band-math ;
    skos:definition "Performs a calculation over imagery bands and returns the resulting raster using the specified band arithmetic."@en ;
    skos:inScheme <https://w3id.org/ogc/ospd/activity-type/families/raster-coverage-processing> ;
    skos:prefLabel "Band Calculation"@en ;
    skos:topConceptOf <https://w3id.org/ogc/ospd/activity-type/families/raster-coverage-processing> ;
    prov:qualifiedAttribution [ prov:agent <https://www.crim.ca> ;
            prov:hadRole <https://def.isotc211.org/codeset/RoleCode/custodian> ] ;
    rim:itemClass acttype:activityTypeItemClass ;
    rim:objectIdentifier "https://w3id.org/ogc/ospd/activity-type/GA008"^^xsd:anyURI ;
    rim:publicationStatus rim:published ;
    rim:validityStatus rim:valid .

<https://w3id.org/ogc/ospd/activity-type/families/raster-coverage-processing> a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/generic/raster-coverage-processing`

