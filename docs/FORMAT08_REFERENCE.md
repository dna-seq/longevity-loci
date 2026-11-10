# just-dna-format 0.8's longevity reference, read for this repository

`docs/format08_reference/` holds two things copied verbatim from `dna-seq/just-dna-compiler` at `241ea8c7fd`
(main, 2026-11-11, MIT), on the person's word (2026-11-11: "read just-dna-format's 0.8 reference example for
longevitymap v2 module, it dissects edge cases of the initial plan, injest it, copy here as reference"):

- `longevity_studies/`, the reference example `reference_examples/longevity_studies`: five loci and thirteen
  `studies.csv` rows in 0.8's columns, built from the papers, enriched, validated strict and compiled. Its
  README says what each row exercises and what building it broke.
- `LONGEVITYMAP_V2_SHAPE_AUDIT.md`, the compiler's `docs/probes/` audit that measured every requirement of
  `docs/longevitymap_v2/` against the 0.8 shape: which column each requirement needs, the twelve gaps and their
  fixes, and the candidate rows. Its relative links point into the compiler's repository and do not resolve
  here.

Neither is edited here. A newer copy replaces both, with the new commit named above.

## What it settles for this repository

**For the export (RM1) and the module seat:**

- **0.8's `studies.csv` columns match FORMATS.md's study fields one for one.** These are `ancestry`, `age_min`,
  `age_max`, `age_of`, `sample_size`, `sample_unit`, `n_cases`, `stratum`, `stratum_level`, `proxy_rsid`,
  `effect_unit` and `phenotype_class`. The example's header is the export's target.
- **Two analyses of one article are told apart by a narrowing cell:** `phenotype_class`, an age band or a stratum.
  So 0.7.1's duplicate (variant, pmid) warning, RM1's first gap, goes away where a row differs in one of those.
  Deelen's 90th and 99th percentiles share a class, so the percentile goes in `statistical_test` (the compiler's
  RM140 rule). Our `percentile_case_control_p90` and `_p99` designs export that way.
- **A preprint is `pmid=NONE` with its `doi`.** Our `doi-` note key exports that way.
- **A Cox model's age-band row leaves `n_cases` empty:** its deaths are events, not cases.
- **The tier scale is open within the module's named scale** (the seed's X, A- and B- are legal). `tradeoff`, the
  causal and effector confidences, the European-only flag and the LD pair are computed, never authored. This is
  already in FORMATS.md for `tradeoff` and `eur_only_evidence`; C and E join it.
- **The legacy layer is one row**: a tag selector (`flags: legacy_longevitymap`, tier D) instead of 528 one-member
  rows. A v1 rsID the seed tiers needs a concrete row to beat D. The curator's legacy rows can stay as they are
  planned; the export collapses them.
- **The outcome strip is derived from `phenotype_class`.** Which outcome cell MULTIVARIATE fills is the v2
  module's README to state, not the format's.
- **The example's `variants.csv` uses `trait_efo_id` OBA_VT0005372** (lifespan), and each study gives its own
  trait (EFO_0009762 healthspan, EFO_0007796 parental lifespan). Our rows put EFO_0007796 on the variant. The
  export picks one rule.

**For the curator:**

- **A proxy's `effect_allele` is the proxy's**, and the compiler checks it against the proxy's alleles, never the
  lead's. Which lead allele it travels with (the phase) is the author's to derive: r² has no sign. The example
  derives it from allele frequencies, as the read of 71-ATXN2 did, and says how.
- **Timmers 2019 contradicts itself on two effect alleles.** Table 1 names A as rs10455872's (LPA)
  lifespan-raising allele, and Table 2 names G for rs4970836 (CELSR2's proxy). Its Figure 5 source data labels the
  same variants `rs10455872_G` and `rs4970836_A`, with positive betas. The frequencies and the biology side with
  the tables. The example withholds `effect_allele` on the rows taken from the source data. This bears on 46-LPA
  and on 6 CELSR2.
- **The healthspan GWAS's N is 300,477** (Timmers 2020), not the audit's 300,447.
