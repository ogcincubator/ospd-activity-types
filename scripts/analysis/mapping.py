import csv, re, collections, sys
D = sys.argv[1]
NEW = "https://w3id.org/ogc/ospd/activity-type/"
defs = {r["iri"]: r for r in csv.DictReader(open(f"{D}/definitions.csv"))}
undef = list(csv.DictReader(open(f"{D}/undefined-references.csv")))
GL = "https://w3id.org/geolabs/ospd/process-profiles/process-type/"
GP = "https://w3id.org/geolabs/ospd/generic-profiles/activity-type/"

def scheme(i):
    if i.startswith("http://ospd/demo/"): return "ospd-data GAnnn"
    if i.startswith(GL): return "GeoLabs process-type"
    if i.startswith(GP): return "GeoLabs generic activity-type"
    if "crim-ca.github.io" in i: return "CRIM activity-type"
    if "geolabs.github.io" in i: return "CRIM snapshot of GeoLabs"
    if "example.org/ospd/process-types/" in i: return "openscience process-types"
    if "rss-hydro.lu" in i: return "rss-hydro"
    if "roofer-online" in i or "planspace" in i: return "Geonovum process endpoint"
    if "demo:GA" in i: return "Kurrawong catalog URL"
    return "other"

def slug_of(i):
    if i.startswith("http://ospd/demo/"): return i.rsplit("/", 1)[1]
    if i.startswith(GL): return i[len(GL):].rsplit("/", 1)[-1]
    if i.startswith(GP): return i[len(GP):]
    if "roofer-online" in i or "planspace" in i:
        return re.sub(r"[^A-Za-z0-9]+", "-", i.rsplit("/", 1)[1]).strip("-")
    return re.split(r"[/#]", i.rstrip("/"))[-1]

rows = []
slugs = collections.defaultdict(list)
for i in defs:
    slugs[slug_of(i).lower()].append(i)
collide = {s: v for s, v in slugs.items() if len(v) > 1}

new_of = {}
for i in sorted(defs):
    s = slug_of(i)
    kind, note = "kept", ""
    if s.lower() in collide and i.startswith(GP):
        kind, note = "kept", "generic type keeps the bare slug; colliding implementation types are prefixed"
    elif s.lower() in collide:
        if i.startswith(GL):
            grp = i[len(GL):].rsplit("/", 1)[0].replace("/", "-")
            s = f"{grp}-{s}"
        else:
            s = f"{scheme(i).split()[0].lower()}-{s}"
        kind, note = "renamed-collision", f"slug collides with {', '.join(x for x in collide[slug_of(i).lower()] if x != i)}"
    if scheme(i) == "Geonovum process endpoint":
        kind, note = "review", "process-endpoint URL used as type; provisional slug"
    new_of[i] = NEW + s
    rows.append([i, NEW + s, kind, "", "", scheme(i), defs[i]["repos"], note])

# aliases / gaps from undefined references
ci = {k.lower(): k for k in defs}
for r in undef:
    i, cat = r["iri"], r["category"]
    canon, kind, conf, note, new = "", "gap", "", "", ""
    if cat == "alias-kurrawong-catalog-url":
        ga = "http://ospd/demo/" + i.rsplit(":", 1)[1]
        canon = ga if ga in defs else ""
        kind, new, conf = ("alias", new_of.get(ga, ""), "high") if canon else ("gap", "", "")
    elif cat == "alias-crim-snapshot":
        tail = i.split("/def/process-type/", 1)[1]
        gl = GL + tail
        if gl in defs:
            canon, kind, new, conf = gl, "alias", new_of[gl], "high"
        else:
            kind, note = "gap", "CRIM snapshot IRI with no GeoLabs counterpart found"
    elif cat == "undefined-openscience-process-type":
        s = slug_of(i); new = NEW + s
        note = "referenced in examples; no definition"
    elif cat == "undefined-rim-activity-type":
        s = slug_of(i); new = NEW + s
        note = "no definition; possible alias of https://rss-hydro.lu/ns/mom/WorkflowRun (to review)"
        if "https://rss-hydro.lu/ns/mom/WorkflowRun" in defs:
            canon, conf = "https://rss-hydro.lu/ns/mom/WorkflowRun", "low"
    elif cat == "external-vocabulary":
        kind, note = "external", "external vocabulary; not mapped"
    elif cat == "example-local-type":
        kind, note = "gap-example-local", "type local to an example; decide whether to define or leave"
    rows.append([i, new, kind, canon, conf, scheme(i) if scheme(i) != "other" else cat, r["repos"], note])

with open(f"{D}/mapping.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["old_iri", "new_iri", "kind", "canonical_old_iri", "confidence", "source_scheme", "repos", "notes"])
    w.writerows(rows)
print(collections.Counter(r[2] for r in rows))
print("slug collisions:", {k: v for k, v in collide.items()})
# new IRI uniqueness (excluding aliases which intentionally share)
c = collections.Counter(r[1] for r in rows if r[1] and r[2] in ("kept", "renamed-collision", "review", "gap"))
print("duplicate new IRIs:", {k: v for k, v in c.items() if v > 1})
