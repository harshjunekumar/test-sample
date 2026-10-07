#!/usr/bin/env python3
"""Juhi Bhalla - Category Manager (clean single-column, from ChannelLead base + project). 1 page, ATS-safe, no dashes."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

BLACK = colors.HexColor("#1a1a1a"); GREY = colors.HexColor("#6b6b6b"); RULE = colors.HexColor("#b7b7b7")
LINKB = "#0563C1"
DEMO = "https://quwgk58euw9vyk7yewlnvo.streamlit.app/"
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_CategoryManager.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=15.5, textColor=BLACK, leading=18, spaceAfter=2)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.9, textColor=BLACK, leading=11.5, spaceAfter=1)
tagline = ParagraphStyle("tag", fontName="Helvetica", fontSize=8.5, textColor=GREY, leading=11)
sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=10.1, textColor=BLACK, leading=11.2, spaceBefore=3.6, spaceAfter=1.6)
summ = ParagraphStyle("summ", fontName="Helvetica", fontSize=8.65, textColor=BLACK, leading=11.0, alignment=TA_JUSTIFY)
compln = ParagraphStyle("compln", fontName="Helvetica", fontSize=9.0, textColor=BLACK, leading=11.4, spaceBefore=2.6, spaceAfter=1)
intro = ParagraphStyle("intro", fontName="Helvetica-Bold", fontSize=8.55, textColor=BLACK, leading=10.8, spaceAfter=1)
bul = ParagraphStyle("bul", fontName="Helvetica", fontSize=8.55, textColor=BLACK, leading=10.8, leftIndent=10, bulletIndent=1, spaceAfter=1.2)
edu = ParagraphStyle("edu", fontName="Helvetica", fontSize=8.65, textColor=BLACK, leading=11.8)
skill = ParagraphStyle("skill", fontName="Helvetica", fontSize=8.55, textColor=BLACK, leading=11.9)
subl = ParagraphStyle("subl", fontName="Helvetica-Bold", fontSize=8.5, textColor=GREY, leading=10.6, spaceBefore=2.4, spaceAfter=1)

doc = SimpleDocTemplate(OUT, pagesize=A4, topMargin=10*mm, bottomMargin=8*mm, leftMargin=14*mm,
                        rightMargin=14*mm, title="Juhi Bhalla - Resume", author="Juhi Bhalla")
E = []
def rule(sb=3, sa=2): E.append(HRFlowable(width="100%", thickness=0.7, color=RULE, spaceBefore=sb, spaceAfter=sa))
def sect(t): E.append(Paragraph(t, sec))
def b(t): E.append(Paragraph(f"&bull;&nbsp;&nbsp;{t}", bul))

# ---------- HEADER ----------
E.append(Paragraph("JUHI BHALLA", name))
E.append(Paragraph(
  "+91 88709 52224 &nbsp;|&nbsp; juhibhalla.jblko@gmail.com &nbsp;|&nbsp; "
  f"<link href='https://www.linkedin.com/in/juhi-bhalla' color='{LINKB}'><u>LinkedIn</u></link> &nbsp;|&nbsp; Bengaluru, India", contact))
E.append(Paragraph("Category Manager | E-commerce &amp; Retail | Category Strategy, Assortment &amp; Selection | Pricing &amp; Promotions | "
                   "Demand &amp; Inventory Planning | Vendor / Seller Management | Data Analytics", tagline))
rule(sb=4, sa=1)

# ---------- SUMMARY ----------
sect("PROFESSIONAL SUMMARY")
E.append(Paragraph(
  "Category management professional with 5+ years growing e-commerce and retail categories at Flipkart and Enverus "
  "(B2B SaaS), pairing category strategy with deep analytics. I own category performance against <b>sales and margin</b> "
  "targets - planning assortment, pricing and promotions, tracking performance and driving corrections, and analyzing "
  "market trends and competitor activity to find growth. I develop and execute category strategies, partner with "
  "sellers / vendors, and coordinate cross-functionally with marketing, sales and supply-chain teams. Data-driven "
  "planning drove a 55% category revenue uplift during Big Billion Days.", summ))
rule()

# ---------- EXPERIENCE ----------
sect("EXPERIENCE")
E.append(Paragraph("<b>Flipkart</b> - Category Manager - Large Appliances (eCommerce Marketplace) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jun 2024 - Sep 2026</font>", compln))
E.append(Paragraph("Owned the growth and commercial performance of a large e-commerce category end-to-end - driving sales, "
                   "margin and conversion through assortment, pricing, promotions and demand planning, in partnership with "
                   "sellers / vendors and marketing, sales and supply-chain teams.", intro))
b("Owned category <b>sales and margin levers</b>; through cohort and SKU trend analysis (YoY &amp; MoM), drove <b>product-exchange "
  "bump-ups</b> on high-value SKUs that grew category <b>revenue 19% YoY</b>.")
b("Set <b>category and assortment strategy</b> and partnered with <b>sellers / vendors</b> on selection and terms (market research "
  "+ selection analysis); introduced the <b>Windows segment</b>, expanding coverage and lifting <b>Flipkart market-penetration share ~1%</b>.")
b("Led <b>consumer understanding</b> - cohort analysis, funnel metrics and user personas - and launched <b>targeted loyalty-coupon "
  "campaigns</b> that improved <b>conversion 20%</b> and strengthened repeat purchase.")
b("Planned <b>promotions and offer spend</b>; analyzed payment and regional consumer behavior to roll out <b>South-specific bank "
  "coupons</b>, improving offer adoption and conversion across the region.")
b("Built automated <b>Tableau / Power BI dashboards</b> (SQL, Google Apps Script) with standardized KPIs, giving leadership "
  "real-time visibility into <b>category sales, margin and health</b>.")
b("Built <b>demand and sales forecasting</b> models to guide buying, pricing and promotion planning; data-driven planning drove "
  "a <b>55% category revenue uplift during Big Billion Days</b>.")

E.append(Paragraph("<b>Enverus</b> - Business Analyst I - Market Research (B2B SaaS) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jan 2023 - May 2024</font>", compln))
b("Built and maintained <b>Tableau / Power BI dashboards</b> giving commercial leaders real-time visibility into performance "
  "trends and KPIs, supporting <b>ARR that scaled into the $500MM range</b>.")
b("Re-engineered reporting through <b>Lean Six Sigma</b>, driving a <b>20% reduction in cycle times</b> and standardizing KPIs across "
  "global teams.")

E.append(Paragraph("<b>Associate - Commercial Intelligence</b> &nbsp;|&nbsp; <font color='#6b6b6b'>May 2021 - Dec 2022</font>", compln))
b("Published quantitative <b>market and consumer research</b> across 3 cycles and built unit-economics and pricing models; produced "
  "competitive and price intelligence to guide leadership strategy.")
rule(sb=4)

# ---------- PROJECTS & CERTIFICATIONS ----------
sect("PROJECTS &amp; CERTIFICATIONS")
E.append(Paragraph("<b>AI Personal Stylist</b> - Conversational Fashion Recommender (Streamlit, Python, Generative AI) &nbsp;|&nbsp; "
                   f"<link href='{DEMO}' color='{LINKB}'><u>Live Demo</u></link> &nbsp;|&nbsp; <font color='#6b6b6b'>2026 (Work in Progress)</font>", compln))
b("Designed and built a chatbot that turns <b>4 quick questions</b> (gender/age, style, vibe, colour) into a personalized <b>style persona</b> "
  "with <b>3 complete, colour-matched looks</b> - outfit plus accessories - each linked to <b>Google Shopping</b>, with 2026 trend inputs from current fashion sources.")
b("Applied product thinking end-to-end (problem framing, user flow, recommendation logic): personas that <b>change the recommendation, "
  "not just the label</b>; <b>4 questions vs 20 filters</b> to cut friction; and <b>&ldquo;complete the look&rdquo;</b> as a <b>basket-size / AOV lever</b>.")
E.append(Paragraph("Certifications", subl))
b("<b>Customer Value, Acquisition, and Retention</b> - University of Maryland, College Park &nbsp;&bull;&nbsp; <b>Agile Project Management</b> - Google")
b("<b>Mastering Advanced SQL Queries</b> - Coursera &nbsp;&bull;&nbsp; <b>From Excel to Power BI</b> - Knowledge Accelerators")
rule(sb=4)

# ---------- SKILLS ----------
sect("SKILLS")
E.append(Paragraph(
  "Category Management | Category Strategy &amp; Execution | Assortment &amp; Selection Planning | Pricing &amp; Promotions | "
  "Sales &amp; Margin / Category P&amp;L | Vendor / Seller Performance &amp; Negotiation | Demand &amp; Inventory Planning | "
  "Market &amp; Competitive Intelligence | Consumer Insights | Cohort &amp; Conversion Analysis | Promotional / Deal Analysis | "
  "Growth Opportunity Identification | Cross-functional (Marketing, Sales, Supply Chain, Product) | Stakeholder Management | "
  "Product Thinking | SQL | Tableau | Power BI | Advanced Excel | Generative AI / LLM Apps", skill))
rule(sb=4)

# ---------- EDUCATION ----------
sect("EDUCATION")
E.append(Paragraph("<b>B.Tech - Biotechnology</b> | Vellore Institute of Technology (VIT) | 2017 - 2021 | GPA: 8.55 / 10", edu))
E.append(Paragraph("<b>12th (ISC)</b> | Spring Dale College | 2016 | 88% &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>10th (ICSE)</b> | Spring Dale College | 2014 | 88%", edu))
rule(sb=4)

# ---------- LEADERSHIP & ACHIEVEMENTS ----------
sect("LEADERSHIP &amp; ACHIEVEMENTS")
b("Led cross-functional initiatives and small teams; directed operations, logistics &amp; teams for corporate / college events hosting <b>800-1,000+ participants</b>.")
b("Consistent category growth record - <b>55% BBD category uplift</b>, <b>19% YoY revenue growth</b>, <b>20% conversion lift</b>, and <b>20% faster reporting</b>.")

doc.build(E)
print("built", OUT)
