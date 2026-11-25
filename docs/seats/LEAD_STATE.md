**1. Results page:** https://claude.ai/artifact/9Ga73vyTsg4ZjwJSg4M7Q4 (tabs: tiers, all loci, by mechanism; from the rows at 96fe362, before the literature sweep's rows).

**2. Where it stands** (2026-11-25)
- 🟢 Curation done: all 161 seed loci, the scout's second signals and the literature sweep's new loci, in 172 rows, each claim citing a quote checked verbatim against its article.
- 🟢 Eighteen batches read adversarially (D1 to D43), every correction applied; no tier of the earlier 164 rows moved in the last read.
- 🟢 The module is rebuilt strict green at 9d87300 (signature 997b3356) and is in just-dna-lite's pull request #37, which supersedes the 1.2.0 port; merge and publish are the person's.
- 🟢 This build is re-enriched (from the local Ensembl snapshot, signature unchanged) and rehearsed on the registry's test instance (2026-11-25; the registry reads back 997b3356), by the lead while the module seat is stopped on a usage-limit message (since 2026-11-20).
- 🟢 The literature since HAGR's last data (2015 to Oct 2026) is swept and its loci are in.

**3. Headline results**
- Tiers: A 15, B 75, C 44, D 38 (n = 172 rows). A means a genome-wide hit (N ≥ 100k, P < 5e-8) with an independent replication and no red flag; most loci fall short on the replication.
- 38 rows at D: the discovery failed a powered test in its own ancestry, or its own authors called it anomalous.
- Module: 513 genotype rows (121 protective, 101 risk, 291 neutral), 697 studies from 54 papers, APOE as 12 ε-pair results.

**4. Plan / queue**
- ❓ APOE: drop v2's ε-pair tables and point to the published APOE module, or keep them until just-dna-lite reads them (the person, desk #90; default: kept, D33).
- ❓ Keep the loosened rule that let APOE keep tier A despite one null study (the person, desk #45; default: it stays).
- ❓ A flag in the app for a second signal near an existing locus (the person, desk #46; default: none).
- ❓ Marking the field's consensus top loci: a flag, a tier, or nothing (the person, desk #47; default: nothing built).
- ⏳ Row 46 (LPA, A): a paywalled paper may carry a failed replication; needs a person to fetch it (default: unknown, A held).
- ⏳ v1's own rsIDs beyond the seed loci wait on D6.
