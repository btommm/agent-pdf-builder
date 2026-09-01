# agent-pdf-builder

Locked visual system for agent-written briefing PDFs.

Navy title page, navy header, red rule, Times type, numbered sections, compact tables. Domain content changes. Theme does not.

Live copy of the Grok `dossier-pdf` skill.

## Repo map

```
skill/SKILL.md              Agent instructions
scripts/dossier_theme.py    ReportLab helpers (assemble + chrome)
scripts/example_dossier.py  Title page + body fixture
references/theme.css        Same tokens for HTML mocks
references/layout.md        API
```

## Install

```bash
pip install reportlab
python scripts/example_dossier.py
```

Writes `artifacts/dossier_theme_fixture.pdf` (cover, then one body page).

## Agent contract

Every PDF starts with a full-bleed navy title page. Then numbered body sections. Call `assemble(...)` so the cover cannot be skipped.

```python
from dossier_theme import assemble, styles

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

Cover is unnumbered. First body page is Page 1. Default palette is in `references/theme.css`. Do not invent colors.

## License

MIT
