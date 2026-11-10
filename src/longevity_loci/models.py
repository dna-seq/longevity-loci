"""The two research formats: a curated row (one per locus, `rows/`) and an evidence note (one per article,
`corpus/`). Field names and vocabularies are the requirements' own (docs/longevitymap_v2, §4.2 and §6), so the
module seat's export is a projection, never a translation. docs/FORMATS.md is the prose of this file."""

from __future__ import annotations

import re
from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

_KEY = r"(?:pmid-\d+|doi-[A-Za-z0-9._;()\-]+|db-[a-z0-9]+-[A-Za-z0-9._]+)"  # an article, a preprint, a database release
CITE = re.compile(rf"^(?P<note>{_KEY})#(?P<quote>q\d+)$")
NOTE_KEY = re.compile(rf"^{_KEY}$")


class Tier(StrEnum):
    A = "A"
    B = "B"
    C = "C"
    D = "D"


class Verdict(StrEnum):
    KEPT = "kept"
    RE_TIERED = "re-tiered"
    LEGACY = "legacy"
    DROPPED = "dropped"


class Depth(StrEnum):
    ABSTRACT = "abstract"
    FULL_TEXT = "full_text"
    SUPPLEMENT = "supplement"
    RECORD = "record"  # a database release's record, the one reading a db- note has


class StatSignificance(StrEnum):
    SIGNIFICANT = "significant"
    SUGGESTIVE = "suggestive"
    NOMINAL = "nominal"  # 1e-5 <= p < 0.05: a replication §4.1 counts, below the suggestive band
    NOT_SIGNIFICANT = "not_significant"


class StudyDesign(StrEnum):
    PARENTAL_LIFESPAN_COX = "parental_lifespan_cox"
    PARENTAL_LIFESPAN_LINEAR = "parental_lifespan_linear"  # parents' lifespan regressed linearly (Wright 2019), not Cox
    OWN_SURVIVAL_COX = "own_survival_cox"
    PERCENTILE_CC_P90 = "percentile_case_control_p90"
    PERCENTILE_CC_P99 = "percentile_case_control_p99"
    CENTENARIAN_CC = "centenarian_case_control"
    AGE_THRESHOLD_CC = "age_threshold_case_control"  # cases above an age (90+, say), not a birth-cohort percentile
    MULTIVARIATE = "multivariate_healthspan_lifespan"
    HEALTHSPAN_COX = "healthspan_cox"
    CANDIDATE_GENE = "candidate_gene"
    META_ANALYSIS = "meta_analysis"
    MODEL_ORGANISM = "model_organism"


class PhenotypeClass(StrEnum):
    """§4.5: the definition of "pro-longevity" a study uses (R-DEF-1)."""

    EXTREME_SURVIVAL_CC = "EXTREME_SURVIVAL_CC"
    PARENTAL_LIFESPAN = "PARENTAL_LIFESPAN"
    OWN_SURVIVAL = "OWN_SURVIVAL"
    VIABILITY_AF = "VIABILITY_AF"
    HEALTHSPAN = "HEALTHSPAN"
    MULTIVARIATE_AGEING = "MULTIVARIATE_AGEING"
    FAMILIAL = "FAMILIAL"
    DISEASE_DEPLETION = "DISEASE_DEPLETION"
    RARE_BURDEN = "RARE_BURDEN"
    EVOLUTIONARY = "EVOLUTIONARY"
    MR = "MR"
    BIOMARKER = "BIOMARKER"


class EffectMeasure(StrEnum):
    BETA = "beta"
    HR = "HR"
    OR = "OR"


class QuoteAbsent(StrEnum):
    """Why a study has no quote: the kinds of an empty quote in the plugin's QUOTING.md (issue #7)."""

    NOT_FOUND = "not_found"  # read, and no passage supports the row
    UNCHECKED = "unchecked"  # only the abstract could be read, and it does not say
    OTHER_CLAIM = "other_claim"  # the article is cited for a claim it does not make: the row goes to a decision
    LICENCE_UNCLEAR = "licence_unclear"  # quotable, but the right to quote is not known


PLACEHOLDER_CURATORS = frozenset({"ai", "agent", "model", "machine", "llm", "true", "false", "yes", "no", "auto"})


class Ancestry(StrEnum):
    """just-dna-format 0.8's closed `ancestry` codes (the compiler's INTEGRATION_0_8, issue #6)."""

    AFR = "AFR"
    AMR = "AMR"
    EAS = "EAS"
    EUR = "EUR"
    SAS = "SAS"


class AgeOf(StrEnum):
    PARTICIPANT = "participant"
    PARENT = "parent"


class SampleUnit(StrEnum):
    INDIVIDUALS = "individuals"
    LIVES = "lives"


class AgeClass(StrEnum):
    LIFELONG = "LIFELONG"
    MIDLIFE = "MIDLIFE"
    LATE = "LATE"
    AGE_INVERTING = "AGE_INVERTING"
    EARLY_LIFE = "EARLY_LIFE"
    UNKNOWN = "UNKNOWN"


class AgeConfidence(StrEnum):
    DIRECT = "DIRECT"
    DIRECT_WEAK = "DIRECT_WEAK"
    INFERRED = "INFERRED"
    UNKNOWN = "UNKNOWN"


class Cell(StrEnum):
    """An outcome-profile cell, as §4.2 writes it (its minus is U+2212). `untested` is never read as no effect."""

    PLUS = "+"
    ZERO = "0"
    MINUS = "−"
    UNTESTED = "untested"


def _cell(v: object) -> object:
    """YAML reads a bare 0 as a number and a bare - as nothing; a typed hyphen is the minus."""
    if v == 0 and not isinstance(v, bool):
        return "0"
    return "−" if v == "-" else v


class Who(StrEnum):
    SELF = "act_who:self"
    DOCTOR = "act_who:doctor"


# §4.2's tokens, closed where the requirements close them. An exact token, or a prefix and the pattern of its value;
# a prefix whose value the requirements leave open (mech:<area>) takes any lower-case name.
EXACT_TOKENS = frozenset({
    "broad", "tradeoff", "nonadditive", "mr:drug_target_proxy", "ancestry_tag", "age_dependent", "eur_only_evidence",
    "legacy_longevitymap", "replication_failed", "preprint", "pleiotropic", "conditional",
})
TOKEN_VALUES: dict[str, str] = {
    "causal": r"C[1-4]", "effector": r"E[1-4]", "ap": r"weak|moderate|strong", "sex_specific": r"m|f",
    "PROTECT": r"ABSENCE_OF_RISK|PRESENCE|BUFFERING", "animal": r"genage_mouse|mouse_qtl|worm_rnai",
    "animal_dir": r"concordant|discordant|nonmonotone", "act_who": r"self|doctor",
    "act_test": r"lpa|ldl|bp|hba1c", "act_screen": r"skin", "act_behaviour": r"smoking|weight",
    "ld_proxy_of": r"rs\d+", "mediator": r"(EFO|MONDO)_\d+", "also_in": r"[a-z0-9_]+", "mech": r"[a-z0-9_]+",
    "context": r"[a-z0-9_]+", "ancestry_specific": r"[a-z0-9_]+", "hallmark": r"[a-z0-9_]+",
}


def check_token(token: str) -> str:
    if token in EXACT_TOKENS:
        return token
    prefix, _, value = token.partition(":")
    if prefix in TOKEN_VALUES and re.fullmatch(TOKEN_VALUES[prefix], value):
        return token
    raise ValueError(f"{token!r} is not a §4.2 token (docs/FORMATS.md lists them)")


def _check_tokens(tokens: list[str]) -> list[str]:
    return [check_token(t) for t in tokens]


class Actionability(StrEnum):
    PREVENTABLE = "preventable"
    MODIFIABLE = "modifiable"
    DESCRIPTIVE = "descriptive"


class State(StrEnum):
    PROTECTIVE = "protective"
    RISK = "risk"
    NEUTRAL = "neutral"


class Direction(StrEnum):
    PROTECTIVE = "protective"
    RISK = "risk"
    CONTESTED = "contested"
    UNKNOWN = "unknown"


class Strict(BaseModel):
    model_config = ConfigDict(extra="forbid", frozen=True)


def _check_cites(cites: list[str]) -> list[str]:
    bad = [c for c in cites if not CITE.match(c)]
    if bad:
        raise ValueError(f"a cite is <note key>#q<n> (pmid-31413261#q1); not: {', '.join(bad)}")
    return cites


class Claim(Strict):
    """An axis value with the quotes it rests on. `cites` empty means unsupported, and the check says so."""

    cites: list[str] = Field(default_factory=list)
    _v = field_validator("cites")(_check_cites)


class TierAxis(Claim):
    value: Tier


class Category(StrEnum):
    """§5.2's `category` vocabulary; `other` is not allowed (R-CAT-1)."""

    HEART_VESSELS = "heart_vessels"
    BRAIN_MEMORY = "brain_memory"
    SMOKING_LUNGS = "smoking_lungs"
    IMMUNE_INFLAMMATION = "immune_inflammation"
    METABOLISM = "metabolism"
    SKIN_SUN = "skin_sun"
    GENERAL_AGEING = "general_ageing"
    AGEING_MARKERS = "ageing_markers"
    LEGACY_CANDIDATE = "legacy_candidate"


class MechanismAxis(Claim):
    value: Category


class PleiotropyAxis(Claim):
    values: list[str] = Field(default_factory=list)  # §4.2 tokens: mech:<area>, broad, tradeoff, ...
    _t = field_validator("values")(_check_tokens)


class AgeAxis(Claim):
    value: AgeClass
    confidence: AgeConfidence


class OutcomeAxis(Claim):
    healthspan: Cell
    lifespan: Cell
    exceptional_survival: Cell
    _c = field_validator("healthspan", "lifespan", "exceptional_survival", mode="before")(_cell)


class ActionabilityAxis(Claim):
    label: Actionability
    what: list[str] = Field(default_factory=list)  # act_test:lpa, act_behaviour:smoking, ...
    who: Who | None = None
    _t = field_validator("what")(_check_tokens)


class ContextAxis(Claim):
    values: list[str] = Field(default_factory=list)  # sex_specific:<m|f>, age_dependent, eur_only_evidence, ...
    _t = field_validator("values")(_check_tokens)


class Axes(Strict):
    """The seven axes of the requirements' summary, reported separately and never summed."""

    tier: TierAxis
    mechanism: MechanismAxis
    pleiotropy: PleiotropyAxis
    age_of_action: AgeAxis
    outcome: OutcomeAxis
    actionability: ActionabilityAxis
    context: ContextAxis


class Flag(Claim):
    """One of §4.2's other tokens (causal:C2, effector:E1, PROTECT:PRESENCE, animal:genage_mouse, ld_proxy_of:rs…)."""

    token: str
    _t = field_validator("token")(check_token)


class Genotype(Strict):
    """A §6.2 `variants.csv` row's per-genotype part."""

    genotype: str
    state: State
    conclusion: str


class Variant(Strict):
    """A §6.2 `variants.csv` locus: the per-variant columns, then its genotypes."""

    rsid: str = Field(pattern=r"^rs\d+$")
    gene: str  # the effector call, not the nearest gene
    phenotype: str | None = None  # plain outcome label, at most six words
    trait_efo_id: str | None = None  # the lifespan trait; a mediator goes in flags as mediator:EFO_… or mediator:MONDO_…
    effect_allele: str | None = None
    effect_size: float | None = None
    effect_measure: EffectMeasure | None = None
    stat_significance: StatSignificance | None = None
    direction: Direction
    genotypes: list[Genotype] = Field(default_factory=list)
    negatives: str | None = None

    @field_validator("phenotype")
    @classmethod
    def _short(cls, v: str | None) -> str | None:
        if v is not None and len(v.split()) > 6:
            raise ValueError(f"phenotype is at most six words: {v!r}")
        return v


class Study(Strict):
    """A §6.3 `studies.csv` row; `quote` is its provenance_quote, cited from a note."""

    rsid: str = Field(pattern=r"^rs\d+$")
    note: str
    quote: str | None = None  # a quote id in the note; or none, with quote_absent saying why
    quote_absent: QuoteAbsent | None = None
    phenotype_class: PhenotypeClass
    study_design: StudyDesign
    population: str = Field(min_length=1)  # as the article names it
    ancestry: list[Ancestry] = Field(default_factory=list)  # 0.8's codes for that population
    stat_significance: StatSignificance
    p_value: str | None = None  # as the article writes it
    p_value_num: float | None = Field(default=None, ge=0, le=1)
    age_min: float | None = Field(default=None, ge=0)  # an age band, in years; either end may be open
    age_max: float | None = Field(default=None, ge=0)
    age_of: AgeOf | None = None  # whose age: the participant's, or the parent's (parental lifespan)
    sample_size: int | None = Field(default=None, gt=0)
    sample_unit: SampleUnit | None = None
    n_cases: int | None = Field(default=None, ge=0)
    stratum: str | None = None  # a subgroup the estimate is for (men, women, ...), with its level
    stratum_level: str | None = None
    proxy_rsid: str | None = Field(default=None, pattern=r"^rs\d+$")  # the variant the study reported, when rsid is its lead
    curator: str | None = None  # who located the quote: a name or a model id, never a placeholder like "ai"
    effect_size: float | None = None
    effect_measure: EffectMeasure | None = None
    effect_unit: str | None = None  # years per allele, parental doubled, ...
    effect_allele: str | None = None
    direction: Direction | None = None  # the effect allele's direction as the study reports it
    statistical_test: str | None = None

    @model_validator(mode="after")
    def _quote_in_note(self) -> Study:
        if not NOTE_KEY.match(self.note):
            raise ValueError(f"note is a note key (pmid-31413261 or doi-…); not {self.note!r}")
        if (self.quote is None) == (self.quote_absent is None):
            raise ValueError("a study has a quote, or a quote_absent saying why it has none; one of the two")
        if self.note.startswith("db-"):
            raise ValueError(f"a study is an article's analysis; {self.note} is a database release, cited from an axis or a flag")
        if self.quote is not None:
            _check_cites([f"{self.note}#{self.quote}"])
        if self.curator is not None and self.curator.strip().casefold() in PLACEHOLDER_CURATORS:
            raise ValueError(f"curator names who located the quote (a name or a model id), not {self.curator!r}")
        if self.effect_size is not None and self.effect_measure is None:
            raise ValueError("an effect_size says its effect_measure (beta, HR, OR)")
        if (self.stratum is None) != (self.stratum_level is None):
            raise ValueError("stratum and stratum_level are given both or neither")
        if self.age_min is not None and self.age_max is not None and self.age_min > self.age_max:
            raise ValueError(f"age_min {self.age_min} is above age_max {self.age_max}")
        if (self.age_min is not None or self.age_max is not None) and self.age_of is None:
            raise ValueError("an age band says whose age it is (age_of: participant or parent)")
        if self.n_cases is not None and self.sample_size is not None and self.n_cases > self.sample_size:
            raise ValueError(f"n_cases {self.n_cases} is above sample_size {self.sample_size}")
        return self

    @property
    def cite(self) -> str | None:
        return None if self.quote is None else f"{self.note}#{self.quote}"


FILE_UNSAFE = re.compile(r"[^A-Za-z0-9._-]+")


def row_file(locus_id: int, locus_name: str) -> str:
    """A row's file name: `<locus_id>-<locus_name>.yaml`, each run of characters outside [A-Za-z0-9._-] in the name
    made one `_` (a slash would be a directory, a space a quoting chore), and `<locus_id>.yaml` for an unnamed locus.
    The row itself keeps the seed's name exactly."""
    slug = FILE_UNSAFE.sub("_", locus_name).strip("_")
    return f"{locus_id}-{slug}.yaml" if slug else f"{locus_id}.yaml"


class Row(Strict):
    """One locus, in `rows/` under `row_file(locus_id, locus_name)`."""

    locus_id: int
    locus_name: str
    also_loci: list[int] = Field(default_factory=list)  # seed ids naming the same signal, folded in here (D14)
    verdict: Verdict
    verdict_reason: str
    axes: Axes
    flags: list[Flag] = Field(default_factory=list)
    variants: list[Variant]
    studies: list[Study] = Field(default_factory=list)

    @model_validator(mode="after")
    def _consistent(self) -> Row:
        if len(set(self.also_loci)) != len(self.also_loci):
            raise ValueError(f"also_loci names a locus twice: {self.also_loci}")
        lower = sorted(i for i in self.also_loci if i <= self.locus_id)
        if lower:
            raise ValueError(f"a signal's row is filed under its lowest seed id; {self.locus_id} folds in {', '.join(map(str, lower))}, so the row is theirs")
        rsids = {v.rsid for v in self.variants}
        orphans = sorted({s.rsid for s in self.studies} - rsids)
        if orphans:
            raise ValueError(f"studies name rsids the row's variants do not: {', '.join(orphans)}")
        if "tradeoff" in self.axes.pleiotropy.values:
            bare = [v.rsid for v in self.variants if not v.negatives]
            if bare:
                raise ValueError(f"a tradeoff locus says what the longer-life version may raise (negatives): {', '.join(bare)}")
        return self

    def cites(self) -> list[tuple[str, str]]:
        """Every (where, cite) in the row, in file order."""
        out: list[tuple[str, str]] = []
        for name in Axes.model_fields:
            out += [(f"axes.{name}", c) for c in getattr(self.axes, name).cites]
        for i, f in enumerate(self.flags):
            out += [(f"flags[{i}] {f.token}", c) for c in f.cites]
        out += [(f"studies[{i}] {s.rsid}", s.cite) for i, s in enumerate(self.studies) if s.cite is not None]
        return out


class Quote(Strict):
    qid: str
    text: str
    reading: date
    depth: Depth  # the reading's: a supplement quote is looked for in the cached supplements (RM4)


class NoteHead(Strict):
    """The front matter of `corpus/<key>.md`."""

    key: str = Field(pattern=NOTE_KEY.pattern)
    pmid: int | None = None
    doi: str | None = None
    title: str | None = None
    year: int | None = None
    title_checked: date | None = None  # the date the title was matched against PubMed (or the DOI's record)
    database: str | None = None  # a db- note: the database, as its key names it (opentargets, gnomad)
    release: str | None = None  # a db- note: the release read (26.09, 4.1)
    url: str | None = None  # a db- note: where the record was read
    accessed: date | None = None  # a db- note: the day it was read
    depth: Depth  # the deepest reading so far

    @property
    def is_database(self) -> bool:
        return self.key.startswith("db-")

    @model_validator(mode="after")
    def _key_matches(self) -> NoteHead:
        if self.is_database:
            return self._database_release()
        missing = [f for f in ("title", "year", "title_checked") if getattr(self, f) is None]
        if missing:
            raise ValueError(f"a note on an article gives {', '.join(missing)}")
        if self.depth is Depth.RECORD:
            raise ValueError("depth record is a database release's; an article is read as abstract, full_text or supplement")
        if self.pmid is not None and self.key != f"pmid-{self.pmid}":
            raise ValueError(f"key {self.key} does not name pmid {self.pmid}")
        if self.pmid is None:
            if self.doi is None:
                raise ValueError("a note names its pmid, or its doi for a preprint")
            if self.key != "doi-" + self.doi.replace("/", "_"):
                raise ValueError(f"key {self.key} does not name doi {self.doi}")
        if not 1900 <= self.year <= date.today().year + 1:
            raise ValueError(f"year {self.year} is not a publication year")
        return self

    def _database_release(self) -> NoteHead:
        given = [f for f in ("pmid", "doi", "title_checked") if getattr(self, f) is not None]
        if given:
            raise ValueError(f"a database release's note has no {', '.join(given)}: it is not an article")
        missing = [f for f in ("database", "release", "url", "accessed") if getattr(self, f) is None]
        if missing:
            raise ValueError(f"a database release's note gives {', '.join(missing)}")
        if self.key != f"db-{self.database}-{self.release}":
            raise ValueError(f"key {self.key} does not name database {self.database} release {self.release}")
        if self.depth is not Depth.RECORD:
            raise ValueError(f"a database release is read as a record, not {self.depth.value}")
        return self
