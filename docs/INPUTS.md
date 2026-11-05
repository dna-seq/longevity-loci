# Inputs

The databases the re-curation starts from, kept outside git under `$LOCI_INPUTS` (set on the machine, never a
path here), each with where it came from, when, and its digest. Fetched 2026-11-05 by the lead.

| Input | Source | Under `$LOCI_INPUTS` | sha256 |
|---|---|---|---|
| v1's module database (OakVar `longevitymap.sqlite`: tables `variant` 3,476 rows, `allele_weights` 1,043, `gene` 886, `population` 82, `categories` 12) | `dna-seq/just_longevitymap` at debb5f8 (its last push 2025-03-05), `data/longevitymap.sqlite` | `v1_just_longevitymap/longevitymap.sqlite` | `f4a6439e8646b8febc6a208b198b54450f6b8e6a844c4dad50867a0887e294a7` |
| HAGR LongevityMap Build 3 (550 entries, 884 genes, 3,144 variants; released 2017-06-24) | `https://genomics.senescence.info/longevity/longevity_genes.zip` (Last-Modified 2017-06-24) | `hagr_longevitymap/longevity_genes.zip`, unpacked in `extracted/` (`longevity.csv`, `release.html`) | `5226be2961140bf1b7776a23b7eb7aede4c7a5e896f3bc21f33e1ddd30625763` |
| HAGR LongevityMap, live entry pages (ids 1 to 3,480) | `https://genomics.senescence.info/longevity/entry.php?id=N`, by `scripts/hagr_snapshot.py` | `hagr_live/entries_2026-11-05.csv` | `a0f4350330a00a8fc33dd94be2febf36d65113be25bd6eef0c12609534fbe33d` (3,457 entries) |

**Licence.** HAGR's pages: "This work is licensed under a Creative Commons Attribution 3.0 Unported License"
(genomics.senescence.info/legal.html, read 2026-11-05). Citation, as Build 3's release notes give it: Budovsky
et al. (2013), "LongevityMap: A database of human genetic variants associated with longevity". The module's
`licensing.csv` carries the attribution (requirements R-LEGACY-3). v1's module repository is under its own
`LICENSE` (to be read before anything of it ships).

## Has the original moved since v1? (2026-11-05)

Only a little. The live site's real entries end at id 3,476, v1's last id. Ids past it return an empty page,
which is why the S14 audit's scrape of ids 1 to 3,500 counted 3,500 found. Against v1's `variant` table:

- **19 ids v1 holds are empty on the live site now** (256, 257, 276-278, 280, 290, 330, 343, 344, 347, 371, 375,
  383, 764, 1926, 2598, 3474, 3475): removed upstream, or never shown.
- **Identifiers**: 97 differ because v1 replaced HAGR's named variants (E2/E3/E4, I/D) by rsIDs, as the audit
  records; about 20 more are rsIDs the live site gives where v1 has none, and one merged rsID (VDR rs10735810 on
  the site, rs2228570 in v1).
- **Conclusions**: none differs from v1's, all 3,457 live entries compared (letters and digits, case folded). The
  first snapshot cut texts at a `<` ("aged <70"); the one recorded here is the fixed re-run.

The download is unchanged since 2017, so Build 3 is not where any later curation would show.
