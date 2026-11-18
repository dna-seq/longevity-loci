# Lead — notes

The lead seat's working state, rewritten to the present before a reset (`docs/seats/LEAD.md`, "Before a reset").
Rewritten whole on 2026-11-16 for the org move (the person: "Make sure they commit all to notes, transcripts are not
moving"): a fresh session carries on from this file, `docs/seats/LEAD_STATE.md` and `docs/DECISIONS.md` alone.

## Now (2026-11-16)

Curation is complete. All 161 seed loci are curated, in 156 rows, and the eight second signals the scout queued are
rows 162 to 169: 164 rows, A 15, B 73, C 41, D 35. Seventeen batches have been read adversarially, the last settled as
D40 (fb32e6c). The curator reports every D40 correction applied and pushed (12c673f, latest 1ffba5f). The scout's
queue is empty (d8e0a08), and `scripts/dashboard.py --left` reports 0. The module was rebuilt strict green with batch
seventeen (signature aebf5e38: 489 genotype rows, 679 studies) and rehearsed on the test instance only (3ee0bbb).
**Nothing is on production; nothing goes there without the person's explicit word.**

The quote check is clean: the full run found 6,531 located and 1 unknown (db-gwascatalog-2025.01.09 has no cached
text). `loci check quotes --since REV` is now the curator's per-row check (d63682d, 1ffba5f). fetch-supp renders .html
pages (3aafb3c).

## Waiting on the person (desk; defaults stand meanwhile)

- #344 (now desk #45 in the new organisation's desk): the APOE exception, D34.1 with its reason corrected in D34.10. Default: it stays.
- #346 (now desk #46): a flag the app shows for a second signal. Default: none (0.8 has no column for it).
- #345 and #274 withdrawn 2026-11-16 under the kit's v0.1.227 rule (only a real fork goes to the person): the brain-age
  loci stay unscored (D36.3); rehearsals stay under `test-longevity-loci`.
- #266 (now desk #47): how to mark the field's consensus top loci (a flag, a tier, or nothing). Nothing is built until answered.
- #200: the trust register; the person said "trust register reask in a month", so ask again on 2026-12-10.
- desk #56 (2026-11-18): publish 2.0.0 to production now, or after the sweep's rows are read and rebuilt. Default: wait
  (nothing published).
- Also on their word: an app display check by a local install (the APOE pair table, and APOE's studies with no variant
  row), and the production publish.

## Open curation items (decided, waiting on a source)

- 165: B. A waits on a quoted mothers' D21 heterogeneity test (D40.4). Wright prints 0.031, which our derivations do
  not reproduce.
- 167: its mechanism moves to general_ageing once the source is cached (D40.5).
- 117: at D, pending Broer's table.

## The org move (2026-11-16, in hand)

The person plans to move this repository's seats to the chat organisation desk-antonkulaga (genie's), driven by
agents-kit/lead's handoff hand-loci-prep and its addendum. Done by the lead:
- auto-mode rules: `automode.py --check` from v0.1.226 reads current (19 allow rules, the kit's newest of
  2026-11-16), so `--apply` was not run;
- keys made for all six seats and genie's secretary imported into each as
  desk-antonkulaga/secretary@longevity-genie.zulipchat.com, embassy `genie`, fingerprint E7BB 5D47 8EA2 0887 CC57
  DEF0 80E0 DE40 2E3F AC72 (it matched the handoff); encryption subkeys run until 2026-11-30, so rotate before then
  if the move slips;
- the six public keys sent to agents-kit/lead by handoff (640872377);
- every seat asked in #longevity-loci>org-move to commit its notes and reply with the commit; the liaison asked to
  move the pin to v0.1.226 or later (moving the pin is the liaison's job).
Still owed: reply to agents-kit/lead with each seat's notes commit, one `keys contacts` line, and the
`automode.py --check` line, once the five seats have answered. Nothing switches until the person says so.

## Standing rules learned here

- Pacing is off, full forward, on the person's word. Their standing order (2026-11-11): "After 10 adjust pacing and go
  next 10 and so on unless blocked or I steer". After each batch of about ten rows: three adversarial subagent reads,
  findings settled as D-decisions, one corrections handoff to the curator, the module seat rebuilds and rehearses on
  the test instance, then LEAD_STATE is updated and reposted.
- Pacing and quota measurements stay out of the repository (the person, 2026-11-11: "Keep pacing/quota measures
  uncommited, only rules commited").
- The milestones duty is held acting (L139, no pm seat). The state post comes from `docs/seats/LEAD_STATE.md` via
  `watchdog.sh keep lead state '#longevity-loci>state' FILE`.
- The job prefix is `ll-`, set in the machine's `slurm.toml` under `[slurm.repo.longevity-loci]`.
- Never chain an edit onto `git pull &&`: a failed pull silently skips the edit.
- My own mistakes this run, all caught by the adversarial reads: D39.18 skipped §4.5/D16's co-occurring lifespan gate
  (fixed by D40.1), and D39.19 read a residual P two-sided (withdrawn by D40.2). When a new rule lands, check every
  older gate still applies to the row it moves.

## Plan

- reflect after 2026-11-19: classes/base/BASE.md as of v0.1.191 (wake rules spelled out, secrets never repeated, the
  organisation's script account, handout renamed handoff).
- reflect after 2026-11-21: classes/base/BASE.md as of v0.1.207 (the button closes the wake, not the turn).
- Scratch processes outside the repository (a quota sampler and the curator's compaction waker) do not move with the
  seat; a new session starts without them.

- 2026-11-17: moved to the chat organisation desk-antonkulaga (bin/org-move.py).

- Reporting in this organisation follows its house style (desk docs/REPORTING.md, the person's ask 2026-11-17 via its
  secretary): #longevity-loci topics `state` (one kept message: results-page link, where it stands with marks, headline
  results, plan with owner and wait), `milestones` (one post per landed result), `decisions` (one question per message,
  numbered options and default), `general`, `daily`.

- Milestones (the person, 2026-11-17: "you only did one on the movement, and none on preceding work"): one post in
  `#longevity-loci>milestones` per landed result, 1 to 3 lines, finding first, a figure where it helps; the eleven
  earlier results were posted that day. README rewritten the same day on their ask (d42de36); refresh its numbers
  and figures (`scripts/readme_figures.py`) at each milestone that moves them.

- 2026-11-17, on the person's question ("what about vs newly published data 2023-2026?"): the scout's sweeps run
  forward from 2026-10-20 and rely on tracks A-K (no recorded queries) for 2023-2026. Asked the scout for a backfill
  sweep with its own queries, plus bioRxiv/medRxiv listings from April 2026 (Zulip 641384225). Window widened on the
  person's word to 2015-01-01 -> 2026-10-20 ("Lookup should cover the range past last date of HAGR base": Build 3
  released 2017-06-24, its newest cited PMID from 2015).
  Done 2026-11-18 (c0a8726 to d77ae4a; D41): rule fixed after calibration (54/58), 47 uncited papers on 18 rows, rs1927465
  and 13 Catalog lines queued; the curator works the queue. Next: read the rows it moves as a batch (adversarial reads).

- Filed 2026-11-18 as kit #537: the seat's watchdog died five times in about 30 hours while the session lived (the last
  pid 1849426, reported by the machine's watchdog), each restarted only by the next prompt's hook.

- 2026-11-18, Anton's ask: a deck comparing HAGR LongevityMap, module v1 and v2, and the agent loop, in the look of their
  Bucharest deck (fetched by its public export link). `scripts/longevitymap_deck.py` builds it (14 slides; numbers as of
  that day; the v1 error slide from the manuscript's Table S14). Sent as .pptx in #longevity-loci; the Drive upload is
  Anton's (no Google login here). Not rendered here: running a downloaded office suite was denied, so layout was
  checked by a text-fit estimate only.
