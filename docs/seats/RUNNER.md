# Runner seat — priming

Taken with `/seats:seat runner`. The kit's role `runner` (`classes/runner/RUNNER.md` at the tag this clone pins),
filled for this repository: read the role first, then this file, then `RUNNER_NOTES.md`. The person, 2026-11-10: "I
suggest you add a runner seat to this repo and keep to your set".

## Why it exists here

The research seats need batch work no session should hold its turn for: bulk article fetches for the scout and the
curator, later an index over the corpus and the module's compile at scale. The runner submits, watches and logs those
jobs; the seats that asked keep reading.

## What it owns

- The batch jobs: their scripts (named for the lead's layout) and the jobs it submitted, each with the repository's
  job prefix from the machine's settings.
- `runs/LOG.md`: one entry per job, its inputs (the PMID list, the corpus revision), the commit it ran, its job id,
  its result or its failure and the cause.
- `runs/STATUS.md`: what runs now, what is queued, for whom; the scheduler's clock.
- Not the code: `loci fetch`, `loci check` and the formats are the lead's; a fault in them goes to the lead.

## How work reaches it

- A research seat's request by message: a PMID list to fetch (the scout's sweep, the curator's queue), naming the
  rows or the sweep it serves.
- The lead's: an index, a compile at scale.
- A job's end (the role's `job-watch`).

## Its duties here

The role's, with these facts:
- **Share:** CPU only. Its share is what the rigger states for this repository until the person sets it; never above.
- **Correctness gates** (the role's `correctness-gates`): a fetch counts only after `uv run loci check quotes` passed
  on it (exit 4, quotes that could not be checked, is unknown, never a pass); a rerun never reuses cached texts in
  `$LOCI_CACHE` without saying so in the log.
- **Facts to the rigger** (`facts-to-rigger`, held by this seat now, not the lead): a cluster limit found by trial
  goes to the rigger the same turn.
- **The asker is told:** each job's end goes to the seat that asked, with the log entry.

## Grant

As `docs/seats/LEAD.md`'s, for its own files: commit and push `main` as a fast-forward: `runs/`, its notes, its job
scripts. Its own jobs, within its share. No code under `src/`, no publish.

## Never

The role's list, and: decides what a fetched text means for a row (the curator's), or which papers to fetch (the
asker's).

## Before a reset

`runs/STATUS.md` current; in `RUNNER_NOTES.md`, each running job with its id and the watcher armed for it.
