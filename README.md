# CSF / OKR / KPI Framework — Grok Skill

A reusable Grok skill that teaches the integrated use of **Critical Success Factors (CSFs)**, **OKRs**, and **KPIs** for focused strategy and execution.

Based on the practical hierarchy popularized by leaders like Eric Partaker:

> CSFs = What’s critical to succeed  
> OKRs = The goals you set to achieve it  
> KPIs = The metrics that show progress

## What’s inside

| Path | Description |
|------|-------------|
| `SKILL.md` | Core skill instructions (hierarchy, rules, best practices, examples, application steps) |
| `references/diagnostics.md` | Diagnostic questions, failure modes, red flags, interventions |
| `references/examples-and-templates.md` | Extra industry examples + cascade structures |
| `assets/cascade-template.md` | Editable markdown one-pager |
| `assets/generate_one_page_template.py` | Python script (reportlab) that produces a polished printable PDF template |

## How to use with Grok

1. Place the skill folder in your Grok skills directory (or reference this repo).
2. Grok will automatically load it when conversations mention OKRs, KPIs, CSFs, strategy alignment, goal frameworks, etc.
3. Ask things like:
   - “Help me define CSFs, OKRs and KPIs for my Series B SaaS”
   - “Review this set of OKRs — are the CSFs missing?”
   - “Give me a full cascade for client retention”
   - “Print the one-page template”

## Generate the PDF template

```bash
cd assets
pip install reportlab   # if needed
python generate_one_page_template.py
```

This creates `csf-okr-kpi-one-page-template.pdf` — a clean single-page form with sections for CSFs, OKRs, KPIs, non-priorities, and review cadence.

## License

Feel free to use, adapt, and share.
