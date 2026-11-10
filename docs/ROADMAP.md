# Roadmap

Open work only, in order. Each item is a section `## RMn — name` with a line saying its state and its
owner. A done item leaves this file; `docs/CHANGELOG.md` says what landed.

## RM1 — the export of curated rows to the module's tables

**State:** waits until 2026-11-12. **Owner:** lead. Then look whether the registry serves 0.8 and the plugin
released for it (issue #6); built after both. The compiler's 0.8.0 was cut 2026-11-05;
the registry's 0.28.3 (on enricher 0.8.1) was being cut on 2026-11-07, its test instance to get it at the
maintainer's deploy.
`rows/` projected onto `variants.csv` and `studies.csv` for the module seat, 0.8's columns from the fields
`docs/FORMATS.md` already records; `tradeoff` and `eur_only_evidence` never authored. Per quote, the export
records the text it was located in (the reading's depth, the cache sidecar's source), so the module's README can
explain the plugin's `quotes_found` zeros: upstream checks Europe PMC's body text only (issue #7, point 3).

The module seat's ask (2026-11-10, module/ scaffolded on the plugin v0.48.5, format 0.7.1): `variants.csv` one row
per (rsid, genotype): rsid, genotype, state, conclusion (required); gene, phenotype, category (from
axes.mechanism), direction, effect_allele, effect_size, effect_measure, stat_significance, negatives, trait_efo_id,
actionability (label), priority (A high, B medium, C/D low), flags (`tier:X` plus the §4.2 axis tokens and the row's
flags), `requires_callable=false` and `acmg_sf=false` written out, weight empty; never chrom/start/ref/alts (the
enricher resolves them) nor curator/method (spec defaults). `studies.csv` one row per (rsid, study): pmid (or doi),
rsid, population, study_design, stat_significance, p_value, p_value_num, effect_size, effect_measure,
effect_allele, trait_efo_id, statistical_test, provenance_quote as the quote's text, curator. 0.7.1 has no
ancestry, age, sample, stratum or proxy columns; those come with 0.8. Strict validate refuses an empty
`studies.csv`, so the first exported locus is also the module's first green build.
