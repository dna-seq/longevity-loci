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
- **First rehearsal, 2026-11-12:** 47's authored locus (0343039) re-exported: strict validate and strict compile
  pass (17e7770; 192 rows, 331 studies, fully resolved). `test-longevity-loci` claimed on the polygon (the lead's
  word on the default; the person not yet answered), `registry_validate` clear, published
  test-longevity-loci/longevitymap@2.0.0 (receipt `module/published.json`). The name is not test-prefixed, so the
  operator's sweep keeps it: delete it with `registry_delete_version` before the next rehearsal of 2.0.0.
  Warnings left: 6 indel VRS ids unverifiable (carried), module_not_closed, ClinVar 2026-11-01 superseded.
- **Standing (the lead, 639797615):** RM1 closed. Hold at the rehearsal: no production publish and no close
  without the person's word. Re-export and re-rehearse after each curation batch, not per row (delete the polygon's
  2.0.0 first, then publish again).
- S147 settled upstream (RM434, 5e124dfb, in just-dna-format 0.8.5): `stat_significance` is the authors' verdict at
  their own test's threshold, so the export's `significant` for a passing nominal look-up is the format's reading.
- 75 (KLF12 region, 81b55f0), tier D: its lead rs35257605 is a poly-T repeat (the 15-T allele). At the next
  re-export check how enrich resolves a multi-allelic repeat (expansion, as rs371933919's three loci did) and whether
  the row needs an authored locus (D29.8) before strict passes.
- **Batch eight rehearsed, 2026-11-12:** 75's locus authored (2d16f3d), re-export strict-valid and strict-compiled
  (72 rows, 216 variant rows, 370 studies, fully resolved). The first 2.0.0 deleted from the polygon, batch eight
  published there (published 23:20 UTC). Its content_signature equals the local compile's; the artifact digest
  differs (the registry compiles on polars 2.1.0, ours 1.44.2), as the compiler says a toolchain moves it.
  `published.json` was left on the first receipt by the tool; the second appended by hand from registry_get_module.
- **Batch nine (76 to 87), 2026-11-13:** a trial build of the rows as they stood under the lead's read (a scratch
  copy, nothing published) went green on 0.8.5: strict validate and strict compile, 82 loci, 246 variant rows, 422
  studies, fully resolved, warnings unchanged, no new locus to author. The lead read the batch (D30, 83499c8); the
  curator corrects 76 to 87 now. Next: once those corrections land, export to `module/`, enrich, strict, delete
  the polygon's 2.0.0, republish, verify, append the receipt, report to the lead.
- **Batch nine rehearsed, 2026-11-13:** after the curator's D30 corrections to 76 to 87 (trunk dfb21f9): export,
  enrich, strict compile green (249 variant rows, 427 studies, fully resolved, 242 of 242 VRS alleles identified,
  warnings unchanged). The polygon's 2.0.0 deleted and republished (17:11 UTC); its content_signature equals the
  local compile's, the digest moved by the toolchain as before. The server compiled with compiler 0.8.4, ours
  0.8.5. Receipt appended by hand again. just-dna 0.8.6 is on PyPI; the liaison moves the pin.
- **2026-11-14:** the liaison pinned plugin v0.48.10 and just-dna 0.8.6 (7e62509); this session runs v0.48.10 after
  its reload, so the batch-ten rehearsal is the first on 0.8.6. Watch for it: 96 APOE is curated last, after D2 (APOE
  as a diplotype inside v2, its proxies ld_proxy_of under it). A diplotype is a shape the export has not projected:
  when D2 lands, ask the tool how 0.8 carries a two-SNP haplotype (describe_table) before the row reaches an export.
- **Batch ten rehearsed, 2026-11-14:** rows through 99 after the lead's read and the curator's corrections (trunk
  571e5b1), the first on just-dna 0.8.6: export, enrich, strict compile green (93 loci, 279 variant rows, 465 studies,
  fully resolved, 264 of 264 VRS alleles identified, warnings unchanged). The polygon's 2.0.0 replaced (18:26 UTC),
  content_signature equal to ours; the server still compiles with compiler 0.8.4. Receipt appended by hand.
- **APOE diplotype probe for desk #307, 2026-11-14** (the lead, 640351176; a scratch copy, nothing published, the
  rows marked as probes): batch ten's module plus `haplotypes.csv` (e2, e3, e4 by rs429358 and rs7412) and
  `diplotypes.csv` (the six pairs). On 0.8.6 enrich places both SNPs, strict validate and strict compile are green, and
  the artifact gains `haplotypes.parquet` and `diplotypes.parquet` (6 rows each) beside the variant tables;
  `registry_validate` on the polygon is clear and counts APOE among the genes (27). What it does not do: a diplotype row
  has no pmid or study link (studies.csv keys on variant_key), so its grounding lives only in its conclusion text; a
  pair naming a haplotype nobody defined is a warning, not an error, even strict (`star_allele_undefined`). Not seen:
  how the app or the registry's page shows the table (a publish of the probe would show the registry page; the app
  needs a local install, which this seat runs only on an ask).
  Published on the lead's word (640351839) as `test-longevity-loci/test_apoe_probe@0.0.1` on the polygon (test-named,
  so the operator's sweep takes it; delete it once #307 is settled). What the registry shows, read from its record and
  its web page's code at registry 0.30.0: the version lists `haplotypes.parquet` and `diplotypes.parquet` among the
  artifact's files (size, hash, download) and the inputs list both CSVs; APOE joins the gene list (27); the variant,
  study and rsID tiles are unchanged (93, 465, 93). The page has no view of a diplotype's rows: no pair, direction or
  conclusion is shown, and the page code holds no reference to diplotypes or haplotypes. The server compiled it with
  compiler 0.8.4, which ships both tables too. How the app shows them waits for the person (the app install).
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
- 2026-11-15: plugin pinned at v0.48.11 (the liaison, 8250a35; toolchain unchanged, just-dna 0.8.6), running here.
  `enrich_module` now reports `build_diagnoses` (rows whose ref mismatch reads as hg19): read it at the next
  rehearsal. Next batch so far: rows 3, 100, 101, 108, 130, 134, 135.
- 2026-11-15, batch eleven trial build (trunk 2df1202): enrich clean (167 resolved, build_diagnoses empty); the strict
  compile refuses row 101's Wright entry at proxy rs6753712 (effect_allele C, the lead's; the proxy is A/G, and the
  row's effect_unit says per A). Put to the lead and the curator (640407208); the rehearsal waits on the fix.
- 2026-11-15, batch eleven rehearsed (trunk 1e0cc6f, 0.8.6): 101 loci, 303 variant rows, 496 studies, 283/283 VRS
  alleles identified; the polygon's content_signature equals ours (0fb54bbf; server compiles with 0.8.4); receipt
  appended. Warnings unchanged (13 indel VRS carried, not closed, ClinVar currency). The D31 sweep lands in the next build.
- 2026-11-15, next batch trial (trunk ea97295, rows 22 KALRN and 34 LINC01411 in): strict green, 309 variant rows,
  502 studies. Both leads are indels: carried unverified VRS warnings rise from 13 to 16 (rs3830412, rs138762279).
  34's unknown direction exports as is ('unknown') and compiles.
- 2026-11-15, batch twelve rehearsed (trunk ca028a8, 0.8.6): 112 loci, 336 variant rows, 529 studies, 305/305 VRS
  alleles identified; the polygon's content_signature equals ours (68e345d2); receipt appended. Warnings: 16 carried
  indel VRS ids (rows 22 and 34 added three), not closed, ClinVar currency; build_diagnoses empty.
- 2026-11-15, D32 (the person's D4: the 18 biological-ageing marker loci as an unscored section): carried in 0.8 as
  category ageing_markers, every genotype state and direction neutral, the tendency in conclusion, phenotype and the
  effect columns; no score since the module authors no weights. 0.8 has no per-section unscored or folded field. Put
  to the lead (640483383): the export tags every variant OBA_VT0005372 and gives BIOMARKER studies no trait, so a
  marker row needs the marker's trait (the export's change). Check the first marker row's projection when it lands.
- 2026-11-15, D33 (the person's D2, desk #307): APOE goes in this module as ε pairs in haplotypes.csv and
  diplotypes.csv, the probe's shape. The probe test_apoe_probe is deleted from the polygon. To do when row 96
  lands: project its pairs (the export has no diplotype path yet; ask the lead), and at that build say the app's
  display of the pairs is unchecked.
- 2026-11-15, row 96 APOE rehearsed with its ε pairs (trunk 7040f7d, D33/D34): 113 loci, 342 variant rows, 554
  studies, haplotypes.csv 6 (ε2, ε3, ε4 at rs429358, rs7412), diplotypes.csv 12 (six pairs, a lifespan and an
  Alzheimer's result each). validate and compile strict green; both tables compile into parquet. The 19 studies on
  rs429358/rs7412 (no variants.csv row) are kept in studies.parquet with no warning at all under compiler 0.8.6:
  no study_variant_orphan, no refusal, no drop. Warnings: 18 carried indel VRS (rows 122's rs10610954 adds two),
  module_not_closed, dataset_currency. content_signature 688ef9e7…, equal local and polygon; artifact c7a4e714…
  (server). The app's display of the pairs and of the orphan studies is unchecked. Shared clone: an export reads
  the working tree, so a seat's uncommitted row edit can ride along (here the curator's 7040f7d was in the tree
  before it was committed; the build matches 7040f7d).
- 2026-11-15, trial at trunk fbdf589 (rows 124 RPS6, 125 PRAC2, and the D34.5–7 unit bf0cca3 on 120/124/125): strict
  green, 351 variant rows, 561 studies, every rsID resolved. Row 125's insertion rs199607933 (T>TG, T>TGG) raises
  the carried, unverified indel VRS ids to 20. No refusal; held for the batch's close.
- 2026-11-16, pending (the lead, 640548398): when the curator's one-unit commit for batch thirteen's corrections
  lands (D34.10–15; rows 96, 121–126, 131, 136, 107), export, rebuild strict and rehearse on the test instance.
  96's pair texts change; the tables keep their shape.
- 2026-11-16, plugin v0.48.12 pinned (liaison, a7bfed4): enricher 0.8.7 in the lock, format and compiler stay 0.8.6.
  compile_module now reports the toolchain that wrote the artifact; compare_to_published lists the published one's.
  Batch thirteen's rehearsal runs on it after the reload; a moved artifact digest with an unchanged
  content_signature is the enricher bump, read from the toolchain field.
- 2026-11-16, batch thirteen rehearsed (trunk efb975f; D34.10–15 on 96, 107, 120–126, 131, 136; rows 124–126,
  131, 136, 137 new): 360 variant rows, 571 studies, haplotypes 6, diplotypes 12 (96's pair texts changed, shape
  kept). Strict green; 20 carried indel VRS (125's insertion adds two), module_not_closed, dataset_currency.
  content_signature 0abd2bde…, equal local and polygon; artifact 74e7e5e5… (server). Enricher 0.8.7 in the lock;
  this session's plugin still the pre-reload one.
- 2026-11-16, trial at trunk 452e85a (rows 138, 140, 147, 150 and D35 on 121/138/140/147): strict green, 375
  variant rows, 589 studies, every rsID resolved, carried indel VRS still 20. No refusal; held for the batch's close.
- 2026-11-16, trial at trunk 52033b3 (rows 148, 151, 152, 154 added; 154's rs7754015 absent from 1000 Genomes still
  resolves): strict green, 384 variant rows, 594 studies, every rsID resolved, carried indel VRS 20. Held for the
  batch's close.
- 2026-11-16, trial at trunk 5f631bf (rows 111, 139, 146, 155, 156 added): strict green, 399 variant rows, 609
  studies, every rsID resolved (the rare rs373800184 and rs79645902 too), carried indel VRS 20. Held for the close.
- 2026-11-16, batch fourteen rehearsed (trunk 3b2c3f1; D35–D37; eff13b1's nominal statistical_test wording; rows
  117, 127, 159 new since the last trial): 408 variant rows, 615 studies, haplotypes 6, diplotypes 12. Strict green,
  every rsID resolved; 20 carried indel VRS, module_not_closed, dataset_currency. content_signature cc75b113…,
  equal local and polygon; artifact b99639c8… (server). No marker row yet (23 TERC next).
- 2026-11-16, first marker row checked (23 TERC, 8a8adc0; trial with the curator's uncommitted 30 TERT in the tree):
  strict green, 414 variant rows, 622 studies. Projection as D32: category ageing_markers, state neutral on all
  three genotypes, trait_efo_id OBA_0003784 (the marker's), weight null; the two telomere studies BIOMARKER with
  the marker's trait, the lifespan and healthspan look-ups keep theirs. One difference from D32's wording: direction
  is written `unknown` (the row's), not `neutral`; both carry no colour in 0.8's vocabulary. Put to the lead.
  Settled (the lead, 640645516): keep `unknown`. A marker row's direction speaks to longevity, where it is not
  known; the marker's own direction lives in the conclusions and the BIOMARKER studies.
- 2026-11-16, batch fifteen rehearsed (trunk c483cf3; D38; the first marker rows): 429 variant rows, 634 studies,
  haplotypes 6, diplotypes 12. Strict green; 20 carried indel VRS, module_not_closed, dataset_currency.
  content_signature da319d43…, equal local and polygon; artifact 3232e9e1… (server). Seven marker rows (23 TERC and
  114 TFAM at A; 30, 105, 106, 112, 128 at B): category ageing_markers, 3 genotypes each, state neutral, direction
  unknown, weight null, the marker's trait (OBA_0003784 telomere length, EFO_0022597 epigenetic age acceleration,
  EFO_0006312 mtDNA copy number, EFO_0000473 for 112), the tier a flag token; their BIOMARKER studies carry the same
  trait, the lifespan and healthspan look-ups their own. 23 and 112 carry an empty gene, as the rows write it.
- 2026-11-16, trial at trunk a4f6e86 (117's partial; markers 132, 133, 141, 143, 144 added): strict green, 444
  variant rows, 642 studies, every rsID resolved (144's rs59294613 too), carried indel VRS 20. Held for the close.
- 2026-11-16, trial at trunk 4700f7b (markers 145 TSC22D2, 153, 160 added): strict green, 453 variant rows, 648
  studies, every rsID resolved. 145's A/AT insertion rs59633341 resolves and joins the carried, unverified A>AT
  group (20 warning lines, now 21 alleles). Held for the close.
