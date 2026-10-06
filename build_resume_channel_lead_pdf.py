#!/usr/bin/env python3
"""Juhi Bhalla - tailored for Channel Lead - Ecommerce (Brand Concepts Ltd). 1 page, ATS-safe, no dashes."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

BLACK = colors.HexColor("#1a1a1a"); GREY = colors.HexColor("#6b6b6b"); RULE = colors.HexColor("#b7b7b7")
LINKB = "#0563C1"
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_ChannelLead.pdf"

name = ParagraphStyle("name", fontName="Helvetica-Bold", fontSize=15.5, textColor=BLACK, leading=18, spaceAfter=2)
contact = ParagraphStyle("contact", fontName="Helvetica", fontSize=8.9, textColor=BLACK, leading=11.5, spaceAfter=1)
tagline = ParagraphStyle("tag", fontName="Helvetica", fontSize=8.5, textColor=GREY, leading=11)
sec = ParagraphStyle("sec", fontName="Helvetica-Bold", fontSize=10.3, textColor=BLACK, leading=12, spaceBefore=5, spaceAfter=2)
summ = ParagraphStyle("summ", fontName="Helvetica", fontSize=8.75, textColor=BLACK, leading=11.3, alignment=TA_JUSTIFY)
compln = ParagraphStyle("compln", fontName="Helvetica", fontSize=9.2, textColor=BLACK, leading=12, spaceBefore=3, spaceAfter=1)
intro = ParagraphStyle("intro", fontName="Helvetica-Bold", fontSize=8.65, textColor=BLACK, leading=11.1, spaceAfter=1)
bul = ParagraphStyle("bul", fontName="Helvetica", fontSize=8.65, textColor=BLACK, leading=11.1, leftIndent=10, bulletIndent=1, spaceAfter=1.4)
edu = ParagraphStyle("edu", fontName="Helvetica", fontSize=8.8, textColor=BLACK, leading=12.3)
skill = ParagraphStyle("skill", fontName="Helvetica", fontSize=8.7, textColor=BLACK, leading=12.6)

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
E.append(Paragraph("Channel Lead - E-commerce | Digital Business &amp; P&amp;L | Marketplace &amp; Quick-Commerce Growth | "
                   "Brand Strategy | Pricing, Promotions &amp; Digital Marketing | Consumer Insights", tagline))
rule(sb=4, sa=1)

# ---------- SUMMARY ----------
sect("PROFESSIONAL SUMMARY")
E.append(Paragraph(
  "E-commerce and digital-business professional with 5+ years driving channel growth, revenue and margin at Flipkart and "
  "Enverus (B2B SaaS). I own category commercials end-to-end - revenue, margin, pricing, promotions, assortment and demand "
  "planning - and partner closely with sales, marketing and operations to grow the digital channel. Fluent in the marketplace "
  "and quick-commerce landscape, consumer understanding and digital-marketing levers. A startup mindset suited to unscripted, "
  "ambiguous environments, using facts and trends to bring clarity and drive decisions.", summ))
rule()

# ---------- EXPERIENCE ----------
sect("EXPERIENCE")
E.append(Paragraph("<b>Flipkart</b> - Assistant Manager - Business Development, Large Appliances (eCommerce) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jun 2024 - Sep 2026</font>", compln))
E.append(Paragraph("Owned the growth and commercial performance of a large e-commerce category end-to-end - driving revenue, "
                   "margin and conversion through assortment, pricing, promotions and demand planning, in partnership with "
                   "sales, marketing and supply-chain teams.", intro))
b("Owned category <b>revenue and margin levers</b>; through cohort and SKU trend analysis (YoY &amp; MoM), drove <b>product-exchange "
  "bump-ups</b> on high-value SKUs that grew category <b>revenue 19% YoY</b>.")
b("Set <b>channel and assortment strategy</b> using market research and selection analysis; introduced the <b>Windows segment</b>, "
  "expanding category coverage and lifting <b>Flipkart market-penetration share ~1%</b>.")
b("Led <b>consumer understanding</b> - cohort analysis, funnel metrics and user personas - and launched <b>targeted loyalty-coupon "
  "campaigns</b> that improved <b>conversion 20%</b> and strengthened repeat purchase.")
b("Optimized <b>promotion and digital-offer spend</b>; analyzed payment and regional consumer behavior to roll out "
  "<b>South-specific bank coupons</b>, improving offer adoption and conversion across the region.")
b("Built automated <b>Tableau / Power BI dashboards</b> (SQL, Google Apps Script) giving leadership real-time visibility into "
  "channel revenue, margin and operational health.")
b("Built <b>demand and revenue forecasting</b> models to guide buying, pricing and promotion planning; data-driven planning drove "
  "a <b>55% category revenue uplift during Big Billion Days</b>.")

E.append(Paragraph("<b>Enverus</b> - Business Analyst I - Market Research (B2B SaaS) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jan 2023 - May 2024</font>", compln))
b("Built revenue and sales-trend <b>dashboards</b> for US commercial leaders, supporting <b>ARR that scaled into the $500MM range</b>; "
  "informed commercial and pricing decisions.")
b("Re-engineered reporting through <b>Lean Six Sigma</b>, driving a <b>20% reduction in cycle times</b> and standardizing KPIs across "
  "global teams.")

E.append(Paragraph("<b>Associate - Commercial Intelligence</b> &nbsp;|&nbsp; <font color='#6b6b6b'>May 2021 - Dec 2022</font>", compln))
b("Published quantitative <b>market and consumer research</b> across 3 cycles and built unit-economics and pricing models; produced "
  "competitive and price intelligence to guide leadership strategy.")
rule(sb=4)

# ---------- SKILLS ----------
sect("SKILLS")
E.append(Paragraph(
  "E-commerce Channel Strategy | Digital Business &amp; P&amp;L Levers | Marketplace Growth | Quick-Commerce Landscape | "
  "Brand Strategy &amp; Go-to-Market | Pricing &amp; Promotions | Digital Marketing Spend | Assortment &amp; Merchandising | "
  "Demand &amp; Revenue Forecasting | Consumer Research &amp; Insights | Cohort &amp; Conversion Analysis | "
  "Competitive &amp; Price Intelligence | Sales / Marketing / Operations Partnership | New Business Development | "
  "Stakeholder Management | SQL | Tableau | Power BI | Advanced Excel", skill))
E.append(Paragraph(
  "<font color='#6b6b6b'>Platforms / landscape:</font> Marketplaces (Amazon, Flipkart, Myntra, Nykaa) &amp; "
  "Quick Commerce (Blinkit, Zepto, Instamart) - channel &amp; ecosystem fluency; Online + Offline Integration (familiarity).", skill))
rule(sb=4)

# ---------- EDUCATION ----------
sect("EDUCATION")
E.append(Paragraph("<b>B.Tech - Biotechnology</b> | Vellore Institute of Technology (VIT) | 2017 - 2021 | GPA: 8.55 / 10", edu))
E.append(Paragraph("<b>12th (ISC)</b> | Spring Dale College | 2016 | 88% &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>10th (ICSE)</b> | Spring Dale College | 2014 | 88%", edu))
rule(sb=4)

# ---------- CERTIFICATIONS ----------
sect("CERTIFICATIONS")
b("<b>Customer Value, Acquisition, and Retention</b> - University of Maryland, College Park &nbsp;&bull;&nbsp; <b>Agile Project Management</b> - Google")
b("<b>Mastering Advanced SQL Queries</b> - Coursera &nbsp;&bull;&nbsp; <b>From Excel to Power BI</b> - Knowledge Accelerators")
rule(sb=4)

# ---------- LEADERSHIP & ACHIEVEMENTS ----------
sect("LEADERSHIP &amp; ACHIEVEMENTS")
b("Led cross-functional initiatives and small teams; directed operations, logistics &amp; teams for corporate / college events hosting <b>800-1,000+ participants</b>.")
b("Consistent commercial growth record - <b>55% BBD category uplift</b>, <b>19% YoY revenue growth</b>, <b>20% conversion lift</b>, and <b>20% faster reporting</b>.")

doc.build(E)
print("built", OUT)
