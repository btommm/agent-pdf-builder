#!/usr/bin/env python3
"""Fixture proving title page + body chrome render."""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(Path(__file__).resolve().parent))
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, Spacer
from dossier_theme import (
    assemble, styles, section_rule,
    make_table, blank_field, checkbox,
)

OUT = ROOT / "artifacts" / "dossier_theme_fixture.pdf"


def main():
    OUT.parent.mkdir(parents=True, exist_ok=True)
    sty = styles()
    body = [
        Paragraph("1. How this pack is used", sty["H2"]),
        Paragraph(
            "This page exists so a new agent can see the header, footer, type, and table contract. "
            "The title page is required and is unnumbered.",
            sty["Body"],
        ),
        Paragraph("2. Sample table", sty["H2"]),
        make_table(
            ["Rank", "Item", "Note"],
            [["1", "Primary artifact", "Act on this first"],
             ["2", "Market price", "Not the same as rank"]],
            [0.7 * inch, 2.2 * inch, 4.3 * inch],
        ),
        Spacer(1, 8),
        blank_field("Unknown fact from source system"),
        checkbox("Confirm owner name before shipping."),
        section_rule(),
        Paragraph("Body pages use the navy header, red rule, and numbered footer.", sty["Small"]),
    ]
    assemble(
        str(OUT),
        owner="OWNER",
        kind="DOCUMENT KIND",
        year="2026",
        classification="INTERNAL",
        constraint="Draft only. Do not submit.",
        title="Dossier theme fixture",
        subtitle="Agents copy this chrome. Domain content replaces the table.",
        prepared_for="This league",
        prepared_by="OWNER",
        date="2026-09-01",
        author="dossier-pdf",
        body=body,
    )
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
