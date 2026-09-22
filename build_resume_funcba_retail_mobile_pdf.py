#!/usr/bin/env python3
"""Functional & Business Analyst - Retail + Mobile Apps tailored resume for Juhi Bhalla. 1 page, ATS-safe."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor("#1F3A5F"); GREY = colors.HexColor("#3f3f3f"); LINE = colors.HexColor("#9fb0c3")
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_Functional_BA_Retail_Mobile.pdf"

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
E.append(Paragraph("Functional &amp; Business Analyst&nbsp; &middot;&nbsp; Retail &amp; Mobile Commerce&nbsp; &middot;&nbsp; Requirements, Solutions &amp; App Analytics&nbsp; &middot;&nbsp; SQL, Tableau / Power BI", title))
E.append(Paragraph("Bengaluru, India (open to relocation)&nbsp; |&nbsp; Serving notice &mdash; available at short notice&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

head("Professional Summary")
E.append(Paragraph(
  "Functional and Business Analyst with 5+ years in high-scale retail and mobile-commerce (Flipkart) and global B2B SaaS "
  "(Enverus), pairing strong business analysis with functional solution delivery. I analyze business problems, gather and "
  "translate requirements into functional solutions, and partner with cross-functional and technical teams to develop, "
  "test (UAT), and ship improvements &mdash; including in-app features such as a product exchange flow and loyalty coupons "
  "within the payment method. On a mobile-first retail marketplace I track app funnel, conversion, traffic, "
  "pricing, and in-app promotions, and build the dashboards and KPIs that drive category growth and innovation. Proficient "
  "in SQL, Tableau, Power BI, and Advanced Excel; skilled in requirement analysis, process improvement (Lean Six Sigma), "
  "and stakeholder management, delivering results in fast-paced environments. VIT engineering graduate &mdash; currently "
  "serving notice and available at short notice.", body))

head("Skills &amp; Core Competencies")
def cell(h, items): return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("Functional &amp; Business Analysis",
       "Business Analysis, Functional Analysis, Functional Design &amp; Specs, Requirement Gathering &amp; BRDs, Solution "
       "Design, Gap / Impact Assessment, UAT, SDLC (familiarity)"),
  cell("Retail &amp; Category (domain)",
       "Retail Analytics, Category &amp; Merchandising, Assortment &amp; Pricing, Sell-through &amp; GMV, In-Stock &amp; Inventory, "
       "Demand Planning")],
 [cell("Mobile Commerce &amp; Apps",
       "Mobile-Commerce App Analytics (Flipkart), App Funnel &amp; Conversion, In-App Promotions, App Feature Delivery "
       "(Product Exchange, Loyalty Coupons in Payments), Requirements &amp; UAT"),
  cell("BI, SQL &amp; Reporting",
       "SQL, Tableau, Microsoft Power BI, Advanced Excel (Pivots, Power Query), Dashboards &amp; KPIs, Automated / "
       "AI-Assisted Reporting")],
 [cell("Analytics &amp; Methods",
       "Cohort &amp; Retention Analysis, Demand Forecasting, Trend &amp; Variance Analysis, Regression, Root-Cause Analysis, "
       "Unit Economics &amp; Profitability"),
  cell("Ways of Working &amp; Stakeholders",
       "Cross-functional Collaboration (Product, Tech, Category, Marketing), Stakeholder Management, Process Improvement "
       "(Lean Six Sigma), Data Storytelling, Ownership, Fast-paced Delivery")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
                       ("RIGHTPADDING",(0,0),(0,-1),6),("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Large Appliances (Retail / Mobile-Commerce Marketplace)", [
 "Analyze business problems and identify improvement opportunities for a mobile-first retail marketplace category; "
 "gather and translate business needs into functional solutions with product and tech teams.",
 "Drove requirements and functional design for in-app features &mdash; a product exchange flow and loyalty coupons within "
 "the payment method &mdash; from requirement analysis through development, UAT, and rollout.",
 "Track app funnel, conversion, traffic, pricing, and in-app promotions; build and automate Tableau / Power BI "
 "dashboards (SQL, Google Apps Script) and standardize KPIs across teams.",
 "Run demand forecasting and pull growth levers (pricing, assortment, promotions); data-driven planning and promotion "
 "analysis drove a 55% category revenue uplift during Big Billion Days.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Gathered and analyzed requirements and delivered reporting solutions for global commercial stakeholders; built "
 "Tableau / Power BI dashboards supporting ARR that scaled into the $500MM range.",
 "Re-engineered reporting with Lean Six Sigma (20% faster), standardizing KPIs and documentation across global teams.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence", [
 "Published quantitative research across 3 cycles and built financial / operational and unit-economics models to "
 "support leadership decisions.",
])
job("Technology Risk Partners", "Feb 2021 &ndash; May 2021", "GRC Consultant &mdash; Intern", [
 "Built Oracle Cloud reporting components and automated control testing to support UAT and compliance &mdash; hands-on "
 "functional and technical delivery.",
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
