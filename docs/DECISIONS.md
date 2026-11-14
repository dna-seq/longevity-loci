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
   (TMEM43) is not D: a powered European null at Deelen, but its proxies lean to T in Timmers (P 0.05 to 0.14) and
   Zenin's healthspan gives P 0.0035. (C when written; B with `replication_failed` since D25.13 and D26.11.) Where a paper prints a P its own β and SE do not reproduce, the row reads the
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
   Asian discovery) is not D (B with `replication_failed` since D26.11). Applied: 26 is D (Deelen's own UK Biobank validation, power about 1.00, heterogeneity P
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
10. **31 is B.** Gurinovich's main text (quoted, 03d4ef5) gives 306 NECS referents and 2,593 Illumina repository
   controls; neither Deelen 2019 nor Gurinovich names the other's cohorts, so Deelen's 99th percentile (P 0.012 at
   an r² 1.0 proxy, NECS's direction) is independent as far as both papers show (D19.1 asks a measured overlap, and
   none is shown). R-TIER-2 is lifted; LifeGen's red flag under both calibrations (D25.3) caps the row at B with
   `replication_failed`. NECS prints no effect size, so the row enters the crude odds ratio derived from its printed
   allele frequencies, saying it is derived and how (the curator's option (a)); keeping C until an effect is printed
   somewhere, (b), rejected: the effect is the paper's own counts, only not divided out. `check rows` lifted
   R-TIER-2 only on a second genome-wide study; it now follows D22.2 (the lead's fix, with its test). The open
   points, the repository controls' source studies and any LLFS member in NECS, stay in the row.
11. **35 is B, not A.** D16 tiers a healthspan locus with a co-occurring lifespan study by §4.1, and D22.2 says what
   replicates: a scoring-class study. Zenin's healthspan hit replicating in 96,313 other UK Biobank people is
   healthspan replicating healthspan, which counts for nothing toward A; LifeGen (P 0.0016) shares UK Biobank, so it
   co-occurs (D16) but does not replicate; Deelen is flat (P 0.13, 0.15), with no red flag. The curator's default A
   rejected; its own reading of D22.2 taken. **One mechanism, one actionability**: `skin_sun` rows are `modifiable`,
   `act_screen:skin` (§4.2 names sun among the behaviours), so 17 moves from `descriptive` to match 35.
12. **36 keeps B, and is E2 ZSCAN23.** D25.3's second calibration is a mean over loci, not one other locus: scaled
   within FinnGen, APOE flags (power 0.97, heterogeneity P 1e-4) and MUC5B alone is not the mean. If the FinnGen
   look-up holds enough non-APOE leads with both measures to average, the row computes that mean, and A follows only
   if it raises no flag; otherwise "no red-flag heterogeneity", A's last criterion, is unknown, and unknown is not
   shown, so B. Effector: §4.2's E2 is "coloc alone", and Park's own colocalisation (PP4 0.934, one pancreatic
   tissue) meets it; with no Open Targets record, D24's rival check could not run, and the row says so rather than
   reading that as no rival (as 57's single adipose QTL). The curator's default E4 rejected: it would file an
   assessed colocalisation as unassessed.
   The mean is over leads that hold up in the look-up's own cohort: leads that themselves fail there (36's PRKD3 and
   CELF2, rare and sex-specific) pull the factor toward zero and would clear every flag by construction. With only
   MUC5B left, the mean is unknown and 36 is B (the curator's (a)).
13. **A replication's P is one-sided, in the discovery's direction.** §4.1 asks the same allele and direction, so the
   test is directional and a two-sided P counts the wrong tail too; 25 already counted Timmers 2022's one-sided P,
   and D25.1's "p < 0.05 in the discovery's direction" reads so. A row says which it quotes. 37: AncestryDNA mothers
   at rs3130467 (one-sided 0.037) and LifeGen mothers (0.048) replicate, so not D. **`replication_failed` marks a
   sample that fails**, not one that replicates with a smaller effect: AncestryDNA's printed heterogeneity P 0.040
   at power 0.97 makes 37 §4.1's "replication with a much smaller effect", B, and the flag comes off unless another
   sample fails. Mechanism stays `general_ageing` (D25.7) with `mech:autoimmune`; immune_inflammation rejected, no
   route shown.
   It holds back to every row, D16's co-occurring lifespan study included (p < 0.05 one-sided, same allele and
   direction): 2 PABPC4, 4, 17 CASP8, 18 TMEM43 and 93 LDLR, which read a same-direction P of 0.05 to 0.10 as a miss,
   are re-read under it as one sweep, each tier move reported and read adversarially by the lead. A cross-ancestry
   look-up that now passes (18) is §4.1's "ancestry-specific replication only" at most.

## D26 — batch five: corrected P values, one-sided cells, an invalid discovery, a weak discovery contradicted (2026-11-11)

From the curator's rows 40 to 47 and the D25.13 sweep; the lead settled them under the person's standing word.

1. **A P value is read after the paper's own genomic control.** Wright 2019's Table 9 AncestryDNA P is raw; at its
   Supplementary Table 3 λ (1.113 mothers, 1.182 fathers) 27's and 71's fathers (raw 0.0496, 0.0498) become 0.065
   and 39's 0.055, and do not replicate; 37's 0.037 holds either way. The paper's own calls use the corrected P, and
   a raw P counts its inflation as evidence. The curator's default; raw P rejected.
2. **An outcome cell reads one-sided too**, as D25.13 reads a replication: `+` is p < 0.05 in the discovery's
   direction. The curator's default.
3. **A flag that converts scales needs both calibrations shown (D25.3); one that cannot be computed is unknown, and
   unknown sets no token.** 40's FinnGen null flags under APOE's factor (power 0.86) with the within-FinnGen mean
   (D25.12) not computed, and 47's LifeGen and FinnGen nulls flag under APOE's top 1 % factor with no mean factor
   for that phenotype: neither row carries `replication_failed`, and each says the second calibration is unknown.
   The curator's default at 40 (as 39); the default at 47 (flag on APOE's factor alone) rejected. Both stay B.
4. **40 carries no trade-off.** The longer-life C lowers cystatin C eGFR, but the quoted disease sets at the locus
   (acute renal failure at the lead, three chronic kidney disease sets) run with T, so no quote ties C to a harm
   (D18.1). The curator's default; a trade-off by the biomarker alone, as 39, rejected.
5. **`PROTECT:ABSENCE_OF_RISK` needs a disease at the locus**, as §4.2 defines it ("the common non-risk allele at a
   disease locus"). 42 carries no token (the curator's default, as 21), and 28, whose pleiotropy is empty, drops
   its token.
6. **43 FOXO3 stays B.** Broer 2015's P 1.85e-10 pools the candidate SNP with the published samples that proposed
   it, so it is a candidate meta-analysis, not a genome-wide discovery (Timmers 2020: never genome-wide in a scan);
   it does not anchor A. The healthspan cell is 0: Zenin and Timmers 2020 lean G healthier at nominal P, while
   Foote's frailty factor (healthspan class, D25.8) puts G frailer at P 4e-10, and `+` would tell a reader the
   opposite of a genome-wide result. The row says mixed. The curator's `+` rejected.
7. **A genome-wide P the paper's own filter excludes is no discovery: 44 is D**, §4.1's "overfit source". Park
   2025's deposit line (P 8.9e-9) rests on about 28 allele copies, thirty times below the paper's MAF 0.1 % filter,
   and the paper does not report it. The genotypes stay neutral (D25.2), lifespan becomes `untested` (the one test
   is the excluded line), and gene PLN at E2 stands by §4.2's letter (L2G ≥ 0.5 alone). 75 KLF12, from the same
   deposit, is read the same way when reached. The curator's C rejected: C is "suggestive", and this line is not a
   suggestive test but an invalid one.
8. **A sub-genome-wide discovery that fails a powered test in its own ancestry is D, a fortiori of D25.1: 45 is D.**
   Deelen's trans-ethnic P 9.8e-7 meets LifeGen's red flag under both calibrations (heterogeneity P 0.044 and
   0.0011), with no independent scoring-class p < 0.05 its way (LifeGen one-sided 0.088, FinnGen 0.14, Zenin null).
   A genome-wide discovery would be D on that evidence; a weaker one cannot stand above it. The genotypes go
   neutral and the trade-off goes: Kemp 2014's paediatric bone density with no quoted adult harm is not D18.1's
   "low bone density for osteoporosis and fracture". The curator's C rejected.
9. **47's age of action stays UNKNOWN.** Its two contrasts (Deelen's 99th against 90th percentile, Pilling's top
   1 % against the continuous scan) contrast extremity of survival, not the age the allele acts. It carries the
   surviving id rs371933919 with the seed's rs528161076 as a synonym. Indel genotypes are written in the VCF
   alleles (`T/T`, `T/TC`, `TC/TC`), now said in FORMATS.md.
10. **41 PRDM13 is D on 7's ground, not on an r² cut.** NECS's genome-wide P (3.58e-8, its own 5e-8 threshold)
   rests on a control frequency of 0.0004 where every reference sample has about 0.10, which the authors themselves
   doubt: an overfit source, as 44. LifeGen's lean at rs12660804 (r² 0.605, D′ 1; one-sided about 0.02) is
   therefore not weighed as replicating a discovery. Rescaled it fits a tiny common-haplotype effect, consistent
   with Deelen's flat line, not NECS's, and FinnGen leans the other way at the same proxy. The row names it without
   counting it. There is no "r² 0.8 the rows use": 25 counted rs362273 at r² 0.67, and the row drops that phrase. The
   curator's (a); (b), C as row 19, rejected (19's replication is unknown; 41's has been tested, and by D25.1's
   letter a counted replication would give B with the flag, not C).
   Corrections: the heterogeneity uses the Woolf SE from the counts (17.7 case copies, 2.32 control copies; SE
   0.70, z about 4.0, not 0.51 and 5.4); the flag holds. The crude OR (15 to 19 by the one-figure control
   frequency, on about 2 control copies, Wald z 4.0 against the paper's 5.51) leaves `variants[]` and stays only in
   NECS's `statistical_test`: D25.10 entered a crude OR because the counts were the paper's own, and here the paper
   disowns them. Deelen includes LLFS, with a Boston field centre and NECS's authors among its authors, so "no NECS
   among them" becomes "no NECS named; LLFS overlap unknown", as row 31.
11. **The sweep's raises: 2 and 17 are B; 18 is B with `replication_failed`.** 2 PABPC4: Timmers' one-sided 0.035
   is D16's co-occurring study (D16 asks no independence), capped by D18.3. 17 CASP8: B as 35; Zenin's nulls are no
   red flag, being the discovery's own people and unpowered on the lifespan scale (power about 0.4), and the row
   says lifespan `+` rests on one look of three. 18 TMEM43: counting Timmers (one-sided 0.028, independent, European)
   as the replication that lifts R-TIER-2 also counts Deelen's 90th percentile, a powered European look-up in the
   discovery's own phenotype class: Liu's β 0.146 (SE 0.029) against 0.0069 (SE 0.0198), power about 1.0,
   heterogeneity P about 7.5e-5 (99th about 8e-4). Both are log odds of long-lived status, so no scale converts and
   D25.3's two calibrations do not arise; the row states that at half Liu's effect the P is about 0.06. A row cannot
   count one European look-up and set aside the other, so 18 carries the flag, as 31; C (no European look-up
   counts) rejected, being the reading D25.13 replaced. D22.3 and D25.1 are amended to say so. A one-sided pass
   counted as replication is marked `stat_significance: nominal` (as 25), on all three rows.
12. **`check rows` cannot see R-TIER-2 behind a meta-analysis.** Liu's anchor is `meta_analysis` of old-against-young
   samples, and the design field does not carry its parts' designs, so the check passes 18 unchecked. That is a
   limit of the field, said here rather than guessed by the check; the row's prose carries the rule.
13. **A one-sided P derived from a printed two-sided one is its own field, `p_one_sided`.** `p_value` and
   `p_value_num` stay what the article prints; `p_one_sided` holds half of it in the discovery's direction, and
   the nominal band reads it (`check rows` asks it to be half the printed value, within 5 % for rounding). It
   applies to every study that counts a derived one-sided pass (2, 17, 18, 37, 39 and any other), which is then
   marked `nominal`. A source that prints a one-sided P itself (25's Timmers 2022) keeps it in `p_value_num`. The
   curator's (b), the printed value replaced in `p_value_num`, rejected: the field would stop being what the
   article says; (a), `not_significant` with the pass in prose, rejected: the field would read as a non-replication.
   **Row 2 drops `PROTECT:ABSENCE_OF_RISK`** (D26.5): its pleiotropy is broad, but no disease is quoted at the locus.
14. **48 IL6 (rs2069837) is D, on 41's ground before D25.1's.** Zeng 2016's combined P 1.8e-9 rests on genotypes its
   own group later disowned: Liu 2021 says the SNP failed its quality control, and Zeng's southern controls carry G
   at 0.033 against 1000 Genomes CHS 0.143. The authors' own QC rejecting the call is an overfit source (§4.1's D,
   as 41 and 44), and §4.1 names IL6 among its contradicted examples. Deelen 2019's European 90th percentile
   (one-sided 0.019, A's side) is therefore not weighed as replicating a discovery; it is named, not counted, as
   41's LifeGen lean, and the other independent looks lean the other way or are flat (Timmers one-sided 0.84, a red
   flag under both calibrations; the EU 2014 consortium inside Deelen at P 0.90 on G's side; FinnGen death and
   Zenin toward G). The curator's (b), row 18's shape, rejected: 18's discovery is not in doubt, 48's is. (c)
   rejected as the reason: Deelen 2019's 90th is independent of CLHLS, and the D does not rest on it. Genotypes
   neutral, no trade-off.

## D27 — rows 48 to 52: an arm against its own pool, the mean factor's direction, a Genomic SEM factor (2026-11-11)

From the curator's rows 48 to 52; the lead settled them under the person's standing word.

1. **An arm inside a pooled P contradicts it no more than it replicates it (D25.9's mirror), but its heterogeneity is
   the discovery's own.** 49's Liu dataset 2 (β −0.097 against dataset 1's 0.370, heterogeneity P 6.7e-5) is not an
   independent sample, so no D rests on it; it is recorded as heterogeneity inside the discovery, which bars A by
   §4.1's last criterion on its own. 49's D rests on Deelen's 99th and Timmers under D22.3 (Liu is East Asian; corrected by D28.8). The curator's default.
2. **The mean factor divides.** Timmers' Figure 4 sheet defines Alpha as calibrated longevity β over lifespan β, so a
   longevity log OR carried to the parental scale is divided by 0.4175. 48 and 33 multiplied and are corrected;
   48's flag holds. At 33 the flagging test is Timmers itself, which also replicates (one-sided 0.017): a smaller
   effect replicating, §4.1's B, no `replication_failed` (D25.13). 31 and 45 already divided.
3. **A Genomic SEM factor is multivariate, whatever its traits.** Foote 2025's frailty factors are latent factors of
   several traits, which its own deposit calls multivariate: `MULTIVARIATE_AGEING`, scoring at B only beside a
   co-occurring lifespan study (D18.3), as mvAge. 51 is B (the curator's (b)); ABO, IGF2R, POM121C, GBX2/ASB18 and
   HP are read the same way. (a), A on Foote as healthspan-class, rejected: D25.8 made a frailty *index* healthspan,
   not a factor modelled out of other traits; (c), C, rejected: R-TIER-4 is about n = 1 genomes, and D18.3 already
   scores a multivariate hit at B. 43's Foote entry takes the same class; D26.6's healthspan 0 there stands on the
   conflict of directions.
4. **A cell's `+` is set aside only by a genome-wide opposite (D26.6).** 50's lifespan stays `+` (Timmers 0.0016),
   FinnGen's nominal opposite (P 0.035, power 0.50) named. 48's defaults stand (Deelen's 90th a nominal entry,
   exceptional survival 0, healthspan 0, E3 by the letter). 51's trade-off (lumbar disc herniation) makes it
   descriptive (D18.2).
5. **Triglycerides have no `act_test` in §4.2: 52 is descriptive.** The curator's (a). Adding `act_test:tg` changes
   §4.2's vocabulary, which is the design's, not the curation's; it waits for a design pass. (c), stretching
   `act_test:ldl`, rejected: rs268 barely moves LDL.
6. **D25.5 holds for any scoring-class set the tier does not rest on**, multivariate included: Foote's sets at 43
   (PIP 0.065) and 27 (0.043) set no causal confidence, so both stay C4. The curator's (a); (b), D17.2's letter
   giving C3, rejected: D25.5's reason is that causal confidence follows the evidence the tier stands on.
7. **A colocalisation its own source flags for QC names a candidate, not an effector: 53 is E3.** The single-cell
   eQTL study behind GULOP (303 samples, a QC flag, its set led by another SNP, lead PIP 0.058, CLPP 0.05) meets E2's
   letter, but a flag the source itself raises makes the call ambiguous, §4.2's E3, with GULOP named as the candidate
   in prose. 36's E2 (D25.12) stands: its colocalisation carried no such flag. The curator's (a) rejected; (c), E4,
   rejected: the gene was assessed.
8. **53's mechanism is `general_ageing`** (D25.7): no record at the lead shows a route; the tag's lung-cancer set and
   a nearby smoking locus are neighbours, not the lead. The curator's default.
9. **A red flag is calibrated from the discovery's own effect, as D21 says,** here Pilling's 0.0303 (flag under both
   factors at Deelen's 90th), not Timmers' pooled β. Every row whose discovery is Pilling's is swept under it (6 at
   A first), each tier move reported and read adversarially by the lead. The curator's default.

## D28 — batch six: whose effect a red flag scales, a cell against the allele, sweeps (2026-11-12)

From the curator's rows 48 to 59 and the Pilling and A-row sweeps; the lead settled them under the person's standing
word.

1. **A discovery effect that needs a conversion no source prints sets no flag (D26.3).** 42's genome-wide result is
   Pilling's age at death in years; carrying it to Timmers' scale through Pilling's Table 1 SD is the curator's own
   conversion, not a calibration either source gives, so the red flag it raises is unknown and 42 stays B on the
   attained-age column. The curator's (a).
2. **A sex-specific discovery is tested in a sex-combined sample on the discovery paper's both-parents effect**, which
   is that paper's own estimate of the effect averaged over the sexes; a same-sex sample (LifeGen fathers) is tested
   on the sex's own effect. 37 and 56 carry no flag (the curator's defaults); 56's second question falls away.
3. **A cell is `−` when the study it reads gives p < 0.05 one-sided against the longer-life allele and none gives
   `+`** (D26.2's mirror). 56's healthspan (Zenin, against G, one-sided about 0.025) is `−`, and 55's exceptional
   survival (Deelen's UK Biobank parental 90th, against, P 0.021) is `−`. The curator's 0 rejected at both: a cell
   reading one-sided in one direction reads it in the other.
4. **The uncalibrated Deelen nulls are swept where a flag could move a tier**: B rows whose every independent look
   is flat or against (a flag there makes D under D25.1). A row with an independent pass cannot move and is done
   when next opened. The curator's "sweep the A rows" is done (21 holds, 80 moved).
5. **A credible set built on a signal the row does not read as genome-wide sets no causal or effector level**
   (D25.5's reason): 54 is C4/E4, gene empty, WRN in prose (L2G 0.591, computed on that set). The curator's (a)
   rejected.
6. **58 stays B with `replication_failed`.** NECS's twofold control deficit across four haplotype SNPs is R-TIER-2's
   confounding, not 41's disowned genotypes; R-TIER-2 is lifted by Deelen's 99th (one-sided 0.043), a pass in a
   sample independent of NECS. Its 90th being flat does not cancel it: the 99th's cases are the more extreme, which
   is where a centenarian discovery's effect should show. The curator's defaults.
7. **A disease-informed Bayesian scan's call is genome-wide for B, never for A: 59 ABO is B.** Timmers 2019 calls a
   locus genome-wide by its iGWAS Bayes-factor permutation P below 2.5e-8 (q42), with priors drawn from lipid and
   coronary disease GWAS. D17.3 reads "genome-wide" by the paper's own call, so ABO's 1.9e-8 is a genome-wide locus,
   §4.1's B. It is not A's "p < 5e-8 for a longevity ... phenotype": part of its evidence is the disease GWAS behind
   the prior. Rows 6, 11 and 51, which did not count the Bayesian P, are B or A on other grounds and do not move.
   The curator's C rejected: no decision excluded the paper's own call, and this is the first row it decides.
   Foote at the lead is unknown, not untested: factor 3's file is complete for the window, the general factor's and
   factors 2 and 4's are header-only there. D27.3's list (ABO, IGF2R, POM121C, GBX2/ASB18, HP) is checked row by row.
8. **The batch's other moves hold on adversarial reading**: 49 D (on D22.3, Liu being East Asian; D27.1's "D21,
   D25.1" is corrected to D22.3, and the row names Liu's own LD explanation), 54 C (Wright's genomic-control P, as
   D26.1), 55 D (Deelen's UK Biobank validation lies outside its meta-analyses, so it is independent, as 26).
9. **6 CELSR2 and 80 CHRNA3/5 leave A, each with `replication_failed`; both held on adversarial reading.**
   - 6: Timmers' LifeGen-without-UK-Biobank arm is independent of Pilling's UK Biobank discovery (D25.9 does not
     apply) and flat (power 0.92, heterogeneity P 0.0075). The row's "same scale" is wrong as written: Timmers'
     0.0296 is Pilling's effect carried over by APOE's factor. Taking LifeGen out of Timmers' own pooled β (Figure 4,
     0.0218) leaves UK Biobank at 0.0285 on Timmers' scale, and the flag holds there (power 0.91, P 0.010); the row
     says that instead. The flag needs at least 0.81 of the discovery's effect. AncestryDNA's independent arms run
     at 0.63 (fathers) and 1.15 (mothers) of UK Biobank's, and the row states that floor and those ratios, as 80
     states its own. No winner's-curse correction is applied: D21 calibrates from the discovery's effect, and a
     shrinkage method would be a new rule with no source behind it.
   - 80: Deelen's 90th percentile tests cumulative survival against early deaths, a phenotype that carries smoking
     liability (Deelen's genetic correlation with cigarettes per day −0.49). The mean factor 0.4175 already pools
     midlife loci, CHRNA3/5 among them, and leaving it out makes the flag stronger; the 18 loci show no spread in
     the factor (Q 9.0 on 17 df). So the flag is no calibration artefact, and §4.1's "no red-flag heterogeneity"
     bars A whether the cause is fading with age or not. The curator's B; A on Figure 5's 80 to 90 hazard band,
     the reading most favourable to A, rejected.
   Both loci are on the field-consensus list the person asked about (desk #266): the field's consensus and this
   curation's evidence part there, as that question said they would.
10. **On a tier D row, the contradicted discovery gives no `+`.** D28.3's "none gives `+`" counts the studies the
   row stands on, and a D row stands on none: 55's exceptional survival is `−` on Deelen's UK Biobank validation,
   and 49's is `−` on Deelen's 99th (one-sided 0.017 against), Liu's own `+` not counted. The curator's default at
   49 (0) rejected.
11. **A nominal look against with its power unknown sets no flag:** 4 and 20 stay B. Heterogeneity holds at any
   positive factor there, but power needs a factor no source prints (D28.1), and a flag is power and heterogeneity
   both (D21). The curator's default. *Amended the same day:* the premise was a misread (Deelen's entries at 4 and 20 are
   written for the risk allele, so Deelen favours the longer-life C), and an allele-aware rescan finds no row where the
   rule applies today; it stands for the next one.
12. **Sets built on an overfit source set no causal or effector level** (D28.5's reason): 48 IL6 and 44 go to C4/E4,
   gene empty, the candidate (IL6, PLN) in prose. D26.7's "PLN at E2 stands by §4.2's letter" is superseded: its L2G
   rests on the excluded deposit line. The curator's default (unchanged) rejected.
13. **A hit its own authors call anomalous is an overfit source: 60 LINC02907 is D.** Pilling 2016 says its top 1 %
   hit at rs75824829 (P 4.0e-8) "may be anomalous": a lone SNP with no peak of correlated neighbours, the shape a
   genotyping artefact leaves. As at 41 (authors doubting their controls), 44 (below the paper's own filter) and 48
   (its group's QC), the source's own judgment of its call decides (D17.3's spirit), and nothing independent stands
   for it: Deelen has no line at the lead or its proxy, FinnGen death leans against, LifeGen's own cohorts lean
   against. Genotypes neutral, exceptional survival 0 (D28.10), no causal or effector level (D28.12). The curator's
   (a), B as 47, rejected: 47's authors call it suggestive, not anomalous, and Deelen replicates it.

## D29 — batch seven: a healthspan anchor's red flag, a database line as a replication (2026-11-12)

From the curator's rows 60 onward; the lead settled them under the person's standing word.

1. **63 TCF7L2 is B: a curator-read database line replicates nothing, and a healthspan discovery's red flag is
   scaled from its own effect.** Zenin's healthspan hit (T, P 4.2e-30) has one look outside UK Biobank, FinnGen
   R11's death endpoint (T one-sided 0.017), read by the curator from the release. D12 lets a study rest on an
   article, never on a database release: its quotes stay unknown until a fetcher caches the record, so a tier
   resting on it would rest on a value nothing checks. A release line may weigh against a row (D25.12's FinnGen
   nulls, which only ever withhold A) but never lifts one. And D27.9 scales a red flag from the discovery's own
   effect, here Zenin's healthspan hazard, which no source converts to Deelen's or LifeGen's scale; so the flag is
   unknown (D28.1), A's last criterion with it, and the row is B (D25.12). D16's co-occurring lifespan study is
   Zenin's parents' death (one-sided 0.048). The cost is stated: while no source prints a healthspan-to-lifespan
   factor, a healthspan-anchored row reaches A only through a printed scoring-class replication with no flag on a
   one-scale test. 35's B (D25.11) agrees. The curator's default (b); (a), calibrating from the co-occurring
   lifespan study's effect and letting the release line replicate, rejected on D27.9 and D12.
2. **64 BET1L: where a paper's footnote names one allele and its own text, supplement and figure the other, the
   three agreeing win.** Table 1's footnote gives HR 0.92 per C, but the main text's APOE hazard ratios are the
   reciprocals of Supplementary Data 2's printed-allele lines (per reference allele), the proxy rs2280543's minor
   T (C's partner, r² 0.98) is the shorter-lived throughout the text, and Supplementary Fig. 3's genotype effects
   at the proxy (C/T +0.05, T/T +0.21 log HR) settle it: T, the common allele, is the longer-lived, against the
   seed. The row says the footnote's contradiction and how it was resolved, as the format 0.8 reference does for
   Timmers 2019's two effect alleles. The curator's default; direction unknown with every genotype neutral,
   rejected: the paper's own figure is a direct reading, and a footnote outvoted three times is not an unknown.
3. **Where a study tests the lead, a proxy line in the same study does not stand in for it.** 62's lead has its own
   LifeGen line, flat; rs74904474 (r² about 0.5 in TSI, outside the paper's r² ≥ 0.6 list, imputation info 0.86,
   its frequency varying twentyfold across cohorts) reads G's way at one-sided 0.003. A proxy carries the lead's
   signal only diluted by its r², so a proxy stronger than the lead in the same sample measures something else, or
   noise; it is named in prose, never counted toward D25.1's independent p < 0.05. A proxy stands in only where the
   study has no line at the lead (D13). 62 stays D. A line read from a deposit and not yet quoted is named, never
   used (D12's spirit), until a note quotes it.
4. **An overfit source's discovery leaves exceptional survival `untested` when it is the only test at the lead**
   (D26.7's 44, D28.12): the overfit line tests nothing. 60's cell becomes `untested`; a proxy line inside the
   discovery's own pooled sample (LifeGen's rs113450114, which holds Pilling's UK Biobank people) is named, not
   counted (D26.10).
5. **A printed P is read as printed, with no correction of the curator's own** (D17.3, D28.1). 63's co-occurring
   study, Zenin's parents' death at P 0.0952 two-sided (one-sided 0.048), stands, though a genomic-control
   correction Zenin does not apply would push it past 0.05 and the rounded β and SE give 0.046; the row says both
   and that B over C rests on this one cell. A centenarian look-up whose paper prints only allele frequencies
   (Garagnani 2013 at rs7903146, r² 1.0) enters as a study with the crude odds ratio derived from them, saying so
   (D25.13's 31): it sets the exceptional-survival cell, while its overlap with Deelen's Italian arm is unknown and
   it lifts no tier.
6. **A heterogeneity P counts both estimates' errors.** D21's test compares two estimates, each with its own
   error; 63's figures, which left the discovery's out, are recomputed. No flag moves.
   (Items 3 to 6 were settled and handed to the curator on 2026-11-12 in 1fc91f6, whose DECISIONS.md text a failed
   pull dropped; restored here verbatim from the handout.)
7. **Consistent nominal support does not make a tier B anchor.** 65 HSD17B12's lead is Wright 2019's current-age
   hit, genome-wide only before genomic control (raw 3.6e-9, corrected 4.8e-7, read corrected by D26.1); FinnGen
   death, Park, Zenin's healthspan, Timmers and Deelen each lean A's way at one-sided p < 0.05, across three sample
   families. §4.1's B starts from a genome-wide result and R-TIER-4 holds it; pooling the look-ups into a genome-wide
   P of our own would be a meta-analysis no source prints (D28.1's spirit), so it is not done. 65 is C, with the
   look-ups in prose and in its studies; if a published meta-analysis reaches 5e-8 at the locus, it is B on that.
   The curator's default.
8. **A row whose rsID names several loci authors the one it means.** 47 AP5Z1's rs371933919 resolves to three Ensembl
   loci at 7:4,787,883 (T>TC,TCC; TC>T; TCCC>T); 0.8 expands an rsID-only row onto every locus that could host its
   genotype and strict refuses a locus it cannot host, by design (the compiler's resolution code, read by the liaison).
   An authored chrom, start and ref beside the rsID take 0.8's verify path instead. The variant's optional `locus`
   (chrom, start, ref, with cites) states it, and the export writes it on the variant's rows and its studies. The
   coordinate restates the row's own choice (D26.9, from its Ensembl and paper quotes), which the compiler then
   checks is one of the rsID's loci: it is not filled from the enricher's resolution.csv. Only rows whose rsID names
   several loci carry it; every other locus stays the enricher's to resolve.
9. **A quoted trade-off keeps a skin_sun row descriptive.** 66 TYR's longer-life G raises vitiligo (OR 1.50, P 1e-43)
   and, through MTAG, glaucoma: a disease, so a trade-off by D18.1, and D18.2 makes a trade-off descriptive. D25.11's
   "skin_sun rows are modifiable" was written for rows with no trade-off (17, 35) and does not override §4.2's rule;
   the sun advice leaves 66's genotype texts. The curator's default (a).
10. **A coding lead's effector call is not vetoed by another gene's QTL.** §4.2's E1 coding clause names the gene
   whose protein the lead changes (66: TYR R402Q, L2G 0.83). D24's rival rule weighs calls that rest on expression
   (L2G, colocalisation); one NOX4 artery tuQTL colocalisation says the haplotype also moves an RNA elsewhere, not
   that TYR's protein change is not the effector. 66 is E1 TYR, NOX4's colocalisation named in prose. The curator's
   default (a); (b), D24 over coding leads, rejected.
11. **A multivariate or healthspan discovery's red flag stays unknown even where two lifespan arms can be compared on
   one scale.** 70 FGD6's discovery is Timmers 2020's multivariate test (P 8e-9); Wright's AncestryDNA fathers at
   rs11107904 (r² 0.88) are flat (P 0.60) against Wright's UK Biobank fathers (P 3e-5), heterogeneity P 0.035 and
   power 0.975 on the UK arm's β. D21 scales from the discovery's own effect (D27.9), and D29.1 kept 63's flag unknown
   rather than scale from a lifespan arm that is not the discovery; the same holds here, conversion or not. The row
   names the comparison with both numbers, and that the flag would need 0.87 of the UK arm's β, and carries no
   `replication_failed`. Tier B either way. The curator's default (a) rejected for consistency with D29.1; if the
   person wants co-occurring lifespan arms tested against each other, it is one rule for 63, 70 and their kind.
12. **70 is heart_vessels**: the lifespan set colocalises with coronary disease (H4 0.95), G lowers CAD, MI and angina,
   and Timmers reads it as less cardiovascular disease, as at 51. A platelet colocalisation as strong (H4 0.97) names
   a trait on the same road, not a rival route. The curator's default.
13. **Animal evidence is a flag, not a study** (`animal:mouse_qtl`, `animal:worm_rnai`, cited). §4.5's classes are
   human outcomes; a model-organism study class would be a design change, not taken here. The curator's default.
14. **A genotype-model claim is tiered, read and tested on its own model** (73 KL-VS, the curator's four defaults).
   Arking's heterozygote advantage is replicated only in small or same-group samples (Invidia independent but small;
   three meta-analyses significant in abstracts without a model), so C by §4.1. The large per-allele looks (LifeGen,
   Deelen, FinnGen, Park, Zenin) test an additive model the claim does not make; under Arking's own model an additive
   test expects about +0.154 (SE 0.097, heterogeneity P 0.19), unpowered, so no flag and no D. Genotypes stay neutral
   (R-LEGACY-1: a v1 row below A/B), the heterozygote claim said in the conclusions. Mechanism `legacy_candidate`: a
   v1 candidate nothing large carries. The outcome cells read the genotype claim's own tests (healthspan untested,
   lifespan 0 on Arking 2005 against de Vries 2017, exceptional survival + on Arking 2002, Invidia, Revelas), and the
   per-allele lines are named, not read into cells. Rejected: D on de Vries alone (one study, not a powered test of
   the model), and the per-allele cells (they would score a model no one claimed).
15. **74 is B with `replication_failed`.** AncestryDNA's mothers fail the UK arm on one scale (heterogeneity P 7.4e-5,
   power about 1.00), a D21 flag; but LifeGen's sample b (one-sided 0.046) and Deelen's 99th (0.020) each give
   p < 0.05 in the discovery's direction outside its UK Biobank mothers, which is D25.1's exception. Their sharing
   Rotterdam with each other does not matter: each is independent of the discovery. The curator's default (a).
16. **`sex_specific` rests on a test of the difference, not on one sex significant and the other not.** 74's mothers
   (P 2.9e-8) against fathers (P 0.67) is a contrast of significance; Timmers' moderator misses its own legend's
   FDR (Q 0.13), where 37's held (Q 0.0017). The curator computes mothers against fathers from Pilling's β and SE
   (both errors, D29.6): heterogeneity P < 0.05 keeps `sex_specific:f`; otherwise it is dropped and the contrast
   said in prose. The curator's default (a) rejected as stated.
17. **A row is tiered on its lead's own evidence; an overfit line at the locus sets nothing** (D28.12 carried to the
   tier). 75's seed lead rs35257605, a common poly-T repeat, is a suggestive line in Park's deposit (P 4.9e-6), not
   reported, unreplicated and uncontradicted (the looks are flat or co-occur); the genome-wide line is the seed's
   second rsID rs116257533, an allele about 21 times below Park's own frequency filter (D26.7, 44's kind). So 75 is
   C on the repeat, rs116257533 named in prose as an overfit line that sets nothing, genotypes neutral, lifespan from
   Park's suggestive line. The curator's default (a), D for the locus, rejected: the lead never made the overfit
   claim, and D would put the overfit line's verdict on a variant it does not describe.
18. **A replication read from a table filtered on a meta-analysis that holds it is selected, and counts only when the
   other arm alone would pass the filter.** Wright 2019's Supplemental Table 9 prints only representative SNPs whose
   AncestryDNA–UK Biobank meta P is below 2.5e-3 (pmid-31484785#q6). Where the UK arm alone does not reach 2.5e-3,
   a line appears only because the AncestryDNA arm pushed the meta under the cut, so its nominal pass was close to
   guaranteed by the table's own filter and is not an independent replication (§4.1, D25.1): it is named, with the
   filter, and not counted. Where the UK arm alone reaches 2.5e-3, inclusion does not hang on the AncestryDNA arm,
   and its line counts as before. Supplemental Table 8 filters on the AncestryDNA arm's own P (below 3e-3), so a line
   there passes on its own; only its absence is uninformative (68). Found by the lead's adversarial read of 69 (UK arm
   P 0.0056, so 69's AncestryDNA fathers no longer count; 69 stays B, D18.3's cap). The curator sweeps every row
   that counts a Table 9 AncestryDNA line, reports each tier or token that moves, and the lead reads the moves.
19. **A genotype-model claim is tested whole, as the row states it** (D29.14 corrected). 73's model, heterozygote
   advantage with homozygote harm, does draw a powered additive test (power about 1.00); it raises no flag because
   its two terms nearly cancel (+0.307 and −0.152), leaving a large error, not because the test is weak. Arking
   2002's homozygote-only sub-claim alone fails Deelen's 90th with power (heterogeneity P 0.002; 99th 0.006); the row
   names that, but the row's claim is the combined model, which is not contradicted. 73 stays C. Exceptional survival
   reads Arking 2002 only (Revelas has no direction, Invidia is null); `PROTECT:BUFFERING` is set if a quote ties KL-VS
   heterozygosity to lower risk in APOE ε4 carriers (§4.2's own example), else the row says why not.
20. **74 keeps `sex_specific:f`**: Pilling's mothers (T β 0.0251, SE 0.00451) against fathers (+0.00206, SE 0.00449)
   differ at P 2.9e-4, both errors counted (D29.16), from the deposits the curator caches and quotes.

## D30 — batch nine: how far D17.1 reaches, a sub-suggestive locus, the Table 9 test corrected (2026-11-13)

From the lead's adversarial read of rows 76 to 87 and the curator's questions on them, settled under the person's
standing word (pacing off, "full steam ahead"; the advisor pattern for the requirements' silent cells).

1. **D29.18's test is corrected: a Wright Table 9 AncestryDNA line counts only if the table would hold the line
   with the AncestryDNA arm at z = 0.** "The UK arm alone under 2.5e-3" was the wrong test: a meta-analysis with a
   null arm is weaker than the UK arm alone, so a UK arm at 0.0019 (78's rs11855102) still needed the AncestryDNA arm
   to enter the table. The curator computes, per line, the inverse-variance meta from the two printed arms with the
   AncestryDNA z set to 0, deflated by the factor that turns the printed arms into the printed meta P (about 1.17 to
   1.24 at 76, 78 and 79), and counts the line only if that P is below 2.5e-3; at these errors the UK arm needs
   roughly P 1e-4 or less. The row states the number. 76 and 79 pass (0.0013, 1.5e-4); 78's three lines do not. The
   D29.18 sweep is run again under this test, and the moves reported in one message. Rejected: reading a line
   "conditional on inclusion" as a P of its own (no rule sets it, and 76 and 79 count either way).
2. **D17.1 reaches any nearby lifespan signal, a row's lead or not, but only the co-occurring study, never the
   anchor.** A healthspan or multivariate row's co-occurring lifespan study (D16) is the locus's own signal when it
   survives conditioning on the stronger lifespan lines in the window, jointly where there are several, with the LD
   cached and quoted. 87 DHX58: Timmers' lead line passes against each of the two stronger peaks alone (one-sided
   about 0.008 and 0.005) and fails against both together (about 0.11), in a reviewer's approximation from uncached
   LD. The curator caches the LD, computes the joint conditional, reads Park at the two peaks and conditions it the
   same way: if either study stays below one-sided 0.05, 87 is B; if neither, C (D16). B stands until then. The
   anchor is read at the paper's own P (D17.3): 82's MANOVA stays genome-wide although a reviewer's approximate
   conditional on rs4784227 (traits taken as independent) drops it to about 0.002; the row names that. Rejected:
   conditioning the anchor, which would re-correct a paper's call by an approximation of ours; and stopping D17.1 at
   another row's lead, which would score one lifespan signal for two loci whenever the other has no row yet.
3. **103 is re-read at its next touch under D25.1.** Its healthspan replication is a D21 red flag on D21's own
   definition (one-sided power about 0.99, heterogeneity P 0.024; its "about 0.8" was Zenin's power at 0.05/12).
   The curator computes Timmers' line at 103 conditioned on row 38's lead, with phase and both errors (D17.1 gave
   only z about 0.6 to 1.7). One-sided 0.05 or above: no independent pass, so D (D25.1, D25.2, D28.10). Below:
   the row has a lifespan signal of its own, B with `replication_failed` (D16, D17.1's cap). 86 DEF8 is D under
   D25.1 (the curator's (a)); its prose's comparison with 103 is corrected to the same definition. Rejected: (b),
   reading a failed same-scale replication as a cap, which would make "explicitly contradicted" unreachable for
   any healthspan discovery.
4. **A seed locus with nothing genome-wide or suggestive, whose own lifespan lines in the large samples are nominal,
   one-way and contradicted nowhere, is C.** §4.1 is silent: C's "suggestive" is not met and none of D's clauses
   is (the lead is no candidate-gene claim, nothing contradicts it, no meta-analysis is null). C keeps it in the
   research view with no weight, as row 8 IL6R and 84 CETP stand. Rejected: D, which would show consistent nominal
   support as negative evidence.
5. **77 APBA2 stays C (R-TIER-2); LGP's null is named, not counted as a powered test.** LGP is Table 2 with 312
   cases and 638 controls (not the abstract's 480 and about 800). Its printed P (0.4) would give a D21 flag, but its
   controls carry G at about 2 %, some 25 times gnomAD's Ashkenazi frequency (0.08 %), so its calls at this rare
   variant are not shown reliable and its power is unknown (D26.3). That LGP and NECS share one imputation pipeline
   bears on the discovery (R-TIER-2's batch confounding, already the cap), not on whether LGP contradicts it. No
   change to 19, 31, 41 or 58. States: protective for G carriers, as 19 (the curator's (a)). Rejected: D under D25.1
   (the reviewer's), on a test whose own control frequency is out by a factor of 25; D as overfit (the curator's
   (b)), since gnomAD (0.27 %) agrees with NECS's controls (0.45 %) and 1000 Genomes and ALFA are the outliers.
6. **`PROTECT:ABSENCE_OF_RISK`'s disease (D26.5) is a genome-wide disease association at the locus, or a disease
   credible set colocalising with the row's own.** A sub-genome-wide line is named. 79 and 87 (coronary disease
   P 3e-7) drop the token, as 28.
7. **A v1 rsID the seed list holds only as a non-lead gets a legacy row of its own** (R-LEGACY-1), curated in the
   legacy pass: 84's rs5882 (CETP I405V, Barzilai 2003), 57's rs1063192 and the seed's other v1 non-leads (at 43 and
   96). The row format can hold two variants but not two tiers. rs5882's tier tests Barzilai's VV model as stated
   (D29.19), not the per-allele looks. 84 names it in its reason meanwhile. Both of the curator's options rejected:
   (a) left it unreachable, since the legacy pass skipped rsIDs the seed list holds; (b)'s premise, that a row
   cannot carry two variants, is false.
8. **The rest, the curator's defaults:** 76 B with `replication_failed`; 78 B (no proxy anchors A at the lead,
   D29.3, D29.17); 79 A with `sex_specific:m` (D19.2 and D17.3 refuse a correction across Pilling's five scans; the
   first A row with a sex token, which never folds into the tier); 82's lead rs4783780 and its mechanism metabolism,
   modifiable through weight (rs4784227 has no lifespan signal of its own once the lead is accounted for; it goes to
   the scout's queue as a healthspan candidate, D25.6); 83 B (a Genomic SEM factor is multivariate whatever its
   traits, D27.3) with `tradeoff`, descriptive (the lead leads luminal-A breast cancer, P 2.1e-15); 84's He 2016
   set named, not counted (no β, the HDL signal); 87 E1 DHX58 (D24, D29.10). 78's and 87's red flags read unknown
   (D29.11).
9. **A locus "acts through weight" (D18.2) when its lifespan signal is shown to share the weight signal**: a
   colocalisation with body-composition sets (82, 18 sets at H4), or a mediation. An allele that merely goes with
   lower BMI in sets it does not lead is named and stays `general_ageing`, descriptive. 88 B4GALNT2P1 (C lowers BMI in
   17 sets, leads none, no mediation): the curator's (a). Rejected: (b), metabolism through weight on direction
   alone, which would label most lifespan loci by the BMI they correlate with.
10. **D30.5 generalised: a replication sample whose controls misfit their population's reference frequency at the
   variant (P < 0.01, either direction) has calls not shown reliable there; its power is unknown (D26.3).** It is
   named with the misfit, never counted, and the rule cuts both ways: such a sample's pass does not count either.
   92 FBXO15: LGP's controls carry G at 0.006 against gnomAD's Ashkenazi 0.0166 (about 8 copies where 21 are
   expected, P about 0.001), so its null (P 0.9) is not a D21 flag and 92 stays C (R-TIER-2), the curator's (a).
   Rejected: (b), D on a test whose own controls misfit at that level; and a fold-change cut, which says nothing
   about the counts it rests on.
11. **A suggestive discovery that fails a powered test is D, as a genome-wide one is (D25.1, a fortiori), and a pass
   inside the failing sample is no independent pass.** 94 CEP89: Deelen's suggestive discovery (P 1.7e-7 European)
   fails Timmers under both calibrations (heterogeneity P 0.006 and 2e-5). Pilling's UK Biobank parents (one-sided
   0.038) sit inside Timmers, the sample that fails, so they are part of that failure, not D25.1's independent
   exception; at 74 the passing samples sat outside the flagging one. 94 is D, genotypes neutral, lifespan 0
   (D25.2, D28.10). The curator's (a), C with Pilling counted, rejected.
12. **An own-death endpoint is compared on the per-self scale; a database release line neither makes D nor makes A.**
   A parental-lifespan β per offspring allele is half the effect in the carrier, so FinnGen's death endpoint (the
   carrier's own) is compared with the per-self effect (Timmers' Figure 2 scale, twice the per-parent β), under
   both calibrations where a conversion is involved (D25.3). A FinnGen release line is a curator-read database line:
   it never replicates (D12, D29.1), and by D27.1's mirror it contradicts no more than it replicates, so its flag is
   stated and bars A (§4.1's last criterion) but sets no D. 95 (Pilling's fathers, P 8.2e-9): FinnGen on the per-self
   scale flags (power 0.82, heterogeneity P 0.0028), stated; 95 stays B with `sex_specific:m` (option (c)). 45's and
   94's FinnGen tests are re-read on the per-self scale at their next touch, for the statement only. Rejected: (a),
   the per-parent scale, which halves the expected effect in the carrier; (b), D on a database line.
13. **95's mechanism: general_ageing, descriptive, `mech:smoking`, `mech:lipids` (as 29), the curator's (a).** The
   longer-lived A raises cotinine and years smoked (P 1e-12): smoking runs against the lifespan effect, so the locus
   does not act through it, and `smoking_lungs` with `act_behaviour:smoking` (b) would label it by a behaviour that
   goes the wrong way. A raised smoking measure is an established risk factor, so `tradeoff` is set (D18.1) where
   the quote ties A to it; the label stays descriptive.
14. **Withdrawn (2026-11-14, same day): APOE is not settled here.** An earlier text of this item made 96 one row with
   two scored variants. That contradicts the requirements: R-APOE-1 scores APOE once, as an ε diplotype from
   rs429358 and rs7412, with every proxy `ld_proxy_of`, and APOE's ownership is the person's open decision D2
   (§8; recommended there: a diplotype inside v2, `also_in:apoe_epsilon`, after R-APOE-3's render check). 96 stays
   last in rows/PROGRESS.md, waiting on D2, as the curator pointed out.
15. **A tier D row carries no `sex_specific` token; the contrast is named in prose.** A context token describes an
   effect the row supports, and a D row supports none (D25.2): `sex_specific:m` on 97 C20orf187 would be read as a
   property of a real effect. Its conclusions say the discovery was reported in fathers only (P 1.2e-10, mothers
   0.78) and not supported. 97's top-10 % look, the discovery's own parents, gives no `+` (D28.10), as the curator
   has it. Rejected: keeping the token as the discovery's own description, which the prose already carries.
16. **D30.12, D30.13 and D30.15 corrected by the batch-ten read.**
   - **D30.12's facts were wrong; its rule stands.** Timmers' summary-statistics `beta1` is already per self ("the
     log hazard protection per a1 in self", the parental estimate doubled; pmid-30642433 note), so an expectation
     calibrated through it (the APOE and mean factors) is already on the per-self scale and is not doubled again.
     94's restatement doubled it: its FinnGen test goes back to APOE-factor power 0.77, no flag. 45's needs no
     re-read. 95's expectation used the fathers' conversion (2.287) on Pilling's both-parents β, where Timmers' sheet
     converts both-parents results at about 1.97: expected +0.0166, power 0.71, no flag; 95 stays B, nothing
     stated as a flag. The rule (an own-death endpoint compares per self; a database line sets no D) is unchanged.
   - **D30.13's `tradeoff` is dropped** (D26.4, as 40): A raises cotinine and years smoked, but every signed
     lung-disease set at the locus runs with G, and A lowers respiratory failure and chronic bronchitis, so no quote
     ties A to a harm. 95 stays general_ageing, descriptive, `mech:smoking`, `mech:lipids`.
   - **D30.15 covers every context token that describes the effect**: `sex_specific`, `ancestry_specific`,
     `age_dependent`. Evidence-scope tokens (`eur_only_evidence`) and flags (`replication_failed`) stay. D rows 48,
     49 and 72 drop `ancestry_specific:eas` at their next touch and name it in prose. 94's D30.11 reason narrows:
     Pilling's parents are the same parents the pooled Timmers estimate holds, and that estimate does not pass.
17. **On a tier D row no outcome cell is `+` from a study that shares the discovery's sample** (D28.10 read whole:
   a D row stands on no study). An independent pass would have kept the row off D (D25.1); a pass inside the
   discovery's biobank is the discovery's echo, not support. A study against still gives `−`, as 86's Park. 98
   NOL4L (row 86's shape): Atkins' UK Biobank frailty, Pilling's fathers, Timmers and Park all share UK Biobank, so
   healthspan and lifespan are 0, the curator's (b). Rejected: (a), `+` cells on a row whose discovery is
   contradicted, which would show it as supported in the outcome strip.
18. **Batch ten's read, rows 88 to 91: how D30.2 conditions, what D30.9 shares, D30.10's reference.**
   - **D30.2's joint conditional is built stepwise**: from the window's lifespan lines stronger than the lead, add
     the strongest, condition, and repeat while a remaining line stays stronger than the lead conditionally
     (COJO's logic), then condition the lead on the selected set. The row reports the range across other readings
     it tried. 91 MC4R: stepwise 0.054 (CEU) and 0.131 (all Europeans), range 0.02 to 0.16: not shown, C stands
     (D16). Rejected: conditioning on every stronger line at once, which over-conditions on one correlated cluster
     (8 of 91's 13 lines, |r| to 0.92), and on the distant lines alone (0.008), which ignores the cluster.
   - **D30.9's shared signal is the row's lifespan signal; a multivariate anchor's colocalisation does not stand in
     for it.** 91's BMI colocalisation belongs to Foote's disability factor, which holds no lifespan component, and
     the row shows no lifespan signal of its own: general_ageing, descriptive, `mech:adiposity`, `broad`; its texts
     say the lifespan link is not shown. 82 differs: its multivariate set pools lifespan.
   - **D30.10's reference is the gnomAD population that matches the sample** (Ashkenazi for LGP, non-Finnish European
     for a French or Danish sample, Finnish for a Finnish one). 89 FN3KRP: the French controls misfit NFE (P 2e-4),
     so they are named and not counted; D (D26.8) rests on the Danish sample alone (controls fit, P 0.015; power
     0.92, heterogeneity P 0.009).
