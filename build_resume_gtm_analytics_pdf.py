#!/usr/bin/env python3
"""Juhi Bhalla - Senior Analytics & Insights Analyst (GTM). 1 page, ATS-safe, hyphens only."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

BLACK = colors.HexColor("#1a1a1a"); GREY = colors.HexColor("#6b6b6b"); RULE = colors.HexColor("#b7b7b7")
LINKB = "#0563C1"
DEMO = "https://quwgk58euw9vyk7yewlnvo.streamlit.app/"
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_GTM_Analytics.pdf"

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
E.append(Paragraph("Senior Analytics &amp; Insights Analyst | GTM Analytics (Sales, Customer Success, Business Development) | KPI Design | "
                   "Dashboards &amp; Data Storytelling | SQL, Tableau, Power BI | Statistical Methods", tagline))
rule(sb=4, sa=1)

sect("PROFESSIONAL SUMMARY")
E.append(Paragraph(
  "Analytics professional with 5+ years turning data into revenue decisions for commercial teams at Flipkart (e-commerce) and "
  "Enverus (B2B SaaS). I partner with sales, business development and commercial leadership to <b>define KPIs, build the dashboards "
  "they run on, and surface revenue, retention and growth opportunities</b> - then validate them with data. Strong in SQL, Tableau, "
  "Power BI and statistical methods (regression forecasting, cohort and funnel analysis), and known for clear data storytelling, "
  "standardized reporting and prioritizing competing asks in fast, results-driven teams.", summ))
rule()

sect("EXPERIENCE")
E.append(Paragraph("<b>Flipkart</b> - Business Analyst - Large Appliances (eCommerce Marketplace) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jun 2024 - Sep 2026</font>", compln))
E.append(Paragraph("Analytics partner to category, seller / business-development and marketing teams for a large marketplace category - "
                   "owning KPIs, insights and recommendations across GMV, conversion, retention and in-stock.", intro))
b("<b>Identified a revenue opportunity</b> from cohort and SKU trend analysis (YoY &amp; MoM) on under-converting high-value SKUs; "
  "recommended product-exchange bump-ups that grew category <b>revenue 19% YoY</b>.")
b("<b>Improved customer retention:</b> used cohort analysis, funnel metrics and user personas to size the loyal-customer opportunity; "
  "the resulting loyalty-coupon program drove a <b>20% improvement in conversion</b> and stronger repeat purchase.")
b("Analyzed payment-method and bank behavior across demographics to <b>validate a regional growth opportunity</b>; South-specific bank "
  "coupons improved bank-offer adoption and conversion across the region.")
b("Used <b>market research and competitive analysis</b> to make the case for a new segment (Windows), lifting <b>Flipkart market-penetration share ~1%</b>.")
b("<b>Defined standardized KPIs</b> and built automated <b>Tableau / Power BI dashboards</b> (SQL, Google Apps Script) used in weekly "
  "performance reviews; partnered with data and engineering teams on source data and metric definitions to keep reporting clean and consistent.")
b("Built <b>regression-based demand and sales forecasting</b> (statistical modeling) to guide planning; data-driven planning drove a "
  "<b>55% category revenue uplift during Big Billion Days</b>.")

E.append(Paragraph("<b>Enverus</b> - Business Analyst I - Market Research (B2B SaaS) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jan 2023 - May 2024</font>", compln))
b("<b>GTM analytics partner to US commercial / sales leadership:</b> built and maintained Tableau / Power BI dashboards on sales trends, "
  "pipeline and KPIs, supporting <b>ARR that scaled into the $500MM range</b>.")
b("<b>Established operational rigor:</b> re-engineered reporting through Lean Six Sigma, cutting <b>cycle times 20%</b> and standardizing "
  "KPIs and performance reporting across global teams.")
E.append(Paragraph("<b>Associate - Commercial Intelligence</b> &nbsp;|&nbsp; <font color='#6b6b6b'>May 2021 - Dec 2022</font>", compln))
b("Published quantitative market research across <b>3 cycles</b>, built unit-economics models, and delivered competitive and pricing "
  "intelligence that shaped <b>go-to-market and leadership decisions</b>.")
rule(sb=4)

sect("SKILLS")
E.append(Paragraph(
  "<b>GTM &amp; Business:</b> GTM Strategy &amp; Analytics | Sales Performance Analysis | Customer Retention &amp; Churn Analysis | "
  "Revenue Opportunity Sizing | KPI Definition | Performance Reviews | Competitive Intelligence | Business Acumen | Cross-functional Collaboration | Stakeholder Management", skill))
E.append(Paragraph(
  "<b>Analytics &amp; Tools:</b> SQL | Tableau | Power BI | Advanced Excel | Statistical Methods (Regression, Hypothesis Testing, "
  "Cohort &amp; Funnel Analysis) | Forecasting | Dashboard Adoption | Data Quality | Data Storytelling | Jira | Confluence | Python (familiarity)", skill))
rule(sb=4)

sect("CERTIFICATIONS")
b("<b>Mastering Advanced SQL Queries</b> - Coursera &nbsp;&bull;&nbsp; <b>From Excel to Power BI</b> - Knowledge Accelerators &nbsp;&bull;&nbsp; "
  "<b>Agile Project Management</b> - Google")
b("<b>Customer Value, Acquisition, and Retention</b> - University of Maryland &nbsp;&bull;&nbsp; <b>Introduction to Generative AI</b> - Google Cloud "
  "&nbsp;&bull;&nbsp; <b>Generative AI for Leaders</b> - Vanderbilt University")
rule(sb=4)

sect("EDUCATION")
E.append(Paragraph("<b>B.Tech - Biotechnology</b> | Vellore Institute of Technology (VIT) | 2017 - 2021 | GPA: 8.55 / 10", edu))
E.append(Paragraph("<b>12th (ISC)</b> | Spring Dale College | 2016 | 88% &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>10th (ICSE)</b> | Spring Dale College | 2014 | 88%", edu))
rule(sb=4)

sect("LEADERSHIP &amp; ACHIEVEMENTS")
b("Led operations, logistics &amp; teams for corporate / college events hosting <b>800-1,000+ participants</b>.")
b("Insight-to-revenue record - <b>55% BBD category uplift</b>, <b>19% YoY revenue growth</b>, <b>20% conversion lift</b>, <b>20% faster reporting</b>.")

doc.build(E)
print("built", OUT)
