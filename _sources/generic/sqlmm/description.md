# SQL/MM spatial operations

The spatial operations and predicates on geometries defined by ISO/IEC 13249-3 (SQL/MM Spatial) and OGC Simple Features Access: area, buffer, centroid, convex hull, the set operations and the spatial relation tests. Each specialises a grouping type of vector geometry processing.

This family has 16 generic activity types. It is a profile of the OSPD Activity Types Register block
(`ogc.register.ospd.core`) and its data resource (`data.ttl`) is uploaded to the OSPD Prez instance when the register is built.

## Activity types

- [Area](https://w3id.org/ogc/ospd/activity-type/area) (`area`)
- [Buffer](https://w3id.org/ogc/ospd/activity-type/buffer) (`buffer`)
- [Centroid](https://w3id.org/ogc/ospd/activity-type/centroid) (`centroid`)
- [Contains](https://w3id.org/ogc/ospd/activity-type/contains) (`contains`)
- [Convex hull](https://w3id.org/ogc/ospd/activity-type/convex-hull) (`convex-hull`)
- [Crosses](https://w3id.org/ogc/ospd/activity-type/crosses) (`crosses`)
- [Difference](https://w3id.org/ogc/ospd/activity-type/difference) (`difference`)
- [Disjoint](https://w3id.org/ogc/ospd/activity-type/disjoint) (`disjoint`)
- [Equals](https://w3id.org/ogc/ospd/activity-type/equals) (`equals`)
- [Intersection](https://w3id.org/ogc/ospd/activity-type/intersection) (`intersection`)
- [Intersects](https://w3id.org/ogc/ospd/activity-type/intersects) (`intersects`)
- [Is simple](https://w3id.org/ogc/ospd/activity-type/is-simple) (`is-simple`)
- [Symmetric difference](https://w3id.org/ogc/ospd/activity-type/symdifference) (`symdifference`)
- [Touches](https://w3id.org/ogc/ospd/activity-type/touches) (`touches`)
- [Union](https://w3id.org/ogc/ospd/activity-type/union) (`union`)
- [Within](https://w3id.org/ogc/ospd/activity-type/within) (`within`)
