# Roadmap

Open work only, in order. Each item is a section `## RMn — name` with a line saying its state and its
owner. A done item leaves this file; `docs/CHANGELOG.md` says what landed.

## RM1 — the export of curated rows to the module's tables

State: after the compiler's 0.8 cut, the registry's deploy and the plugin's release (issue #6). Owner: lead.
`rows/` projected onto `variants.csv` and `studies.csv` for the module seat, 0.8's columns from the fields
`docs/FORMATS.md` already records; `tradeoff` and `eur_only_evidence` never authored. Per quote, the export
records the text it was located in (the reading's depth, the cache sidecar's source), so the module's README can
explain the plugin's `quotes_found` zeros: upstream checks Europe PMC's body text only (issue #7, point 3).
