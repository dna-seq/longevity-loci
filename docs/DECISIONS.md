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

## D10 — the quote check set beside the plugin's QUOTING.md (2026-11-05)

Amends D9, now that the module-creator plugin (v0.48.0) is installed and its `find-evidence` skill's
`references/QUOTING.md` was read. Its `quote_matches` is whitespace- and case-insensitive literal containment;
ours keeps case (D9), so ours is the stricter on case and the looser on typography (quotes, dashes, ligatures,
line-break hyphens). Kept as D9, with two of its rules added: a quote that is the article's title is refused
(its rule 1), and one quote cited for two or more variants is flagged `shared_quote` (its rule 2, whose default
grain is one passage per article and variant). The looser side matters downstream: the plugin matches against
its own retrieved text, so a quote is best copied from the cached text, never retyped (its rule 3c). Rejected:
adopting its case-insensitive match (it locates a quote whose gene or protein symbol changed case).

## D11 — a nominal replication, and a design for an age threshold (2026-11-10)

The curator's first row (46-LPA) held a tier-A replication at p 0.002 (CHARGE-EU, cases aged 90+), which the
vocabulary could only call `not_significant`, so it supported nothing and §4.1's "independent replication (p <
0.05)" was invisible to the check. `stat_significance` gains `nominal` (1×10⁻⁵ ≤ p < 0.05), which supports;
`study_design` gains `age_threshold_case_control`, cases above an age against younger controls, which is neither
a birth-cohort percentile nor a centenarian design. Rejected: a `replicates:` marker on the study, a second field
saying what the p-value already says. Not added: a band on `not_significant` (a row tagged so with p < 0.05 would
turn red at once; the curator re-tags), and a hard rule that tier A needs two supporting articles (a new rule, the
person's to ask for). The module's 0.7.1 vocabulary is closed at significant, suggestive, not_significant and
unknown, so the export (RM1) has no value for `nominal` yet; that is RM1's to settle.

## D12 — a database release is cited like an article, and its quotes stay unknown (2026-11-10)

The curator's first row rested three claims on database releases (Open Targets 26.09 fine-mapping and L2G,
gnomAD frequencies), which no cite could name, so they stood unsupported. A release gets a note,
`db-<database>-<release>`, cited from axes and flags; a study may not rest on one. Its quotes are what the record
shows. `check quotes` finds them unknown (`no_text`, exit 4) until a fetcher caches the release's record, which is
a plan item of its own. Rejected: letting the curator cache the record by hand, since the check would then locate
the curator's quote in the curator's own paste and agree with itself; and a free-text source field on the claim,
which no check could read.
