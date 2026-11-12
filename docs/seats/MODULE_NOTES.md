# Module — notes

The module seat's working state, rewritten to the present before a reset (`docs/seats/MODULE.md`).

## Now (2026-11-10)

First seated 2026-11-10. The seat-builder's first-seating handout is worked; its first work stands as below.

**Awake (the lead, 2026-11-12, 639780560, on the person's "just spend all you can, 95% cap for next week").**
Reload, validate under 0.8, the Ensembl cache; rehearsals on the polygon only, nothing to prod; no rows until RM1's
export (the lead starts it today, to 0.8's studies/variants shape per `docs/FORMAT08_REFERENCE.md`).

- 2026-11-12, after the reload: plugin server v0.48.7, client format 0.8.4; polygon registry 0.30.0, format 0.8.4,
  contract compatible. `validate_module` strict on the scaffold: invalid, the one error "studies.csv is present but
  has no study rows. Grounding evidence is mandatory." (as under 0.7.1), one warning `module_not_closed`.
- **Read against 0.8.4's `studies.csv` (`describe_table`) and `docs/format08_reference/`, 2026-11-12.** Settled:
  proxy (`proxy_rsid`, the proxy's own `effect_allele`, the phase derived by the author), stratum (`stratum`,
  `stratum_level`: 61's women, 13's men), a Martingale effect (`beta` with `effect_unit` saying Martingale
  residual, the example's rs429358 row), a Bayes-factor P (`statistical_test` says which P, the example's
  rs646776 row: 59), `tradeoff` computed in `meta.csv` from per-trait rows, tier in `meta.csv`. Open, sent to
  the lead for RM1: `stat_significance` is closed (significant, suggestive, not_significant, unknown), no
  `nominal`; studies.csv has no `direction` column, so a study with allele, direction and P but no effect size
  (D13, D15, D20) carries its direction nowhere but `conclusion`; no field marks an effect as derived (31, 58),
  only `effect_unit`'s text; `effect_measure` is open, so a Z (19, 58) may be written `Z` with a warning, or left
  empty. The key is still (variant_key, pmid), equality; the reference says `phenotype_class` narrows its warning.
  The lead's mapping (639782292): nominal writes `not_significant`, the P exact, "nominal replication look-up
  (p < 0.05)" in `statistical_test`; direction into the study's `conclusion`; a derived effect says so in
  `effect_unit`; Z stays `Z`, its warning reported. (1) and (2) went upstream as format wishes, S147 and S148 with the compiler's triage (the liaison, 639785042). The
  export lands on a branch first; the lead hands its output here to validate.
- **RM1's export in, 2026-11-12 (b0b6089):** `loci export` at 4e49fd0's tree, enriched online (112 resolution
  rows, all resolved, no mismatch). Strict validate: 11 errors, nine Zenin 2019 P pairs (the curator's), 93 LDLR's
  proxy allele A at rs6511720 (G/T; the reverse strand's, the curator's), 47 AP5Z1's T/TC refused at rs371933919's
  third locus TCCC>T: by design (the liaison, 639792035), a row names its locus by authoring chrom, start, ref (7:4787883, T), the export's to write. Best-effort compile green, warnings the same. Not
  rehearsed; polygon only, once strict passes.
- **Namespace, asked of the person 2026-11-12:** production holds longevitymap 1.2.1 under `just-dna-seq`; the
  polygon account owns none, both `just-dna-seq` and `test-longevity-loci` free there. Default on silence:
  claim `test-longevity-loci` on the polygon once strict passes, rehearse there.
- Plugin caches moved to the data volume (`remember_setting JUST_DNA_PIPELINES_CACHE_DIR`, user config, not the
  repo): `$HOME` is the small volume and Ensembl's lane is about 15 GB. Ensembl lane present 2026-11-12: ensembl-variation-2026_07_13-vep116.0, 14.5 GB (du shows 7.6 GB on BeeGFS).

- **Version in progress: 2.0.0**, scaffolded in `module/` with the plugin (v0.48.5, format 0.7.1, compiler 0.7.2):
  `module_spec.yaml`, header-only `variants.csv`, `studies.csv`, `licensing.csv`. No rows, no loci yet.
- **Strict validation refuses the empty scaffold**, verbatim: "studies.csv is present but has no study rows.
  Grounding evidence is mandatory." That is the format's rule, not a defect: the module validates once the first
  curated locus lands. No stub row was added to turn it green.
- **The spec's hand-filled cells are the requirements' recommended defaults, not decisions**: D1 (`weighting:
  scale none`, order by priority), D3 (name `longevitymap`, title "Longevity genetics"), §6.2's `defaults:`. Each
  logged with `record_override` (`module/logs/authoring.log`). `license:` left out until the person names one.
- **Deferred table kinds**, added by `scaffold_module` when their turn comes: `haplotypes.csv` + `diplotypes.csv`
  (APOE, D2, after R-APOE-3's render check in just-dna-lite), `pgs.csv` (PGS000906, opened in the PGS Catalog at
  curation time). `licensing.csv` gets HAGR's row (CC BY 3.0, R-LEGACY-3) with the first increment.
- **Format version**: the scaffold's headers are 0.7.1's. RM1's export targets 0.8's columns; the module moves to
  0.8 when the plugin does (it waits on 0.8.0 on PyPI and both registry instances serving it). No 0.8 column is
  hand-added before then.

## The first curated row, read for the export (2026-11-10)

`rows/46-LPA.yaml` (060c9bd), tier A kept, one variant (rs10455872, three genotypes), seven studies. Not built into
`module/`: the module takes rows through the lead's export (RM1), never by hand. Read against 0.7.1 and sent to the
lead (639271942): studies.csv's key (variant, pmid) collides twice in LPA (probed in a scratch spec: "Duplicate
(variant, pmid): (rs10455872, 29030599)", a warning); the lead's new `nominal` has no 0.7.1 stat_significance
value; the proxy studies' alleles (T, C) belong to rs55730499 and must not land on rs10455872's row. Asked the
liaison whether 0.8 widens the study key.

## v1.2.0, the legacy layer (registry prod, read 2026-11-10)

528 rsIDs, 1022 weight rows, 671 studies, 272 genes; categories antioxidant, genome_maintenance, heat-shock,
inflammation, insulin, lipids, mitochondria, mtor, other, renin-angiotensin, sirtuin, tumor-suppressor. Compiled
strict on compiler 0.7.0, fully resolved; no `weighting:`, no licence, no README, not closed; 126 literature rows,
0 quotes authored. Coverage gaps the compiler names: 307 sites lack the reference homozygote, 186 the hom-alt, 6 a
het. R-LEGACY-1 carries the 528 as tier C/D research-view rows, `flags: legacy_longevitymap`, no weight, neutral.

## Registry

- Polygon (test): answers again by 2026-11-11 (the liaison, 639307944; ledgers 438d527): registry 0.28.5, mode
  test, serving format 0.8.0. The plugin's 0.7.1 gets 409 on every publish, validate, check and download; reads
  work. No rehearsal is possible until the plugin moves to 0.8, token or not (desk #251 updated so).
- Enrich's GWAS pass is broken in every installable enricher (compiler RM428, high): 0.7.3 gets 410 from the
  retired GWAS Catalog v1, 0.8.x sends a page size v2 refuses. An empty GWAS result from `enrich_module` is
  unknown, never "no associations".
- No test token on this machine. Asked of the person; never read from a file, never minted by this seat.
- No rehearsal yet.

## Open

- Avatar: set 2026-11-10, a beaver stacking labelled blocks, drawn by agents-kit/tooling (639270008).
- Polygon account: registered 2026-11-11 on the person's answer to desk #251 (option 2): account `longevity-loci`,
  test instance only, `registry_whoami` accepts it. Token and install-id live in the plugin's local state on this
  machine, never in the repo. No namespace claimed yet (a claim is irreversible; pick it to match the production
  namespace when a rehearsal is near). Polygon at registry 0.29.1 serving format 0.8.4, so contract_compatible is
  false for the plugin's 0.7.1. Superseded 2026-11-12: the plugin is on 0.8 (below), rehearsals work.
- `first seating:` report to the seat-builder: sent.
- On waking: read `docs/format08_reference/` (just-dna-format 0.8's longevity reference example and the compiler's longevitymap v2 shape audit; the lead, 639310707). It notes Timmers 2019 contradicting itself on effect alleles (639310710), which bears on LPA and CELSR2.
- For the projection, on waking: rows at effector E3 or E4 name no gene (`gene: ""`; E3 57, 67, 80, 53; E4 44, 48, 54,
  55, 60; requirements §4.2/§6.2),
  and a `multivariate_healthspan_lifespan` study supports with allele, direction and P but no effect size (D15,
  67's Timmers 2020), and so does a `meta_analysis` study with arm effects only (D20, 21 IP6K1 at tier A). Check
  that a tier A/B variant whose supporting studies carry no effect size still passes the format. Check both land in 0.8's variants and studies tables as the format allows. Likewise the repo's own study
  designs (`age_threshold_case_control`, D11; `current_age_quantitative`, 10 RABGAP1L) against the format's
  study_design vocabulary.
- Proxy studies now recur (10 RABGAP1L's study at rs16847402 carries the proxy's C, 756730c), so the LPA finding
  (a proxy's allele must not land on the lead's row) is general, not LPA's. Check 0.8's proxy rsid column takes
  it. Effect alleles are harmonised to the lifespan-increasing allele (D17.4).
- A study may print a Z, not a beta (19 HMGB3P12, Gurinovich 2021; the GWAS Catalog files that Z as "beta").
  Check the format's effect_measure takes a Z score, else the export leaves effect_size empty, never a beta.
  An effect size may also be derived by the curator (31 LINC02064, a crude OR from printed frequencies, D25.10,
  said in effect_unit and the test): check the format has a place to say derived, so it never reads as printed.
- The first tier D row (26 GPR78, 4970b24): a genome-wide hit contradicted by a powered null. Check how the
  requirements carry tier D into the module (research view, flags, no direction a report would read as advice).
  The lead settled the row side (D25.1, D25.2, 80b7691): D holds and every genotype of a tier D row is neutral.
- Studies now carry `p_one_sided` (D26.13): a replication printed two-sided 0.05-0.10 is `nominal` on its one-sided
  P, the printed P unchanged (2, 4, 10, 12, 14, 17, 18, 29, 36, 39, 43, 67, 93). Check whether the format holds
  stat_significance to p_value_num; if it does, those rows' studies disagree with it in the module, a projection
  question for the lead, never a value to change by hand.
- The first insertion (47 AP5Z1, rs371933919, T>TC; the seed's rs528161076 merged into it, 5a63a03): check that
  enrich resolves the current id and that the format's genotype cells take a multi-base allele.
- A second insertion, on a tier D row with `gene: ""` (55 RP1, rs35262860, G>GCT in VCF alleles, 2ffbadb):
  genotypes G/G, G/GCT, GCT/GCT, all neutral, yet the variant carries `direction: protective` and an OR. Check the
  module keeps a tier D variant's direction and effect from reading as advice when every genotype is neutral.
- A study whose P is a Bayes-factor permutation P, not an association test's (59 ABO, Timmers 2019's integrated
  scan, P 1.9e-8, `significant`, D28.7, e4ec1d0), beside the same paper's conventional 6.3e-6. Check the format has
  a place to say which P it is, so the module never shows it as a plain GWAS P. 59 is also a trade-off row
  (descriptive, D18.2): check how the module carries a trade-off's negatives.
- A sex-specific tier B row whose effect is on a Martingale residual of own survival (61 CELF2, Park 2025's
  women, rs547541271 T +0.0369, `sex_specific:f`, 2bbd85a; row 13's shape). Check the format's effect_measure and
  stratum take both, else the export leaves effect_size empty rather than call it a beta.
- **0.8 is in (the liaison's handoff, 2026-11-12, b9123d6):** plugin v0.48.7, server and lock on format, compiler
  and enricher 0.8.4. Rehearsals on the polygon work; production only once it answers on 0.8. GWAS pass fixed
  (RM428; one request a second, hours for dozens of variants). First on waking, after `/reload-plugins`:
  `validate_module` on the scaffold under 0.8 (new `meta.csv`, `model_organisms.csv`, the #6 study fields);
  `provision_caches` for the Ensembl lane (none on this machine), enrich online (indels). `tradeoff` is computed
  in `meta.csv`, never authored (bears on 59's trade-off point); `enrich_module` names `allele_mismatches`.
  Not started: the seat sleeps until the person or the lead wakes it.
- Plugin pinned at v0.48.6 (the liaison, f69789a; toolchain unchanged, format 0.7.1): `validate_module` returns
  `warnings_summary` and `carried`; the polygon's 409 is named as the instance's format skew; the GWAS fix
  (RM428) is on the compiler's main, unreleased. The new session after waking loads the new pin.
