#!/usr/bin/env python3
"""Category Manager tailored resume for Juhi Bhalla. 1 page, ATS-safe."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor("#1F3A5F"); GREY = colors.HexColor("#3f3f3f"); LINE = colors.HexColor("#9fb0c3")
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_Category_Manager.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19, textColor=NAVY, leading=22, spaceAfter=1)
title = ParagraphStyle("title", fontName="Helvetica", fontSize=9.4, textColor=GREY, leading=12.3, spaceAfter=3)
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
E.append(Paragraph("Category Management &amp; Analytics&nbsp; &middot;&nbsp; Category Strategy, Assortment, Pricing &amp; Promotions&nbsp; &middot;&nbsp; Sales &amp; Margin Growth&nbsp; &middot;&nbsp; Competitive Insights", title))
E.append(Paragraph("Bengaluru, India (open to relocation)&nbsp; |&nbsp; Serving notice &mdash; available at short notice&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

head("Professional Summary")
E.append(Paragraph(
  "Business Analyst with 5+ years managing and growing e-commerce / retail categories at Flipkart, pairing category "
  "strategy with deep analytics. I own category performance against <b>sales and margin</b> targets &mdash; planning "
  "assortment, pricing, and promotions; tracking performance and driving corrections; and analyzing <b>market trends and "
  "competitor activity</b> to identify growth opportunities. I develop and execute category strategies, coordinate "
  "cross-functionally with marketing, sales, and supply-chain teams, and prepare performance reports and recommendations "
  "for leadership. My data-driven category planning drove a 55% category revenue uplift during Big Billion Days. "
  "Proficient in SQL, Tableau, Power BI, Advanced Excel, and PowerPoint. VIT engineering graduate &mdash; currently serving "
  "notice and available at short notice.", body))

head("Skills &amp; Core Competencies")
def cell(h, items): return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("Category Management &amp; Strategy",
       "Category Strategy Development &amp; Execution, Sales &amp; Margin Targets, Assortment Planning, Pricing &amp; Promotions, "
       "Category P&amp;L Support, Growth Opportunity Identification"),
  cell("Vendor &amp; Commercial",
       "Vendor / Seller Performance Management, Vendor Negotiation &mdash; Terms, Pricing &amp; Promotions (familiarity), "
       "Promotional Planning, Margin &amp; Profitability, Deal / Promo Analysis")],
 [cell("Market &amp; Competitive Insight",
       "Market &amp; Industry Trend Analysis, Competitive Intelligence &amp; Benchmarking, Consumer Preference Insights, Whitespace / "
       "Opportunity Sizing, Category Innovation"),
  cell("Analytics &amp; Reporting",
       "Category Performance Tracking, Dashboards &amp; Scorecards, KPI Standardization, Demand Forecasting, "
       "Leadership Reports &amp; Presentations, Root-Cause Analysis")],
 [cell("BI &amp; Tools",
       "SQL, Tableau, Microsoft Power BI, Advanced Excel (Pivots, Power Query), PowerPoint, Automated / "
       "AI-Assisted Reporting"),
  cell("Cross-functional &amp; Ways of Working",
       "Cross-functional Execution (Marketing, Sales, Supply Chain, Product), Stakeholder Management, Data Storytelling, "
       "Ownership, Structuring Ambiguous Problems")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
                       ("RIGHTPADDING",(0,0),(0,-1),6),("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Large Appliances (eCommerce Category)", [
 "Manage and optimize a marketplace category against sales and margin targets &mdash; planning assortment, pricing, and "
 "promotions and driving corrections to improve competitiveness and conversion.",
 "Analyze market trends, competitor activity, and consumer behavior to identify growth opportunities and shape category "
 "strategy aligned to business objectives.",
 "Partner with sellers / vendors on pricing and promotional plans, using performance analytics to inform terms; track "
 "category performance via dashboards and KPIs (SQL, Tableau / Power BI).",
 "Work cross-functionally with marketing, sales, and supply-chain teams to execute category plans, and prepare "
 "performance reviews and recommendations for leadership &mdash; driving a 55% category revenue uplift during Big Billion Days.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Built dashboards and reporting giving commercial leaders visibility into performance trends and KPIs; supported ARR "
 "that scaled into the $500MM range.",
 "Re-engineered reporting with Lean Six Sigma (20% faster), standardizing KPIs across global teams.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence", [
 "Published quantitative research across 3 cycles and built financial / operational and unit-economics models; produced "
 "competitive and price intelligence to support leadership decisions.",
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
 "55% category revenue uplift at Flipkart through data-driven category planning and assortment / promotion analysis.",
 "20% faster reporting at Enverus via Lean Six Sigma process improvement and automation.",
 "Directed operations and logistics for corporate / college events hosting 800&ndash;1,000+ participants.",
]:
    E.append(Paragraph(f"&bull;&nbsp; {x}", bullet))

doc.build(E)
print("built", OUT)
