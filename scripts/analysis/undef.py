import csv,re,sys
D=sys.argv[1]
rows=list(csv.DictReader(open(f'{D}/activity-types.csv')))
def cat(i):
    if re.search(r'demo:GA\d+$',i): return 'alias-kurrawong-catalog-url'
    if 'geolabs.github.io/bblocks-process-profiles/def/process-type' in i: return 'alias-crim-snapshot'
    if 'example.org/ospd/process-types/' in i: return 'undefined-openscience-process-type'
    if i.endswith('w3id.org/ogc/rim/activity-type/ActivityType'): return 'external-vocabulary'  # the RIM class itself, not a type
    if 'w3id.org/ogc/rim/activity-type/' in i: return 'undefined-rim-activity-type'
    if re.search(r'wf4ever|purl.org/geojson|w3.org/ns/prov|xmlns.com/foaf',i) or i.startswith('wfprov:'): return 'external-vocabulary'
    if re.search(r'example\.(org|com)',i): return 'example-local-type'
    return 'other'
und=[r for r in rows if r['is_definition']=='False' and 'ref:' in r['methods']]
w=csv.writer(open(f'{D}/undefined-references.csv','w',newline=''))
w.writerow(['iri','category','repos','n_files','example_file'])
import collections
print(collections.Counter(cat(r['iri']) for r in und))
for r in sorted(und,key=lambda r:(cat(r['iri']),r['iri'])): w.writerow([r['iri'],cat(r['iri']),r['repos'],r['n_files'],r['example_file']])
