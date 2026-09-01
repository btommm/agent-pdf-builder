---
name: dossier-pdf
description: Build letter-size briefing PDFs in the Dossier theme (navy title page, navy header, red rule, Times type, numbered sections, compact tables). Use when the user or another agent wants a research pack, briefing, cheat sheet, decision card, or audit-style PDF that should look like the Belicheck draft pack. Triggers include dossier, briefing pack, navy-red PDF, research pack, agent briefing, same theme as Belicheck.
metadata:
  type: workflow
  version: "1.1"
---

# Dossier PDF

Produce print-ready letter PDFs with one locked visual system. Domain content changes. Theme does not.

Use the bundled `pdf` skill for library choice (ReportLab Platypus). Use this skill for look, structure, and voice.

## When to use

- Research packs, draft boards, weekly decision cards, audits, runbooks, strategy briefs
- User asks for the same theme as the fantasy pack, dossier, or briefing PDF
- Another agent needs a reusable template for its own topic

Do not use for forms, fillable IRS PDFs, slide decks, or marketing one-pagers.

## Theme tokens

Load exact values from `references/theme.css`. Do not invent new colors.

| Token | Hex | Role |
|---|---|---|
| navy | `#0B1F33` | Title page field, header/footer bars, table header, H1/H2 |
| navy-2 | `#13293D` | Body text |
| steel | `#4A5560` | Captions, blanks, page furniture |
| silver | `#C5C9CE` | Footer secondary text, cover subtitle |
| red | `#8B1E1E` | Cover accent rule; 3pt rule under header; table-header underline |
| row-alt | `#E8EDF1` | Even table rows |
| rule | `#1C3348` | Section hairline |
| line | `#C9D2DA` | Row rules |

Type is Times only (`Times-Roman`, `Times-Bold`, `Times-Italic`). No sans. No emoji. No icons.

Page is US Letter. Margins 0.65in left/right, 0.62in top, 0.55in bottom.

## Cover page (required)

Every dossier opens on a full-bleed navy cover matching `btommm/dossier`. No header bar. No footer bar. No page number.

- Top left: classification, 8pt Times-Bold
- Optical center: short red rule, 28pt Times-Bold title, optional subtitle
- Bottom: `PREPARED FOR` / `PREPARED BY` / `DATE`

Call `assemble(...)`. Do not start the story on a body page. If wiring by hand: `onFirstPage=cover_page_fn(...)`, first story item `cover_break()`, `onLaterPages=header_footer_fn(..., page_offset=1)`.

## Page chrome (required on every body page)

Top bar is full-width navy 0.42in plus a 0.04in red rule under it.

Header left is `OWNER  ·  DOCUMENT KIND` in 9pt Times-Bold white.

Header right is `YEAR  ·  CLASSIFICATION` in 8pt Times-Roman white.

Footer bar is full-width navy 0.38in.

Footer left is the constraint line (example `Do not submit picks. Research only.`).

Footer right is `Page N`. Cover does not count. First body page is Page 1.

## Document skeleton

Always number sections. Keep this order unless the domain skill overrides it.

0. Title page — required. Full-bleed navy cover with title, subtitle, prepared-for/by/date.
1. How this pack is used — one paragraph. Who writes it, what is in-bounds, what is forbidden.
2. Context / settings — facts from the source system. Blank lines if unknown. Never invent.
3. Strategy / decision — Plan A, Plan B, Do-not.
4. Primary table — the artifact the reader will act on (ranking, lineup, checklist).
5. Variance vs market — values and fades, or equivalent.
6. Tiers / groups
7. Targets and traps
8. Sequence / round plan / timeline
9. Contingency table
10. Bench / late / leftovers
11. News desk — dated sources
12. Open questions — checkboxes

Drop unused sections. Do not leave a numbered hole. Renumber. Never drop the title page.

## Voice

- Short sentences. No hype. No emoji.
- Rank is the author's board. Price/ADP/quote is the market. Show the spread.
- Cite source and date on every number that came from outside the source system.
- Missing fact becomes a blank line plus a flag in Open questions.

## Tables

- Header row navy, white Times-Bold 7.5–8pt, red 0.5pt rule under header.
- Body 8pt Times-Roman, navy-2. Alternate white / row-alt.
- Cell padding 5pt L/R, 3.5pt T/B. Valign middle. Repeat header on wrap.
- Wrap cell text in `Paragraph`. Never raw long strings.
- Split tables that would orphan fewer than 8 rows onto the next page. Prefer 25-row chunks for 100-row boards.

## Implementation

1. Copy or import `scripts/dossier_theme.py`.
2. Build body flowables (sections 1+). Do not put the title in the body.
3. Call `assemble(path, owner=..., kind=..., year=..., classification=..., constraint=..., title=..., subtitle=..., prepared_for=..., prepared_by=..., date=..., body=...)`.
4. Write to `/home/workdir/artifacts/<slug>_<YYYY-MM-DD>.pdf`.
5. Run `pdfinfo` and spot-check page 1 as the navy cover. Body chrome starts on page 2. Fix overflow before handing the file over.

Full API and copy-paste builder live in `references/layout.md`.

## Domain agents

A domain skill (fantasy GM, KOTH, training log) owns content rules. This skill owns look and pagination.

Domain skill must pass

- `owner` — short name on the header (example BELICHECK)
- `kind` — document kind (example DRAFT RESEARCH PACK)
- `constraint` — footer prohibition
- `title` / `subtitle` — cover title block
- `prepared_for` / `prepared_by` / `date` — cover footer
- `classification` — default internal / league / project label
- `sections` — ordered list of heading plus flowables

Do not put passwords, tokens, or 2FA in the PDF.
