---
name: dossier-pdf
description: Build letter-size briefing PDFs in the Dossier theme (navy header, red rule, Times type, numbered sections, compact tables). Use when the user or another agent wants a research pack, briefing, cheat sheet, decision card, or audit-style PDF that should look like the Belicheck draft pack. Triggers include dossier, briefing pack, navy-red PDF, research pack, agent briefing, same theme as Belicheck.
metadata:
  type: workflow
  version: "1.1"
---

# Dossier PDF

Produce print-ready letter PDFs with one locked visual system. Domain content changes. Theme does not.

## Cover page (required)

Page 1 is the btommm/dossier cover. Full-bleed navy, confidentiality, short red rule, title, subtitle, prepared-for / prepared-by / date. Use cover_page_fn as onFirstPage. First story item is cover_break(). Body chrome starts on page 2.
