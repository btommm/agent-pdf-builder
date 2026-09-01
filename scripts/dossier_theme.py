#!/usr/bin/env python3
"""Dossier theme helpers for ReportLab Platypus."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, white
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, HRFlowable

NAVY = HexColor("#0B1F33")
NAVY2 = HexColor("#13293D")
STEEL = HexColor("#4A5560")
SILVER = HexColor("#C5C9CE")
RED = HexColor("#8B1E1E")
ROW_ALT = HexColor("#E8EDF1")
RULE = HexColor("#1C3348")
LINE = HexColor("#C9D2DA")

PAGE_W, PAGE_H = letter
CONTENT_W = PAGE_W - 1.3 * inch  # 7.2in


def styles():
    s = getSampleStyleSheet()
    s.add(ParagraphStyle(name="H1", fontName="Times-Bold", fontSize=16, leading=20,
                         textColor=NAVY, spaceAfter=6, spaceBefore=4))
    s.add(ParagraphStyle(name="H2", fontName="Times-Bold", fontSize=12, leading=16,
                         textColor=NAVY, spaceBefore=10, spaceAfter=4))
    s.add(ParagraphStyle(name="Body", fontName="Times-Roman", fontSize=9.5, leading=13,
                         textColor=NAVY2, spaceAfter=6))
    s.add(ParagraphStyle(name="Small", fontName="Times-Roman", fontSize=8, leading=11,
                         textColor=STEEL, spaceAfter=4))
    s.add(ParagraphStyle(name="Cell", fontName="Times-Roman", fontSize=8, leading=10.5,
                         textColor=NAVY2))
    s.add(ParagraphStyle(name="CellB", fontName="Times-Bold", fontSize=8, leading=10.5,
                         textColor=NAVY))
    s.add(ParagraphStyle(name="Callout", fontName="Times-Italic", fontSize=9, leading=12.5,
                         textColor=NAVY2, leftIndent=8, rightIndent=8, spaceAfter=8, spaceBefore=4))
    s.add(ParagraphStyle(name="Blank", fontName="Times-Roman", fontSize=9, leading=14,
                         textColor=STEEL, spaceAfter=2))
    return s


def header_footer_fn(owner, kind, year, classification, constraint):
    left = f"{owner}  ·  {kind}".upper()
    right = f"{year}  ·  {classification}".upper()

    def _draw(canvas, doc):
        canvas.saveState()
        canvas.setFillColor(NAVY)
        canvas.rect(0, PAGE_H - 0.42 * inch, PAGE_W, 0.42 * inch, fill=1, stroke=0)
        canvas.setFillColor(RED)
        canvas.rect(0, PAGE_H - 0.46 * inch, PAGE_W, 0.04 * inch, fill=1, stroke=0)
        canvas.setFillColor(white)
        canvas.setFont("Times-Bold", 9)
        canvas.drawString(0.65 * inch, PAGE_H - 0.28 * inch, left)
        canvas.setFont("Times-Roman", 8)
        canvas.drawRightString(PAGE_W - 0.65 * inch, PAGE_H - 0.28 * inch, right)
        canvas.setFillColor(NAVY)
        canvas.rect(0, 0, PAGE_W, 0.38 * inch, fill=1, stroke=0)
        canvas.setFillColor(SILVER)
        canvas.setFont("Times-Roman", 8)
        canvas.drawString(0.65 * inch, 0.16 * inch, constraint)
        canvas.drawRightString(PAGE_W - 0.65 * inch, 0.16 * inch, f"Page {doc.page}")
        canvas.restoreState()

    return _draw


def section_rule():
    return HRFlowable(width="100%", thickness=0.8, color=RULE, spaceAfter=8, spaceBefore=2)


def make_table(headers, rows, col_widths):
    sty = styles()
    th = ParagraphStyle("th", fontName="Times-Bold", fontSize=7.5, leading=10, textColor=white)
    data = [[Paragraph(str(h), th) for h in headers]]
    for r in rows:
        data.append([Paragraph(str(c), sty["Cell"]) for c in r])
    t = Table(data, colWidths=col_widths, repeatRows=1)
    cmds = [
        ("BACKGROUND", (0, 0), (-1, 0), NAVY),
        ("TEXTCOLOR", (0, 0), (-1, 0), white),
        ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("TOPPADDING", (0, 0), (-1, -1), 3.5),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
        ("LINEBELOW", (0, 0), (-1, 0), 0.5, RED),
        ("LINEBELOW", (0, 1), (-1, -1), 0.25, LINE),
    ]
    for i in range(1, len(data)):
        bg = ROW_ALT if i % 2 == 0 else white
        cmds.append(("BACKGROUND", (0, i), (-1, i), bg))
    t.setStyle(TableStyle(cmds))
    return t


def blank_field(label):
    return Paragraph(f"<b>{label}</b>  ______________________________________________", styles()["Blank"])


def checkbox(text):
    return Paragraph(f"☐  {text}", styles()["Body"])


def build_doc(path, title, author="Dossier"):
    return SimpleDocTemplate(
        path,
        pagesize=letter,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.62 * inch,
        bottomMargin=0.55 * inch,
        title=title,
        author=author,
    )
