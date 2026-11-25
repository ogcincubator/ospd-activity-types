# Analysis tables

Tables behind the registers, published for review. They are a **snapshot of the consolidation** (2026-11-25): the
`data.ttl` files are now edited by hand and are the source of truth, so these tables are not regenerated from them.

- `activity-types-review.csv`: one row per defined activity type (157). Review here. The `suggested_*` columns are machine-made first guesses (generic/specific level, generic parent, action, basis); fill in `reviewer_level`, `reviewer_generic_parent` and `reviewer_comment` to override or comment.
- `proposed-generic-types.csv`: the three generic types we added (no source IRI) so that every specific type has a parent.
- `mapping.csv`: every source IRI mapped to its register IRI (kind: kept, alias, renamed-collision, gap, external, review).
- `duplicates.csv`: duplicate/related groups with canonical item, role, confidence and rationale (confidence medium/low needs human review).
- `family-assignment.csv`: family (group) of each register item.
- `undefined-references.csv`: IRIs referenced as activity types but not defined anywhere.
