"""`loci`: the research seats' command line."""

from __future__ import annotations

import logging
import os
from collections import Counter
from pathlib import Path

import typer
from dotenv import load_dotenv

from longevity_loci.fetch import Outcome, fetch
from longevity_loci.check import FAILING, UNKNOWN, Finding, Kind, check_quotes, check_rows, load_seed, summary

app = typer.Typer(no_args_is_help=True, help="Checks over the curated rows, the corpus and the article cache.")
check_app = typer.Typer(
    no_args_is_help=True,
    help="The format checks. Exit 0 all passed, 1 a failure, 2 an input missing, 4 nothing failed but something "
    "(or everything) could not be checked.",
)
app.add_typer(check_app, name="check")

ROOT = Path.cwd()
SEED = ROOT / "docs" / "longevitymap_v2" / "data" / "seed_variants.csv"


@app.callback()
def _main() -> None:
    load_dotenv(override=False)
    logging.basicConfig(level=logging.INFO, format="%(message)s")


def _report(findings: list[Finding], verbose: bool) -> None:
    """A line per failure; the unknowns by note, with a count; warnings with -v; the passes only counted."""
    for f in findings:
        if f.kind in FAILING or f.kind is Kind.SHARED_QUOTE or (verbose and f.kind in (Kind.UNSUPPORTED, Kind.INCOMPLETE)):
            typer.echo(f"{f.kind.value:12} {f.path}  {f.where}  {f.detail}".rstrip())
    unknown = Counter((f.kind, f.path) for f in findings if f.kind in UNKNOWN)
    for (kind, path), n in sorted(unknown.items()):
        typer.echo(f"{kind.value:12} {path}  {n} quote(s) not checked")
    counts = summary(findings)
    if not counts:
        typer.echo("nothing to check: no file was read, which is not a pass")
        raise typer.Exit(4)
    typer.echo("  ".join(f"{k.value}: {n}" for k, n in sorted(counts.items())))
    if any(k in FAILING for k in counts):
        raise typer.Exit(1)
    if any(k in UNKNOWN for k in counts):
        typer.echo("not all checked: the unknowns above are neither a pass nor a failure")
        raise typer.Exit(4)


def _run(fn, *args) -> list[Finding]:
    try:
        return fn(*args)
    except FileNotFoundError as e:
        typer.echo(str(e), err=True)
        raise typer.Exit(2) from e


@check_app.command("rows")
def rows_cmd(
    rows: Path = typer.Option(ROOT / "rows", help="the rows directory"),
    corpus: Path = typer.Option(ROOT / "corpus", help="the corpus directory"),
    seed: Path = typer.Option(SEED, help="the seed list, whose locus ids name the rows"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="list unsupported axes too"),
) -> None:
    """Each row parses, is named <locus_id>-<locus_name>.yaml as the seed list names it, holds its own locus, and
    cites only quotes the corpus holds."""
    if not seed.is_file():
        typer.echo(f"no seed list: {seed}", err=True)
        raise typer.Exit(2)
    _report(_run(check_rows, rows, corpus, load_seed(seed)), verbose)


@check_app.command("quotes")
def quotes_cmd(
    corpus: Path = typer.Option(ROOT / "corpus", help="the corpus directory"),
) -> None:
    """Each note's quote is found verbatim in $LOCI_CACHE/<key>.txt."""
    _report(_run(check_quotes, corpus, _cache()), False)


def _cache() -> Path:
    cache = os.environ.get("LOCI_CACHE", "")
    if not cache or not Path(cache).is_dir():
        typer.echo(f"LOCI_CACHE names no directory: {cache!r}", err=True)
        raise typer.Exit(2)
    return Path(cache)


@app.command("fetch")
def fetch_cmd(pmids: list[int] = typer.Argument(..., help="PMIDs to fetch")) -> None:
    """Fetch articles into $LOCI_CACHE: Europe PMC's open full text where there is one, else the abstract.
    Exit 0 all fetched, 1 one has no record or no text, 3 the service did not answer (retry)."""
    cache = _cache()
    results = [fetch(p, cache) for p in pmids]
    for r in results:
        typer.echo(f"{r.outcome.value:12} {r.key}  {r.source.value if r.source else ''}  {r.title or r.detail}".rstrip())
    if any(r.outcome is Outcome.UNREACHABLE for r in results):
        raise typer.Exit(3)
    if not all(results):
        raise typer.Exit(1)
