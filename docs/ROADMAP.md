# Roadmap

Open work only, in order. Each item is a section `## RMn — name` with a line saying its state and its
owner. A done item leaves this file; `docs/CHANGELOG.md` says what landed.

## RM1 — the export of curated rows to the module's tables

**State:** waits until 2026-11-12. **Owner:** lead. Then look whether the registry serves 0.8 and the plugin
released for it (issue #6); built after both. The compiler's 0.8.0 was cut 2026-11-05.
`rows/` projected onto `variants.csv` and `studies.csv` for the module seat, 0.8's columns from the fields
`docs/FORMATS.md` already records; `tradeoff` and `eur_only_evidence` never authored. Per quote, the export
records the text it was located in (the reading's depth, the cache sidecar's source), so the module's README can
explain the plugin's `quotes_found` zeros: upstream checks Europe PMC's body text only (issue #7, point 3).
