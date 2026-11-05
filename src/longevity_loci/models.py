"""The two research formats: a curated row (one per locus, `rows/`) and an evidence note (one per article,
`corpus/`). Field names and vocabularies are the requirements' own (docs/longevitymap_v2, §4.2 and §6), so the
module seat's export is a projection, never a translation. docs/FORMATS.md is the prose of this file."""

from __future__ import annotations

import re
from datetime import date
from enum import StrEnum

from pydantic import BaseModel, ConfigDict, Field, field_validator, model_validator

CITE = re.compile(r"^(?P<note>(?:pmid-\d+|doi-[A-Za-z0-9._;()\-]+))#(?P<quote>q\d+)$")
NOTE_KEY = re.compile(r"^(?:pmid-\d+|doi-[A-Za-z0-9._;()\-]+)$")


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


class StatSignificance(StrEnum):
    SIGNIFICANT = "significant"
    SUGGESTIVE = "suggestive"
    NOT_SIGNIFICANT = "not_significant"


class StudyDesign(StrEnum):
    PARENTAL_LIFESPAN_COX = "parental_lifespan_cox"
    OWN_SURVIVAL_COX = "own_survival_cox"
    PERCENTILE_CC_P90 = "percentile_case_control_p90"
    PERCENTILE_CC_P99 = "percentile_case_control_p99"
    CENTENARIAN_CC = "centenarian_case_control"
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
    """An outcome-profile cell. `untested` is never read as no effect (§4.2)."""

    PLUS = "+"
    ZERO = "0"
    MINUS = "-"
    UNTESTED = "untested"


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


class AgeAxis(Claim):
    value: AgeClass
    confidence: AgeConfidence


class OutcomeAxis(Claim):
    healthspan: Cell
    lifespan: Cell
    exceptional_survival: Cell


class ActionabilityAxis(Claim):
    label: Actionability
    what: list[str] = Field(default_factory=list)  # act_test:lpa, act_behaviour:smoking, ...
    who: str | None = None  # act_who:self | act_who:doctor


class ContextAxis(Claim):
    values: list[str] = Field(default_factory=list)  # sex_specific:<m|f>, age_dependent, eur_only_evidence, ...


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


class Genotype(Strict):
    """A §6.2 `variants.csv` row's per-genotype part."""

    genotype: str
    state: State
    conclusion: str


class Variant(Strict):
    rsid: str = Field(pattern=r"^rs\d+$")
    gene: str
    effect_allele: str | None = None
    direction: Direction
    genotypes: list[Genotype] = Field(default_factory=list)
    negatives: str | None = None


class Study(Strict):
    """A §6.3 `studies.csv` row; `quote` is its provenance_quote, cited from a note."""

    rsid: str = Field(pattern=r"^rs\d+$")
    note: str
    quote: str
    phenotype_class: PhenotypeClass
    study_design: StudyDesign
    population: str
    stat_significance: StatSignificance
    p_value: str | None = None
    effect_size: float | None = None
    effect_measure: EffectMeasure | None = None
    effect_allele: str | None = None
    statistical_test: str | None = None

    @model_validator(mode="after")
    def _quote_in_note(self) -> Study:
        if not NOTE_KEY.match(self.note):
            raise ValueError(f"note is a note key (pmid-31413261 or doi-…); not {self.note!r}")
        _check_cites([f"{self.note}#{self.quote}"])
        return self

    @property
    def cite(self) -> str:
        return f"{self.note}#{self.quote}"


class Row(Strict):
    """One locus, `rows/<locus_id>-<locus_name>.yaml`."""

    locus_id: int
    locus_name: str
    verdict: Verdict
    verdict_reason: str
    axes: Axes
    flags: list[Flag] = Field(default_factory=list)
    variants: list[Variant]
    studies: list[Study] = Field(default_factory=list)

    def cites(self) -> list[tuple[str, str]]:
        """Every (where, cite) in the row, in file order."""
        out: list[tuple[str, str]] = []
        for name in Axes.model_fields:
            out += [(f"axes.{name}", c) for c in getattr(self.axes, name).cites]
        for i, f in enumerate(self.flags):
            out += [(f"flags[{i}] {f.token}", c) for c in f.cites]
        out += [(f"studies[{i}] {s.rsid}", s.cite) for i, s in enumerate(self.studies)]
        return out


class Quote(Strict):
    qid: str
    text: str
    reading: date


class NoteHead(Strict):
    """The front matter of `corpus/<key>.md`."""

    key: str = Field(pattern=NOTE_KEY.pattern)
    pmid: int | None = None
    doi: str | None = None
    title: str
    year: int
    title_checked: date  # the date the title was matched against PubMed (or the DOI's record)
    depth: Depth  # the deepest reading so far

    @model_validator(mode="after")
    def _key_matches(self) -> NoteHead:
        if self.pmid is not None and self.key != f"pmid-{self.pmid}":
            raise ValueError(f"key {self.key} does not name pmid {self.pmid}")
        if self.pmid is None and self.doi is None:
            raise ValueError("a note names its pmid, or its doi for a preprint")
        return self
