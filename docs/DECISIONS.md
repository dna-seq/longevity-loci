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

## D21 — when a non-replication is a red flag (2026-11-11)

The 71/67 rule caps a row at B on "a powered non-replication in an independent sample". The reads of 103, 12 and 21
put numbers on "powered", and 21 landed between the earlier two (103: power about 0.8, heterogeneity P about 0.02,
red flag; 12: about 0.7, P 0.26, not). The lead fixes the line under the person's standing word: **a non-replication
is a red flag when its one-sided power is at least 0.8 and the heterogeneity P below 0.05.** Power is computed
from the discovery effect without the replicating sample (backed out of a pooled estimate that contains it), at the
replication's standard error. The row says both numbers. 21 (power 0.6 to 0.7, heterogeneity P about 0.055) is no
red flag and keeps A.

## D22 — R-TIER-2's reach, and what replicates (2026-11-11)

From the lead's adversarial read of rows 16 to 19, settled under the person's standing word.

1. **R-TIER-2 covers every old-against-young case-control**, a centenarian design or an age threshold (90+ against
   controls under 75, D11's `age_threshold_case_control`). Its stated reason, cohort and batch confounding, is the
   design's, not the cut-off's. `check rows` holds both to it. A percentile case-control against a birth cohort
   (Deelen's) stays outside it.
2. **A replication is a study in a scoring class** (§4.5's first row: extreme survival, parental lifespan, own
   survival, viability as confirmation). A healthspan or multivariate result replicates nothing on its own. It
   scores only beside a lifespan study (D16), so it does not lift R-TIER-2's "unreplicated".
3. **A cross-ancestry null is not "explicitly contradicted" (tier D) when the locus's proxies lean the discovery's
   way.** It is D when the European look-up is flat, as for §4.1's own IL6 example (Timmers P 0.84). Row 18
   (TMEM43) is C: a powered European null at Deelen, but its proxies lean to T in Timmers (P 0.05 to 0.14) and
   Zenin's healthspan gives P 0.0035. Where a paper prints a P its own β and SE do not reproduce, the row reads the
   printed P (D17.3) and says the discrepancy.

## D23 — a frailty index is healthspan-class; viability confirms, never replicates (2026-11-11)

From the curator's 24 (NLGN1): Atkins 2021's frailty index is genome-wide at a proxy of the lead. A frailty index
measures accumulated deficits, which the requirements' outcome profile files under healthspan, so it is
`HEALTHSPAN`-class (§4.5): it can anchor §4.1's first criterion, and it scores only beside a lifespan study (D16).
A viability result (`VIABILITY_AF`, a GWAS of current age) is "confirmation only" in §4.5. It does not replicate,
so it cannot carry a row to A. 24 is B: the curator's option (a), recommended.

## D24 — when a second gene makes the effector call ambiguous (2026-11-11)

§4.2's E3 is "ambiguous" and the requirements do not say what makes it so. Once the curator's Open Targets queries
included QTL colocalisations (cis only, H4 ≥ 0.8), four rows had a leading gene and a minor rival, so the letter
read by row 17 (two genes each meeting a criterion) dropped each to E3. The lead's rule, under the person's standing
word: **a rival gene makes the call ambiguous when it meets an E1/E2 criterion of its own (L2G ≥ 0.5, or a cis-QTL
colocalisation) and holds at least a tenth of the locus's cis colocalisations, or passes L2G itself.** A rival with
a stray tissue's eQTL, under a tenth, does not veto. Counts are over the row's lifespan-class credible sets.
Applied: 81 is E1 FES (FURIN 7 of 120 colocalisations); 15 is E3 (the unnamed ENSG00000230393 holds 6 of 24); 71 is
E3 (ALDH2 holds every colocalisation, SH2B3 none); 6 is E3 (SORT1 and CELSR2 both pass L2G). Rejected: the bare
letter, under which one tissue's eQTL vetoes any call; and a looser dominance cut, which no source gives.


## D25 — when a tested discovery is tier D; calibrating a red flag; the fourth batch's questions (2026-11-11)

From the lead's adversarial read of rows 25, 26 and 31 and the curator's questions on 25 to 31, settled under the
person's standing word.

1. **A genome-wide discovery that fails a powered test in its own ancestry is tier D** ("explicitly contradicted",
   §4.1) when the test is a D21 red flag and no independent scoring-class study (D22.2) gives p < 0.05 in the
   discovery's direction. §4.1's own example has this shape: USP42 and TMTC2, genome-wide in one study, null in
   Timmers' powered look-up "at effect sizes originally published" though leaning the same way (P 0.27, 0.11). B's
   "a single study without independent replication" is a hit nobody has tested, not one tested and failed; the
   71/67 rule is a ceiling on A, never a floor under D. A null in another ancestry stays with D22.3, so 18 (an East
   Asian discovery) is C. Applied: 26 is D (Deelen's own UK Biobank validation, power about 1.00, heterogeneity P
   2e-4 to 9e-4 at half the effect for the parental cut). 31 keeps C: Deelen's 99th percentile gives P 0.012 at an
   r² 1.0 proxy, and whether Deelen is independent of NECS is not yet shown; once the curator has quoted NECS's
   controls from the main text, it is B (capped) if the independence holds and C if it cannot be shown. A smaller
   replicated effect is §4.1's B clause, never a reason for D.
2. **A tier D row is neutral on every genotype**, as R-TIER-1's row is: not supported means no weight. Its
   conclusions say what was reported and that it was not supported. `check rows` holds every D row to it.
3. **A red flag that rests on converting one scale to another** (a parental-lifespan β against a percentile or
   centenarian odds ratio) must hold under both of Timmers 2019's calibrations: the APOE factor (q91's method) and
   the loci's mean factor (Figure 4 source data, "Mean"). APOE's effect grows with age, so its factor overstates
   what a midlife locus should show at the oldest ages, and the mean understates it for a late one; a flag that
   only one of them raises is no flag. The row states power and heterogeneity under both. Applied: 25's Deelen 90th
   percentile flags under APOE only (power 1.00, heterogeneity P 0.0024; mean factor 0.74, 0.36), so 25 keeps A on
   FinnGen with Biobank Japan (one-sided P 0.0011, the size expected at r² 0.67) and Deelen's 99th (P 0.0093 at the
   lead). 31's LifeGen null flags under both. A comparison on one scale (26: Deelen against Deelen's validation)
   needs no calibration.
4. **A folded locus's credible sets count for the effector** (D14, D24): folding says the two seed ids are one
   signal, so every lifespan-class set holding either counts. 25 is E3: in mvAge's set, MSANTD1 passes L2G (0.55)
   and RGS12 holds 4 of 18 colocalisations. Its conclusions may name HTT only to say the SNP is not the
   Huntington's repeat, never as the gene acting (R-CAUSAL).
5. **A healthspan-class credible set the tier does not rest on does not set causal confidence** (D17.2). 27 keeps
   C4/E4; Foote 2025's frailty set (lead PIP 0.043, KLF3 L2G 0.76) is named in prose.
6. **A second, independent signal at a seed locus with no seed id of its own** (28's rs13141210; ADD1 rs16843603,
   found at 25) goes to the scout's queue as a candidate row, curated after the seed list; meanwhile the row names
   it in prose.
7. **A mechanism is named when something shows the effect runs through it.** 29 is `general_ageing`: its lead tops
   three smoking sets at PIP about 0.06, and smoking, adiposity and diabetes are about equally strong; the smoking
   link goes in prose. The curator's default, `smoking_lungs`, rejected.
8. **Vocabulary**: a frailty index stays `meta_analysis` with `HEALTHSPAN` (D23); a look-up whose model the paper
   does not state is written as the paper describes it. Deelen's parental 90th line stays `EXTREME_SURVIVAL_CC`,
   `percentile_case_control_p90`, with `age_of: parent` and the case and control definition in its test.
9. **An arm already inside the discovery's pooled P replicates nothing**, however separate its people (32 and 16:
   Chang 2022's 129 healthy agers and 500 others, the same Singapore cohort and team, genotyped later). The P it
   would replicate already holds it, and §4.1 files "replicated only in small or same-group samples" under C. D19.1
   is about a sample outside the discovery that shares a measured part of it, not an arm within it. The curator's
   default (a); (b), separate people read as independent, rejected.
