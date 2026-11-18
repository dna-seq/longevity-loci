"""Build the LongevityMap v1 -> v2 comparison deck (python-pptx), in just-dna-lite's look: its UI's white ground and the four colours of its helix logo.

Run: uv run --no-project --with python-pptx python -I scripts/longevitymap_deck.py LOGO.png OUT.pptx
LOGO is just-dna-lite's images/just_dna_seq.jpg (the helix on white). Numbers are written in as of 2026-11-18; update them from
rows/, module/ and the v1 audit (just-dna-lite docs/longevitymap_v2) before reusing.
"""

import sys
from pathlib import Path

from pptx import Presentation
from pptx.chart.data import CategoryChartData
from pptx.dml.color import RGBColor
from pptx.enum.chart import XL_CHART_TYPE, XL_LEGEND_POSITION, XL_LABEL_POSITION
from pptx.enum.shapes import MSO_SHAPE
from pptx.enum.text import PP_ALIGN, MSO_ANCHOR
from pptx.util import Emu, Pt

LOGO = Path(sys.argv[1])
OUT = Path(sys.argv[2])

# just-dna-lite's UI (lite.just-dna.life): white ground, slate text, and the four colours of the logo's
# protein-bank-style helix rendering (green, cyan, yellow, orange), the UI's green/teal/blue for accents.
BG = RGBColor(0xFF, 0xFF, 0xFF)
PANEL = RGBColor(0xF5, 0xF7, 0xFA)
LINE = RGBColor(0xE0, 0xE0, 0xE0)
WHITE = RGBColor(0x11, 0x18, 0x27)  # ink for titles and labels (the name kept from the dark draft)
TEXT = RGBColor(0x1F, 0x29, 0x33)
MUTED = RGBColor(0x4B, 0x55, 0x63)
GREEN = RGBColor(0x21, 0xBA, 0x45)   # helix green, the UI's green
TEAL = RGBColor(0x00, 0xB5, 0xAD)    # helix cyan, the UI's teal
YELLOW = RGBColor(0xD4, 0xB1, 0x06)  # helix yellow, darkened to read on white
ORANGE = RGBColor(0xE0, 0x7B, 0x00)  # helix orange
BLUE = RGBColor(0x21, 0x85, 0xD0)    # the UI's blue
LIME = TEAL
AMBER = YELLOW
RED = RGBColor(0xDB, 0x28, 0x28)     # the UI's red
FONT = "Arial"

prs = Presentation()
prs.slide_width, prs.slide_height = Emu(12192000), Emu(6858000)
W, H = prs.slide_width, prs.slide_height
BLANK = prs.slide_layouts[6]
IN = 914400


def inch(x: float) -> Emu:
    return Emu(int(x * IN))


def slide(title: str | None = None, kicker: str | None = None, logo: bool = True):
    s = prs.slides.add_slide(BLANK)
    s.background.fill.solid()
    s.background.fill.fore_color.rgb = BG
    if logo:
        s.shapes.add_picture(str(LOGO), W - inch(1.35), inch(0.3), inch(1.0), inch(0.66))
    if kicker:
        text(s, kicker.upper(), 0.6, 0.35, 10, 0.3, size=11, color=TEAL, bold=True)
    if title:
        text(s, title, 0.6, 0.62, 11.0, 0.9, size=28, color=WHITE, bold=True)
    return s


def text(s, body, x, y, w, h, size=16, color=TEXT, bold=False, align=PP_ALIGN.LEFT, anchor=MSO_ANCHOR.TOP):
    """body: a string, or a list of strings / (string, dict) runs-per-paragraph."""
    tb = s.shapes.add_textbox(inch(x), inch(y), inch(w), inch(h))
    tf = tb.text_frame
    tf.word_wrap = True
    tf.vertical_anchor = anchor
    tf.margin_left = tf.margin_right = Emu(0)
    paras = body if isinstance(body, list) else [body]
    for i, p in enumerate(paras):
        para = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
        para.alignment = align
        opts = {}
        if isinstance(p, tuple):
            p, opts = p
        para.space_after = Pt(opts.get("after", 6))
        run = para.add_run()
        run.text = p
        f = run.font
        f.name = FONT
        f.size = Pt(opts.get("size", size))
        f.bold = opts.get("bold", bold)
        f.color.rgb = opts.get("color", color)
    return tb


def box(s, x, y, w, h, fill=PANEL, line=None, shape=MSO_SHAPE.ROUNDED_RECTANGLE):
    b = s.shapes.add_shape(shape, inch(x), inch(y), inch(w), inch(h))
    b.fill.solid()
    b.fill.fore_color.rgb = fill
    if line is None:
        b.line.fill.background()
    else:
        b.line.color.rgb = line
        b.line.width = Pt(1.25)
    if shape == MSO_SHAPE.ROUNDED_RECTANGLE:
        b.adjustments[0] = 0.06
    b.shadow.inherit = False
    return b


def footer(s, note: str):
    text(s, note, 0.6, 7.0, 12.0, 0.35, size=10, color=MUTED)


def style_chart(chart, legend=False):
    chart.font.name = FONT
    chart.font.size = Pt(12)
    chart.font.color.rgb = TEXT
    chart.has_legend = legend
    if legend:
        chart.legend.position = XL_LEGEND_POSITION.TOP
        chart.legend.include_in_layout = False
        chart.legend.font.color.rgb = TEXT
    va = chart.value_axis
    va.visible = False
    va.has_major_gridlines = False
    ca = chart.category_axis
    ca.format.line.color.rgb = LINE
    ca.tick_labels.font.color.rgb = TEXT
    ca.tick_labels.font.size = Pt(13)


# ---------------------------------------------------------------- 1 title
s = slide(logo=False)
s.shapes.add_picture(str(LOGO), inch(8.3), inch(1.9), inch(4.5), inch(2.96))
text(s, "JUST-DNA-LITE · LONGEVITY MODULE", 0.7, 1.5, 7.5, 0.4, size=13, color=TEAL, bold=True)
text(s, "LongevityMap, re-curated from the evidence", 0.7, 1.95, 7.6, 2.0, size=40, color=WHITE, bold=True)
text(s, "From HAGR's 2017 database, through the module we shipped, to a version where every locus earns its place",
     0.7, 4.0, 7.4, 1.0, size=18, color=TEXT)
bar = box(s, 0.7, 5.25, 2.2, 0.05, fill=TEAL, shape=MSO_SHAPE.RECTANGLE)
box(s, 2.9, 5.25, 1.2, 0.05, fill=ORANGE, shape=MSO_SHAPE.RECTANGLE)
text(s, "Curated by a team of six Claude Code agents, steered by the maintainers · November 2026", 0.7, 5.45, 7.6, 0.8,
     size=14, color=MUTED)

# ---------------------------------------------------------------- 2 three generations, like against like
s = slide("Three generations of one idea", "What changed")
table_rows = [
    ("", "HAGR LongevityMap", "Module v1", "Module v2"),
    ("Release", "Build 3, frozen June 2017", "1.2.0 (shipped)", "2.0.0 (test registry)"),
    ("Variants (rsIDs)", "3,144", "528", "163"),
    ("Genes", "884", "272", "48 named"),
    ("Genotype rows", "—", "1,022", "489"),
    ("Papers cited by study rows", "—", "126, 1993–2015 (median 2009)", "51, mostly 2014–2026 GWAS"),
    ("What counts as evidence", "any reported “significant”", "as HAGR, plus 50 later entries", "tier A–D: genome-wide P, N, independent replication"),
    ("Genotype rows: protective / risk / neutral", "—", "975 / 47 / 0", "113 / 99 / 277"),
    ("Score", "none", "weight = SNP × genotype, summed", "none summed; tier and six axes shown apart"),
    ("Quotes located in a source", "—", "0", "6,765, checked by machine"),
]
heads = (None, MUTED, ORANGE, TEAL)
gt = s.shapes.add_table(len(table_rows), 4, inch(0.6), inch(1.65), inch(12.15), inch(4.9)).table
for j, wdt in enumerate((3.15, 2.9, 2.9, 3.2)):
    gt.columns[j].width = inch(wdt)
for i, r in enumerate(table_rows):
    for j, val in enumerate(r):
        c = gt.cell(i, j)
        c.fill.solid()
        c.fill.fore_color.rgb = BG if i == 0 else (PANEL if i % 2 else BG)
        c.margin_left = c.margin_right = inch(0.1)
        c.margin_top = c.margin_bottom = inch(0.04)
        c.vertical_anchor = MSO_ANCHOR.MIDDLE
        tf = c.text_frame
        tf.word_wrap = True
        p = tf.paragraphs[0]
        run = p.add_run()
        run.text = val
        f = run.font
        f.name = FONT
        if i == 0:
            f.size, f.bold = Pt(16), True
            f.color.rgb = heads[j] or WHITE
        else:
            f.size = Pt(13)
            f.bold = j == 0 or (j == 3)
            f.color.rgb = MUTED if j == 0 else (TEAL if j == 3 and val[:1].isdigit() else TEXT)
footer(s, "v2: the 2.0.0 build (164 loci; the sweep has since added 5). HAGR, v1: just-dna-lite manuscript v0.7 and its v1 audit.")

# ---------------------------------------------------------------- 3 what the audit found in v1
s = slide("Why v1 had to be rebuilt", "The audit of the shipped module")
facts = [
    ("280 of 516", "study-cited rsIDs rest on one 2012 classifier paper, whose 2010 predecessor was retracted", RED),
    ("35 of 528", "rsIDs have two or more independent significant studies", ORANGE),
    ("≈ 7 of ~150", "genome-wide longevity rsIDs present; LPA, CHRNA3/5, 9p21, ATXN2/SH2B3, LDLR absent", ORANGE),
    ("ρ = 0.16", "between a variant's weight and the strength of its evidence", AMBER),
    ("975 : 47", "protective to risk genotype rows, and no neutral one: a report reads mostly “good”", AMBER),
    ("0", "quotes located in a source; no effect allele, effect size or P on any of 671 study rows", MUTED),
]
for i, (big, small, c) in enumerate(facts):
    col, row = i % 2, i // 2
    x, y = 0.6 + col * 6.15, 1.75 + row * 1.6
    box(s, x, y, 5.9, 1.4)
    text(s, big, x + 0.25, y + 0.22, 2.1, 0.9, size=23, color=c, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    text(s, small, x + 2.35, y + 0.2, 3.35, 1.05, size=14, color=TEXT, anchor=MSO_ANCHOR.MIDDLE)
footer(s, "Source: just-dna-lite, docs/longevitymap_v2 (v1.2.0 measured 2026-11-03). v1 also carried 50 post-2017 additions and 876 edited records by its curator.")

# ---------------------------------------------------------------- 3b how many mistakes v1 carried
s = slide("462 of v1's 528 rsIDs carry at least one error", "Hand curation, audited")
cd = CategoryChartData()
errs = [("Weighted, though the cited result is not significant", 222), ("Direction inverted against a cited study", 124),
        ("Sex- or subgroup-only effect applied to everyone", 51), ("Weighted genotype cannot be called", 32),
        ("Genetic model differs from the study", 18), ("Cited evidence lost at the port", 6),
        ("rsID is not the variant studied", 4), ("Gene label wrong", 4), ("Citation error", 1)]
errs = list(reversed(errs))
cd.categories = [e for e, _ in errs]
cd.add_series("rsIDs", [n for _, n in errs])
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, inch(0.6), inch(1.65), inch(7.9), inch(5.05), cd)
ch = gf.chart
style_chart(ch)
ch.category_axis.tick_labels.font.size = Pt(11)
plot = ch.plots[0]
plot.gap_width = 35
plot.has_data_labels = True
plot.data_labels.font.color.rgb = WHITE
plot.data_labels.font.size = Pt(12)
plot.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
plot.series[0].format.fill.solid()
plot.series[0].format.fill.fore_color.rgb = RED
box(s, 8.85, 1.75, 3.9, 2.25)
text(s, [
    ("88 %", {"size": 40, "bold": True, "color": RED, "after": 2}),
    ("of v1's rsIDs: each counted once, under its most serious finding. 50 had no error; 16 could not be checked.", {"size": 13}),
], 9.1, 1.85, 3.5, 2.1)
box(s, 8.85, 4.15, 3.9, 2.55)
text(s, [
    ("Where they came in", {"size": 13, "bold": True, "color": TEAL, "after": 6}),
    ("Most inverted directions (127) were made in the hand curation of weights, not in HAGR. Most weights on non-significant results (182) came with HAGR's own records.", {"size": 12, "after": 6}),
    ("281 rows rest on one 2012 paper; 82 of those rows point the wrong way.", {"size": 12}),
], 9.1, 4.25, 3.5, 2.4)
footer(s, "Source: just-dna-lite manuscript v0.7, Table S14. 626 rows read against their papers by AI agents, a quote per verdict; provisional until a curator confirms.")

# ---------------------------------------------------------------- 3c and the agents' own mistakes
s = slide("Agents err too; the loop is built to catch it", "A fair comparison")
box(s, 0.6, 1.75, 5.9, 4.95, line=ORANGE)
text(s, "Hand curation (v1)", 0.95, 1.95, 5.2, 0.4, size=13, color=ORANGE, bold=True)
text(s, [
    ("● One curator's reading, with no second reader and no rule for what counts as evidence.", {"after": 10}),
    ("● No quote kept, so a weight cannot be traced to a sentence in the paper.", {"after": 10}),
    ("● The errors surfaced only when the module was audited, nine years after its source froze.", {}),
], 0.95, 2.45, 5.3, 4.1, size=15)
box(s, 6.8, 1.75, 5.95, 4.95, line=TEAL)
text(s, "Agent curation (v2)", 7.15, 1.95, 5.2, 0.4, size=13, color=TEAL, bold=True)
text(s, [
    ("● Every claim quotes its source; 6,765 quotes found word for word by machine, none failed.", {"after": 10}),
    ("● Every batch of ~10 rows gets three independent adversarial reads. 17 reads settled 119 numbered rulings, many of them the curator's or the lead's own mistakes, corrected the same day.", {"after": 10}),
    ("● Not yet measured the same way: v2 has not had an independent audit by v1's method. Until it has, the fair claim is that its errors are findable and get fixed, not that it has none.", {"color": MUTED}),
], 7.15, 2.45, 5.35, 4.1, size=14)
footer(s, "v2 figures: longevity-loci docs/DECISIONS.md and the quote check of 2026-11-18.")

# ---------------------------------------------------------------- 4 the v2 design
s = slide("v2: only genome-wide, replicated signals score", "The design")
rules = [
    ("Evidence tier", "A: P < 5×10⁻⁸, N ≥ 100,000, independent replication, no red flag. B: one shortfall. C: suggestive. D: contradicted."),
    ("One signal, one row", "APOE scored once, as its ε2/ε3/ε4 pair (12 results), not through five proxies counted as five findings."),
    ("Seven axes, never summed", "Tier, mechanism, pleiotropy, age of action, outcome profile, actionability, ancestry and sex."),
    ("Every genotype has a row", "The common genotype is the neutral reference; the others protective or risk relative to it."),
    ("Receipts", "Each claim cites a passage quoted word for word from its source, checked by machine."),
    ("Negative evidence kept", "A locus that failed a powered test stays visible at tier D, with the study that contradicted it."),
]
for i, (h, b) in enumerate(rules):
    col, row = i % 2, i // 2
    x, y = 0.6 + col * 6.15, 1.75 + row * 1.6
    box(s, x, y, 5.9, 1.4)
    box(s, x, y, 0.08, 1.4, fill=TEAL, shape=MSO_SHAPE.RECTANGLE)
    text(s, h, x + 0.35, y + 0.15, 5.3, 0.4, size=17, color=WHITE, bold=True)
    text(s, b, x + 0.35, y + 0.55, 5.3, 0.85, size=13, color=TEXT)
footer(s, "The design: docs/longevitymap_v2 in just-dna-lite, moved into longevity-loci unchanged. The rule texts: longevity-loci docs/DECISIONS.md.")

# ---------------------------------------------------------------- 5 tiers
s = slide("Only 15 of 169 loci reach tier A", "What the evidence says")
cd = CategoryChartData()
cd.categories = ["A  genome-wide, replicated", "B  one shortfall", "C  suggestive", "D  contradicted"]
cd.add_series("Loci", (15, 75, 43, 36))
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, inch(0.6), inch(1.7), inch(7.6), inch(5.0), cd)
ch = gf.chart
style_chart(ch)
plot = ch.plots[0]
plot.gap_width = 55
plot.has_data_labels = True
dl = plot.data_labels
dl.font.size = Pt(18)
dl.font.bold = True
dl.font.color.rgb = WHITE
dl.position = XL_LABEL_POSITION.OUTSIDE_END
for pt, c in zip(plot.series[0].points, (GREEN, LIME, AMBER, RED)):
    pt.format.fill.solid()
    pt.format.fill.fore_color.rgb = c
text(s, [
    ("Most loci are genome-wide but miss one test, usually an independent replication.", {"after": 14}),
    ("36 are contradicted: their discovery failed a powered test in its own ancestry, or its authors called it anomalous.", {"after": 14}),
    ("Seed tiers did not always hold. The first pilot row, ZW10/TTC12, fell from A to B; CELSR2/SORT1 and CHRNA3/5 fell from A after an independent sample failed them.", {"after": 14}),
    ("A tier grades the evidence for an association. It is not an effect size, and not a prediction for one person.", {"color": MUTED, "size": 14}),
], 8.6, 1.9, 4.2, 5.0, size=15)
footer(s, "Rows 170–174 (the 2015–2026 literature sweep) are included and not yet through their adversarial read.")

# ---------------------------------------------------------------- 6 genotype balance
s = slide("Reports no longer read “mostly good”", "Genotype rows, v1 against v2")
cd = CategoryChartData()
cd.categories = ["Module v1", "Module v2"]
cd.add_series("Protective", (975, 113))
cd.add_series("Risk", (47, 99))
cd.add_series("Neutral reference", (0, 277))
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_STACKED, inch(0.6), inch(1.8), inch(8.0), inch(3.6), cd)
ch = gf.chart
style_chart(ch, legend=True)
plot = ch.plots[0]
plot.gap_width = 45
plot.has_data_labels = True
plot.data_labels.font.color.rgb = BG
plot.data_labels.font.bold = True
plot.data_labels.font.size = Pt(13)
for ser, c in zip(plot.series, (TEAL, ORANGE, MUTED)):
    ser.format.fill.solid()
    ser.format.fill.fore_color.rgb = c
text(s, [
    ("v1: 1,022 genotype rows, 95 % protective, none neutral. Its weights were summed into a “net weight” with no reference distribution.", {"after": 12}),
    ("v2: 489 genotype rows. The most common genotype is the neutral reference; protective and risk are stated relative to it, and no score is summed.", {}),
], 8.9, 1.9, 3.9, 4.6, size=15)
text(s, "v2 has fewer rows because it keeps one lead per signal and drops what the evidence does not carry, not because it covers less of the field: the genome-wide loci v1 lacked are all in.",
     0.6, 5.65, 8.0, 1.0, size=14, color=MUTED)

# ---------------------------------------------------------------- 7 FOXO3
s = slide("One locus, two readings: FOXO3 rs2802292", "Worked example")
box(s, 0.6, 1.75, 5.9, 4.95, line=ORANGE)
text(s, "Module v1", 0.95, 1.95, 5.2, 0.4, size=13, color=ORANGE, bold=True)
text(s, [
    ("Priority 0.95: among the module's strongest.", {"bold": True, "color": WHITE, "size": 18, "after": 12}),
    ("Five linked studies: Japanese-American, Southern Italian, Han Chinese and Danish candidate-gene samples.", {"after": 10}),
    ("G/T heterozygote → weight 0.475, shown as protective.", {"after": 10}),
    ("The studies do not name the associated allele at rs2802292; the direction is the curators' reading.", {"color": MUTED}),
], 0.95, 2.4, 5.3, 4.2, size=15)
box(s, 6.8, 1.75, 5.95, 4.95, line=TEAL)
text(s, "Module v2", 7.15, 1.95, 5.2, 0.4, size=13, color=TEAL, bold=True)
text(s, [
    ("Tier B: real, replicated, but never genome-wide on its own.", {"bold": True, "color": WHITE, "size": 18, "after": 12}),
    ("The only genome-wide result at the locus is a multivariate test (healthspan, parental lifespan, 90th-percentile longevity, P 1×10⁻⁸ at rs1159806); its authors say no input is genome-wide alone.", {"after": 10}),
    ("rs2802292 tags that signal (r² 0.40) from outside its credible set. G travels with the longer-life allele.", {"after": 10}),
    ("Replicated in AncestryDNA parents, who share no one with UK Biobank: same allele, same direction, P 1.1×10⁻⁴.", {}),
], 7.15, 2.4, 5.35, 4.2, size=14)
footer(s, "v1: just-dna-lite manuscript v0.7, §3.1 and Figure 1b. v2: longevity-loci rows/43-FOXO3.yaml.")

# ---------------------------------------------------------------- 8 mechanism
s = slide("What the loci act through", "Mechanism, the second axis")
cd = CategoryChartData()
mech = [("No single system shown (general ageing)", 111), ("Heart and vessels", 17), ("Metabolism", 9),
        ("Smoking and lungs", 4), ("Immune and inflammation", 4), ("Skin and sun", 3), ("Brain and memory", 1),
        ("Legacy candidate gene", 1)]
mech = list(reversed(mech))
cd.categories = [m for m, _ in mech]
cd.add_series("Loci", [n for _, n in mech])
gf = s.shapes.add_chart(XL_CHART_TYPE.BAR_CLUSTERED, inch(0.6), inch(1.7), inch(7.8), inch(5.0), cd)
ch = gf.chart
style_chart(ch)
ch.category_axis.tick_labels.font.size = Pt(12)
plot = ch.plots[0]
plot.gap_width = 40
plot.has_data_labels = True
plot.data_labels.font.color.rgb = WHITE
plot.data_labels.font.size = Pt(12)
plot.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
plot.series[0].format.fill.solid()
plot.series[0].format.fill.fore_color.rgb = BLUE
text(s, [
    ("19 more rows are biological-ageing markers (telomere length, epigenetic clocks, brain age, loss of Y). They are shown and scored by nothing: a marker is not lifespan.", {"after": 14}),
    ("v1 sorted variants into 11 pathway categories, 47 % of rows in “other”. v2 names the system a locus acts through, and allows no “other”.", {"after": 14}),
    ("Most genome-wide longevity loci still have no system the evidence shows. That is said, not guessed.", {"color": MUTED}),
], 8.8, 1.9, 4.0, 5.0, size=15)

# ---------------------------------------------------------------- 9 the agent loop
s = slide("How a row is made: an agent loop", "The curation process")
steps = [
    ("Find", "scout", "Sweeps the literature track by track and queues each paper that bears on a locus."),
    ("Read", "curator", "Reads the articles at the depth a claim needs: abstract, full text, supplements, summary statistics, database releases."),
    ("Write", "curator", "One YAML row per locus, one evidence note per source; every axis value cites quote ids."),
    ("Check", "code", "Tier gates and required fields; every quote found verbatim in the cached source, or reported unknown, never passed."),
    ("Challenge", "lead", "Three independent adversarial reads of each batch of ~10 rows; each finding settled as a numbered decision."),
    ("Build", "module", "Exports to just-dna-format 0.8, compiles strict, rehearses on the registry's test instance."),
]
for i, (h, who, b) in enumerate(steps):
    x = 0.6 + i * 2.07
    box(s, x, 1.85, 1.9, 4.1, line=TEAL if h == "Challenge" else None)
    circ = box(s, x + 0.65, 2.05, 0.6, 0.6, fill=TEAL if h != "Challenge" else ORANGE, shape=MSO_SHAPE.OVAL)
    text(s, str(i + 1), x + 0.65, 2.1, 0.6, 0.5, size=18, color=BG, bold=True, align=PP_ALIGN.CENTER)
    text(s, h, x + 0.1, 2.85, 1.7, 0.4, size=17, color=WHITE, bold=True, align=PP_ALIGN.CENTER)
    text(s, who, x + 0.1, 3.25, 1.7, 0.3, size=11, color=TEAL, align=PP_ALIGN.CENTER)
    text(s, b, x + 0.15, 3.65, 1.6, 2.3, size=11, color=TEXT)
    if i < 5:
        arr = s.shapes.add_shape(MSO_SHAPE.RIGHT_ARROW, inch(x + 1.92), inch(2.25), inch(0.14), inch(0.2))
        arr.fill.solid()
        arr.fill.fore_color.rgb = MUTED
        arr.line.fill.background()
box(s, 0.6, 6.15, 12.15, 0.65, fill=PANEL)
text(s, "The maintainers set direction and settle the forks with a real cost either way (APOE scored per ε pair, markers unscored, when to publish), by chat and a question desk. The seats decide the rest, and record each call with the alternative they rejected.",
     0.85, 6.2, 11.7, 0.6, size=12, color=TEXT, anchor=MSO_ANCHOR.MIDDLE)

# ---------------------------------------------------------------- 10 the team
s = slide("Six seats, each a standing Claude Code session", "The team")
seats = [
    ("lead", "Builds the code the others run (formats, checks, fetchers, export), runs the adversarial reads, keeps the plan, reports."),
    ("curator", "Re-reads each locus against its articles and writes its row and notes."),
    ("scout", "Sweeps the literature since 2015 and queues new papers and second signals."),
    ("module", "Builds the annotation module from the rows; rehearses each version on the test registry."),
    ("runner", "Runs bulk fetches as batch jobs on the cluster and logs them."),
    ("liaison", "Tracks the upstream tools (module creator, compiler, format, registry) and files their defects there."),
]
for i, (n, b) in enumerate(seats):
    col, row = i % 2, i // 2
    x, y = 0.6 + col * 6.15, 1.75 + row * 1.25
    box(s, x, y, 5.9, 1.05)
    text(s, n, x + 0.3, y + 0.15, 1.5, 0.75, size=18, color=TEAL, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    text(s, b, x + 1.75, y + 0.12, 3.95, 0.85, size=13, color=TEXT, anchor=MSO_ANCHOR.MIDDLE)
text(s, "They talk in the team chat, hand work over in writing, and commit everything they decide to the repository, so any seat can be picked up by a fresh session from its notes.",
     0.6, 5.65, 12.0, 0.8, size=14, color=MUTED)

# ---------------------------------------------------------------- 11 pace and checks
s = slide("169 rows in nine days, every quote checked", "In numbers")
cd = CategoryChartData()
days = [("10 Nov", 6), ("11 Nov", 47), ("12 Nov", 19), ("13 Nov", 13), ("14 Nov", 13), ("15 Nov", 22), ("16 Nov", 44), ("18 Nov", 5)]
cd.categories = [d for d, _ in days]
cd.add_series("Rows added", [n for _, n in days])
gf = s.shapes.add_chart(XL_CHART_TYPE.COLUMN_CLUSTERED, inch(0.6), inch(1.75), inch(6.6), inch(4.3), cd)
ch = gf.chart
style_chart(ch)
ch.category_axis.tick_labels.font.size = Pt(11)
plot = ch.plots[0]
plot.gap_width = 50
plot.has_data_labels = True
plot.data_labels.font.color.rgb = WHITE
plot.data_labels.position = XL_LABEL_POSITION.OUTSIDE_END
plot.series[0].format.fill.solid()
plot.series[0].format.fill.fore_color.rgb = TEAL
text(s, "Rows added per day. 18 Nov: the first rows from the 2015–2026 literature sweep.", 0.6, 6.15, 6.6, 0.5, size=11, color=MUTED)
nums = [
    ("6,765", "quotes found word for word in their source; none failed"),
    ("140", "evidence notes: 131 articles, 2 preprints, 7 database releases"),
    ("17", "adversarial batch reads; decisions D1–D42, each with the option it rejected"),
    ("22,759", "records screened in the 2015–2026 sweep → 47 uncited papers on 18 rows, 5 new rows"),
]
for i, (big, small) in enumerate(nums):
    y = 1.75 + i * 1.12
    box(s, 7.5, y, 5.25, 1.0)
    text(s, big, 7.75, y + 0.12, 1.9, 0.75, size=24, color=TEAL, bold=True, anchor=MSO_ANCHOR.MIDDLE)
    text(s, small, 9.6, y + 0.1, 3.0, 0.8, size=12, color=TEXT, anchor=MSO_ANCHOR.MIDDLE)
footer(s, "Over 1,150 commits since 4 Nov 2026. Article texts are cached outside git; the public repository keeps citations, short quotes and verdicts only.")

# ---------------------------------------------------------------- 12 status
s = slide("Where it stands, and its limits", "Status")
box(s, 0.6, 1.75, 5.9, 4.9)
text(s, "Status", 0.9, 1.95, 5.3, 0.4, size=13, color=TEAL, bold=True)
text(s, [
    ("● Curation of all 161 seed loci done; second signals and the literature sweep added rows 162–174.", {"after": 10}),
    ("● The module compiles strict on just-dna-format 0.8 (489 genotype rows, 679 studies).", {"after": 10}),
    ("● On the registry's test instance only, as 2.0.0. Production waits on the maintainers' word.", {"after": 10}),
    ("● Next: the sweep's rows through their adversarial read, a rebuild, then publication.", {}),
], 0.9, 2.45, 5.3, 4.1, size=15)
box(s, 6.8, 1.75, 5.95, 4.9)
text(s, "Limits", 7.1, 1.95, 5.3, 0.4, size=13, color=ORANGE, bold=True)
text(s, [
    ("● Agents did the reading. Quotes are checked by machine; whether a P value replicates a hit is a judgement, and the adversarial reads will not have caught every mistake.", {"after": 10}),
    ("● The evidence is mostly European. Ancestry is recorded per study, and a European-only row says so.", {"after": 10}),
    ("● A tier grades an association, not a cause, and not a person's lifespan.", {}),
], 7.1, 2.45, 5.35, 4.1, size=15)
footer(s, "github.com/dna-seq/longevity-loci · just-dna-lite: github.com/dna-seq/just-dna-lite · lite.just-dna.life")

prs.save(OUT)
print("wrote", OUT, len(prs.slides), "slides")
