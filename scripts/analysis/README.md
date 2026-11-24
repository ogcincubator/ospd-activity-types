# Analysis pipeline (run from a scratch venv with rdflib installed)

Inputs: shallow clones of the OSPD repositories in `<repos>/<owner>__<name>` (list in `repos.txt`).

1. `scan.py <repos> <out>`        -> activity-types.csv, range-properties.txt, untyped-activity-instances.txt, parse-failures.txt
2. `post.py definitions <out>`    -> definitions.csv
3. `undef.py <out>`               -> undefined-references.csv (categories: alias / gap / external / example-local)
4. `mapping.py <out>`             -> mapping.csv (new IRIs, kinds kept / renamed-collision / alias / gap / review / external)
5. dedupe: an LLM pass over definitions.csv using `analysis/prompts/dedupe-prompt.md` -> duplicates.csv
6. `post.py merge-dups <out>`     -> adds dup_groups to mapping.csv
7. `families.py <out>`            -> family-assignment.csv (the committed copy is hand-edited and is the source of truth;
                                    the script writes family-assignment.generated.csv when one exists)
8. `../generate.py <repos> <out>` -> _sources/<family>/data.ttl and _sources/core/data.ttl

`<out>` = this repository's `analysis/` directory. The committed CSVs are the current results.
