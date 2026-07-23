#!/usr/bin/env python3
"""Generate a clean one-page CSF → OKR → KPI cascade template PDF."""

from reportlab.lib.pagesizes import letter
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
import os

# Output next to this script by default
OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "csf-okr-kpi-one-page-template.pdf")

# Colors
DARK = HexColor("#1a1a2e")
ACCENT = HexColor("#0f3460")
LIGHT_BG = HexColor("#f8f9fa")
BORDER = HexColor("#dee2e6")
CSF_COLOR = HexColor("#e94560")
OKR_COLOR = HexColor("#0f3460")
KPI_COLOR = HexColor("#16213e")
MUTED = HexColor("#6c757d")

def draw_rounded_rect(c, x, y, w, h, radius=6, fill_color=None, stroke_color=None, stroke_width=1):
    c.saveState()
    if fill_color:
        c.setFillColor(fill_color)
    if stroke_color:
        c.setStrokeColor(stroke_color)
        c.setLineWidth(stroke_width)
    p = c.beginPath()
    p.moveTo(x + radius, y)
    p.lineTo(x + w - radius, y)
    p.arcTo(x + w - 2*radius, y, x + w, y + 2*radius, -90, 90)
    p.lineTo(x + w, y + h - radius)
    p.arcTo(x + w - 2*radius, y + h - 2*radius, x + w, y + h, 0, 90)
    p.lineTo(x + radius, y + h)
    p.arcTo(x, y + h - 2*radius, x + 2*radius, y + h, 90, 90)
    p.lineTo(x, y + radius)
    p.arcTo(x, y, x + 2*radius, y + 2*radius, 180, 90)
    p.close()
    if fill_color and stroke_color:
        c.drawPath(p, fill=1, stroke=1)
    elif fill_color:
        c.drawPath(p, fill=1, stroke=0)
    else:
        c.drawPath(p, fill=0, stroke=1)
    c.restoreState()

def main():
    c = canvas.Canvas(OUTPUT, pagesize=letter)
    width, height = letter  # 612 x 792

    # Margins
    left = 0.5 * inch
    right = width - 0.5 * inch
    top = height - 0.4 * inch
    usable_width = right - left

    y = top

    # ===== HEADER =====
    c.setFillColor(DARK)
    c.rect(0, height - 0.85*inch, width, 0.85*inch, fill=1, stroke=0)

    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 16)
    c.drawString(left, height - 0.38*inch, "CSF  →  OKR  →  KPI")
    c.setFont("Helvetica", 9)
    c.drawString(left, height - 0.58*inch, "One-Page Cascade Template")
    c.setFont("Helvetica", 8)
    c.drawRightString(right, height - 0.38*inch, "Critical Success Factors  ·  Objectives & Key Results  ·  Key Performance Indicators")
    c.drawRightString(right, height - 0.55*inch, "Fill · Align · Focus")

    y = height - 1.05*inch

    # ===== CONTEXT LINE =====
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 8)
    c.drawString(left, y, "Context / Company / Team:")
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.6)
    c.line(left + 1.35*inch, y - 1, right - 1.8*inch, y - 1)
    c.drawString(right - 1.7*inch, y, "Period:")
    c.line(right - 1.35*inch, y - 1, right, y - 1)

    y -= 0.28*inch

    # ===== MENTAL MODEL BAR =====
    bar_h = 0.32*inch
    draw_rounded_rect(c, left, y - bar_h, usable_width, bar_h, radius=4, fill_color=LIGHT_BG, stroke_color=BORDER, stroke_width=0.5)
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 7.5)
    c.drawCentredString(width/2, y - 0.21*inch, "CSFs = What’s critical to succeed     ·     OKRs = The goals you set to achieve it     ·     KPIs = The metrics that show progress")
    y -= (bar_h + 0.18*inch)

    # ===== SECTION: CSFs =====
    section_header_h = 0.22*inch
    c.setFillColor(CSF_COLOR)
    c.roundRect(left, y - section_header_h, usable_width, section_header_h, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(left + 0.1*inch, y - 0.15*inch, "1. CRITICAL SUCCESS FACTORS  (Foundation — list 3–7 only)")
    y -= (section_header_h + 0.08*inch)

    # CSF boxes (5 slots)
    csf_box_h = 0.28*inch
    gap = 0.05*inch
    for i in range(1, 6):
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.7)
        c.setFillColor(white)
        c.roundRect(left, y - csf_box_h, usable_width, csf_box_h, 3, fill=1, stroke=1)
        c.setFillColor(CSF_COLOR)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(left + 0.08*inch, y - 0.19*inch, f"{i}.")
        c.setStrokeColor(HexColor("#f1f3f5"))
        c.setLineWidth(0.5)
        c.line(left + 0.28*inch, y - 0.22*inch, right - 0.1*inch, y - 0.22*inch)
        y -= (csf_box_h + gap)

    y -= 0.08*inch

    # ===== SECTION: OKRs =====
    c.setFillColor(OKR_COLOR)
    c.roundRect(left, y - section_header_h, usable_width, section_header_h, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(left + 0.1*inch, y - 0.15*inch, "2. OKRs  (this period — link each Objective to the CSF(s) it advances)")
    y -= (section_header_h + 0.08*inch)

    # Three OKR blocks
    okr_block_h = 1.05*inch
    for obj_num in range(1, 4):
        # Outer box
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.7)
        c.setFillColor(HexColor("#f8f9fc"))
        c.roundRect(left, y - okr_block_h, usable_width, okr_block_h, 4, fill=1, stroke=1)

        # Objective header line
        c.setFillColor(OKR_COLOR)
        c.setFont("Helvetica-Bold", 8)
        c.drawString(left + 0.1*inch, y - 0.16*inch, f"Objective {obj_num}")
        c.setFillColor(MUTED)
        c.setFont("Helvetica", 7)
        c.drawString(left + 0.85*inch, y - 0.16*inch, "(advances CSF #____ )")
        # underline for objective text
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.5)
        c.line(left + 2.2*inch, y - 0.18*inch, right - 0.1*inch, y - 0.18*inch)

        # Key Results
        kr_y = y - 0.38*inch
        for kr in range(1, 4):
            c.setFillColor(DARK)
            c.setFont("Helvetica", 7.5)
            c.drawString(left + 0.15*inch, kr_y, f"KR{kr}:")
            c.setStrokeColor(HexColor("#e9ecef"))
            c.line(left + 0.4*inch, kr_y - 1, right - 0.15*inch, kr_y - 1)
            kr_y -= 0.22*inch

        y -= (okr_block_h + 0.07*inch)

    y -= 0.05*inch

    # ===== SECTION: KPIs =====
    c.setFillColor(KPI_COLOR)
    c.roundRect(left, y - section_header_h, usable_width, section_header_h, 3, fill=1, stroke=0)
    c.setFillColor(white)
    c.setFont("Helvetica-Bold", 9)
    c.drawString(left + 0.1*inch, y - 0.15*inch, "3. KPIs  (ongoing health & progress — map each back to a CSF or OKR)")
    y -= (section_header_h + 0.06*inch)

    # Table header
    col_widths = [2.4*inch, 1.5*inch, 0.85*inch, 1.1*inch, 0.9*inch, 0.85*inch]
    headers = ["KPI", "Maps to (CSF / OKR)", "Current", "Target", "Owner", "Cadence"]
    row_h = 0.22*inch
    table_top = y

    # Header row
    c.setFillColor(HexColor("#e9ecef"))
    c.rect(left, y - row_h, usable_width, row_h, fill=1, stroke=0)
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.rect(left, y - row_h, usable_width, row_h, fill=0, stroke=1)

    x = left
    c.setFillColor(DARK)
    c.setFont("Helvetica-Bold", 7)
    for i, h in enumerate(headers):
        c.drawString(x + 0.05*inch, y - 0.15*inch, h)
        x += col_widths[i]
    y -= row_h

    # Data rows (4 blank)
    for r in range(4):
        c.setStrokeColor(BORDER)
        c.setLineWidth(0.4)
        c.setFillColor(white if r % 2 == 0 else HexColor("#fafbfc"))
        c.rect(left, y - row_h, usable_width, row_h, fill=1, stroke=1)
        # vertical lines
        x = left
        for w in col_widths[:-1]:
            x += w
            c.line(x, y, x, y - row_h)
        y -= row_h

    y -= 0.12*inch

    # ===== NON-PRIORITIES + CADENCE (two columns) =====
    col_w = (usable_width - 0.15*inch) / 2
    box_h = 0.85*inch

    # Non-priorities
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.7)
    c.setFillColor(HexColor("#fff8f8"))
    c.roundRect(left, y - box_h, col_w, box_h, 4, fill=1, stroke=1)
    c.setFillColor(CSF_COLOR)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(left + 0.1*inch, y - 0.18*inch, "Explicit Non-Priorities")
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 6.5)
    c.drawString(left + 0.1*inch, y - 0.32*inch, "(Things we will NOT focus on this period)")
    for i in range(3):
        c.setStrokeColor(HexColor("#f1f3f5"))
        c.line(left + 0.1*inch, y - 0.48*inch - i*0.14*inch, left + col_w - 0.1*inch, y - 0.48*inch - i*0.14*inch)

    # Review Cadence
    c.setStrokeColor(BORDER)
    c.setFillColor(HexColor("#f0f4f8"))
    c.roundRect(left + col_w + 0.15*inch, y - box_h, col_w, box_h, 4, fill=1, stroke=1)
    c.setFillColor(OKR_COLOR)
    c.setFont("Helvetica-Bold", 8)
    c.drawString(left + col_w + 0.25*inch, y - 0.18*inch, "Review Cadence")
    c.setFillColor(DARK)
    c.setFont("Helvetica", 7.5)
    items = [
        ("CSFs:", "Annual / when strategy shifts"),
        ("OKRs:", "Quarterly"),
        ("KPIs:", "Weekly / Monthly"),
    ]
    iy = y - 0.38*inch
    for label, default in items:
        c.setFont("Helvetica-Bold", 7.5)
        c.drawString(left + col_w + 0.25*inch, iy, label)
        c.setFont("Helvetica", 7)
        c.setFillColor(MUTED)
        c.drawString(left + col_w + 0.7*inch, iy, default)
        c.setFillColor(DARK)
        iy -= 0.16*inch

    y -= (box_h + 0.12*inch)

    # ===== FOOTER =====
    c.setStrokeColor(BORDER)
    c.setLineWidth(0.5)
    c.line(left, y, right, y)
    y -= 0.15*inch
    c.setFillColor(MUTED)
    c.setFont("Helvetica", 6.5)
    c.drawString(left, y, "Rule of thumb: Limit CSFs to 3–7. Every OKR must advance a CSF. Every KPI must map to an OKR or CSF. Growth without focus is just noise.")
    c.drawRightString(right, y, "csf-okr-kpi-framework skill")

    c.save()
    print(f"Created: {OUTPUT}")

if __name__ == "__main__":
    main()
