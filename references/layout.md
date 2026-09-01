# Dossier layout API

Import from `scripts/dossier_theme.py` (copy next to the builder if the skill path is awkward).

## Functions

```python
from dossier_theme import (
    assemble, build_doc, styles, header_footer_fn, cover_page_fn, cover_break,
    section_rule, make_table, blank_field, checkbox,
)
```

### `assemble(path, *, owner, kind, year, classification, constraint, title, body, ...)`

Required entry point. Navy title page, then body. Cover is unnumbered. First body page is Page 1.

```python
assemble(
    "out.pdf",
    owner="BELICHECK",
    kind="DRAFT RESEARCH PACK",
    year="2026",
    classification="CONFIDENTIAL TO THIS LEAGUE",
    constraint="Do not submit picks. Research only.",
    title="2026 Draft Research Pack",
    subtitle="Board, prices, and week-one contingency.",
    prepared_for="This league",
    prepared_by="Belicheck",
    date="September 2026",
    body=story,
)
```

### `cover_page_fn(title, subtitle, prepared_for, prepared_by, date, confidentiality)`

Canvas callback for the cover. Full-bleed navy, short red rule, title, subtitle, meta footer. Used by `assemble`.

### `cover_break() -> PageBreak`

First story item when wiring cover by hand. Prefer `assemble`.

### `build_doc(path, title, author) -> SimpleDocTemplate`

Letter, dossier margins, PDF metadata title/author. Body-only unless you pass cover callbacks.

### `styles() -> StyleSheet`

Named styles — `H1`, `H2`, `Body`, `Small`, `Cell`, `CellB`, `Callout`, `Blank`.

### `header_footer_fn(owner, kind, year, classification, constraint, page_offset=0)`

Body chrome. Pass `page_offset=1` when a cover precedes the body so numbering starts at 1.

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
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph
from dossier_theme import assemble, styles, make_table, section_rule, blank_field, checkbox

sty = styles()
body = [
    Paragraph("1. How this pack is used", sty["H2"]),
    Paragraph("Body...", sty["Body"]),
    make_table(["A", "B"], [["1", "2"]], [3.6*inch, 3.6*inch]),
    blank_field("Unknown fact"),
    checkbox("Confirm source system."),
]
assemble(
    "/home/workdir/artifacts/example_2026-09-01.pdf",
    owner="OWNER", kind="KIND", year="2026",
    classification="INTERNAL", constraint="Draft only.",
    title="Example Dossier",
    subtitle="One-line subtitle with date and source.",
    prepared_for="Client", prepared_by="Agent", date="September 2026",
    body=body,
)
```

## Pagination rules

- Page 1 is always the title page. Do not put body flowables on it.
- Do not start a 100-row table on a page that already has a long intro. Page-break before the primary board.
- Chunk long boards (1–25, 26–50, 51–75, 76–100).
- After building, render page 1. It must be full navy. If body type shows through, the cover break is missing.

## HTML preview (optional)

`references/theme.css` can style an HTML mock. PDF output still goes through ReportLab. Do not ship the HTML as the deliverable unless the user asks.
