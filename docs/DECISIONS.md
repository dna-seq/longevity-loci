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

## D13 — a replication look-up supports on its allele, direction and p (2026-11-10)

The curator's 46-LPA holds CHARGE-EU 90+ (Joshi 2017, Table 2), a look-up at P 0.002 that states the allele and
the direction and no effect size, so as `nominal` it failed §6.3 ("required on every row supporting a tier A/B
variant": p_value, effect_size, effect_measure, effect_allele) and was held as `not_significant`. The person,
asked: (a) a replication look-up may support with allele, direction and p < 0.05 only, or (b) keep §6.3 strict;
answered "1a". A `nominal` study on a tier A/B row now owes `p_value`, `p_value_num`, `effect_allele` and a
`direction` (a new optional study field; `unknown` does not count), or an effect size; a `significant` or
`suggestive` one still owes all five. Rejected: (b), which leaves §4.1's "independent replication (p < 0.05)"
invisible whenever the replicating table prints only P. The export (RM1) writes no study direction on 0.7.1.

On the same question the person declined a new rule that tier A needs a second supporting article ("3 no"); D11's
"not added" stands.

## D14 — one signal named by two seed ids is one row (2026-11-10)

The seed list names some signals more than once: IL6R Asp358Ala as 8 and 157 (rs2228145, rs8192284, merged in
dbSNP), HTT as 25 and 158, TERT as 132, 133 and 153. The person, asked: (a) one row under the lower id, the other
ids noted, or (b) a row per id; answered "2a". A row gains `also_loci`, the ids it folds in, each above its own
`locus_id` and each a seed locus; a row for a folded id is a duplicate. Rejected: (b), two rows scoring one
signal twice in the module.

## D15 — a multivariate test supports on its allele, direction and P (2026-11-11)

At 67-TTC12 the curator could not write Timmers 2020's multivariate test (P 4e-10) as a study: §6.3 asks an
effect size of every study supporting a tier A/B row, and a MANOVA across healthspan, lifespan and longevity has
none. The lead settled it under the person's standing word (2026-11-11, "if this is autonomous"): a
`multivariate_healthspan_lifespan` study owes what a nominal look-up owes (D13), the allele, a direction and its P.
Rejected: an effect size from one of its component traits (that is a different study row, with that trait's
`phenotype_class`), and leaving the test in prose (the strongest P at the locus would support nothing the check
sees).

## D16 — a co-occurring lifespan signal is a lifespan study at p < 0.05, same allele and direction (2026-11-11)

§4.5 lets `HEALTHSPAN` and `MULTIVARIATE_AGEING` score "only with a co-occurring lifespan signal", and does not say
what a signal is. At 103 (rs1049053, HLA-DQB1) the curator read it as at least suggestive (p < 1×10⁻⁵) and set tier
C. Zenin's healthspan GWAS is genome-wide there (P 1.4×10⁻¹¹), and the lifespan look-ups are nominal on the same
side (Timmers 2019's summary statistics P 1.4×10⁻⁴; AncestryDNA mothers at a tag, P 3.3×10⁻⁴). The lead settled
it under the person's standing word (2026-11-11, "if this is autonomous"; "Advisor pattern" for the requirements'
silent cells): **a co-occurring lifespan signal is a scoring-class lifespan study (§4.5's first row) at p < 0.05,
on the same allele in the same direction.** That is the bar §4.1 sets for a replication, and D11/D13 already let a
nominal study support. With it, a genome-wide healthspan locus is tiered by §4.1 as any other: unreplicated in
healthspan, it is B ("a single study without independent replication"). With no such lifespan study, it is C, in
the research view, and needs no token of its own to stay out of scoring.

Rejected: the suggestive bar, which no text sets and which would make the healthspan clause of §4.1's tier A
unreachable in practice; and a `HEALTHSPAN_ONLY` token, which the tier already carries. This decides 103 and the
seed's other healthspan loci (35 IRF4, 66 TYR, 86 DEF8). Not a hard rule in the check: which study is the
co-occurring one is the curator's reading.

## D17 — what the second batch's reviews settled (2026-11-11)

The lead's adversarial reads of rows 2, 8, 10 and 103 found four points no rule settled. The lead decided them under
the person's standing word (2026-11-11, "if this is autonomous").

1. **D16's co-occurring lifespan study is the locus's own signal.** At 103, Timmers 2019's P 1.4×10⁻⁴ at
   rs1049053 is about what LD with row 38's lead predicts (conditional z ≈ 0.6 to 1.7), and its AncestryDNA tag
   also tags 38's lead. A lifespan study whose association LD with another row's lead explains co-occurs with
   that row, not this one: one lifespan signal is scored once. 103 is C. Its healthspan replication failed with
   about 0.8 power (heterogeneity P ≈ 0.02), red-flag heterogeneity under the 71/67 rule, which caps it at B even
   with a signal of its own.
2. **Causal confidence is read from the credible sets of the row's own claim.** These are the scoring classes'
   studies (lifespan, longevity, healthspan, multivariate ageing). A variant in sets for other traits only (IL6R
   rs2228145, in 286 sets for CRP, IL-6 and others) is C4 for the row, §4.2's "not assessed" for the lifespan
   claim. The other traits' sets are cited from the mechanism.
3. **"Genome-wide" is read at the P the paper uses for its own significance call**, and the row says which
   correction that is (genomic control, LD score intercept, none) in `statistical_test`. Rows do not re-correct a
   paper's P by another method.
4. **`effect_allele` is the lifespan-increasing allele** (§6.2: "Harmonise `effect_allele` to the
   lifespan-increasing allele"). `check rows` lists a variant with `direction: risk` as `unharmonised`, a warning.
   Its `trait_efo_id` is the anchor study's trait, by §6.2's list (healthspan EFO_0009762, parental longevity
   EFO_0007796, life span OBA_VT0005372).

## D18 — a trade-off, an obesity locus's label, and multivariate ageing at tier A (2026-11-11)

From the curator's row 11 (LINC01875); the lead settled it under the person's standing word.

1. **A `tradeoff` is quoted harm.** The longer-life allele raises a disease, or an established risk factor for one
   (LDL, blood pressure, low bone density for osteoporosis and fracture). With no quote tying it to a harm, it is no
   trade-off.
2. **A locus acting through weight is `modifiable`** with `act_behaviour:weight`, as §4.2's label line says
   ("acts through a behaviour: smoking, weight, sun"). It is not `modifiable` when it is a trade-off or LATE, which
   §4.2 makes unlabelled and descriptive.
3. **A multivariate ageing result does not meet tier A's first criterion.** §4.1 names longevity, lifespan,
   parental-lifespan or healthspan phenotypes; `MULTIVARIATE_AGEING` scores at B only, beside its co-occurring
   lifespan study (D16, D17.1).

## D19 — an overlapping replication, and a stratum's genome-wide hit (2026-11-11)

From the curator's 12 (KCNK3) and 13 (PRKD3), after the lead's adversarial read of 12; settled under the person's
standing word.

1. **A replication sharing a minor part of the discovery's sample is independent** when the shared part is small
   and the papers measure the cross-study covariance as negligible. 12's Deelen 2019 holds the Rotterdam Study
   (6.9 % of its 90th-percentile cases), which is also in LifeGen, and Timmers measured the covariance at about
   0.01. A replication that contains most of the discovery sample, or one the papers do not separate, is not
   independent. So 12 is A on §4.1's letter, and the row says the overlap.
2. **A genome-wide hit in one stratum is a genome-wide study, read at the paper's own threshold** (D17.3). 13's
   men-only P 3.2×10⁻⁸ at the paper's per-GWAS 5×10⁻⁸ stays B, as "a single study without independent
   replication", with `sex_specific:m`. The verdict says the paper did not correct across its three GWAS, and that
   the variant is at the frequency floor (0.1 %). Rejected: re-correcting the paper's threshold here, which D17.3
   already refuses.
3. `study_design: own_death_case_control` is added, for deceased against living in a biobank (FinnGen's Death
   endpoint). A Finnish sample's `ancestry` is `EUR`, the 1000 Genomes superpopulation; `population` names the
   Finns.

## D20 — a meta-analysis that prints no pooled effect supports on allele, direction and P (2026-11-11)

At 21-IP6K1 the genome-wide anchor is Wright 2019's maternal meta-analysis (AncestryDNA with UK Biobank, N about
660,000, P 6.9×10⁻¹⁰), which prints each arm's z-score effect and no pooled one, so §6.3's effect size has no
value to copy. As for a multivariate test (D15) and a nominal look-up (D13), a `meta_analysis` study with no
`effect_size` owes the allele, a direction and its P; the arms' effects go in `statistical_test`. The curator's
option (a), recommended. Rejected: (b), fetching Rosoff's supplement by hand to anchor on the multivariate copy of
the same signal, a manual step that changes nothing the check sees.

