#!/usr/bin/env python3
"""Category Growth / Growth Manager tailored resume for Juhi Bhalla. 1 page, ATS-safe."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor("#1F3A5F"); GREY = colors.HexColor("#3f3f3f"); LINE = colors.HexColor("#9fb0c3")
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_Category_Growth.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19, textColor=NAVY, leading=22, spaceAfter=1)
title = ParagraphStyle("title", fontName="Helvetica", fontSize=9.5, textColor=GREY, leading=12.4, spaceAfter=3)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.7, textColor=GREY, leading=11)
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
E.append(Paragraph("Business Analyst&nbsp; |&nbsp; Category Growth &amp; Analytics&nbsp; &middot;&nbsp; Cohort &amp; Conversion Insights&nbsp; &middot;&nbsp; Promotions &amp; Retention&nbsp; &middot;&nbsp; Cross-functional Growth", title))
E.append(Paragraph("Bengaluru, India&nbsp; |&nbsp; Serving notice &mdash; available at short notice&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

head("Professional Summary")
E.append(Paragraph(
  "Business Analyst with 5+ years driving category growth and analytics in high-scale e-commerce (Flipkart) and B2B SaaS "
  "(Enverus). I identify growth opportunities and drive category-creation and growth initiatives across cohorts, channels, "
  "and assortment; run customer cohort, conversion, and funnel analyses to unblock shopper bottlenecks; and build "
  "target-vs-actual visibility across region, channel, and cohort to steer course correction. I drive promotion and "
  "retention levers (including an in-app loyalty coupons feature) and partner with product, data science, and "
  "performance-marketing teams to ship growth. Proficient in SQL, Tableau, Power BI, and Advanced Excel; my data-driven "
  "planning drove a 55% category revenue uplift during Big Billion Days. VIT engineering graduate &mdash; currently serving "
  "notice and available at short notice.", body))

head("Skills &amp; Core Competencies")
def cell(h, items): return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("Category Growth &amp; Creation",
       "Category Creation &amp; Growth Initiatives, Growth Opportunity Identification, Cross-sell &amp; LOB Growth, Channel "
       "Growth / Offline-to-Online (familiarity), New Category Launch, Assortment &amp; Pricing Levers"),
  cell("Customer &amp; Cohort Analytics",
       "Customer Cohort Analysis, Conversion / Funnel &amp; Shopper Bottlenecks, Retention Analysis, Segmentation, "
       "Trend &amp; Variance Analysis, Regression &amp; Forecasting")],
 [cell("Performance Visibility &amp; Course Correction",
       "Target vs Actuals Tracking, Dashboards &amp; Scorecards (Region / Channel / Cohort), KPI Standardization, "
       "Root-Cause Analysis, Data-Driven Recommendations"),
  cell("Promotions &amp; Commercial",
       "Sales Promotion Charter, Promotion &amp; Deal Analysis, Customer Retention &amp; Loyalty, Margin &amp; Unit Economics, "
       "Revenue Growth Levers")],
 [cell("BI, SQL &amp; Tools",
       "SQL, Tableau, Microsoft Power BI, Advanced Excel (Pivots, Power Query), Automated / AI-Assisted Reporting, "
       "Data Storytelling"),
  cell("Cross-functional &amp; Ways of Working",
       "Collaboration with Product, Data Science &amp; Performance Marketing, Stakeholder Management, Project Execution, "
       "Ownership, Structuring Ambiguous Problems")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
                       ("RIGHTPADDING",(0,0),(0,-1),6),("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Large Appliances (eCommerce Marketplace)", [
 "Drive category growth initiatives &mdash; identify growth opportunities across customer cohorts, channels, and assortment "
 "&mdash; and drive them with cross-functional teams (product, marketing, supply chain).",
 "Run customer cohort, conversion, and funnel analyses to pinpoint shopper and conversion bottlenecks and recommend "
 "actions to accelerate growth.",
 "Create target-vs-actual visibility via Tableau / Power BI dashboards and scorecards across region, channel, and "
 "cohort; identify course-correction areas and standardize KPIs (SQL, Google Apps Script).",
 "Drive promotion / deal analysis and loyalty features (in-app coupons in payments) to influence retention; data-driven "
 "planning drove a 55% category revenue uplift during Big Billion Days.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Built Tableau / Power BI dashboards giving commercial leaders target-vs-actual visibility into sales trends and KPIs, "
 "supporting ARR that scaled into the $500MM range.",
 "Re-engineered reporting with Lean Six Sigma (20% faster), standardizing KPIs across global teams.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence", [
 "Published quantitative research across 3 cycles and built cohort, financial, and unit-economics models to support "
 "growth and leadership decisions.",
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
