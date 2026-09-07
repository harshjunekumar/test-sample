#!/usr/bin/env python3
"""Purplle Revenue & Marketing pod - tailored resume for Juhi Bhalla (ATS-safe, 1 page)."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor("#1F3A5F")
GREY = colors.HexColor("#3f3f3f")
LINE = colors.HexColor("#9fb0c3")
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_Purplle.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19, textColor=NAVY, leading=22, spaceAfter=1)
title = ParagraphStyle("title", fontName="Helvetica", fontSize=9.6, textColor=GREY, leading=12.5, spaceAfter=3)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.8, textColor=GREY, leading=11)
sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=10.3, textColor=NAVY, leading=12,
                     spaceBefore=4.5, spaceAfter=1.5)
body = ParagraphStyle("body", fontName="Helvetica", fontSize=8.9, textColor=colors.black, leading=11.1, alignment=TA_LEFT)
skillcell = ParagraphStyle("skillcell", fontName="Helvetica", fontSize=8.4, textColor=colors.black, leading=10.2)
role = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9.3, textColor=colors.black, leading=11.5)
comp = ParagraphStyle("comp", fontName="Helvetica-Bold", fontSize=9.1, textColor=NAVY, leading=11.5)
dt = ParagraphStyle("dt", fontName="Helvetica-Oblique", fontSize=8.4, textColor=GREY, leading=11)
bullet = ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.8, textColor=colors.black,
                        leading=10.8, leftIndent=9, bulletIndent=0, spaceAfter=1)

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
E.append(Paragraph("Business Analyst&nbsp; |&nbsp; Revenue &amp; Growth Analytics &middot; Consumer &amp; Competitive Intelligence &middot; P&amp;L &amp; Margin Levers", title))
E.append(Paragraph("Bengaluru, India (open to relocation)&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

head("Professional Summary")
E.append(Paragraph(
  "Commercially-driven business analyst with 5+ years turning e-commerce and market data into revenue and margin "
  "outcomes. At Flipkart I own category revenue analytics &mdash; GMV, conversion, pricing, assortment, promotions, and "
  "in-stock &mdash; and pull the levers that drove a 55% category revenue uplift during Big Billion Days. Earlier, in a "
  "Commercial Intelligence role, I published quantitative research and built unit-economics and profitability models plus "
  "competitive and pricing intelligence for leadership. A VIT engineering graduate fluent in SQL, Tableau/Power BI and "
  "Advanced Excel (with Looker and Python/R familiarity), I build real-time revenue dashboards and scorecards and translate "
  "complex data into commercially actionable narratives across Brand, Supply Chain, Product, and Marketing. Built for a "
  "P&amp;L-owning, fast-paced pod: revenue growth, margin, consumer insight, and platform health.", body))

head("Skills &amp; Core Competencies")
def cell(h, items): return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("Revenue, P&amp;L &amp; Growth Levers",
       "Revenue &amp; Gross-Margin Analytics, P&amp;L Tracking, Unit Economics &amp; Profitability, Pricing &amp; Margin Levers, "
       "Assortment &amp; Promotions, Base Reactivation &amp; Growth Opportunities"),
  cell("Market Intelligence &amp; Consumer Insights",
       "Quantitative Research, Competitive &amp; Pricing Intelligence, Cohort Analysis, Pricing &amp; Elasticity (regression-based), "
       "Demand Signals &amp; Assortment, Share-of-Wallet &amp; Whitespace, Qualitative Research / FGDs (familiarity)")],
 [cell("Marketing, Growth &amp; Campaigns",
       "Promotion &amp; Deal-Construct Analytics, Offer Panels &amp; Sale Events, CRM / Push / In-App Campaigns (familiarity), "
       "CAC &amp; Conversion Analysis (familiarity), Cohort Reactivation"),
  cell("Platform Health &amp; Fulfilment",
       "Availability &amp; In-Stock Rate, Catalogue Fill &amp; Listing Quality, Order Completion &amp; RTO, "
       "Revenue-Leakage / Stock-out Analysis, Supply-Chain &amp; Inventory Coordination, Fulfilment SLAs")],
 [cell("Analytics, Reporting &amp; Tools",
       "SQL, Tableau, Microsoft Power BI, Looker (familiarity), Advanced Excel (Pivots, Power Query), Real-time Dashboards "
       "&amp; Scorecards, Revenue Models, Python / R (familiarity), AI-Assisted Analysis"),
  cell("Stakeholders &amp; Ways of Working",
       "Cross-functional (Brand, Supply Chain, Product, Marketing), Commercial Acumen, Ownership &amp; Accountability, "
       "Fast-paced Execution, Data Storytelling, Influence Without Authority")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
                       ("RIGHTPADDING",(0,0),(0,-1),6),("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Large Appliances (eCommerce Marketplace)", [
 "Own category revenue and gross-margin analytics &mdash; GMV, conversion, traffic, pricing, and in-stock &mdash; pulling growth "
 "and margin levers (pricing, assortment, inventory, promotions) to unlock revenue opportunities.",
 "Build and maintain real-time Tableau / Power BI revenue dashboards and weekly scorecards (SQL, Google Apps Script) "
 "with standardized KPIs, giving the team live visibility into performance.",
 "Own platform revenue-health metrics &mdash; availability / in-stock, catalogue and SKU quality &mdash; flagging stock-outs and "
 "revenue leakage during sale periods and coordinating with supply-chain and inventory teams ahead of activations.",
 "Ran demand forecasting and promotion / deal analysis across sale events that drove a 55% category revenue uplift "
 "during Big Billion Days.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Built revenue dashboards giving commercial leaders real-time KPI visibility, supporting ARR that scaled into the "
 "$500MM range; assessed profitability and forecast inputs.",
 "Re-engineered reporting with Lean Six Sigma (20% faster), standardizing KPIs across global teams.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence", [
 "Published quantitative commercial research across 3 cycles and built financial / unit-economics and profitability "
 "models; produced competitive and pricing intelligence to guide leadership decisions.",
])
job("Technology Risk Partners", "Feb 2021 &ndash; May 2021", "GRC Consultant &mdash; Intern", [
 "Built Oracle Cloud reporting components and automated control testing to support UAT and compliance.",
])
job("Sun Pharmaceutical Industries", "Jun 2020 &ndash; Jan 2021", "Intern &mdash; Research &amp; Data", [
 "Compiled and validated large multi-source datasets with high accuracy to support research and operations.",
])

head("Education")
E.append(Paragraph("<b>Vellore Institute of Technology (VIT)</b> &mdash; B.Tech (Engineering), Biotechnology, GPA 8.55 / 10 &nbsp;(2021)", body))
E.append(Paragraph("<b>Spring Dale College</b> &mdash; ISC (Class XII): 88% &nbsp;|&nbsp; ICSE (Class X): 88% &nbsp;(2014 / 2016)", body))

head("Impact &amp; Leadership")
for x in [
 "55% category revenue uplift at Flipkart through data-driven demand planning and promotion analysis.",
 "20% faster reporting at Enverus via Lean Six Sigma process improvement and automation.",
 "Directed operations and logistics for corporate / college events hosting 800&ndash;1,000+ participants &mdash; execution "
 "and ownership under tight timelines.",
]:
    E.append(Paragraph(f"&bull;&nbsp; {x}", bullet))

doc.build(E)
print("built", OUT)
