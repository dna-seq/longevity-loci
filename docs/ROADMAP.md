# Roadmap

Open work only, in order. Each item is a section `## RMn — name` with a line saying its state and its
owner. A done item leaves this file; `docs/CHANGELOG.md` says what landed.

## RM1 — the export of curated rows to the module's tables

**State:** waits until 2026-11-12. **Owner:** lead. Then look whether the registry serves 0.8 and the plugin
released for it (issue #6); built after both. Kept so on 2026-11-10, against building for 0.7.1 first: the person, "module b - wait for 0.8 on
registry". The compiler's 0.8.0 was cut 2026-11-05;
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

Read from the first row (46-LPA, the module seat, 2026-11-10), three things the export cannot project on 0.7.1:
`studies.csv` is keyed (variant, pmid), and a row may hold two analyses of one article (validate warns on the
duplicate); `stat_significance` has no `nominal` (D11); a study on a proxy states the proxy's alleles, which must not
be written on the lead variant while 0.7.1 has no `proxy_rsid`. Each is RM1's to settle when it is built.

## RM3 — a database release's record fetched into the cache

**State:** unattended. **Owner:** lead. A `db-` note's quotes are unknown until its record is in `$LOCI_CACHE`
(D12). `loci fetch` learns a database release: Open Targets' variant and locus-to-gene records first (the
curator's 46-LPA cites them), gnomAD's frequencies next, each rendered to lines a quote can be located in, with a
sidecar saying the release, the URL and the sha256. The release read must equal the note's `release`, or the fetch
refuses: a later release is a different source.

## RM4 — a supplement's table in the cache, so its values can be quoted

**State:** unattended, paused with the pilot until the person's go. **Owner:** lead. In four of the pilot's five
rows the replication outside UK Biobank lives only in a supplement (Deelen 2019's Supplementary Data 1, Wright
2019's figshare tables). The cache holds an article's text, so those values sit in notes as prose, and no study row
can quote them. Deelen's look-ups are study rows at 71 and prose elsewhere. `loci fetch` learns a supplement: an
xlsx or csv rendered to lines (one table row a line, cells tab-separated, the sheet named), cached as
`<key>.supp-<n>.txt` with a sidecar giving the file's URL and sha256. A quote then names its supplement, and
`check quotes` locates it there. This makes the existing reading depth `supplement` checkable rather than adding a
new one.

## RM5 — the pilot's small format fixes

**State:** unattended, paused with the pilot. **Owner:** lead. From the curator's pilot notes:
- `ungrained` ignores a study's `proxy_rsid`, so a quote naming the proxy still warns.
- `mediator:` takes `EFO_` only, and coronary artery disease's EFO id is retired for MONDO_0005010.
- `study_design` has no parental-lifespan design other than Cox; Wright 2019's linear model was written as Cox.

