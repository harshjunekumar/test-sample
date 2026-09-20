#!/usr/bin/env python3
"""Life Sciences / Regulatory (RIM) BA - HONEST transition-tailored resume for Juhi Bhalla. 1 page, ATS-safe."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor("#1F3A5F"); GREY = colors.HexColor("#3f3f3f"); LINE = colors.HexColor("#9fb0c3")
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_LifeSciences_BA.pdf"

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
E.append(Paragraph("Business Analyst&nbsp; &middot;&nbsp; Life Sciences Background (B.Tech Biotechnology)&nbsp; &middot;&nbsp; Requirements &amp; Stakeholder Management&nbsp; &middot;&nbsp; Validated-System Compliance", title))
E.append(Paragraph("Bengaluru, India (open to Hyderabad)&nbsp; |&nbsp; Serving notice &mdash; available at short notice&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

head("Professional Summary")
E.append(Paragraph(
  "Business Analyst with 5+ years leading requirements management, stakeholder liaison, and process / solution delivery "
  "across e-commerce (Flipkart) and B2B SaaS (Enverus), built on a <b>Biotechnology engineering degree</b> and "
  "<b>pharmaceutical R&amp;D experience</b> (Sun Pharma). Strong in requirement analysis, change management, traceability, "
  "impact assessment, UAT, and cross-functional delivery coordination, with GRC exposure to validated, controlled system "
  "environments and compliance. Now focused on <b>Life Sciences / Regulatory Information Management (RIM) Business "
  "Analysis</b> &mdash; bringing life-sciences domain grounding and BA rigor, and actively upskilling on Veeva Vault RIM, "
  "Jira, and ServiceNow. A VIT engineering graduate (16 years full-time education) who researches, gathers, and "
  "synthesizes information to assess current state and define clear future-state solutions.", body))

head("Skills &amp; Core Competencies")
def cell(h, items): return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("Business Analysis &amp; Requirements",
       "Requirements Management, Business Requirements Analysis, BRDs &amp; Functional Designs, Traceability, "
       "Impact Assessment, Change Requests, UAT Coordination"),
  cell("Stakeholder &amp; Delivery",
       "Stakeholder Management &amp; Liaison, Cross-functional Coordination, Delivery Coordination, Prioritization, "
       "Change Management, Agile Delivery (familiarity)")],
 [cell("Life Sciences &amp; Regulatory (domain)",
       "Biotechnology (B.Tech), Pharmaceutical R&amp;D Exposure, Life Sciences Industry, Regulatory Information Management "
       "/ RIM (upskilling), Regulatory Submissions (familiarity), Industry Insight"),
  cell("Validated Systems &amp; Compliance",
       "GRC &amp; Controls, UAT &amp; Compliance Testing, Validated / Controlled Environments, Business Process Design &amp; "
       "Modeling, Process Documentation, Data Quality &amp; Validation")],
 [cell("Tools",
       "Jira (familiarity), ServiceNow (familiarity), Veeva Vault RIM (upskilling), SQL, Advanced Excel, "
       "Tableau / Power BI, Oracle Cloud"),
  cell("Analysis &amp; Ways of Working",
       "Research &amp; Synthesis, Analytical Problem-Solving, Functional Design, Communication &amp; Documentation, "
       "Ownership, Structuring Ambiguous Problems")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
                       ("RIGHTPADDING",(0,0),(0,-1),6),("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Marketplace (eCommerce)", [
 "Lead end-to-end requirements management for a marketplace category &mdash; gathering business needs, writing "
 "specifications, and managing change requests, prioritization, and impact assessment.",
 "Act as liaison between business, product, supply-chain, and marketing teams; coordinate development, testing (UAT), "
 "and delivery of features and system changes.",
 "Build reporting / analytics solutions (SQL, Tableau / Power BI), standardize processes and KPIs, and maintain data "
 "quality and traceability across systems.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Gathered and analyzed requirements and delivered reporting solutions for global commercial stakeholders; coordinated "
 "delivery and stakeholder sign-off.",
 "Re-engineered reporting processes with Lean Six Sigma (20% faster), standardizing KPIs and documentation.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence", [
 "Researched, gathered, and synthesized information; built financial / operational and unit-economics models and "
 "analyses to support leadership decisions.",
])
job("Technology Risk Partners", "Feb 2021 &ndash; May 2021", "GRC Consultant &mdash; Intern (Compliance &amp; Validated Systems)", [
 "Built Oracle Cloud reporting components and automated control testing supporting UAT and compliance in a controlled "
 "environment; documented controls and change traceability.",
])
job("Sun Pharmaceutical Industries", "Jun 2020 &ndash; Jan 2021", "Intern &mdash; Research &amp; Data (Life Sciences R&amp;D)", [
 "Compiled and validated multi-source research datasets supporting R&amp;D operations &mdash; hands-on exposure to "
 "life-sciences R&amp;D data and processes.",
])

head("Education")
E.append(Paragraph("<b>Vellore Institute of Technology (VIT)</b> &mdash; B.Tech (Engineering), <b>Biotechnology</b>, GPA 8.55 / 10 &nbsp;(2021)", body))
E.append(Paragraph("<b>Spring Dale College</b> &mdash; ISC (Class XII): 88% &nbsp;|&nbsp; ICSE (Class X): 88% &nbsp;(2014 / 2016) &nbsp;&mdash;&nbsp; <b>16 years full-time education (10 + 2 + 4) &mdash; meets the 15-year requirement</b>", body))

head("Impact &amp; Leadership")
for x in [
 "Re-engineered reporting processes at Enverus with Lean Six Sigma &mdash; 20% faster, with improved accuracy and documentation.",
 "Led operations and teams for corporate / college events hosting 800&ndash;1,000+ participants &mdash; delivery under tight timelines.",
 "Drove a 55% category revenue uplift at Flipkart through data-driven planning and cross-functional execution.",
]:
    E.append(Paragraph(f"&bull;&nbsp; {x}", bullet))

doc.build(E)
print("built", OUT)
