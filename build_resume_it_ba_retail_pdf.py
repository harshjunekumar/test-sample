#!/usr/bin/env python3
"""Juhi Bhalla - IT Business Analyst - Retail / CPG. 1 page, ATS-safe, hyphens only."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

BLACK = colors.HexColor("#1a1a1a"); GREY = colors.HexColor("#6b6b6b"); RULE = colors.HexColor("#b7b7b7")
LINKB = "#0563C1"
DEMO = "https://quwgk58euw9vyk7yewlnvo.streamlit.app/"
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_IT_BA_Retail.pdf"

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
  f"<link href='https://www.linkedin.com/in/juhi-bhalla' color='{LINKB}'><u>LinkedIn</u></link> &nbsp;|&nbsp; Bengaluru, India (Open to Hyderabad / Pune, Hybrid)", contact))
E.append(Paragraph("IT Business Analyst | Retail &amp; E-commerce Domain | Requirements, User Stories &amp; Functional Specs | SQL &amp; Data Analysis | "
                   "Agile / Scrum | UAT | Process Mapping &amp; Gap Analysis | Jira &amp; Confluence", tagline))
rule(sb=4, sa=1)

sect("PROFESSIONAL SUMMARY")
E.append(Paragraph(
  "Business Analyst with 5+ years in retail e-commerce (Flipkart) and B2B SaaS (Enverus), working between business and technology "
  "teams to <b>gather requirements, write functional specifications and user stories, analyze data in SQL, and support delivery "
  "through UAT</b> in Agile / Scrum teams. Deep understanding of retail business processes - assortment, pricing, promotions, "
  "payments, demand planning - and of customer journeys from browse to checkout. Strong in process mapping, gap analysis, "
  "stakeholder management and reporting in Excel, Power BI and Tableau.", summ))
rule()

sect("EXPERIENCE")
E.append(Paragraph("<b>Flipkart</b> - Business Analyst - Large Appliances (eCommerce Marketplace) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jun 2024 - Sep 2026</font>", compln))
E.append(Paragraph("Business analyst for a large retail marketplace category - translating business needs into requirements for "
                   "in-app features and processes across assortment, pricing, promotions, payments and in-stock.", intro))
b("<b>Gathered and documented requirements</b> with category, marketing, payments and tech stakeholders; wrote <b>BRDs / FRDs, user "
  "stories and acceptance criteria</b> in Jira and Confluence for customer-facing features.")
b("Used <b>SQL</b> cohort and SKU trend analysis (YoY &amp; MoM) to define the <b>product-exchange bump-up</b> requirement for high-value "
  "SKUs, growing category <b>revenue 19% YoY</b>.")
b("Mapped the <b>customer journey and funnel</b> (personas, cohort and conversion analysis) to identify gaps; specified "
  "<b>loyalty-customer coupons</b> that drove a <b>20% improvement in conversion</b>.")
b("Ran <b>gap analysis</b> on payment-method and bank behavior across regions; specified <b>South-specific bank-offer coupons in the "
  "payment flow</b> and supported <b>UAT</b> of eligibility and discount rules before go-live, improving offer adoption and conversion.")
b("Performed <b>process mapping</b> and market / selection analysis for the category plan; introduced the <b>Windows segment</b>, "
  "lifting <b>Flipkart market-penetration share ~1%</b>.")
b("Built automated <b>Tableau / Power BI</b> reporting (SQL, Google Apps Script) with standardized KPIs, and regression-based demand "
  "forecasting that drove a <b>55% category revenue uplift during Big Billion Days</b>.")

E.append(Paragraph("<b>Enverus</b> - Business Analyst I - Market Research (B2B SaaS) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jan 2023 - May 2024</font>", compln))
b("Gathered reporting requirements from US commercial stakeholders and delivered <b>Tableau / Power BI dashboards</b> on sales trends "
  "and KPIs, supporting <b>ARR that scaled into the $500MM range</b>.")
b("Mapped the as-is reporting workflow and re-engineered it through <b>Lean Six Sigma</b>, cutting <b>cycle times 20%</b> and "
  "standardizing KPIs across global teams.")
E.append(Paragraph("<b>Associate - Commercial Intelligence</b> &nbsp;|&nbsp; <font color='#6b6b6b'>May 2021 - Dec 2022</font>", compln))
b("Published quantitative research across <b>3 cycles</b> and built financial / operational and unit-economics models; produced "
  "competitive and price intelligence for leadership decisions.")
rule(sb=4)

sect("PROJECTS &amp; CERTIFICATIONS")
E.append(Paragraph("<b>AI Personal Stylist</b> - Conversational Fashion Recommender (Streamlit, Python, Generative AI) &nbsp;|&nbsp; "
                   f"<link href='{DEMO}' color='{LINKB}'><u>Live Demo</u></link> &nbsp;|&nbsp; <font color='#6b6b6b'>2026 (Work in Progress)</font>", compln))
b("Defined the problem, user flow and recommendation logic for a retail styling chatbot: <b>4 questions</b> produce a style persona "
  "and <b>3 complete looks</b> linked to Google Shopping; <b>&ldquo;complete the look&rdquo;</b> designed as a basket-size / AOV lever.")
E.append(Paragraph("Certifications", subl))
b("<b>Agile Project Management</b> - Google &nbsp;&bull;&nbsp; <b>Mastering Advanced SQL Queries</b> - Coursera &nbsp;&bull;&nbsp; "
  "<b>From Excel to Power BI</b> - Knowledge Accelerators")
b("<b>Customer Value, Acquisition, and Retention</b> - University of Maryland &nbsp;&bull;&nbsp; <b>Introduction to Generative AI</b> - "
  "Google Cloud &nbsp;&bull;&nbsp; <b>Generative AI for Leaders</b> - Vanderbilt University")
rule(sb=4)

sect("SKILLS")
E.append(Paragraph(
  "<b>Business Analysis:</b> Requirements Gathering | BRD / FRD &amp; Functional Specifications | User Stories &amp; Acceptance Criteria | "
  "Process Mapping (As-Is / To-Be) | Gap Analysis | UAT Support | Agile / Scrum | Stakeholder Management | Workflow Documentation", skill))
E.append(Paragraph(
  "<b>Domain &amp; Tools:</b> Retail / E-commerce Processes (Assortment, Pricing, Promotions, Payments, Inventory) | Customer Journeys | Consumer Goods / CPG (familiarity) | "
  "SQL | Advanced Excel | Power BI | Tableau | Jira | Confluence | Python (familiarity)", skill))
rule(sb=4)

sect("EDUCATION")
E.append(Paragraph("<b>B.Tech - Biotechnology</b> | Vellore Institute of Technology (VIT) | 2017 - 2021 | GPA: 8.55 / 10", edu))
E.append(Paragraph("<b>12th (ISC)</b> | Spring Dale College | 2016 | 88% &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>10th (ICSE)</b> | Spring Dale College | 2014 | 88%", edu))
rule(sb=4)

sect("LEADERSHIP &amp; ACHIEVEMENTS")
b("Led operations, logistics &amp; teams for corporate / college events hosting <b>800-1,000+ participants</b>.")
b("Delivery record - <b>55% BBD category uplift</b>, <b>19% YoY revenue growth</b>, <b>20% conversion lift</b>, <b>20% faster reporting</b>.")

doc.build(E)
print("built", OUT)
