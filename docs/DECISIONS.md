# Decisions

The calls settled with the maintainer, one section each, `## Dn — the call (date)`, newest last: what
was decided, why, and the alternative it rejected. A call is never edited after the fact; a later one
that changes it says which it amends.

D1 to D7 are the requirements' decisions for the module author (`docs/longevitymap_v2/longevitymap_v2_requirements.md`
§11); this record starts at D8 so the two never share a number.

## D8 — the row and note formats (2026-11-05)

Taken by the lead, reversible, for the person's review. A row is a YAML file per locus carrying the seven axes of
the requirements' summary (tier, mechanism, pleiotropy, age of action, outcome profile, actionability, context) as
fields, each with the quotes it cites; §4.2's other rows (causal, effector, protection type, animal support, LD
redundancy) are `flags` tokens, as the requirements' interim format homes them. Rejected: all eleven §4.2 rows as
fields (heavier rows, and the requirements' own count is seven); Markdown rows with front matter (prose the
check cannot read, where the corpus already holds the prose). A note is Markdown, one per article, quotes as
`> [qN]` lines under dated readings, so a later reading appends and never rewrites.

## D9 — what "verbatim" means to the quote check (2026-11-05)

Taken by the lead. The requirements point to the module-creator plugin's `QUOTING.md` for how a quote is located;
the plugin is not installed on the lead's machine, so the rule is this repository's own (`docs/FORMATS.md`):
compatibility forms, typographic quotes and dashes, soft hyphens and whitespace are forgiven, a line-break hyphen
is tried both ways, case and words must match. To be reconciled with `QUOTING.md` when the plugin is read.
Rejected: case-insensitive matching (it would locate a quote whose meaning changed with case, gene against
protein symbols); exact bytes (every PDF extraction would fail it).
