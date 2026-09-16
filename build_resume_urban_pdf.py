#!/usr/bin/env python3
"""Urban Company Category/City Ops (SCM) - tailored resume for Juhi Bhalla. ATS-safe, 1 page."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor("#1F3A5F"); GREY = colors.HexColor("#3f3f3f"); LINE = colors.HexColor("#9fb0c3")
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_UrbanCompany.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19, textColor=NAVY, leading=22, spaceAfter=1)
title = ParagraphStyle("title", fontName="Helvetica", fontSize=9.6, textColor=GREY, leading=12.5, spaceAfter=3)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.8, textColor=GREY, leading=11)
sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=10.3, textColor=NAVY, leading=12, spaceBefore=4.5, spaceAfter=1.5)
body = ParagraphStyle("body", fontName="Helvetica", fontSize=8.9, textColor=colors.black, leading=11.1, alignment=TA_LEFT)
skillcell = ParagraphStyle("skillcell", fontName="Helvetica", fontSize=8.4, textColor=colors.black, leading=10.2)
role = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9.3, textColor=colors.black, leading=11.5)
comp = ParagraphStyle("comp", fontName="Helvetica-Bold", fontSize=9.1, textColor=NAVY, leading=11.5)
dt = ParagraphStyle("dt", fontName="Helvetica-Oblique", fontSize=8.4, textColor=GREY, leading=11)
bullet = ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.8, textColor=colors.black, leading=10.8,
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
E.append(Paragraph("Category Operations &amp; Growth&nbsp; &middot;&nbsp; Operational Excellence &amp; Process Improvement&nbsp; &middot;&nbsp; Cross-functional Execution &amp; Ownership", title))
E.append(Paragraph("Bengaluru, India&nbsp; |&nbsp; Serving notice &mdash; available to join at short notice&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

head("Professional Summary")
E.append(Paragraph(
  "Analytics-driven operations professional with 5+ years owning category performance and operational excellence in "
  "high-scale e-commerce (Flipkart) and global SaaS (Enverus). At Flipkart I own a marketplace category end to end &mdash; "
  "tracking seller / partner and SKU performance, pulling growth levers (pricing, assortment, promotions), and driving a "
  "55% category revenue uplift during Big Billion Days under intense timelines. I re-engineer operations for excellence "
  "(Lean Six Sigma, 20% faster) and execute across cross-functional teams (category, marketing, supply chain, product). "
  "A VIT engineering graduate with a high-ownership, intrapreneurial mindset and proven project and event-operations "
  "leadership (directing operations and teams for 1,000+ participants), I thrive on scaling volumes and revenue across "
  "geographies while keeping customer and partner experience superlative. Currently serving notice &mdash; available at "
  "short notice.", body))

head("Skills &amp; Core Competencies")
def cell(h, items): return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("Category Operations &amp; Growth",
       "Category Performance Ownership, Volume &amp; Revenue Scaling, Growth Levers (Pricing, Assortment, Promotions), "
       "Selection &amp; Assortment, Demand Forecasting &amp; Planning, Multi-city / Geography Ops (familiarity)"),
  cell("Operational Excellence &amp; Process",
       "Operational Excellence, Lean Six Sigma, Process Re-engineering &amp; SOPs, Quality &amp; Service Improvement, "
       "Root-Cause Analysis, Continuous Improvement")],
 [cell("Partner &amp; Stakeholder Management",
       "Seller / Partner Performance, Partner Enablement &amp; Training (familiarity), Cross-functional Execution (Category, "
       "Marketing, Supply Chain, Product), Stakeholder Management, Vendor Coordination"),
  cell("Leadership &amp; Ownership",
       "Project Leadership, Team &amp; Operations Coordination, Delivery Under Tight Timelines, High-Ownership / "
       "Intrapreneurial, Problem-Solving in Ambiguity")],
 [cell("Analytics &amp; Tools",
       "SQL, Tableau, Microsoft Power BI, Advanced Excel (Pivots, Power Query), Dashboards &amp; KPIs, Unit Economics &amp; "
       "Profitability, Data-Driven Decision Making"),
  cell("Customer, Partner &amp; Business",
       "Customer &amp; Partner Experience at Scale, Revenue &amp; Margin Growth, Sustainable / Profitable Growth, Competitive "
       "Intelligence, Business Narratives &amp; Insights")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
                       ("RIGHTPADDING",(0,0),(0,-1),6),("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Large Appliances (eCommerce Marketplace)", [
 "Own a marketplace category end to end &mdash; seller / partner and SKU performance, GMV, pricing, assortment, and in-stock "
 "&mdash; scaling volumes and revenue while safeguarding customer and partner experience.",
 "Drive category growth through pricing, assortment, inventory, and promotion levers; data-driven demand planning and "
 "promotion execution delivered a 55% category revenue uplift during Big Billion Days, under tight timelines.",
 "Re-engineer reporting and operating cadences for excellence and build the dashboards / KPIs that give leaders "
 "real-time visibility; standardize processes across teams.",
 "Partner cross-functionally with category, marketing, supply chain, and product to execute swiftly and unblock growth.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Re-engineered reporting operations with Lean Six Sigma (20% faster), standardizing KPIs and process across global "
 "teams &mdash; operational excellence at scale.",
 "Built dashboards giving commercial leaders real-time visibility into trends and KPIs; supported ARR that scaled into "
 "the $500MM range.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence (Strategy &amp; Research)", [
 "Published quantitative research across 3 cycles and built unit-economics and profitability models plus competitive "
 "intelligence to guide strategy and leadership decisions.",
])
job("Technology Risk Partners", "Feb 2021 &ndash; May 2021", "GRC Consultant &mdash; Intern", [
 "Consulting engagement: built Oracle Cloud reporting and automated control testing to support UAT and compliance.",
])
job("Sun Pharmaceutical Industries", "Jun 2020 &ndash; Jan 2021", "Intern &mdash; Research &amp; Data", [
 "Compiled and validated large multi-source datasets to support research and operations.",
])

head("Education")
E.append(Paragraph("<b>Vellore Institute of Technology (VIT)</b> &mdash; B.Tech (Engineering), Biotechnology, GPA 8.55 / 10 &nbsp;(2021)", body))
E.append(Paragraph("<b>Spring Dale College</b> &mdash; ISC (Class XII): 88% &nbsp;|&nbsp; ICSE (Class X): 88% &nbsp;(2014 / 2016)", body))

head("Leadership &amp; Impact")
for x in [
 "Led operations, logistics, and on-ground teams for corporate / college events hosting 800&ndash;1,000+ participants "
 "&mdash; planning, coordination, and delivery under tight timelines.",
 "55% category revenue uplift at Flipkart through data-driven demand planning and promotion execution.",
 "20% faster reporting at Enverus via Lean Six Sigma operational excellence and automation.",
]:
    E.append(Paragraph(f"&bull;&nbsp; {x}", bullet))

doc.build(E)
print("built", OUT)
