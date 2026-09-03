#!/usr/bin/env python3
"""ISB Academic/Program Operations - tailored resume for Juhi Bhalla (ATS-safe, 2-col skills)."""
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
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_ISB.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=19, textColor=NAVY,
                      leading=22, spaceAfter=1)
title = ParagraphStyle("title", fontName="Helvetica", fontSize=9.6, textColor=GREY,
                       leading=12.5, spaceAfter=3)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.8, textColor=GREY, leading=11)
sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=10.3, textColor=NAVY,
                     leading=12, spaceBefore=4.5, spaceAfter=1.5)
body = ParagraphStyle("body", fontName="Helvetica", fontSize=8.9, textColor=colors.black,
                      leading=11.1, alignment=TA_LEFT)
skillcell = ParagraphStyle("skillcell", fontName="Helvetica", fontSize=8.4, textColor=colors.black,
                           leading=10.2)
role = ParagraphStyle("role", fontName="Helvetica-Bold", fontSize=9.3, textColor=colors.black, leading=11.5)
comp = ParagraphStyle("comp", fontName="Helvetica-Bold", fontSize=9.1, textColor=NAVY, leading=11.5)
dt = ParagraphStyle("dt", fontName="Helvetica-Oblique", fontSize=8.4, textColor=GREY, leading=11)
bullet = ParagraphStyle("bullet", fontName="Helvetica", fontSize=8.8, textColor=colors.black,
                        leading=10.8, leftIndent=9, bulletIndent=0, spaceAfter=1)

doc = SimpleDocTemplate(OUT, pagesize=A4, topMargin=9*mm, bottomMargin=7*mm,
                        leftMargin=14*mm, rightMargin=14*mm, title="Juhi Bhalla - Resume",
                        author="Juhi Bhalla")
E = []

def rule():
    return HRFlowable(width="100%", thickness=0.7, color=LINE, spaceBefore=1.5, spaceAfter=3)

def head(t):
    E.append(Paragraph(t, sec)); E.append(rule())

def b(t):
    E.append(Paragraph(f"&bull;&nbsp; {t}", bullet))

def job(company, date, rolename, bullets):
    row = Table([[Paragraph(company, comp), Paragraph(date, dt)]],
                colWidths=[120*mm, 62*mm])
    row.setStyle(TableStyle([("ALIGN",(1,0),(1,0),"RIGHT"),("VALIGN",(0,0),(-1,-1),"BOTTOM"),
                             ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(-1,-1),0),
                             ("TOPPADDING",(0,0),(-1,-1),1),("BOTTOMPADDING",(0,0),(-1,-1),0)]))
    blk = [row, Paragraph(rolename, role), Spacer(1,1)]
    for x in bullets:
        blk.append(Paragraph(f"&bull;&nbsp; {x}", bullet))
    E.append(KeepTogether(blk)); E.append(Spacer(1,2))

# ---- header ----
E.append(Paragraph("JUHI BHALLA", name))
E.append(Paragraph("Business Analyst&nbsp; |&nbsp; Program &amp; Academic Operations &middot; Dashboards &amp; Process Improvement &middot; Stakeholder Management", title))
E.append(Paragraph("Bengaluru, India (open to Hyderabad)&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

# ---- summary ----
head("Professional Summary")
E.append(Paragraph(
  "Analytics-driven operations professional with 5+ years running high-scale, deadline-bound processes and building the "
  "dashboards, trackers, and KPIs that keep them on track. At Flipkart and Enverus I own reporting and continuous process "
  "improvement for cross-functional teams &mdash; standardizing KPIs, automating trackers, and turning operational data into "
  "decisions, with a Lean Six Sigma record of cutting reporting time 20%. Earlier GRC (audit &amp; compliance) and event "
  "operations (directing logistics for 1,000+ participants) round out a profile built for academic and program operations. "
  "Target scope: course setup, grading coordination, examinations and tutorials, academic advising support, scheduling "
  "&amp; allocation, and audit/compliance readiness &mdash; backed by SQL, Tableau/Power BI, Advanced Excel and Google Sheets, "
  "with CRM/Salesforce and LMS/Moodle familiarity.", body))

# ---- skills (2-col, row-major ATS-safe) ----
head("Skills &amp; Core Competencies")
def cell(h, items):
    return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("Program &amp; Operations Coordination",
       "Scheduling &amp; Allocation, Workload &amp; Timeline Management, Operational Bottleneck Resolution, "
       "Priority &amp; Escalation Management, Process Documentation &amp; Coordination"),
  cell("Dashboards &amp; Reporting",
       "SQL, Tableau, Microsoft Power BI, Advanced Excel (Pivots, Power Query), Google Sheets / Apps Script, "
       "KPI Standardization, Trackers &amp; Reporting Accuracy")],
 [cell("Audit, Compliance &amp; Quality",
       "Compliance Readiness, Audit &amp; Control Support (GRC), Policy Adherence, Process Documentation, "
       "Data Quality &amp; Validation, Attention to Detail"),
  cell("Process Improvement &amp; Automation",
       "Lean Six Sigma, Automated Reporting Pipelines, Continuous Improvement, System Enhancements, "
       "Efficiency &amp; Visibility")],
 [cell("Systems &amp; Tools",
       "CRM / Salesforce (familiarity), LMS / Moodle (familiarity), Oracle Cloud, DOMO, Amazon QuickSight, "
       "Institutional / ERP Systems"),
  cell("Stakeholders &amp; Ways of Working",
       "Cross-functional &amp; Multi-stakeholder Coordination (Faculty / Partner / Administrative Teams), Stakeholder "
       "Management, Communication &amp; Storytelling, Ownership &amp; Accountability, Adaptability")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),
                       ("LEFTPADDING",(0,0),(-1,-1),0),("RIGHTPADDING",(0,0),(0,-1),6),
                       ("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

# ---- experience ----
head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Large Appliances (eCommerce Marketplace)", [
 "Build and automate interactive trackers and dashboards (Tableau / Power BI, SQL, Google Apps Script) that give "
 "leaders real-time visibility into performance and standardize KPIs and reporting accuracy across teams.",
 "Coordinate category, seller, and SKU performance (GMV, conversion, traffic, pricing, in-stock), resolving "
 "operational bottlenecks and surfacing improvement opportunities across a matrixed organization.",
 "Translate complex, multi-source data into clear narratives and recommendations for category, marketing, and "
 "supply-chain stakeholders, managing competing priorities against tight timelines.",
 "Built regression-based demand / sales forecasting and data-driven planning that drove a 55% category revenue "
 "uplift during Big Billion Days.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Built and maintained dashboards and trackers giving US-based leaders real-time KPI visibility, supporting ARR "
 "that scaled into the $500MM range; assessed profitability and forecast inputs.",
 "Re-engineered reporting with Lean Six Sigma (20% faster), standardizing KPIs and improving reporting efficiency "
 "and accuracy across global teams &mdash; continuous process improvement, end to end.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence", [
 "Published quantitative research across 3 cycles and built financial / operational and unit-economics models to "
 "support leadership decisions; maintained data quality and validation across multi-source datasets.",
])
job("Technology Risk Partners", "Feb 2021 &ndash; May 2021", "GRC Consultant &mdash; Intern", [
 "Built Oracle Cloud reporting components and automated control testing to support UAT, audit, and compliance &mdash; "
 "establishing checkpoints and documentation for control readiness.",
])
job("Sun Pharmaceutical Industries", "Jun 2020 &ndash; Jan 2021", "Intern &mdash; Research &amp; Data", [
 "Compiled and validated large multi-source datasets with high accuracy to support research and operations.",
])

# ---- education ----
head("Education")
E.append(Paragraph("<b>Vellore Institute of Technology (VIT)</b> &mdash; B.Tech (Engineering), Biotechnology, GPA 8.55 / 10 &nbsp;(2021)", body))
E.append(Paragraph("<b>Spring Dale College</b> &mdash; ISC (Class XII): 88% &nbsp;|&nbsp; ICSE (Class X): 88% &nbsp;(2014 / 2016)", body))

# ---- impact & leadership ----
head("Impact &amp; Leadership")
b("Directed operations, logistics, scheduling and on-ground coordination for corporate / college events hosting "
  "800&ndash;1,000+ participants &mdash; planning, allocation, and stakeholder management under tight timelines.")
b("55% category revenue uplift at Flipkart through data-driven demand planning and promotion analysis.")
b("20% faster reporting at Enverus via Lean Six Sigma process improvement and automation.")

doc.build(E)
print("built", OUT)
