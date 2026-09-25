#!/usr/bin/env python3
"""Merchandise / Sales Planning tailored resume for Juhi Bhalla. 1 page, ATS-safe."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor("#1F3A5F"); GREY = colors.HexColor("#3f3f3f"); LINE = colors.HexColor("#9fb0c3")
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_Merchandise_Planning.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19, textColor=NAVY, leading=22, spaceAfter=1)
title = ParagraphStyle("title", fontName="Helvetica", fontSize=9.4, textColor=GREY, leading=12.3, spaceAfter=3)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.7, textColor=GREY, leading=11)
sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=10.3, textColor=NAVY, leading=12, spaceBefore=4.5, spaceAfter=1.5)
body = ParagraphStyle("body", fontName="Helvetica", fontSize=8.9, textColor=colors.black, leading=11.1, alignment=TA_LEFT)
skillcell = ParagraphStyle("skillcell", fontName="Helvetica", fontSize=8.35, textColor=colors.black, leading=10.1)
role = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9.3, textColor=colors.black, leading=11.5)
comp = ParagraphStyle("comp", fontName="Helvetica-Bold", fontSize=9.1, textColor=NAVY, leading=11.5)
dt = ParagraphStyle("dt", fontName="Helvetica-Oblique", fontSize=8.4, textColor=GREY, leading=11)
bullet = ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.8, textColor=colors.black, leading=10.7,
                        leftIndent=9, bulletIndent=0, spaceAfter=1)

doc = SimpleDocTemplate(OUT, pagesize=A4, topMargin=9*mm, bottomMargin=7*mm, leftMargin=14*mm,
                        rightMargin=14*mm, title="Juhi Bhalla - Resume", author="Juhi Bhalla")
E = []
def rule(): return HRFlowable(width="100%", thickness=0.7, color=LINE, spaceBefore=1.5, spaceAfter=3)
def head(t): E.append(Paragraph(t, sec)); E.append(rule())
def job(company, date, rolename, bullets):
    row = Table([[Paragraph(company, comp), Paragraph(date, dt)]], colWidths=[120*mm, 62*mm])
    row.setStyle(TableStyle([("ALIGN",(1,0),(1,0),"RIGHT"),("VALIGN",(0,0),(-1,-1),"BOTTOM"),
                             ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                             ("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    blk = [row, Paragraph(rolename, role), Spacer(1,1)]
    for x in bullets: blk.append(Paragraph(f"&bull;&nbsp; {x}", bullet))
    E.append(KeepTogether(blk)); E.append(Spacer(1,2))

E.append(Paragraph("JUHI BHALLA", name))
E.append(Paragraph("Business Analyst&nbsp; &middot;&nbsp; Merchandise &amp; Sales Planning&nbsp; &middot;&nbsp; Assortment, Inventory &amp; Forecasting&nbsp; &middot;&nbsp; Category Revenue Planning &amp; 360&deg; Reporting", title))
E.append(Paragraph("Bengaluru, India (open to relocation)&nbsp; |&nbsp; Serving notice &mdash; available at short notice&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

head("Professional Summary")
E.append(Paragraph(
  "Business Analyst with 5+ years in retail and e-commerce category planning and analytics (Flipkart) and B2B SaaS "
  "(Enverus). I own category performance end to end &mdash; building demand and sales forecasts, planning assortment and "
  "inventory, and tracking revenue by segment (business unit, category, SKU) against plan while mitigating variances. I "
  "develop 360-degree reporting on portfolio health, run monthly planning cadences to realign the sales plan, coordinate "
  "cross-functional inputs, and align plans with stakeholders to timeline. Skilled in assortment health, in-stock / "
  "inventory analytics, pricing and promotion levers, and forecasting; proficient in SQL, Tableau, Power BI, and Advanced "
  "Excel. My data-driven planning drove a 55% category revenue uplift during Big Billion Days. VIT engineering graduate "
  "&mdash; currently serving notice and available at short notice.", body))

head("Skills &amp; Core Competencies")
def cell(h, items): return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("Sales &amp; Merchandise Planning",
       "Annual / Seasonal / Monthly (MOP) Sales Planning, Revenue Planning by Segment (Business Unit / Category / SKU / "
       "Attribute e.g. article, gender), Demand &amp; Sales Forecasting, Plan-vs-Actual &amp; Variance Mitigation, Planning "
       "Cadence &amp; Realignment"),
  cell("Assortment &amp; Inventory",
       "Assortment Health &amp; Planning, In-Stock / Inventory Analytics, Opening Inventory &amp; Inward Capacity (familiarity), "
       "Open-to-Buy / OTB (familiarity), Conversion Optimization, Pricing &amp; Markdown")],
 [cell("Reporting &amp; Analytics",
       "360&deg; Portfolio-Health Reporting, Dashboards &amp; Scorecards, KPI Standardization, Trend &amp; Variance Analysis, "
       "Root-Cause Analysis, Unit Economics"),
  cell("Tools",
       "SQL, Tableau, Microsoft Power BI, Advanced Excel (Pivots, Power Query), Google Sheets / Apps Script, "
       "Automated / AI-Assisted Reporting")],
 [cell("Stakeholder &amp; Coordination",
       "Cross-functional Coordination (Buying / Merchandising, Marketing, Supply Chain, Finance), Stakeholder Alignment "
       "to Timelines, Planning-Input Coordination, Team &amp; Project Coordination"),
  cell("Strategy &amp; Ways of Working",
       "Strategy Building &amp; Execution, Data-Driven Decision-Making, Structuring Ambiguous Problems, Ownership, "
       "Attention to Detail")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
                       ("RIGHTPADDING",(0,0),(0,-1),6),("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Large Appliances (Retail / eCommerce)", [
 "Own category sales and demand planning &mdash; build regression-based sales forecasts, plan assortment and inventory, and "
 "track revenue by segment (category, SKU) against plan, mitigating variances.",
 "Monitor assortment health and in-stock / inventory across key metrics and drive corrections (pricing, assortment, "
 "promotions) to maximize conversions.",
 "Develop 360-degree reporting and dashboards (SQL, Tableau / Power BI) on portfolio health; standardize KPIs and run "
 "monthly planning cadences to realign the sales plan.",
 "Coordinate cross-functional inputs and align plans with stakeholders to timeline; data-driven planning drove a 55% "
 "category revenue uplift during Big Billion Days.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Built dashboards and forecast inputs for commercial leadership; consolidated and validated planning inputs across "
 "global teams; supported ARR that scaled into the $500MM range.",
 "Re-engineered reporting with Lean Six Sigma (20% faster), standardizing KPIs and documentation.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence", [
 "Built financial / operational and unit-economics models and quantitative research to support planning and leadership "
 "decisions.",
])
job("Technology Risk Partners", "Feb 2021 &ndash; May 2021", "GRC Consultant &mdash; Intern", [
 "Built Oracle Cloud reporting components and automated control testing to support UAT and compliance.",
])
job("Sun Pharmaceutical Industries", "Jun 2020 &ndash; Jan 2021", "Intern &mdash; Research &amp; Data", [
 "Compiled and validated large multi-source datasets to support research and operations.",
])

head("Education")
E.append(Paragraph("<b>Vellore Institute of Technology (VIT)</b> &mdash; B.Tech (Engineering), Biotechnology, GPA 8.55 / 10 &nbsp;(2021)", body))
E.append(Paragraph("<b>Spring Dale College</b> &mdash; ISC (Class XII): 88% &nbsp;|&nbsp; ICSE (Class X): 88% &nbsp;(2014 / 2016)", body))

head("Impact &amp; Leadership")
for x in [
 "55% category revenue uplift at Flipkart through data-driven demand planning and assortment / promotion analysis.",
 "20% faster reporting at Enverus via Lean Six Sigma process improvement and automation.",
 "Directed operations, logistics, and teams for corporate / college events hosting 800&ndash;1,000+ participants.",
]:
    E.append(Paragraph(f"&bull;&nbsp; {x}", bullet))

doc.build(E)
print("built", OUT)
