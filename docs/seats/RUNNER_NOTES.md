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

- 6428266 `ll-fetch-supp-zenin`, for the curator; watcher armed (until-event, --skip "watch armed| RUNNING on ").

## Cluster facts sent to the rigger and not yet in its inventory

None.

## To file

- kit #398, the take refused for a seat the clone declares: filed by the lead, nothing more to add here.
- kit: the runner role's `job-watch` command (`until-event.sh -- env JOB=<id> bash watch-job.sh`) wakes at once on
  watch-job's own "watch armed" line; it needs `--skip 'watch armed| RUNNING on '` (the RUNNING transition wakes it too). Seen 2026-11-10 on job 6428266. To file,
  unattended.
