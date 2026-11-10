# Pacing the curation

What a curated row costs in model use, measured, so the curator's rate can be set against the account's quota.
Each measurement is a dated section, newest first; a later one never rewrites an earlier.

## The five-row pilot, 2026-11-10

The person asked for it: "do first 5 rows this way and see what breaks ... measure quota climb for this job
(intergral, ballpark) to understand how to pace this properly, how many rows per hour to do and how to throttle".
The rows were seed tier A loci 93 LDLR, 80 CHRNB4, 57 CDKN2B-AS1, 71 ATXN2 and 67 TTC12. One curator session did
them on Opus 5.5 with no subagents, while the module seat was asked to sleep (it still spent 0.28M finishing a desk question, #251). The window ran from 21:57 to 22:33 UTC.

**Tokens, from the curator's transcript.** Each API response is counted once. Rows are split by their commits.
"Weighted" means input + 1.25 × cache write + 0.1 × cache read + 5 × output, in input-token equivalents. These are
list-price ratios, so the figure is a ballpark of quota use, not a bill.

| Row | Minutes | Calls | Prompt a call | Cache read | Output | Weighted |
|---|---|---|---|---|---|---|
| 93 LDLR | 9 | 46 | 159k | 7.20M | 35.7k | 1.03M |
| 80 CHRNB4 | 4 | 16 | 215k | 3.41M | 20.8k | 0.49M |
| 57 CDKN2B-AS1 | 6 | 30 | 260k | 7.75M | 28.0k | 0.98M |
| 71 ATXN2 | 3 | 10 | 296k | 2.93M | 16.7k | 0.41M |
| 67 TTC12 | 3 | 12 | 320k | 3.82M | 15.8k | 0.49M |
| correction pass over the five | 7 | 8 | 379k | 3.01M | 8.8k | 0.36M |
| **total** | **32** | **122** | | **28.1M** | **125.8k** | **3.76M** |

"Prompt a call" is cache read plus cache write over calls: the context each call carries. It grew 2.4 times over
the pilot, from 159k to 379k, because the curator's session kept every row it had done. The rows only look flat at
0.41M to 1.03M because the later ones took 10 to 12 calls against the first's 46. A call costs about 0.1 × its
prompt plus 5 × its output, so the same row costs about twice as much at the end of a full session as at its start.
The cost of a row is therefore set by the session's age as much as by the locus. The session's reset cadence is a
throttle beside the rate.

**The quota, sampled every five minutes** (`quota.py --json`). This is the whole account: every session on this
machine and any other on the same login. The 5-hour window went from 10% to 15% and the 7-day from 38% to 39%. Both
read in whole percents. Over the same window this machine's four active sessions spent 5.0M weighted, and the
curator 3.96M of it (79%). That gives about 1M weighted per point of the 5-hour window. On the 7-day window it is
roughly 5M per point, but that figure is no better than a factor of two: one whole-percent step was seen. Earlier
the same evening the reading switched to another account (its windows' resets moved), so a percentage is only read
inside one account's stretch.

**Read for pacing.**

- The five rows and their correction pass took 39 minutes of the curator's time, about 8 rows an hour. They used
  about 9% of the 5-hour window an hour, which is sustainable, and about 2% of the 7-day window an hour.
- A row early in a session (a prompt near 150k, 15 to 30 calls) comes to about 0.3M to 0.7M weighted. A row late in
  one (a prompt near 350k) comes to about 0.6M to 1.2M. The pilot's mean, about 0.75M with the correction pass
  shared out, is about 0.75% of the 5-hour window. On the 7-day window it is about 0.15%, the latter coarse.
- Reset the curator's session every five rows or so, or once a call's prompt passes about 300k. That keeps rows
  near the low figure. The kit's compaction does part of this on its own.
- The 156 rows left: about 75M weighted with regular resets, about 150M without. That is roughly 15% to 30% of a
  7-day window, uncertain by a factor of two because the 7-day reading moved by one whole point.
- The five rows had an advantage that cuts the other way. They shared their main papers with 46-LPA (Timmers
  2019, Joshi 2017, Pilling 2017, Deelen 2019), already in the corpus. 93 LDLR read a new paper's supplement and
  had the most calls. A locus whose papers are all new should be expected at the high figure.
- No review is counted: nobody but the curator has read these rows. A second reader per row would add its own
  cost.
- Speed is not the limit, the quota is: 3 to 9 minutes a row. The share of the 7-day window that curation may take
  is the person's call, and the rate follows from it: the share in points ÷ 0.15 = rows, spread over the window's
  hours left.
