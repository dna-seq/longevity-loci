# Pacing the curation

What a curated row costs in model use, measured, so the curator's rate can be set against the account's quota.
Each measurement is a dated section, newest first; a later one never rewrites an earlier.

## The five-row pilot, 2026-11-10

The person asked for it: "do first 5 rows this way and see what breaks ... measure quota climb for this job
(intergral, ballpark) to understand how to pace this properly, how many rows per hour to do and how to throttle".
The rows were seed tier A loci 93 LDLR, 80 CHRNB4, 57 CDKN2B-AS1, 71 ATXN2 and 67 TTC12. One curator session did
them on Opus 5.5 with no subagents, while the module seat slept. The window ran from 21:57 to 22:33 UTC.

**Tokens, from the curator's transcript.** Each API response is counted once. Rows are split by their commits.
"Weighted" means input + 1.25 × cache write + 0.1 × cache read + 5 × output, in input-token equivalents. These are
list-price ratios, so the figure is a ballpark of quota use, not a bill.

| Row | Minutes | Calls | Cache read | Output | Weighted |
|---|---|---|---|---|---|
| 93 LDLR | 9 | 46 | 7.20M | 35.7k | 1.03M |
| 80 CHRNB4 | 4 | 16 | 3.41M | 20.8k | 0.49M |
| 57 CDKN2B-AS1 | 6 | 30 | 7.75M | 28.0k | 0.98M |
| 71 ATXN2 | 3 | 10 | 2.93M | 16.7k | 0.41M |
| 67 TTC12 | 3 | 12 | 3.82M | 15.8k | 0.49M |
| correction pass over the five | 7 | 8 | 3.01M | 8.8k | 0.36M |
| **total** | **32** | **122** | **28.1M** | **125.8k** | **3.76M** |

That is 0.41M to 1.03M a row, about 0.75M with the correction pass shared out. Cache reads are about 80% of the
weighted figure, because every call re-reads the session's context. So a row costs more as the session grows, and
a session reset makes the next row cheaper.

**The quota, sampled every five minutes** (`quota.py --json`). This is the whole account: every session on this
machine and any other on the same login. The 5-hour window went from 10% to 15% and the 7-day from 38% to 39%. Both
read in whole percents. Over the same window this machine's four active sessions spent 5.0M weighted, and the
curator 3.96M of it (79%). That gives about 1M weighted per point of the 5-hour window. On the 7-day window it is
roughly 5M per point, but that figure is no better than a factor of two: one whole-percent step was seen. Earlier
the same evening the reading switched to another account (its windows' resets moved), so a percentage is only read
inside one account's stretch.

**Read for pacing.**

- At the pilot's rate, about 13 rows an hour, one curator takes about 9% of the 5-hour window an hour. That is
  sustainable inside the 5-hour window, about 2% of the 7-day window an hour.
- Per row that is about 0.75% of the 5-hour window, or 0.15% of the 7-day window, the latter coarse.
- The 156 rows left would come to about 120M weighted. That is roughly 25% of a 7-day window, best case. This is a
  ceiling for tier A work and a floor for loci with unread papers.
- These five shared their main papers with 46-LPA (Timmers 2019, Joshi 2017, Pilling 2017, Deelen 2019), already in
  the corpus and the cache. 93 LDLR, the one row that read a new paper's supplement, cost the most. A locus whose
  papers are all new should be expected near or above 1M.
- Speed is not the limit, the quota is: 3 to 9 minutes a row. The share of the 7-day window curation may take is
  the person's call, and the rate follows from it: share in points ÷ 0.15 = rows, spread over the window's hours
  left.
