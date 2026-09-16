#!/usr/bin/env python3
"""Master E-commerce Business Analyst resume (Bangalore) - ATS-optimized, 1 page."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor("#1F3A5F"); GREY = colors.HexColor("#3f3f3f"); LINE = colors.HexColor("#9fb0c3")
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_Ecommerce_Bangalore.pdf"

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
E.append(Paragraph("Business Analyst&nbsp; |&nbsp; E-commerce &amp; Marketplace Analytics &middot; SQL &middot; Tableau / Power BI &middot; GMV, Pricing &amp; Growth Insights", title))
E.append(Paragraph("Bengaluru, India&nbsp; |&nbsp; Serving notice &mdash; available to join at short notice&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

head("Professional Summary")
E.append(Paragraph(
  "Business Analyst with 5+ years in high-scale e-commerce marketplace analytics (Flipkart) and global B2B SaaS "
  "(Enverus), turning large multi-source datasets into the metrics, dashboards, and recommendations that drive growth "
  "and profitability. I track category, seller, and SKU performance &mdash; GMV, conversion, traffic, pricing, and in-stock "
  "&mdash; run cohort, trend, and regression-based forecasting, and translate insights into clear business narratives for "
  "category, marketing, and supply-chain partners. Proficient in SQL, Tableau, Power BI, and Advanced Excel with "
  "automated, AI-assisted reporting; I define and standardize KPIs, assess unit economics and margin, and identify levers "
  "(pricing, assortment, inventory, promotions) that improve performance. VIT engineering graduate, comfortable "
  "structuring ambiguous problems and influencing across a matrixed organization &mdash; currently serving notice and "
  "available to join at short notice.", body))

head("Skills &amp; Core Competencies")
def cell(h, items): return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("Marketplace &amp; Category Analytics",
       "Category / Seller / SKU Performance, GMV, Conversion &amp; Traffic, Pricing Competitiveness, Assortment &amp; "
       "Merchandising, In-Stock &amp; Inventory, Retail Analytics"),
  cell("BI, SQL &amp; Reporting",
       "SQL, Tableau, Microsoft Power BI, Looker (familiarity), DOMO, Amazon QuickSight, Advanced Excel (Pivots, "
       "Power Query), KPI Standardization, Dashboards &amp; Scorecards")],
 [cell("Analytics &amp; Methods",
       "Cohort &amp; Retention Analysis, Trend &amp; Variance Analysis, Regression &amp; Demand Forecasting, Hypothesis Testing, "
       "Root-Cause Analysis, Unit Economics &amp; Profitability"),
  cell("Growth &amp; Commercial",
       "Growth Levers (Pricing, Assortment, Promotions), Margin &amp; Profitability, Promotion &amp; Deal Analysis, Revenue "
       "Opportunity Identification, Competitive Intelligence")],
 [cell("Data Engineering &amp; Automation",
       "Automated Reporting Pipelines (SQL, Google Apps Script), Python (familiarity), Data Quality &amp; Validation, "
       "Multi-Source Data Integration, ETL Concepts, AI-Assisted Analysis"),
  cell("Business Analysis &amp; Stakeholders",
       "Requirement Gathering &amp; BRDs, Data Storytelling, Cross-functional (Category, Marketing, Supply Chain, Product), "
       "Stakeholder Management, Influence Without Authority, Structuring Ambiguous Problems")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
                       ("RIGHTPADDING",(0,0),(0,-1),6),("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Large Appliances (eCommerce Marketplace)", [
 "Track category, seller, and SKU performance &mdash; GMV, conversion, traffic, pricing, and in-stock &mdash; surfacing growth "
 "opportunities and performance gaps across the marketplace.",
 "Build and automate interactive Tableau / Power BI dashboards and reporting frameworks (SQL, Google Apps Script) "
 "that give leaders real-time visibility; define and standardize KPIs across teams.",
 "Run cohort, trend, and regression-based demand / sales forecasting; identify levers (pricing, assortment, inventory, "
 "promotions) and translate complex data into clear narratives for category, marketing, and supply-chain partners.",
 "Data-driven demand planning and promotion analysis drove a 55% category revenue uplift during Big Billion Days.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Built and maintained Tableau / Power BI dashboards giving US-based commercial leaders real-time visibility into sales "
 "trends and KPIs, supporting ARR that scaled into the $500MM range; assessed profitability and forecast inputs.",
 "Re-engineered reporting with Lean Six Sigma (20% faster), standardizing KPIs and improving reporting efficiency "
 "across global teams.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence", [
 "Published quantitative research across 3 cycles and built financial / operational and unit-economics models; produced "
 "competitive intelligence to support leadership decisions.",
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
 "55% category revenue uplift at Flipkart through data-driven demand planning and promotion analysis.",
 "20% faster reporting at Enverus via Lean Six Sigma process improvement and automation.",
 "Directed operations and logistics for corporate / college events hosting 800&ndash;1,000+ participants.",
]:
    E.append(Paragraph(f"&bull;&nbsp; {x}", bullet))

doc.build(E)
print("built", OUT)
