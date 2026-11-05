# Roadmap

Open work only, in order. Each item is a section `## RMn — name` with a line saying its state and its
owner. A done item leaves this file; `docs/CHANGELOG.md` says what landed.

## RM1 — the export of curated rows to the module's tables

State: after the compiler's 0.8 cut, the registry's deploy and the plugin's release (issue #6). Owner: lead.
`rows/` projected onto `variants.csv` and `studies.csv` for the module seat, 0.8's columns from the fields
`docs/FORMATS.md` already records; `tradeoff` and `eur_only_evidence` never authored.

## RM2 — the checks the formats still lack

State: unattended. Owner: lead. Named in `docs/FORMATS.md`, "Not checked yet": §6.3's required columns on a
tier A/B study, all three genotypes of a scored locus with the most common neutral, the hard rules R-TIER-1 to 4.
