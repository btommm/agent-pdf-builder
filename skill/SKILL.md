---
name: dossier-pdf
description: Build letter-size briefing PDFs in the Dossier theme (navy header, red rule, Times type, numbered sections, compact tables). Use when the user or another agent wants a research pack, briefing, cheat sheet, decision card, or audit-style PDF that should look like the Belicheck draft pack. Triggers include dossier, briefing pack, navy-red PDF, research pack, agent briefing, same theme as Belicheck.
metadata:
  type: workflow
  version: "1.1"
---

# Dossier PDF

Produce print-ready letter PDFs with one locked visual system. Domain content changes. Theme does not.

Use the bundled pdf skill for library choice (ReportLab Platypus). Use this skill for look, structure, and voice.

## Cover page (required)

Page 1 is the btommm/dossier cover. Full-bleed navy, confidentiality, short red rule, title, subtitle, prepared-for / prepared-by / date. Use cover_page_fn as onFirstPage. First story item is cover_break(). Body chrome starts on page 2.

## Page chrome (required on body pages)

Top bar is full-width navy 0.42in plus a 0.04in red rule under it.
Header left is OWNER · DOCUMENT KIND.
Header right is YEAR · CLASSIFICATION.
Footer left is the constraint line.
Footer right is Page N.

## Document skeleton

Always number sections. Drop unused sections. Do not leave a numbered hole.

1. How this pack is used
2. Context / settings
3. Strategy / decision
4. Primary table
5. Variance vs market
6. Tiers / groups
7. Targets and traps
8. Sequence / round plan / timeline
9. Contingency table
10. Bench / late / leftovers
11. News desk
12. Open questions

## Voice

Short sentences. No hype. No emoji. Cite source and date. Missing fact becomes a blank plus Open questions.

Do not put passwords, tokens, or 2FA in the PDF.
