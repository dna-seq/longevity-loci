# Runner — notes

The runner seat's working state, rewritten to the present before a reset (`docs/seats/RUNNER.md`).

## Now

Seated 2026-11-10 (account seat-10). The first-seating handout is done:
- the rigger's orientation read (the copy it sent the lead); the share is the default until the person answers
  desk #248, and the rigger tells this seat the answer (its reply, 2026-11-10);
- no `ll-` job in the queue, none taken over;
- `runs/LOG.md` and `runs/STATUS.md` started;
- the scout and the curator told, in the repository's channel, that fetches now come here.

## Running jobs

None (6428266 completed 2026-11-10T23:54Z), so no watcher is armed.

## Cluster facts sent to the rigger and not yet in its inventory

None.

## To file

- kit #398, the take refused for a seat the clone declares: filed by the lead, nothing more to add here.
- kit #410 filed 2026-11-10: the `job-watch` recipe wakes on watch-job's armed and RUNNING lines. Meanwhile arm with
  `until-event.sh --skip 'watch armed| RUNNING on ' -- env JOB=<id> LOG=<log> bash …/watch-job.sh`.
