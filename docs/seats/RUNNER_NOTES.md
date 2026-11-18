# Runner — notes

The runner seat's working state, rewritten whole on 2026-11-16 before the move to another chat organisation, so a fresh
session can carry on from these notes, `docs/seats/RUNNER.md` (the priming), `runs/LOG.md` and `runs/STATUS.md` alone.

## Now

- **Nothing in hand.** No ll- job runs or waits; `runs/STATUS.md` says so. The only batch job so far is 6428266
  ll-fetch-supp-zenin (2026-11-10), completed and counted (`runs/LOG.md`).
- **Curation is caught up.** All 161 seed loci have rows (156 files), the second signals 162 to 169 are in, the scout's
  queue is empty (2026-11-16). No seat has a batch request pending.
- **Org move: done 2026-11-17.** The seats now live in the chat organisation desk-antonkulaga (acb4b4e,
  `[repo] org` in `.blueprints.toml`); this seat was punched in again there on 2026-11-17. Its join ticket is used up
  and was never written anywhere. Message ids from before the move belong to the old organisation's chat.

## Standing arrangements

- **Full quote checks** (from 2026-11-16, Zulip 640823601): the curator sends its periodic full `loci check quotes`
  here as an ll- job, naming the commit to run it at. A full run is about 70 minutes at one core, niced. The curator's
  per-row check is now `loci check quotes --since REV` (about 12 minutes, the lead's d63682d, which also added
  `--key KEY` and a `[n/N] key` progress line on stderr, `-q` to silence). No job script yet: write
  `scripts/ll-check-quotes.sbatch` when the first is asked for, on the pattern of `scripts/ll-fetch-supp.sbatch`
  (1 core, thread caps, revision echoed, exit code passed through). Exit 4 is unknown, never a pass; the run so far
  always shows one unknown, db-gwascatalog-2025.01.09, a database note with no cached text.
- **Fetches:** bulk `loci fetch` / `loci fetch-supp` from the curator, the scout or the lead go through
  `scripts/ll-fetch-supp.sbatch` (2 cores, 4G, 1 h; variables LL_KEY, LL_LOCATOR, LL_RSIDS, LL_ONLY, LL_REVISION).
  A fetch counts only after `loci check quotes` passed on the notes that quote it. A rerun reusing cached texts says
  so in the log. `fetch-supp` cannot extract a table from an HTML page; the lead owns that fix.
- **Per job:** write the LOG.md and STATUS.md entries first, commit by path with a `Seat: runner` line, push; the jobs
  watcher (`[seat.runner.watch.jobs]`, prefix ll-) wakes the seat at each start, requeue and end; check the gate;
  tell the seat that asked, with the job id and result.

## Cluster facts (from the rigger, 2026-11-10; also in memory `cluster-orientation`)

- Lab account and partition as the machine's settings name them; exclude the GPU park nodes from CPU jobs.
- Default share of 16 cores until the person answers desk #248; the rigger tells this seat the answer.
- Job logs go to the runs directory under the user's data volume (`%x-%j.log`), never into the repo.
- The proxy must be exported into the job (the sbatch scripts refuse without it).
- Never touch another user's or another seat's jobs; the GPU jobs in the pinned situation block belong to another repo.

## What I learned

- Kit picker for scripts: the newest `seats/0.1.*` directory that has `bin/py.sh` (an empty one appears mid-update);
  the glob must be `0.1.*`, not `0.1.1*`.
- `watchdog.py react ID` (no seat name). Right after a watchdog restart, wait 15–20 s or it says it holds no Zulip
  account. `ack` takes an outcome: `done:SHA`, `filed:#N`, `relayed:SEAT`, `info` or `declined:WHY`.
- The button (`watchdog.py nothing`) closes the wake, not the turn: with pending work, go on with it.
- Desk watcher errors (GitHub 503, rate limit) are transient; it retries every 300 s and says so again only after a
  read succeeds. v0.1.211 made desk readers on one machine share one copy.
- From v0.1.227 the machine runs one watchdog for every seat. Its "watchdog gone under its live session" wakes here
  were all release handovers, not kills: the old process ends "no seat served for 60 s", the next copy starts and
  reads the card's old pid as an orphan, about 2.5 min with no watcher (counts on kit #537, 2026-11-18). Press
  `nothing`.
- An embassy message marked sensitive is described in `#embassy-review` with the secret cut out, after handling.

## To file

- Nothing open. Kit #438 (empty cold-start jobs line) fixed in v0.1.190; kit #410 fixed in v0.1.182 (and unneeded since
  the prefix watcher, kit #380); kit #398 filed by the lead.

- 2026-11-17: moved to the chat organisation desk-antonkulaga (bin/org-move.py).
