"""`loci`: the research seats' command line."""

from __future__ import annotations

import logging
import os
from pathlib import Path

import typer
from dotenv import load_dotenv

from longevity_loci.check import FAILING, UNKNOWN, Finding, Kind, check_quotes, check_rows, summary

app = typer.Typer(no_args_is_help=True, help="Checks over the curated rows, the corpus and the article cache.")
check_app = typer.Typer(no_args_is_help=True, help="The format checks. Exit 0 all passed, 1 a failure, 4 only unknowns.")
app.add_typer(check_app, name="check")

ROOT = Path.cwd()


@app.callback()
def _main() -> None:
    load_dotenv(override=False)
    logging.basicConfig(level=logging.INFO, format="%(message)s")


def _report(findings: list[Finding], verbose: bool) -> None:
    """One line per failure or unknown; the passes only counted (aggregated by kind)."""
    for f in findings:
        if f.kind in FAILING or (verbose and f.kind not in (Kind.OK, Kind.LOCATED)):
            typer.echo(f"{f.kind.value:12} {f.path}  {f.where}  {f.detail}".rstrip())
    counts = summary(findings)
    typer.echo("  ".join(f"{k.value}: {n}" for k, n in sorted(counts.items())) or "nothing to check")
    if any(k in FAILING for k in counts):
        raise typer.Exit(1)
    if any(k in UNKNOWN for k in counts):
        typer.echo("not all checked: the unknowns above are neither a pass nor a failure")
        raise typer.Exit(4)


@check_app.command("rows")
def rows_cmd(
    rows: Path = typer.Option(ROOT / "rows", help="the rows directory"),
    corpus: Path = typer.Option(ROOT / "corpus", help="the corpus directory"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="list unsupported axes too"),
) -> None:
    """Each row parses, is named <locus_id>-<locus_name>.yaml, and cites only quotes the corpus holds."""
    _report(check_rows(rows, corpus), verbose)


@check_app.command("quotes")
def quotes_cmd(
    corpus: Path = typer.Option(ROOT / "corpus", help="the corpus directory"),
    verbose: bool = typer.Option(False, "--verbose", "-v", help="list unchecked quotes too"),
) -> None:
    """Each note's quote is found verbatim in $LOCI_CACHE/<key>.txt."""
    cache = os.environ.get("LOCI_CACHE", "")
    if not cache:
        typer.echo("LOCI_CACHE is not set: the article cache is unknown, so no quote can be checked", err=True)
        raise typer.Exit(2)
    if not Path(cache).is_dir():
        typer.echo(f"LOCI_CACHE names no directory: {cache}", err=True)
        raise typer.Exit(2)
    _report(check_quotes(corpus, Path(cache)), verbose)
