#!/usr/bin/env python3
"""Juhi Bhalla - Customer Operations Analyst / Buying Operations (Buylist JD). 1 page, ATS-safe, no dashes."""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, HRFlowable
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_JUSTIFY

BLACK = colors.HexColor("#1a1a1a"); GREY = colors.HexColor("#6b6b6b"); RULE = colors.HexColor("#b7b7b7")
LINKB = "#0563C1"
OUT = "/home/user/test-sample/Juhi_Bhalla_Resume_CustomerOps.pdf"

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
E.append(Paragraph("Customer Operations Analyst | Buying &amp; Product Operations | Pricing, Availability &amp; Data Accuracy | "
                   "Vendor &amp; Customer Operations | SLA-Driven | Excel, SQL, Power BI", tagline))
rule(sb=4, sa=1)

# ---------- SUMMARY ----------
sect("PROFESSIONAL SUMMARY")
E.append(Paragraph(
  "Operations-focused analyst with 5+ years in e-commerce and B2B SaaS (Flipkart, Enverus), running product, pricing and "
  "availability operations for a large marketplace category under tight accuracy and SLA standards. Strong at maintaining "
  "product / vendor / pricing / inventory data, resolving vendor and customer queries, exceptions and discrepancies, and "
  "analyzing data to fix errors and process gaps. Works fluently across buying, merchandising, supply-chain, customer-service, "
  "finance and technology teams (offshore / onshore), and drives process improvement, automation and UAT. Advanced Excel, "
  "SQL and Power BI.", summ))
rule()

# ---------- EXPERIENCE ----------
sect("EXPERIENCE")
E.append(Paragraph("<b>Flipkart</b> - Business Analyst - Large Appliances (eCommerce Marketplace) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jun 2024 - Sep 2026</font>", compln))
E.append(Paragraph("Owned product, seller / vendor and SKU operations for a large marketplace category - item setup, pricing, "
                   "availability and data accuracy across the catalogue, with tight SLAs and cross-functional coordination.", intro))
b("Managed end-to-end <b>product / SKU operations</b> - <b>item setup, pricing, and availability / in-stock</b> - maintaining catalogue and listing accuracy and timely updates for a large category.")
b("Reviewed and maintained <b>product, vendor, pricing and inventory data</b>; ran cohort and SKU trend analysis (YoY &amp; MoM) and drove <b>product-exchange bump-ups</b> that grew category <b>revenue 19% YoY</b>.")
b("Handled <b>vendor and customer queries, exceptions and escalations</b>; monitored <b>orders, transactions and discrepancies</b>, resolving operational issues to protect availability and conversion.")
b("Analyzed operational data to surface <b>trends, errors and process gaps</b>; launched targeted pricing and loyalty-coupon actions that improved <b>conversion 20%</b>.")
b("Built automated <b>Tableau / Power BI dashboards</b> (SQL, Google Apps Script) with standardized KPIs; coordinated with <b>buying, merchandising, supply-chain, customer-service and finance</b> teams for real-time visibility.")
b("Drove <b>process improvement and automation</b>; built demand and sales forecasting to guide planning - supporting a <b>55% category revenue uplift during Big Billion Days</b> while meeting accuracy and turnaround SLAs.")

E.append(Paragraph("<b>Enverus</b> - Business Analyst I - Market Research (B2B SaaS) &nbsp;|&nbsp; "
                   "<font color='#6b6b6b'>Jan 2023 - May 2024</font>", compln))
b("Built and maintained <b>Tableau / Power BI dashboards</b> for US (onshore) commercial leaders from an offshore team, standardizing KPIs and supporting <b>ARR that scaled into the $500MM range</b> with strong data accuracy and timeliness.")
b("Re-engineered reporting through <b>Lean Six Sigma</b>, cutting cycle / turnaround times <b>20%</b> and standardizing quality and SLA adherence across global teams.")

E.append(Paragraph("<b>Associate - Commercial Intelligence</b> &nbsp;|&nbsp; <font color='#6b6b6b'>May 2021 - Dec 2022</font>", compln))
b("Published quantitative research across 3 cycles and built unit-economics and pricing models; produced competitive and price intelligence with high <b>data accuracy</b> to support leadership decisions.")
rule(sb=4)

# ---------- SKILLS ----------
sect("SKILLS")
E.append(Paragraph(
  "Buying Operations | Product &amp; Item Setup | Pricing Operations | Availability &amp; In-Stock Management | "
  "Retail / E-commerce Product &amp; Pricing Processes | Product / Vendor / Pricing / Inventory Data | Data Accuracy &amp; Validation | "
  "Vendor &amp; Customer Query Resolution | Exceptions &amp; Escalations | Order &amp; Transaction Monitoring | Discrepancy Resolution | "
  "Trend / Error / Process-Gap Analysis | Process Improvement &amp; Automation | UAT &amp; Documentation | "
  "SLA, Quality &amp; Turnaround (TAT) | Cross-functional (Buying, Merchandising, Supply Chain, Customer Service, Finance, Technology) | "
  "Offshore / Onshore Coordination | Stakeholder Management | Analytical &amp; Problem-Solving | Communication | "
  "SQL | Advanced Excel | Power BI | Tableau | Inventory Management | Oracle / ERP (familiarity)", skill))
rule(sb=4)

# ---------- EDUCATION ----------
sect("EDUCATION")
E.append(Paragraph("<b>B.Tech - Biotechnology</b> | Vellore Institute of Technology (VIT) | 2017 - 2021 | GPA: 8.55 / 10", edu))
E.append(Paragraph("<b>12th (ISC)</b> | Spring Dale College | 2016 | 88% &nbsp;&nbsp;&bull;&nbsp;&nbsp; <b>10th (ICSE)</b> | Spring Dale College | 2014 | 88%", edu))
rule(sb=4)

# ---------- CERTIFICATIONS ----------
sect("CERTIFICATIONS")
b("<b>Agile Project Management</b> - Google &nbsp;&bull;&nbsp; <b>Mastering Advanced SQL Queries</b> - Coursera")
b("<b>From Excel to Power BI</b> - Knowledge Accelerators &nbsp;&bull;&nbsp; <b>Customer Value, Acquisition, and Retention</b> - University of Maryland, College Park")
rule(sb=4)

# ---------- ACHIEVEMENTS ----------
sect("ACHIEVEMENTS")
b("Consistent operations and growth record - <b>55% BBD category uplift</b>, <b>19% YoY revenue growth</b>, <b>20% conversion lift</b>, and <b>20% faster / more accurate reporting</b> via Lean Six Sigma.")
b("Led operations, logistics &amp; cross-functional teams for corporate / college events hosting <b>800-1,000+ participants</b>.")

doc.build(E)
print("built", OUT)
