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

## The five-row pilot (2026-11-10, in hand)

The person: "1a, 2a, 3 no ... do first 5 rows this way and see what breaks ... measure quota climb for this job
(intergral, ballpark) to understand how to pace this properly, how many rows per hour to do and how to throttle.
Module seat sleeps this time. Once done pause". 1a landed as D13 (9f4c886), 2a as D14 (0f8c866), and 3 was
recorded in D13. The curator is doing 93, 80, 57, 71 and 67, one commit and one `done:` per row, and pauses after
the fifth. The module seat is asleep. The lead measures each row's tokens from the curator's transcript (and its
subagents) between row commits, and the account's quota windows sampled every 5 minutes. The quota reading
changed account mid-evening, its windows' resets moved, so tokens are the primary measure and the percentage is
read only where one account holds. After the fifth row the lead reports to the person and pauses too.

## Plan

RM1 the export (after the compiler's 0.8 cut, the registry deploy and the plugin's release). RM2 landed
(9d42ccb, with `loci fetch`), its auditor's findings fixed in 47abe43. The plugin stays enabled for every seat, the person's call (2026-11-05: "3"), about 2.5k
tokens a session while its 81 tools stay deferred.
