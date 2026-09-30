#!/usr/bin/env python3
"""Juhi Bhalla resume in Vishal Rajak's format (single-column, bold metrics). 1 page, ATS-safe."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable, KeepTogether
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY

BLACK = colors.HexColor("#1a1a1a"); GREY = colors.HexColor("#6b6b6b"); RULE = colors.HexColor("#b7b7b7")
LINKB = "#0563C1"
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=15.5, textColor=BLACK, leading=18, spaceAfter=2)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.9, textColor=BLACK, leading=11.5, spaceAfter=1)
tagline = ParagraphStyle("tag", fontName="Helvetica", fontSize=8.6, textColor=GREY, leading=11)
sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=10.3, textColor=BLACK, leading=12, spaceBefore=5, spaceAfter=2)
summ = ParagraphStyle("summ", fontName="Helvetica", fontSize=8.8, textColor=BLACK, leading=11.4, alignment=TA_JUSTIFY)
compln = ParagraphStyle("compln", fontName="Helvetica", fontSize=9.2, textColor=BLACK, leading=12, spaceBefore=3, spaceAfter=1)
intro = ParagraphStyle("intro", fontName="Helvetica-Bold", fontSize=8.7, textColor=BLACK, leading=11.2, spaceAfter=1)
bul = ParagraphStyle("bul", fontName="Helvetica", fontSize=8.7, textColor=BLACK, leading=11.2, leftIndent=10, bulletIndent=1, spaceAfter=1.5)
edu = ParagraphStyle("edu", fontName="Helvetica", fontSize=8.8, textColor=BLACK, leading=12.5)
skill = ParagraphStyle("skill", fontName="Helvetica", fontSize=8.8, textColor=BLACK, leading=13)

doc = SimpleDocTemplate(OUT, pagesize=A4, topMargin=11*mm, bottomMargin=9*mm, leftMargin=14*mm,
                        rightMargin=14*mm, title="Juhi Bhalla - Resume", author="Juhi Bhalla")
E = []
def rule(sb=3, sa=2): E.append(HRFlowable(width="100%", thickness=0.7, color=RULE, spaceBefore=sb, spaceAfter=sa))
def sect(t): E.append(Paragraph(t, sec))
def b(t): E.append(Paragraph(f"&bull;&nbsp;&nbsp;{t}", bul))
def jobline(company, rest, dates):
    E.append(Paragraph(f"<b>{company}</b> - {rest} &nbsp;|&nbsp; <font color='#6b6b6b'>{dates}</font>", compln))

# ---------- HEADER ----------
E.append(Paragraph("JUHI BHALLA", name))
E.append(Paragraph(
  "+91 88709 52224 &nbsp;|&nbsp; juhibhalla.jblko@gmail.com &nbsp;|&nbsp; "
  f"<link href='https://www.linkedin.com/in/juhi-bhalla' color='{LINKB}'><u>LinkedIn</u></link> &nbsp;|&nbsp; Bengaluru, India", contact))
E.append(Paragraph("Business Analyst | E-commerce &amp; Retail | Category Growth | Assortment, Pricing &amp; Promotions | Demand Planning | Data Analytics", tagline))
rule(sb=4, sa=1)

# ---------- SUMMARY ----------
sect("PROFESSIONAL SUMMARY")
E.append(Paragraph(
  "E-commerce and retail Business Analyst with 5+ years owning category growth and analytics at Flipkart and Enverus "
  "(B2B SaaS). Expert in category strategy, assortment, pricing and promotions, demand forecasting, and 360&deg; "
  "reporting - turning data into revenue and margin growth. Known for solving ambiguous problems through analytics "
  "and cross-functional stakeholder management.", summ))
rule()

# ---------- EXPERIENCE ----------
sect("EXPERIENCE")
jobline("Flipkart", "Business Analyst - Large Appliances (eCommerce Marketplace)", "Jun 2024 - Sep 2026")
E.append(Paragraph("Owned category, seller &amp; SKU performance for a large marketplace category - driving growth via "
                   "assortment, pricing, promotions, and demand planning across GMV, conversion, and in-stock.", intro))
b("Owned <b>cohort and SKU trend analysis</b> (YoY &amp; MoM); used these insights to drive <b>product exchange bump-ups</b> on select high-value SKUs, growing overall category <b>revenue by 19% YoY</b>.")
b("Led <b>market research and assortment / selection analysis</b>; introduced the <b>Windows segment</b> into the assortment, lifting overall <b>Flipkart market-penetration share by ~1%</b>.")
b("Ran <b>cohort analysis, customer funnel metrics, and user personas</b>; launched <b>coupons for Flipkart loyal customers</b>, capturing category customers and driving a <b>20% improvement in conversion</b>.")
b("Analyzed <b>payment methods and bank cross-demographic behavior</b>; rolled out <b>South-specific bank coupons</b>, improving overall <b>bank-offer adoption and conversion across the South region</b>.")
b("Built and automated <b>Tableau / Power BI dashboards</b> (SQL, Google Apps Script) with standardized KPIs, giving leaders real-time visibility into category health.")
b("Built regression-based <b>demand and sales forecasting</b> to guide category planning; data-driven planning drove a <b>55% category revenue uplift during Big Billion Days</b>.")

jobline("Enverus", "Business Analyst I - Market Research (B2B SaaS)", "Jan 2023 - May 2024")
b("Built and maintained <b>Tableau / Power BI dashboards</b> giving US commercial leaders real-time visibility into sales trends and KPIs, supporting <b>ARR that scaled into the $500MM range</b>.")
b("Re-engineered reporting through <b>Lean Six Sigma</b> optimization, driving a <b>20% reduction in cycle times</b> and standardizing KPIs across global teams.")

E.append(Paragraph("<b>Associate - Commercial Intelligence</b> &nbsp;|&nbsp; <font color='#6b6b6b'>May 2021 - Dec 2022</font>", compln))
b("Published quantitative research across <b>3 cycles</b> and built financial / operational and unit-economics models; produced competitive and price intelligence to support leadership decisions.")
rule(sb=4)

# ---------- EDUCATION ----------
sect("EDUCATION")
E.append(Paragraph("<b>B.Tech - Biotechnology</b> | Vellore Institute of Technology (VIT) | 2017 - 2021 | GPA: 8.55 / 10", edu))
E.append(Paragraph("<b>12th (ISC)</b> | Spring Dale College | 2016 | 88% &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>10th (ICSE)</b> | Spring Dale College | 2014 | 88%", edu))
rule(sb=4)

# ---------- SKILLS ----------
sect("SKILLS")
E.append(Paragraph(
  "Category Growth | Category Management | Assortment &amp; Merchandising | Pricing &amp; Promotions | Demand Forecasting | "
  "Cohort &amp; Conversion Analysis | Competitive Intelligence | Requirements (BRD / FRD) | Agile / Scrum | "
  "Stakeholder Management | Dashboards &amp; 360&deg; Reporting | SQL | Tableau | Power BI | Advanced Excel | "
  "Jira | Confluence | Python (familiarity)", skill))
rule(sb=4)

# ---------- CERTIFICATIONS ----------
sect("CERTIFICATIONS")
b("<b>Agile Project Management</b> - Google")
b("<b>Mastering Advanced SQL Queries</b> - Coursera")
b("<b>From Excel to Power BI</b> - Knowledge Accelerators")
b("<b>Customer Value, Acquisition, and Retention</b> - University of Maryland, College Park")
b("<b>Introduction to Generative AI</b> - Google Cloud")
b("<b>Generative AI for Leaders</b> - Vanderbilt University")
rule(sb=4)

# ---------- LEADERSHIP & ACHIEVEMENTS ----------
sect("LEADERSHIP &amp; ACHIEVEMENTS")
b("Led operations, logistics &amp; teams for corporate / college events hosting <b>800-1,000+ participants</b>.")
b("Consistent data-led growth record - <b>55% BBD category uplift</b>, <b>19% YoY revenue growth</b>, and <b>20% faster reporting</b>.")

doc.build(E)
print("built", OUT)
