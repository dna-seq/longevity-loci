"""An article's other files in the cache: a supplement's tables, a data deposit's files (Zenodo, figshare), a code
repository's file, each rendered to text as `$LOCI_CACHE/<key>.supp-<name>.txt` beside the article's own text,
with a sidecar `<key>.supp-<name>.source.json` saying where it came from, when, and the sha256 of the file read
and of the text written. A note's quote from one of them is then located like any other (RM4).

Rendering, by the file's kind: a workbook (xlsx) one line per row, cells tab-separated, each sheet opened by a
`## sheet: <name>` line; csv and tsv the same, one table; a PDF its extracted text, page by page; plain text and
code as they are; a zip archive each member it can render, opened by `## file: <name>`. Anything else (an image,
an old binary .xls or .doc) is refused, never cached as nothing: a figure has no text to quote, and its caption
is in the article's.

The files are the authors', not ours: they stay in the cache, never in the repository, a message or an issue."""

from __future__ import annotations

import csv
import gzip
import hashlib
import io
import json
import logging
import re
import zipfile
import xml.etree.ElementTree as ET
from dataclasses import dataclass, field
from datetime import UTC, datetime
from pathlib import Path
from urllib.parse import unquote, urlparse

import openpyxl
import pypdf

from longevity_loci.fetch import Outcome, _request, _write

log = logging.getLogger(__name__)
logging.getLogger("pypdf").setLevel(logging.ERROR)  # font warnings on every page; a failed read still raises

ZENODO = "https://zenodo.org/api/records/{id}"
OPENTARGETS = "https://api.platform.opentargets.org/api/v4/graphql"  # answers POST only
FIGSHARE = "https://api.figshare.com/v2/articles/{id}"
DEPOSIT = re.compile(r"^(?P<host>zenodo|figshare):(?P<id>\d+)$")
GITHUB_BLOB = re.compile(r"^https://github\.com/(?P<repo>[^/]+/[^/]+)/blob/(?P<path>.+)$")  # a file page, not the file
KEY = re.compile(r"^(pmid-\d+|doi-\S+|db-[a-z0-9]+-[A-Za-z0-9._]+)$")
# A database release's own statement of its release, asked before a record is cached (RM3): a later release is a
# different source, so a record read under another release than the note names is refused.
RELEASE_PROBES = {
    "opentargets": ("opentargets:{meta{dataVersion{year month}}}",
                    lambda j: f"{j['data']['meta']['dataVersion']['year']}.{j['data']['meta']['dataVersion']['month']}"),
    "ensembl": ("https://rest.ensembl.org/info/data?content-type=application/json", lambda j: str(j["releases"][0])),
}
TEXT_SUFFIXES = frozenset({".txt", ".md", ".py", ".r", ".R", ".sh", ".yaml", ".yml", ".toml", ".ipynb",
                           ".sas", ".do", ".pl", ".c", ".cpp", ".h", ".java", ".jl", ".m", ".rmd", ".Rmd", ".sql",
                           ".bed", ".vcf", ".gff", ".gtf", ".fa", ".fasta"})
NAME_UNSAFE = re.compile(r"[^A-Za-z0-9._-]+")


class Unrenderable(ValueError):
    """A file whose kind has no text this module can write."""


@dataclass(frozen=True)
class Cached:
    outcome: Outcome
    name: str  # the file's name, as the deposit or the URL gives it
    path: Path | None = None
    detail: str = ""

    def __bool__(self) -> bool:
        return self.outcome is Outcome.FETCHED


@dataclass(frozen=True)
class Supplement:
    """What `fetch_supplement` did with one locator: one result per file it found there."""

    locator: str
    files: list[Cached] = field(default_factory=list)
    outcome: Outcome | None = None  # set when the locator itself failed (no deposit, a refused request)
    detail: str = ""

    def __bool__(self) -> bool:
        return self.outcome is None and bool(self.files) and all(self.files)


def _cell(v: object) -> str:
    return "" if v is None else str(v)


def _table(rows: list[list[str]]) -> str:
    return "".join("\t".join(r).rstrip("\t") + "\n" for r in rows)


def keep_rows(text: str, rows: str) -> str:
    """Only the lines a curator asked for: every `## ` section line, the first line after it (a table's header), and
    each line `rows` (a regular expression) finds. For a deposit too big to cache whole (a GWAS's summary
    statistics): the variants a row needs, and the header that says what their cells are."""
    pattern = re.compile(rows)
    out, header_next = [], True
    for line in text.splitlines(keepends=True):
        if line.startswith("## "):
            out.append(line)
            header_next = True
        elif header_next and line.strip():
            out.append(line)
            header_next = False
        elif pattern.search(line):
            out.append(line)
    return "".join(out)


def _gunzip_rows(data: bytes, rows: str) -> bytes:
    """A gzipped text's header line and the lines `rows` finds, streamed: a summary-statistics file is never
    decompressed whole into memory."""
    pattern = re.compile(rows.encode())
    out = []
    with gzip.GzipFile(fileobj=io.BytesIO(data)) as f:
        for n, line in enumerate(f):
            if n == 0 or pattern.search(line):
                out.append(line)
    return b"".join(out)


ODF_TABLE = "{urn:oasis:names:tc:opendocument:xmlns:table:1.0}"
ODF_TEXT = "{urn:oasis:names:tc:opendocument:xmlns:text:1.0}"
W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"


def _office_kind(data: bytes) -> str | None:
    """What an office file is, read from its zip's contents rather than its name: publishers serve an OpenDocument
    spreadsheet under an .xlsx name (Springer's MOESM files). None when it is not a zip."""
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            names = set(z.namelist())
            mime = z.read("mimetype").decode("ascii", "replace").strip() if "mimetype" in names else ""
    except zipfile.BadZipFile:
        return None
    if mime == "application/vnd.oasis.opendocument.spreadsheet":
        return "ods"
    if mime == "application/vnd.oasis.opendocument.text":
        return "odt"
    if "word/document.xml" in names:
        return "docx"
    if "xl/workbook.xml" in names:
        return "xlsx"
    return None


def _odf_cell_text(cell: ET.Element) -> str:
    return " ".join("".join(p.itertext()).strip() for p in cell.iter(f"{ODF_TEXT}p")).strip()


def _ods(data: bytes) -> str:
    """An OpenDocument spreadsheet as `xlsx` is rendered: a `## sheet:` line, then one line a row, cells tab-separated;
    a repeated cell or row (ODF's run-length) written out, empty trailing cells and rows dropped."""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        root = ET.fromstring(z.read("content.xml"))
    parts = []
    for table in root.iter(f"{ODF_TABLE}table"):
        rows = []
        for row in table.iter(f"{ODF_TABLE}table-row"):
            cells: list[str] = []
            for cell in row:
                if cell.tag not in (f"{ODF_TABLE}table-cell", f"{ODF_TABLE}covered-table-cell"):
                    continue
                n = int(cell.get(f"{ODF_TABLE}number-columns-repeated", "1"))
                cells += [_odf_cell_text(cell)] * min(n, 1000)
            while cells and not cells[-1]:
                cells.pop()
            if cells:
                rows += [cells] * min(int(row.get(f"{ODF_TABLE}number-rows-repeated", "1")), 1000)
        parts.append(f"## sheet: {table.get(f'{ODF_TABLE}name', '')}\n" + _table(rows))
    return "\n".join(parts)


def _docx(data: bytes) -> str:
    """A Word document's text: each paragraph a line, each table row a line with its cells tab-separated."""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        body = ET.fromstring(z.read("word/document.xml")).find(f"{W}body")
    lines: list[str] = []
    for block in body if body is not None else []:
        if block.tag == f"{W}p":
            lines.append("".join(block.itertext()))
        elif block.tag == f"{W}tbl":
            for tr in block.iter(f"{W}tr"):
                cells = [" ".join("".join(p.itertext()) for p in tc.iter(f"{W}p")).strip() for tc in tr.findall(f"{W}tc")]
                lines.append("\t".join(cells).rstrip("\t"))
    return "".join(line + "\n" for line in lines if line.strip())


def _odt(data: bytes) -> str:
    """An OpenDocument text's paragraphs and table rows, as `_docx` writes a Word document's."""
    with zipfile.ZipFile(io.BytesIO(data)) as z:
        root = ET.fromstring(z.read("content.xml"))
    lines = ["".join(p.itertext()) for p in root.iter(f"{ODF_TEXT}p")]
    return "".join(line + "\n" for line in lines if line.strip())


def render(name: str, data: bytes, rows: str | None = None) -> str:
    """A file as text, by its name's suffix; Unrenderable when it has none this module can write. With `rows`, only
    the lines `keep_rows` keeps."""
    suffix = Path(name).suffix
    low = suffix.lower()
    if low == ".gz":
        inner = name[: -len(suffix)]
        body = _gunzip_rows(data, rows) if rows is not None else gzip.decompress(data)
        return render(inner, body, rows)
    if rows is not None:
        return keep_rows(render(name, data), rows)
    office = _office_kind(data) if low in (".xlsx", ".xlsm", ".ods", ".docx", ".odt", ".doc") else None
    if office == "ods":
        return _ods(data)
    if office == "docx":
        return _docx(data)
    if office == "odt":
        return _odt(data)
    if low in (".xlsx", ".xlsm") and office == "xlsx":
        book = openpyxl.load_workbook(io.BytesIO(data), read_only=True, data_only=True)
        parts = []
        for sheet in book.worksheets:
            rows = [[_cell(v) for v in row] for row in sheet.iter_rows(values_only=True)]
            parts.append(f"## sheet: {sheet.title}\n" + _table([r for r in rows if any(r)]))
        return "\n".join(parts)
    if low in (".csv", ".tsv"):
        text = data.decode("utf-8-sig")
        rows = list(csv.reader(io.StringIO(text), delimiter="\t" if low == ".tsv" else ","))
        return _table(rows)
    if low == ".pdf":
        reader = pypdf.PdfReader(io.BytesIO(data))
        return "\n".join(f"## page {i}\n{p.extract_text() or ''}" for i, p in enumerate(reader.pages, 1))
    if low == ".zip":
        parts = []
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            for member in sorted(z.namelist()):
                if member.endswith("/"):
                    continue
                try:
                    parts.append(f"## file: {member}\n" + render(member, z.read(member)))
                except Unrenderable as e:
                    parts.append(f"## file: {member}\n(not rendered: {e})\n")
        return "\n".join(parts)
    if suffix in TEXT_SUFFIXES or low in TEXT_SUFFIXES:
        return data.decode("utf-8")
    try:
        record = json.loads(data.decode("utf-8"))
    except (UnicodeDecodeError, json.JSONDecodeError):
        raise Unrenderable(f"no text for a {suffix or 'suffix-less'} file") from None
    return "".join(f"{path} {value}\n" for path, value in flatten(record))


def cache_name(key: str, name: str, rows: str | None = None) -> str:
    """`<key>.supp-<name>.txt`, the name made file-safe; a filtered rendering adds `.rows-<8 hex of the filter>`, so
    two filters of one file do not overwrite each other."""
    tag = "" if rows is None else ".rows-" + hashlib.sha256(rows.encode()).hexdigest()[:8]
    return f"{key}.supp-{NAME_UNSAFE.sub('_', name).strip('_')}{tag}.txt"


def _scalar(v: object) -> str:
    return "null" if v is None else json.dumps(v) if isinstance(v, bool) else str(v)


def flatten(record: object, path: str = "") -> list[tuple[str, str]]:
    """A JSON record as lines, in the record's own order: an object's scalar fields on one line after its path, as
    `key value` pairs, so one quote can name a population with its frequency
    (`data.variant.alleleFrequencies[2] populationName nfe_adj alleleFrequency 0.0694`); its nested objects and
    lists on lines of their own. A database's answer (Open Targets, Ensembl) is cached this way."""
    if isinstance(record, dict):
        scalars = [(k, v) for k, v in record.items() if not isinstance(v, (dict, list))]
        out = [(path or ".", " ".join(f"{k} {_scalar(v)}" for k, v in scalars))] if scalars else []
        for k, v in record.items():
            if isinstance(v, (dict, list)):
                out += flatten(v, f"{path}.{k}" if path else str(k))
        return out
    if isinstance(record, list):
        return [leaf for i, v in enumerate(record) for leaf in flatten(v, f"{path}[{i}]")]
    return [(path, _scalar(record))]


def _fetch_one(url: str, timeout: float):
    """A URL's answer; `opentargets:<query>` POSTs the GraphQL query to Open Targets' API."""
    if url.startswith("opentargets:"):
        return _request(OPENTARGETS, timeout, json.dumps({"query": url.removeprefix("opentargets:")}).encode())
    return _request(url, timeout)


def _release_parts(release: str) -> tuple[str, ...]:
    """A release as its dot-separated parts, leading zeros dropped: Open Targets' 26.09 and 26.9 are one release."""
    return tuple(p.lstrip("0") or "0" for p in release.split("."))


def check_release(key: str, timeout: float) -> str | None:
    """None when the database's current release is the one the key names (or the database states none this module
    can ask); else why the fetch is refused."""
    _, database, release = key.split("-", 2)
    probe = RELEASE_PROBES.get(database)
    if probe is None:
        return None
    reply = _fetch_one(probe[0], timeout)
    if reply.outcome is not None:
        return f"{database}'s release could not be read: {reply.detail}"
    try:
        current = probe[1](json.loads(reply.body.decode("utf-8")))
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, IndexError, TypeError) as e:
        return f"{database}'s release answer: {type(e).__name__}"
    if _release_parts(current) != _release_parts(release):
        return f"{database} serves release {current}, not {release}: a later release is a different source"
    return None


def _files(locator: str, timeout: float) -> tuple[list[tuple[str, str]], Supplement | None]:
    """The (name, url) pairs a locator names: a deposit's files, or one URL."""
    m = DEPOSIT.match(locator)
    if not m and locator.startswith("opentargets:"):
        return [("opentargets.json", locator)], None
    if not m:
        if urlparse(locator).scheme not in ("http", "https"):
            return [], Supplement(locator, outcome=Outcome.REFUSED, detail="a locator is a URL, zenodo:ID or figshare:ID")
        url = GITHUB_BLOB.sub(r"https://raw.githubusercontent.com/\g<repo>/\g<path>", locator)
        return [(unquote(Path(urlparse(url).path).name) or "file", url)], None
    api = (ZENODO if m["host"] == "zenodo" else FIGSHARE).format(id=m["id"])
    reply = _request(api, timeout)
    if reply.outcome is not None:
        return [], Supplement(locator, outcome=reply.outcome, detail=reply.detail)
    try:
        record = json.loads(reply.body.decode("utf-8"))
        if m["host"] == "zenodo":
            pairs = [(f["key"], f["links"]["self"]) for f in record["files"]]
        else:
            pairs = [(f["name"], f["download_url"]) for f in record["files"]]
    except (UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError) as e:
        return [], Supplement(locator, outcome=Outcome.MALFORMED, detail=f"{m['host']} record: {type(e).__name__}")
    if not pairs:
        return [], Supplement(locator, outcome=Outcome.NO_TEXT, detail=f"{m['host']} record {m['id']} lists no file")
    return sorted(pairs), None


def fetch_supplement(key: str, locator: str, cache: Path, only: str | None = None, timeout: float = 600,
                     rows: str | None = None, name: str | None = None) -> Supplement:
    """Fetch the files a locator names (a URL, `zenodo:ID`, `figshare:ID`) into the cache as text, for the note
    `key`. `only` is a regular expression a deposit's file name must match; `rows` keeps only the lines it finds (and
    each table's header); `name` names the one file a URL gives (an API's answer, whose path names nothing). A note
    key `db-<database>-<release>` caches a database's record (RM3): where the database states its release, a
    different one is refused. A file that cannot be rendered is refused and nothing is written for it."""
    if not KEY.match(key):
        return Supplement(locator, outcome=Outcome.REFUSED, detail=f"{key!r} is not a note key (pmid-…, doi-… or db-<database>-<release>)")
    if key.startswith("db-") and (refusal := check_release(key, timeout)) is not None:
        return Supplement(locator, outcome=Outcome.REFUSED, detail=refusal)
    pairs, failed = _files(locator, timeout)
    if name is not None:
        if len(pairs) != 1:
            return Supplement(locator, outcome=Outcome.REFUSED, detail="--name names one file; the locator gave several")
        pairs = [(name, pairs[0][1])]
    if failed is not None:
        return failed
    if only is not None:
        pairs = [(n, u) for n, u in pairs if re.search(only, n)]
        if not pairs:
            return Supplement(locator, outcome=Outcome.NOT_FOUND, detail=f"no file matches {only!r}")
    out = Supplement(locator)
    for fname, url in pairs:
        reply = _fetch_one(url, timeout)
        if reply.outcome is not None:
            out.files.append(Cached(reply.outcome, fname, detail=reply.detail))
            continue
        try:
            text = render(fname, reply.body, rows)
        except (Unrenderable, UnicodeDecodeError, zipfile.BadZipFile, gzip.BadGzipFile, re.error, EOFError, pypdf.errors.PdfReadError, OSError, KeyError) as e:
            out.files.append(Cached(Outcome.REFUSED, fname, detail=f"{type(e).__name__}: {e}"))
            continue
        if not text.strip():
            out.files.append(Cached(Outcome.NO_TEXT, fname, detail="rendered to no text"))
            continue
        path = cache / cache_name(key, fname, rows)
        sidecar = {"key": key, "file": fname, "locator": locator, "url": url, "rows": rows,
                   "fetched": datetime.now(UTC).isoformat(timespec="seconds"),
                   "file_sha256": hashlib.sha256(reply.body).hexdigest(),
                   "sha256": hashlib.sha256(text.encode("utf-8")).hexdigest()}
        _write(path, text)
        _write(path.with_name(path.name.removesuffix(".txt") + ".source.json"), json.dumps(sidecar, indent=2) + "\n")
        out.files.append(Cached(Outcome.FETCHED, fname, path))
    return out
