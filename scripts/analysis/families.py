import csv, re, sys, collections
D = sys.argv[1]
defs = {r["iri"]: r for r in csv.DictReader(open(f"{D}/definitions.csv"))}
mapping = {r["old_iri"]: r for r in csv.DictReader(open(f"{D}/mapping.csv"))}
dups = list(csv.DictReader(open(f"{D}/duplicates.csv")))
GP = "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/"
GL = "https://w3id.org/geolabs/ospd/process-profiles/process-type/"
F = {"vector": "vector-geometry-processing", "raster": "raster-coverage-processing",
     "eo": "earth-observation", "terrain": "terrain-and-hydrology", "dggs": "spatial-indexing",
     "pc": "point-cloud-processing", "ml": "ml-and-statistical-modeling",
     "info": "information-extraction-and-retrieval", "wf": "workflow-and-scoring"}
ga = {}
for rng, f in [((1, 7), "vector"), ((7, 8), "ml"), ((8, 9), "raster"), ((9, 11), "ml"), ((11, 14), "raster"),
               ((14, 18), "eo"), ((18, 19), "raster"), ((19, 21), "vector"), ((21, 26), "terrain"),
               ((26, 29), "raster"), ((29, 30), "dggs"), ((30, 32), "terrain"), ((32, 33), "raster"),
               ((33, 34), "dggs"), ((34, 36), "terrain"), ((36, 37), "dggs"), ((37, 50), "info")]:
    for n in range(*rng):
        ga[f"http://ospd/demo/GA{n:03d}"] = f
VEC = "area buffer centroid contains convex-hull crosses difference disjoint equals geometry-extent intersection intersects is-simple symdifference touches union within".split()
TER = "analytical-hillshading slope terrain-ruggedness-index topographic-position-index".split()
def explicit(i):
    if i in ga: return ga[i], "explicit (GA item)"
    if i.startswith(GP):
        s = i[len(GP):]
        if s in VEC: return "vector", "explicit (generic type)"
        if s in TER: return "terrain", "explicit (generic type)"
        if s.startswith("point-cloud"): return "pc", "explicit (generic type)"
        if s in ("band-retrieval", "product-selection"): return "eo", "explicit (generic type)"
        if s in ("radiometric-index", "otsu-thresholding") or s.startswith("raster-"): return "raster", "explicit (generic type)"
    if i.startswith(GL):
        g = i[len(GL):].split("/")[0]
        return {"sqlmm": "vector", "vector": "vector", "pointcloud": "pc", "terrain": "terrain", "raster": "raster",
                "algae-bloom": "eo", "water-bodies": "eo", "kindgrove": "eo", "kindgrove-steps": "eo"}.get(g), "group default (GeoLabs)"
    if "crim-ca.github.io" in i: return "ml", "explicit (CRIM)"
    if i.endswith("process-types/ZonalStatistics"): return "raster", "explicit (duplicate of GA027)"
    if i.endswith(("ScoringAndProgressTracking", "WeightedScoringAndClassification")) or i.endswith("mom/WorkflowRun"):
        return "wf", "explicit (openscience)"
    return None, "unassigned"
def broader_in_set(i):
    return [b for b in defs[i]["broader"].split(" | ") if b in defs]
fam, basis = {}, {}
for i in defs:
    f, b = explicit(i)
    fam[i], basis[i] = f, b
# implementation types with an in-set broader inherit the parent's family
for i in defs:
    if i.startswith(GL):
        ps = [fam.get(b) for b in broader_in_set(i) if b.startswith(GP)]
        ps = [p for p in ps if p]
        if ps:
            fam[i], basis[i] = ps[0], "inherited from broader"
issues = []
# (a) parent/child family mismatches and multiple broaders
for i in defs:
    ps = broader_in_set(i)
    fs = {fam.get(b) for b in ps if fam.get(b)}
    if len(fs) > 1:
        issues.append(("multiple-families-via-broader", i, str(fs)))
    for b in ps:
        if fam.get(b) and fam.get(i) and fam[b] != fam[i]:
            issues.append(("child-in-different-family-than-parent", i, f"{fam[i]} vs parent {b} -> {fam[b]}"))
# (b) duplicate groups spanning families
grp = collections.defaultdict(list)
for r in dups:
    grp[r["group_id"]].append(r)
for g, rs in grp.items():
    fs = {fam.get(r["iri"]) for r in rs if r["role"] in ("canonical", "duplicate", "implements") and fam.get(r["iri"])}
    if len(fs) > 1:
        issues.append(("duplicate-or-implements-group-spans-families", g, str(fs)))
    allfs = {fam.get(r["iri"]) for r in rs if fam.get(r["iri"])}
    if len(allfs) > 1 and len(fs) <= 1:
        issues.append(("related-group-spans-families (info)", g, str(allfs)))
import os
OUTF = f"{D}/family-assignment.generated.csv" if os.path.exists(f"{D}/family-assignment.csv") else f"{D}/family-assignment.csv"
with open(OUTF, "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["old_iri", "new_iri", "name", "family", "basis", "kind", "canonical_old_iri"])
    for i in sorted(defs):
        m = mapping[i]
        w.writerow([i, m["new_iri"], defs[i]["name"], F.get(fam[i], ""), basis[i], m["kind"], m["canonical_old_iri"]])
    for old, m in mapping.items():
        if m["kind"] in ("alias", "gap"):
            c = m["canonical_old_iri"]
            fa = F.get(fam.get(c), "") if c in fam else ""
            w.writerow([old, m["new_iri"], "", fa, "alias of canonical" if fa else "no definition", m["kind"], c])
cnt = collections.Counter(F.get(fam[i], "(unassigned)") for i in defs)
for k, v in cnt.most_common(): print(v, k)
print()
for t, a, b in issues: print(t, "|", a.replace(GL, "P:").replace(GP, "G:").replace("http://ospd/demo/", ""), "|", b[:140])
print("unassigned:", [i[-60:] for i in defs if not fam[i]])
