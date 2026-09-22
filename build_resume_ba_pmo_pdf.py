#!/usr/bin/env python3
"""Business Analyst + PMO / Executive Support tailored resume for Juhi Bhalla. 1 page, ATS-safe."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle,
                                HRFlowable, KeepTogether)
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT

NAVY = colors.HexColor("#1F3A5F"); GREY = colors.HexColor("#3f3f3f"); LINE = colors.HexColor("#9fb0c3")
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_BA_PMO_ExecSupport.pdf"

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
E.append(Paragraph("Business Analyst&nbsp; &middot;&nbsp; PMO &amp; Executive Support&nbsp; &middot;&nbsp; Dashboards, QBR / MBR Reporting &amp; Stakeholder Communications&nbsp; &middot;&nbsp; Excel / PowerPoint", title))
E.append(Paragraph("Bengaluru, India (open to relocation)&nbsp; |&nbsp; Serving notice &mdash; available at short notice&nbsp; |&nbsp; +91 88709 52224&nbsp; |&nbsp; juhibhalla.jblko@gmail.com&nbsp; |&nbsp; linkedin.com/in/juhi-bhalla", contact))
E.append(Spacer(1,4))

head("Professional Summary")
E.append(Paragraph(
  "Business Analyst with 5+ years in B2B SaaS (Enverus) and large-MNC e-commerce (Flipkart), pairing strong business "
  "analysis and reporting with the organization, communication, and discretion to support senior leaders and a PMO. I "
  "analyze operational data for trends, risks, and improvement opportunities; build dashboards and consolidate "
  "multi-stakeholder inputs into accurate performance reviews (QBR / MBR); and prepare executive-ready reporting and "
  "presentations. Experienced coordinating cross-functional initiatives across product, marketing, finance, and "
  "supply-chain teams, tracking follow-ups to closure, and re-engineering reporting with Lean Six Sigma (20% faster). "
  "Advanced in Excel, PowerPoint, and BI tools (Tableau / Power BI, SQL); detail-oriented and comfortable handling "
  "confidential information and shifting priorities across time zones. VIT engineering graduate &mdash; currently serving "
  "notice and available at short notice.", body))

head("Skills &amp; Core Competencies")
def cell(h, items): return Paragraph(f"<b>{h}:</b> {items}", skillcell)
skills = [
 [cell("PMO &amp; Program Support",
       "Project Tracking, Project Plans &amp; Documentation, Initiative Management, RAID Logs (Risks / Assumptions / Issues / "
       "Dependencies) (familiarity), Cross-functional Program Coordination (Sales, Marketing, Finance, IT, Ops), "
       "Action-Item Tracking &amp; Follow-up"),
  cell("Business Analysis &amp; Reporting",
       "Operational Data Analysis, Trend / Risk / Opportunity Identification, QBRs / MBRs / Performance Reviews, "
       "Dashboards &amp; Scorecards, Data Consolidation &amp; Validation, Reporting Accuracy, KPI / OKR Frameworks")],
 [cell("Executive Support &amp; Communications",
       "Executive Briefings &amp; Board-Ready Decks, Executive Communications &amp; Presentations, Strategic Documentation, "
       "Stakeholder Alignment, Confidentiality &amp; Discretion"),
  cell("Tools",
       "Microsoft Excel (Advanced), PowerPoint, Outlook, Google Workspace, Tableau, Power BI, SQL, "
       "Project Management Tools (familiarity)")],
 [cell("Analytics &amp; Methods",
       "Trend &amp; Variance Analysis, Root-Cause Analysis, Process Improvement (Lean Six Sigma), Unit Economics, "
       "Forecasting, Data Storytelling"),
  cell("Ways of Working",
       "Organized &amp; Detail-Oriented, Prioritization &amp; Time Management, Written &amp; Verbal Communication, "
       "Multi-tasking with Minimal Supervision, Cross-time-zone Collaboration, Ownership")],
]
t = Table(skills, colWidths=[90*mm, 92*mm])
t.setStyle(TableStyle([("VALIGN",(0,0),(-1,-1),"TOP"),("LEFTPADDING",(0,0),(-1,-1),0),
                       ("RIGHTPADDING",(0,0),(0,-1),6),("RIGHTPADDING",(1,0),(1,-1),0),
                       ("TOPPADDING",(0,0),(-1,-1),1.5),("BOTTOMPADDING",(0,0),(-1,-1),3)]))
E.append(t)

head("Professional Experience")
job("Flipkart", "Jun 2024 &ndash; Present", "Business Analyst &mdash; Large Appliances (eCommerce, MNC)", [
 "Track and report on category initiatives &mdash; maintain dashboards and scorecards, consolidate multi-source inputs, "
 "and standardize KPIs for leadership visibility.",
 "Coordinate cross-functional programs across product, marketing, and supply-chain teams; track action items and "
 "follow-ups to closure.",
 "Analyze operational data for trends, risks, and improvement opportunities, and translate them into clear narratives "
 "and presentations for stakeholders.",
 "Re-engineered reporting cadences and processes; data-driven planning drove a 55% category revenue uplift during Big "
 "Billion Days.",
])
job("Enverus", "Jan 2023 &ndash; May 2024", "Business Analyst I &mdash; Market Research (B2B SaaS)", [
 "Prepared performance dashboards and business-review reporting (QBR / MBR style) for US-based commercial leadership, "
 "consolidating and validating inputs across global teams; supported ARR that scaled into the $500MM range.",
 "Re-engineered reporting with Lean Six Sigma (20% faster), standardizing KPIs and documentation.",
])
job("Enverus", "May 2021 &ndash; Dec 2022", "Associate &mdash; Commercial Intelligence", [
 "Produced quantitative research and executive-ready insights and models to support leadership decisions.",
])
job("Technology Risk Partners", "Feb 2021 &ndash; May 2021", "GRC Consultant &mdash; Intern", [
 "Managed controls, compliance, and documentation with confidentiality; supported UAT and audit readiness.",
])
job("Sun Pharmaceutical Industries", "Jun 2020 &ndash; Jan 2021", "Intern &mdash; Research &amp; Data", [
 "Compiled and validated large multi-source datasets to support research and operations.",
])

head("Education")
E.append(Paragraph("<b>Vellore Institute of Technology (VIT)</b> &mdash; B.Tech (Engineering), Biotechnology, GPA 8.55 / 10 &nbsp;(2021)", body))
E.append(Paragraph("<b>Spring Dale College</b> &mdash; ISC (Class XII): 88% &nbsp;|&nbsp; ICSE (Class X): 88% &nbsp;(2014 / 2016)", body))

head("Impact &amp; Leadership")
for x in [
 "Directed operations, logistics, and follow-up coordination for corporate / college events hosting 800&ndash;1,000+ "
 "participants &mdash; organized delivery under tight timelines.",
 "55% category revenue uplift at Flipkart through data-driven planning and reporting.",
 "20% faster reporting at Enverus via Lean Six Sigma process improvement and automation.",
]:
    E.append(Paragraph(f"&bull;&nbsp; {x}", bullet))

doc.build(E)
print("built", OUT)
