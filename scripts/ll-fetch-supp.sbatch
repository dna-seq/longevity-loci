#!/bin/bash
# A batch `loci fetch-supp` for the runner seat: one deposit or supplement file, optionally filtered to the
# rsIDs of a CSV column, written into $LOCI_CACHE as the CLI writes it.
#
# Submitted from the clone's root, with the cluster's partition, account and log path given on the sbatch line
# (never written here), and these variables:
#   LL_KEY      the note's key, pmid-… or doi-…                         (required)
#   LL_LOCATOR  a file's URL, zenodo:ID or figshare:ID                  (required)
#   LL_RSIDS    a CSV whose `rsid` column becomes --rows '\b(rs…|…)\b'  (optional)
#   LL_ONLY     --only, a regular expression on the deposit's file name (optional)
# The job inherits LOCI_CACHE and the proxy variables from the submitting shell (sbatch's default --export=ALL).
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --time=01:00:00

set -euo pipefail
: "${LL_KEY:?}" "${LL_LOCATOR:?}" "${LOCI_CACHE:?}" "${https_proxy:?the proxy must be exported}"
export HTTPS_PROXY="$https_proxy" HTTP_PROXY="${http_proxy:-$https_proxy}"
export OMP_NUM_THREADS=2 MKL_NUM_THREADS=2 OPENBLAS_NUM_THREADS=2 POLARS_MAX_THREADS=2

echo "start $(date -u +%FT%TZ) on ${SLURMD_NODENAME:-?} job ${SLURM_JOB_ID:-?}"
echo "revision ${LL_REVISION:-unknown}"

args=("$LL_KEY" "$LL_LOCATOR")
if [ -n "${LL_ONLY:-}" ]; then args+=(--only "$LL_ONLY"); fi
if [ -n "${LL_RSIDS:-}" ]; then
    # sorted and unique, so the same CSV always gives the same regex and the same cache name
    rows=$(uv run python -c '
import sys
import polars as pl
ids = pl.read_csv(sys.argv[1], infer_schema_length=0)["rsid"].drop_nulls().unique().sort().to_list()
print(f"{len(ids)} rsids", file=sys.stderr)
print(r"\b(" + "|".join(ids) + r")\b")' "$LL_RSIDS")
    args+=(--rows "$rows")
fi

rc=0
uv run loci fetch-supp "${args[@]}" || rc=$?
echo "end $(date -u +%FT%TZ) exit $rc"
exit $rc
