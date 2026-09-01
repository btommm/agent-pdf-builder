# Dossier layout API

Import from `scripts/dossier_theme.py` (copy next to the builder if the skill path is awkward).

## Functions

```python
from dossier_theme import (
    build_doc, styles, header_footer_fn,
    section_rule, make_table, blank_field, checkbox,
)
```

### `build_doc(path, title, author) -> SimpleDocTemplate`

Letter, dossier margins, PDF metadata title/author.

### `styles() -> StyleSheet`

Named styles — `H1`, `H2`, `Body`, `Small`, `Cell`, `CellB`, `Callout`, `Blank`.

### `header_footer_fn(owner, kind, year, classification, constraint)`

Returns a callback for `onFirstPage` / `onLaterPages`.

```python
chrome = header_footer_fn(
    owner="BELICHECK",
    kind="DRAFT RESEARCH PACK",
    year="2026",
    classification="CONFIDENTIAL TO THIS LEAGUE",
    constraint="Do not submit picks. Research only.",
)
doc.build(story, onFirstPage=chrome, onLaterPages=chrome)
```

### `make_table(headers, rows, col_widths) -> Table`

`headers` and each row are lists of strings. Cells become Paragraphs.

Width budget on letter with 0.65in margins is **7.2in**. Sum of `col_widths` must equal that.

### `blank_field(label) -> Paragraph`

`Label  ________`

### `checkbox(text) -> Paragraph`

`☐  text`

### `section_rule() -> HRFlowable`

## Builder skeleton

```python
from reportlab.platypus import Paragraph, Spacer, PageBreak
from dossier_theme import *

OUT = "/home/workdir/artifacts/example_2026-09-01.pdf"
sty = styles()
doc = build_doc(OUT, title="Example Dossier", author="Agent")
chrome = header_footer_fn("OWNER", "KIND", "2026", "INTERNAL", "Draft only.")

story = []
story.append(Paragraph("Title line", sty["H1"]))
story.append(Paragraph("One-line subtitle with date and source.", sty["Small"]))
story.append(section_rule())
story.append(Paragraph("1. How this pack is used", sty["H2"]))
story.append(Paragraph("Body...", sty["Body"]))
story.append(make_table(["A", "B"], [["1", "2"]], [3.6*inch, 3.6*inch]))
story.append(blank_field("Unknown fact"))
story.append(checkbox("Confirm source system."))

doc.build(story, onFirstPage=chrome, onLaterPages=chrome)
```

## Pagination rules

- Do not start a 100-row table on a page that already has a long intro. Page-break before the primary board.
- Chunk long boards (1–25, 26–50, 51–75, 76–100).
- After building, `pdfinfo` + render page 1. If the header collides with H1, top margin is wrong.

## HTML preview (optional)

`references/theme.css` can style an HTML mock. PDF output still goes through ReportLab. Do not ship the HTML as the deliverable unless the user asks.
