# Analysis tables

Working tables behind the register, published for review.

- `activity-types-review.csv`: one row per defined activity type (157). Review here. The `suggested_*` columns are machine-made first guesses (generic/specific level, generic parent, action, basis); fill in `reviewer_level`, `reviewer_generic_parent` and `reviewer_comment` to override or comment.
- `mapping.csv`: every source IRI mapped to its register IRI (kind: kept, alias, renamed-collision, gap, external, review).
- `duplicates.csv`: duplicate/related groups with canonical item, role, confidence and rationale (confidence medium/low needs human review).
- `family-assignment.csv`: family (group) of each register item.
- `undefined-references.csv`: IRIs referenced as activity types but not defined anywhere.
