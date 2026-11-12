# Lead — notes

The lead seat's working state, rewritten to the present before a reset (`docs/seats/LEAD.md`, "Before a reset").

## Now (2026-11-05)

First seating, the seat-builder's handout:

1. Leak gate: done. The list is metabonet's, on the person's word (2026-11-05: "Take stopwodrs list from
   metabonet"), replacing a longer one the lead drafted.
2. Rules: done, 3e7ed57.
3. Groundwork: done, 3b38d74 (just-dna-lite at 050bf9f). The person told, so its folder there can become a pointer.
4. Cluster: done, differently from the handout. The machine file's `job_prefix` is one value (metabonet's `mn-`)
   and outranks the repository, so this clone sets `JOB_PREFIX=ll-` and `LOCI_CACHE` in its untracked
   `.claude/settings.local.json` env. The digest line read through that setting is not yet seen at a session
   start (checked with the variable inline). Nodes watcher alive.
5. Formats and checks: done (8496cca, the critic's fixes 80eb769, 0.8's study fields 433a1d0 from issue #6,
   D10).
6. Inputs: done, `docs/INPUTS.md` (v1's sqlite, HAGR Build 3, a live snapshot; CC BY 3.0). v1.2.0's registry
   tables are the module seat's to fetch with the plugin.
7. Trust register: desk #200 answered 2026-11-10, "trust register reask in a month": waits until 2026-12-10, then
   ask the person again.
8. Pin: nothing to move.

## To file (unattended, at the next idle turn)

Nothing. Filed: kit #272 (job_prefix per machine), kit #273 (the kit pin in untracked settings). The plugin is
installed (v0.48.0), and `QUOTING.md` read into D10.

## Open

- Avatar set. The `first seating:` line sent to the builder.

## For the person, at their return

Nothing. 2026-11-10, on the person's word ("update your plugin and apply yourself"): the lead moved the kit pin to
v0.1.164 (`move-to-tag`), applied the auto-mode rules (`automode.py --apply`, `--check` clean; the tooling and admin
entries left out as not this clone's), and moved the job prefix to `[slurm.repo.longevity-loci] job_prefix = "ll-"`
in the machine's `slurm.toml`, the `JOB_PREFIX` env override dropped (the driver reads `ll-`, from=repo).

## Open with the person (2026-11-10)

- The runner seat landed (on the person's word, 2026-11-10: "I suggest you add a runner seat to this repo and keep to
  your set"); the lead's `facts-to-rigger` duty, its cluster paragraph and the nodes watcher moved to it.  Seated
  2026-11-10 (seat-10, through the desk's long line; the short take's refusal is kit #398); its first seating done
  (e138b73).
- Cluster orientation from metabonet's rigger: the runner's now; it reads it from the rigger at its first seating.

## The five-row pilot (2026-11-10, done)

93 LDLR, 80 CHRNB4 and 57 CDKN2B-AS1 stayed tier A; 71 ATXN2 and 67 TTC12 went to B, down from the seed's A. What
broke is in the curator's notes under "Pilot". The measurements stay out of the repository (the person,
2026-11-11: "Keep pacing/quota measures uncommited, only rules commited"); the rules they gave are in the curator's
priming (9135a65). The person's answers, 2026-11-11: up to 80% of the weekly window; a re-tier is the lead's to
read adversarially, not a question; RM4 yes, "as deep as neeed"; the requirements' silent cells by the advisor
pattern. The person, 2026-11-11: "After 10 adjust pacing and go next 10 and so on unless blocked or I steer": the
curator runs on in batches of ten; after each, the lead re-measures (tokens per row from the curator's transcript,
the quota windows; the figures stay out of the repository) and sends any pacing change. The self-compaction works, but the session then idles: until kit #409 lands, a waker of the lead's (outside the
repository) watches the curator's transcript for a compaction and wakes it 30 s later. In hand: a ten-row run under that routine, measured again (the
person, 2026-11-11: "go with next 10 measurement on andjusted scenario, remeasure"); the adversarial read of 71
and 67; RM4 and RM5.

## Plan

RM1 the export (after the compiler's 0.8 cut, the registry deploy and the plugin's release). RM2 landed
(9d42ccb, with `loci fetch`), its auditor's findings fixed in 47abe43. The plugin stays enabled for every seat, the person's call (2026-11-05: "3"), about 2.5k
tokens a session while its 81 tools stay deferred.
- reflect after 2026-11-19: classes/base/BASE.md as of v0.1.191 (wake rules spelled out, secrets never repeated, the organisation's script account, handout renamed handoff).
- Milestones duty held acting since 2026-11-12 (L139, v0.1.192; no pm seat): the state post's source is docs/seats/LEAD_STATE.md, kept with `watchdog.sh keep lead state '#longevity-loci>state' FILE` whenever where-it-stands, a headline or the next actions change; one post per landed result in #longevity-loci>milestones.
