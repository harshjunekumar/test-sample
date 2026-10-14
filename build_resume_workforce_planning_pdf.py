#!/usr/bin/env python3
"""Juhi Bhalla - Manager, Workforce Planning. 1 page, ATS-safe, hyphens only."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

BLACK = colors.HexColor("#1a1a1a"); GREY = colors.HexColor("#6b6b6b"); RULE = colors.HexColor("#b7b7b7")
LINKB = "#0563C1"
DEMO = "https://quwgk58euw9vyk7yewlnvo.streamlit.app/"
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_Workforce_Planning.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=15.5, textColor=BLACK, leading=18, spaceAfter=2)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.9, textColor=BLACK, leading=11.5, spaceAfter=1)
tagline = ParagraphStyle("tag", fontName="Helvetica", fontSize=8.5, textColor=GREY, leading=11)
sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=10.0, textColor=BLACK, leading=11.0, spaceBefore=3.2, spaceAfter=1.4)
summ = ParagraphStyle("summ", fontName="Helvetica", fontSize=8.6, textColor=BLACK, leading=10.8, alignment=TA_JUSTIFY)
compln = ParagraphStyle("compln", fontName="Helvetica", fontSize=9.0, textColor=BLACK, leading=11.2, spaceBefore=2.4, spaceAfter=1)
intro = ParagraphStyle("intro", fontName="Helvetica-Bold", fontSize=8.5, textColor=BLACK, leading=10.6, spaceAfter=1)
bul = ParagraphStyle("bul", fontName="Helvetica", fontSize=8.5, textColor=BLACK, leading=10.6, leftIndent=10, bulletIndent=1, spaceAfter=1.0)
edu = ParagraphStyle("edu", fontName="Helvetica", fontSize=8.6, textColor=BLACK, leading=11.4)
skill = ParagraphStyle("skill", fontName="Helvetica", fontSize=8.5, textColor=BLACK, leading=11.5)
subl = ParagraphStyle("subl", fontName="Helvetica-Bold", fontSize=8.5, textColor=GREY, leading=10.4, spaceBefore=2.2, spaceAfter=1)

doc = SimpleDocTemplate(OUT, pagesize=A4, topMargin=9*mm, bottomMargin=7*mm, leftMargin=14*mm,
                        rightMargin=14*mm, title="Juhi Bhalla - Resume", author="Juhi Bhalla")
E = []
def rule(sb=3, sa=2): E.append(HRFlowable(width="100%", thickness=0.7, color=RULE, spaceBefore=sb, spaceAfter=sa))
def sect(t): E.append(Paragraph(t, sec))
def b(t): E.append(Paragraph(f"&bull;&nbsp;&nbsp;{t}", bul))



E.append(Paragraph("JUHI BHALLA", name))
E.append(Paragraph(
  "+91 88709 52224 &nbsp;|&nbsp; juhibhalla.jblko@gmail.com &nbsp;|&nbsp; "
  f"<link href='https://www.linkedin.com/in/juhi-bhalla' color='{LINKB}'><u>LinkedIn</u></link> &nbsp;|&nbsp; Bengaluru, India", contact))
E.append(Paragraph("Capacity Planning &amp; Forecasting | KPI Ownership &amp; Root-Cause Analysis | Vendor / Partner Accountability | "
                   "Operations Leadership | Process Improvement (Lean Six Sigma) | SQL, Excel, Tableau", tagline))
rule(sb=4, sa=1)

sect("PROFESSIONAL SUMMARY")
E.append(Paragraph(
  "Planning and operations leader with 5+ years at Flipkart and Enverus owning <b>forecasts, capacity plans and KPI performance</b> "
  "across in-house teams and external sellers / vendors. I build demand and capacity models, anticipate risks before they hit "
  "service, run root-cause analysis when performance slips, and turn results into clear updates and trade-offs for leadership. "
  "Proven at driving measurable improvement across cross-functional teams (55% revenue uplift at peak, 20% faster cycle times), "
  "with strong analytical rigor in SQL, Excel and Tableau and a coaching, hands-on leadership style.", summ))
rule()

sect("EXPERIENCE")
E.append(Paragraph("<b>Flipkart</b> - Category Manager - Large Appliances &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jun 2024 - Sep 2026</font>", compln))
E.append(Paragraph("Owned planning and performance for a large marketplace category - forecasts, supply / in-stock capacity and KPI "
                   "outcomes across sellers, vendors and cross-functional teams.", intro))
b("<b>Owned forecasting and capacity planning:</b> built regression-based demand and sales forecasts and translated them into "
  "supply and in-stock plans for peak events; data-driven planning drove a <b>55% category revenue uplift during Big Billion Days</b>.")
b("<b>Anticipated risks before peak:</b> tracked forecast vs. actuals and in-stock gaps, flagged shortfalls early and put "
  "mitigation plans in place with supply-chain and seller teams ahead of high-volume sale events.")
b("<b>Owned KPI performance and root-cause analysis</b> across GMV, conversion and in-stock; diagnosed drivers through cohort and "
  "SKU trend analysis (YoY &amp; MoM) and led recovery actions, including exchange offers that grew category <b>revenue 19% YoY</b>.")
b("<b>Held sellers / vendors accountable</b> to commitments on selection, terms and availability; built the category plan within "
  "the <b>Annual Operating Plan (AOP)</b> using market research, lifting <b>Flipkart market-penetration share ~1%</b>.")
b("Built <b>user personas, funnel and cohort analysis</b> behind loyalty-coupon and region-specific bank-offer programs, driving a "
  "<b>20% improvement in conversion</b> and higher offer adoption in the South.")
b("<b>Improved planning tools:</b> built and automated <b>Tableau / Power BI dashboards and templates</b> (SQL, Google Apps Script) "
  "with standardized KPIs, giving leadership real-time visibility and replacing manual tracking.")

E.append(Paragraph("<b>Enverus</b> - Business Analyst I - Market Research (B2B SaaS) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jan 2023 - May 2024</font>", compln))
b("<b>Drove process and efficiency improvement:</b> re-engineered global reporting through <b>Lean Six Sigma</b>, cutting "
  "<b>cycle times 20%</b> and standardizing KPIs across teams in multiple regions.")
b("Built Tableau / Power BI performance reporting for US commercial leadership, supporting <b>ARR that scaled into the $500MM range</b>.")
E.append(Paragraph("<b>Associate - Commercial Intelligence</b> &nbsp;|&nbsp; <font color='#6b6b6b'>May 2021 - Dec 2022</font>", compln))
b("Built financial / operational and unit-economics models and published quantitative research across <b>3 cycles</b> for leadership decisions.")
rule(sb=4)

sect("SKILLS")
E.append(Paragraph(
  "<b>Planning &amp; Operations:</b> Capacity Planning | Demand Forecasting (Regression) | Forecast vs. Actuals Tracking | "
  "KPI Ownership | Root-Cause Analysis &amp; Recovery Planning | Risk Anticipation &amp; Mitigation | Vendor / Partner Accountability | "
  "Annual Operating Plan (AOP) | Process Improvement (Lean Six Sigma) | Goal-Setting &amp; Leadership Reporting", skill))
E.append(Paragraph(
  "<b>Tools &amp; Leadership:</b> SQL | Advanced Excel | Tableau | Power BI | Google Apps Script | Stakeholder Management | "
  "Cross-functional Leadership | Coaching | Agile Project Management", skill))
rule(sb=4)

sect("CERTIFICATIONS")
b("<b>Agile Project Management</b> - Google &nbsp;&bull;&nbsp; <b>Mastering Advanced SQL Queries</b> - Coursera &nbsp;&bull;&nbsp; "
  "<b>From Excel to Power BI</b> - Knowledge Accelerators")
b("<b>Customer Value, Acquisition, and Retention</b> - University of Maryland &nbsp;&bull;&nbsp; <b>Generative AI for Leaders</b> - Vanderbilt University")
rule(sb=4)

sect("EDUCATION")
E.append(Paragraph("<b>B.Tech - Biotechnology</b> | Vellore Institute of Technology (VIT) | 2017 - 2021 | GPA: 8.55 / 10", edu))
E.append(Paragraph("<b>12th (ISC)</b> | Spring Dale College | 2016 | 88% &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>10th (ICSE)</b> | Spring Dale College | 2014 | 88%", edu))
rule(sb=4)

sect("LEADERSHIP &amp; ACHIEVEMENTS")
b("<b>People and operations leadership:</b> led operations, logistics and volunteer teams for corporate / college events hosting "
  "<b>800-1,000+ participants</b> - staffing, scheduling and real-time issue handling on the day.")
b("Measurable improvement record - <b>55% peak-event revenue uplift</b>, <b>19% YoY revenue growth</b>, <b>20% conversion lift</b>, <b>20% faster cycle times</b>.")

doc.build(E)
print("built", OUT)
