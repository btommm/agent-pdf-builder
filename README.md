# agent-pdf-builder

Locked visual system for agent-written briefing PDFs.

Navy header, red rule, Times type, numbered sections, compact tables. Domain content changes. Theme does not.

Live copy of the Grok `dossier-pdf` skill.

## Repo map

```
skill/SKILL.md              Agent instructions
scripts/dossier_theme.py    ReportLab helpers
scripts/example_dossier.py  One-page fixture
references/theme.css        Same tokens for HTML mocks
references/layout.md        API
```

## Install

```bash
pip install reportlab
python scripts/example_dossier.py
```

Writes `artifacts/dossier_theme_fixture.pdf`.

## Agent contract

Pass `owner`, `kind`, `year`, `classification`, `constraint`. Fill numbered sections. Cite source and date. Leave unknowns blank.

```python
from dossier_theme import build_doc, styles, header_footer_fn, make_table, section_rule

chrome = header_footer_fn(
    "BELICHECK",
    "DRAFT RESEARCH PACK",
    "2026",
    "CONFIDENTIAL TO THIS LEAGUE",
    "Do not submit picks. Research only.",
)
```

Default palette is in `references/theme.css`. Do not invent colors.

## License

MIT
