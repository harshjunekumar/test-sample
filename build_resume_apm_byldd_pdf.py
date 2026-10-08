#!/usr/bin/env python3
"""Juhi Bhalla - Associate Product Manager (Byldd). 1 page, ATS-safe, hyphens only."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

BLACK = colors.HexColor("#1a1a1a"); GREY = colors.HexColor("#6b6b6b"); RULE = colors.HexColor("#b7b7b7")
LINKB = "#0563C1"
DEMO = "https://quwgk58euw9vyk7yewlnvo.streamlit.app/"
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_APM_Byldd.pdf"

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
  f"<link href='https://www.linkedin.com/in/juhi-bhalla' color='{LINKB}'><u>LinkedIn</u></link> &nbsp;|&nbsp; Bengaluru, India (Open to Remote)", contact))
E.append(Paragraph("Associate Product Manager | Business Analyst | Product Discovery &amp; Prioritization | User Stories &amp; Requirements | "
                   "Product Analytics | AI-Native Workflow | E-commerce &amp; SaaS", tagline))
rule(sb=4, sa=1)

sect("PROFESSIONAL SUMMARY")
E.append(Paragraph(
  "Business Analyst with 5+ years in product-adjacent roles at Flipkart (e-commerce) and Enverus (B2B SaaS), now moving into "
  "product management. I start with <b>why</b> - using user personas, funnel and cohort data to decide what gets built and what "
  "gets cut - then write requirements and user stories, work with engineering and design to ship, and measure what users "
  "actually do before iterating. Shipped in-app features (product exchange, loyalty and bank-offer coupons) that moved revenue "
  "and conversion, and independently built and launched an AI product. Comfortable with ambiguity and fast cycles; I use AI "
  "daily for research, analysis and prototyping.", summ))
rule()

sect("EXPERIENCE")
E.append(Paragraph("<b>Flipkart</b> - Business Analyst - Large Appliances (eCommerce Marketplace) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jun 2024 - Sep 2026</font>", compln))
E.append(Paragraph("Owned category, seller &amp; SKU performance for a large marketplace category - turning user and market data "
                   "into in-app features and decisions across GMV, conversion and in-stock.", intro))
b("Spotted from cohort and SKU trend analysis (YoY &amp; MoM) that high-value SKUs were under-converting; scoped and drove the "
  "<b>product-exchange bump-up feature</b> for those SKUs, growing category <b>revenue 19% YoY</b>.")
b("Built <b>user personas, funnel and cohort analysis</b> to define the problem, then launched <b>in-app coupons for loyal customers</b> - "
  "capturing category customers and driving a <b>20% improvement in conversion</b>.")
b("Analyzed payment-method and bank behavior across demographics; shipped <b>South-specific bank-offer coupons in the payment flow</b>, "
  "improving bank-offer adoption and conversion across the South region.")
b("Used <b>market research and selection analysis</b> to make the case for a new segment (Windows); launched it, lifting "
  "<b>Flipkart market-penetration share ~1%</b>.")
b("Wrote requirements and worked with <b>engineering, design, marketing and supply-chain</b> teams to ship and track changes; built "
  "automated <b>Tableau / Power BI dashboards</b> (SQL, Google Apps Script) to monitor adoption and KPIs post-launch.")
b("Built regression-based <b>demand and sales forecasting</b> to guide planning; data-driven planning drove a "
  "<b>55% category revenue uplift during Big Billion Days</b>.")

E.append(Paragraph("<b>Enverus</b> - Business Analyst I - Market Research (B2B SaaS) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jan 2023 - May 2024</font>", compln))
b("Gathered requirements from US commercial stakeholders and built <b>Tableau / Power BI dashboards</b> they used daily, supporting "
  "<b>ARR that scaled into the $500MM range</b>.")
b("Re-engineered the reporting workflow with <b>Lean Six Sigma</b>, cutting <b>cycle times 20%</b> and standardizing KPIs across global teams.")
E.append(Paragraph("<b>Associate - Commercial Intelligence</b> &nbsp;|&nbsp; <font color='#6b6b6b'>May 2021 - Dec 2022</font>", compln))
b("Published quantitative market research across <b>3 cycles</b> and built unit-economics models and competitive intelligence for leadership decisions.")
rule(sb=4)

sect("PROJECTS &amp; CERTIFICATIONS")
E.append(Paragraph("<b>AI Personal Stylist</b> - 0-to-1 AI product, built and launched solo (Streamlit, Python, Generative AI) &nbsp;|&nbsp; "
                   f"<link href='{DEMO}' color='{LINKB}'><u>Live Demo</u></link> &nbsp;|&nbsp; <font color='#6b6b6b'>2026 (Live, iterating)</font>", compln))
b("<b>Problem:</b> shoppers don't leave for lack of choice - they leave because there's too much and they can't picture what suits them. "
  "<b>Solution:</b> a chatbot that turns <b>4 questions</b> into a style persona and <b>3 complete looks</b>, each linked to Google Shopping.")
b("<b>Product calls:</b> cut 20 filters down to 4 questions to reduce friction; made personas <b>change the recommendation, not just the label</b>; "
  "treated <b>&ldquo;complete the look&rdquo;</b> as a basket-size lever. Shipped, gathering user feedback, and iterating on the next version.")
E.append(Paragraph("Certifications", subl))
b("<b>Agile Project Management</b> - Google &nbsp;&bull;&nbsp; <b>Generative AI for Leaders</b> - Vanderbilt University &nbsp;&bull;&nbsp; <b>Introduction to Generative AI</b> - Google Cloud")
b("<b>Mastering Advanced SQL Queries</b> - Coursera &nbsp;&bull;&nbsp; <b>From Excel to Power BI</b> - Knowledge Accelerators &nbsp;&bull;&nbsp; "
  "<b>Customer Value, Acquisition, and Retention</b> - University of Maryland")
rule(sb=4)

sect("SKILLS")
E.append(Paragraph(
  "<b>Product:</b> Product Discovery | Prioritization &amp; Scoping | User Stories &amp; Acceptance Criteria | Requirements (BRD / FRD) | "
  "User Personas | User Flows &amp; Wireframe Review | Product Analytics (Funnel, Cohort, Conversion) | Post-launch Measurement &amp; Iteration | Client / Stakeholder Demos | "
  "Agile / Scrum", skill))
E.append(Paragraph(
  "<b>Tools:</b> Jira | Confluence | SQL | Tableau | Power BI | Advanced Excel | Generative AI / LLM tools (ChatGPT, Claude) | "
  "Streamlit | Python (familiarity)", skill))
rule(sb=4)

sect("EDUCATION")
E.append(Paragraph("<b>B.Tech - Biotechnology</b> | Vellore Institute of Technology (VIT) | 2017 - 2021 | GPA: 8.55 / 10", edu))
E.append(Paragraph("<b>12th (ISC)</b> | Spring Dale College | 2016 | 88% &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>10th (ICSE)</b> | Spring Dale College | 2014 | 88%", edu))
rule(sb=4)

sect("LEADERSHIP &amp; ACHIEVEMENTS")
b("Led operations, logistics &amp; teams for corporate / college events hosting <b>800-1,000+ participants</b>.")
b("Shipped-impact record - <b>55% BBD category uplift</b>, <b>19% YoY revenue growth</b>, <b>20% conversion lift</b>, <b>20% faster reporting</b>.")

doc.build(E)
print("built", OUT)
