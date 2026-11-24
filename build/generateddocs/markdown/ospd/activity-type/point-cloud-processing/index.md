
# Point-cloud processing (Model)

`ogc.ospd.activity-type.point-cloud-processing` *v0.1*

Point-cloud thinning, gridding and conversion to shapes.

[*Status*](http://www.opengis.net/def/status): Under development

## Description

# Point-cloud processing

Point-cloud thinning, gridding and conversion to shapes.

This family has 6 activity types. It is a profile of the OSPD Activity Type core block and its data resource
(`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Point Cloud Thinning (Simple)](https://w3id.org/ogc/ospd/activity-type/pointcloud-point-cloud-thinning) (`pointcloud-point-cloud-thinning`)
- [Point cloud thinning (simple)](https://w3id.org/ogc/ospd/activity-type/point-cloud-thinning) (`point-cloud-thinning`)
- [Point Cloud to Grid](https://w3id.org/ogc/ospd/activity-type/pointcloud-point-cloud-to-grid) (`pointcloud-point-cloud-to-grid`)
- [Point cloud to grid](https://w3id.org/ogc/ospd/activity-type/point-cloud-to-grid) (`point-cloud-to-grid`)
- [Point Cloud to Shapes](https://w3id.org/ogc/ospd/activity-type/pointcloud-point-cloud-to-shapes) (`pointcloud-point-cloud-to-shapes`)
- [Point cloud to shapes](https://w3id.org/ogc/ospd/activity-type/point-cloud-to-shapes) (`point-cloud-to-shapes`)

## Examples

### Point Cloud Thinning (Simple)
#### turtle
```turtle
@prefix acttype: <https://w3id.org/ogc/rim/activity-type/> .
@prefix dcterms: <http://purl.org/dc/terms/> .
@prefix ospd: <https://w3id.org/ogc/ospd/activity-type/> .
@prefix skos: <http://www.w3.org/2004/02/skos/core#> .

ospd:pointcloud-point-cloud-thinning a skos:Concept,
        acttype:ActivityType ;
    dcterms:replaces <https://w3id.org/geolabs/ospd/process-profiles/process-type/pointcloud/point-cloud-thinning> ;
    skos:broader ospd:point-cloud-thinning ;
    skos:definition "This simple thinning tool reduces the number of points in a point cloud by sequential point removal. It is therefore most suited for points stored in chronological order."@en ;
    skos:inScheme ospd: ;
    skos:prefLabel "Point Cloud Thinning (Simple)"@en .

ospd: a skos:ConceptScheme .

```


# For developers

The source code for this Building Block can be found in the following repository:

* URL: [https://github.com/ogcincubator/ospd-activity-types](https://github.com/ogcincubator/ospd-activity-types)
* Path: `_sources/point-cloud-processing`

