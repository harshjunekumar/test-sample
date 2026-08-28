#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Amplify Analytix BA Case — FOUNDATIONS & FUNDAMENTALS (start here).
Beginner-friendly: what the case is, the business context, a plain-English
glossary of every keyword, the dataset explained, and every formula with
intuition + a worked example. Built for someone learning this from scratch.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether, PageBreak, ListFlowable, ListItem)

NAVY = HexColor("#1F3A5F"); TEAL = HexColor("#0E7C86"); AMBER = HexColor("#B26A00")
LIGHT = HexColor("#EEF2F7"); WARM = HexColor("#FBF3E4"); MID = HexColor("#C9D6E5"); GREY = HexColor("#555555")
OUT = "/home/user/test-sample/Amplify_Analytix_Case_Foundations.pdf"
M = 0.75 * inch; PAGE_W, PAGE_H = A4; USABLE = PAGE_W - 2 * M

tt = ParagraphStyle("tt", fontName="Helvetica-Bold", fontSize=23, leading=27, textColor=NAVY, spaceAfter=3)
sub = ParagraphStyle("sub", fontName="Helvetica", fontSize=12.5, leading=16, textColor=GREY, spaceAfter=9)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=13.5, leading=16, textColor=NAVY, spaceBefore=11, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.6, leading=13.5, textColor=TEAL, spaceBefore=7, spaceAfter=1)
body = ParagraphStyle("b", fontName="Helvetica", fontSize=9.8, leading=13.4, textColor=black, alignment=TA_JUSTIFY, spaceAfter=5)
bl = ParagraphStyle("bl", parent=body, alignment=TA_LEFT)
bu = ParagraphStyle("bu", fontName="Helvetica", fontSize=9.6, leading=12.9, textColor=black, leftIndent=13, bulletIndent=3, spaceAfter=2.5)
cell = ParagraphStyle("c", fontName="Helvetica", fontSize=8.9, leading=11.4, textColor=black)
cw = ParagraphStyle("cw", fontName="Helvetica-Bold", fontSize=8.9, leading=11.4, textColor=white)
small = ParagraphStyle("sm", fontName="Helvetica-Oblique", fontSize=8.3, leading=10.6, textColor=GREY, spaceAfter=4)
fxs = ParagraphStyle("fx", fontName="Courier", fontSize=8.4, leading=11.4, textColor=TEAL, leftIndent=8, spaceAfter=3)
egs = ParagraphStyle("eg", fontName="Helvetica-Oblique", fontSize=9.2, leading=12.2, textColor=HexColor("#7a4a00"), leftIndent=8, spaceAfter=5)
co = ParagraphStyle("co", fontName="Helvetica", fontSize=10, leading=13.4, textColor=NAVY, leftIndent=9, rightIndent=9, spaceBefore=2, spaceAfter=2)


def rule(c=TEAL, th=1.4, sb=1, sa=6):
    return HRFlowable(width="100%", thickness=th, color=c, spaceBefore=sb, spaceAfter=sa)


def sec(t):
    return KeepTogether([Paragraph(t, h1), rule()])


def P(t, st=body):
    return Paragraph(t, st)


def blist(items):
    return ListFlowable([ListItem(Paragraph(t, bu), leftIndent=13, value="•") for t in items],
                        bulletType="bullet", start="•", leftIndent=6)


def glo(rows):
    data = [["Term", "In plain English"]]
    for term, mean in rows:
        data.append([Paragraph("<b>" + term + "</b>", cell), Paragraph(mean, cell)])
    t = Table(data, colWidths=[USABLE * 0.26, USABLE * 0.74], repeatRows=1)
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 5),
             ("RIGHTPADDING", (0, 0), (-1, -1), 5), ("TOPPADDING", (0, 0), (-1, -1), 3.5),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5), ("BACKGROUND", (0, 0), (-1, 0), NAVY),
             ("TEXTCOLOR", (0, 0), (-1, 0), white), ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
             ("FONTSIZE", (0, 0), (-1, 0), 8.9),
             ("LINEBELOW", (0, 0), (-1, -1), 0.4, MID), ("LINEBEFORE", (0, 0), (-1, -1), 0.4, MID),
             ("LINEAFTER", (0, 0), (-1, -1), 0.4, MID), ("LINEABOVE", (0, 0), (-1, 0), 0.4, MID)]
    for r in range(1, len(data)):
        if r % 2 == 0:
            style.append(("BACKGROUND", (0, r), (-1, r), LIGHT))
    t.setStyle(TableStyle(style))
    return t


def box(paras, bg=LIGHT, edge=TEAL):
    inner = Table([[p] for p in paras], colWidths=[USABLE - 10])
    inner.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                               ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                               ("BACKGROUND", (0, 0), (-1, -1), bg), ("LINEBEFORE", (0, 0), (0, -1), 3.5, edge)]))
    return KeepTogether(inner)


def formula(title, meaning, fxstr, example, gotcha=None):
    parts = [P("<b>" + title + "</b> &mdash; " + meaning, bl), P(fxstr, fxs), P("Example: " + example, egs)]
    if gotcha:
        parts.append(P("Watch out: " + gotcha, small))
    return KeepTogether(parts)


story = []
story.append(rule(TEAL, 3, 0, 9))
story.append(P("Amplify Analytix BA Case — Foundations", tt))
story.append(P("Start here: the fundamentals, the keywords, the dataset, and the formulas &mdash; explained from scratch", sub))
story.append(rule(NAVY, 1, 0, 8))
story.append(P("<b>How to use this:</b> read it top to bottom once. It assumes you know nothing about the case and "
               "builds the foundation so the numbers, words, and formulas all make sense &mdash; then you&rsquo;re "
               "ready for the deeper prep pack and a mock interview.", bl))

# 1
story.append(sec("1&nbsp;&nbsp;What a case-study interview is (and what this one tests)"))
story.append(P("A <b>case study</b> is a mini real-world problem the interviewer gives you to see how you think. "
               "You&rsquo;re not expected to have a perfect answer &mdash; they&rsquo;re watching <i>how</i> you "
               "break the problem down, handle messy data, make sensible choices, and explain them to "
               "non-technical people."))
story.append(P("This case (for a <b>Business Analyst</b> role at <b>Amplify Analytix</b>, a data-analytics "
               "consultancy) has two parts:"))
story.append(blist([
    "<b>Task 1 &mdash; Data analysis:</b> you get a spreadsheet of customers and are asked to analyse it and "
    "recommend what to do about the top customers. This tests your <b>data skills and business judgement</b>.",
    "<b>Task 2 &mdash; Case-study proposal:</b> a written business problem (different regions measure their sales "
    "&lsquo;funnel&rsquo; differently) and you propose how you&rsquo;d fix it. This tests your <b>structured "
    "thinking and consulting instincts</b> &mdash; no data needed.",
]))

# 2
story.append(sec("2&nbsp;&nbsp;The business context (so the data makes sense)"))
story.append(P("The data comes from <b>Henkel</b>, a large company that sells <b>adhesives and industrial "
               "products to other businesses</b> (this is <b>B2B</b> &mdash; business-to-business, not selling to "
               "you and me). So each &lsquo;customer&rsquo; is actually another <b>company</b> that buys from "
               "Henkel."))
story.append(P("Three teams inside Henkel care about these customers, and the whole analysis is really about "
               "helping them:"))
story.append(blist([
    "<b>Sales</b> &mdash; wins deals and grows revenue. Cares about win rate and pipeline.",
    "<b>Marketing</b> &mdash; creates interest and nurtures customers (emails, campaigns). Cares about reach and "
    "engagement.",
    "<b>Customer Experience (CX)</b> &mdash; makes sure orders are delivered on time and customers stay happy. "
    "Cares about delivery scores.",
]))
story.append(box([P("<b>The one idea to hold onto:</b> every number in Task 1 is answering &lsquo;which customers "
                    "matter most, and what should Sales, Marketing, or CX <i>do</i> about them?&rsquo;", co)]))

# 3 GLOSSARY
story.append(sec("3&nbsp;&nbsp;The keywords, in plain English (the foundation)"))
story.append(P("3.1&nbsp;&nbsp;Money &amp; growth", h2))
story.append(glo([
    ("NES (Net External Sales)", "The money a customer actually paid Henkel. &lsquo;Net&rsquo; = after returns/credits; "
     "&lsquo;external&rsquo; = real outside sales, not internal transfers. Simplest way to say it: <b>revenue from "
     "that customer</b>."),
    ("YoY growth", "&lsquo;Year over year.&rsquo; This year&rsquo;s sales vs last year&rsquo;s, as a %. E.g. 110 "
     "vs 100 = +10%."),
    ("CAGR", "Compound Annual Growth Rate &mdash; the <b>smoothed average yearly growth</b> over several years. It "
     "answers &lsquo;what steady % per year would take sales from the start value to the end value?&rsquo;"),
    ("Tenure / Recency / Purchase cycle", "How long they&rsquo;ve been a customer / how recently they last bought "
     "/ how often they typically buy. Together they hint at loyalty and whether a customer is &lsquo;overdue.&rsquo;"),
]))
story.append(P("3.2&nbsp;&nbsp;The sales pipeline (deals)", h2))
story.append(glo([
    ("Opportunity", "A potential deal &mdash; a specific chance to sell something to a customer. Tracked in the "
     "sales software (here called <b>ACE</b>, a CRM)."),
    ("Won / Lost / Open / In-progress / Stopped", "The status of an opportunity. <b>Won</b> = closed successfully; "
     "<b>Lost</b> = customer said no / bought elsewhere; <b>Open / In-progress</b> = still being worked; "
     "<b>Stopped</b> = abandoned."),
    ("Win rate", "Of the deals that reached a decision (won or lost), what share did we win? A core measure of "
     "sales effectiveness. Below 50% at big accounts is a red flag."),
    ("Opportunity conversion rate", "The share of opportunities that turned into sales. (In this dataset it&rsquo;s "
     "actually calculated as won &divide; (won + lost) &mdash; see the formulas.)"),
    ("CRM", "Customer Relationship Management software &mdash; the system that records every customer, contact and "
     "deal (e.g. Salesforce; here &lsquo;ACE&rsquo;)."),
]))
story.append(P("3.3&nbsp;&nbsp;Customer value &amp; company info", h2))
story.append(glo([
    ("Segment (Champions, Promising, Sustainers, Need Attention, Drifters)", "Customers grouped by how valuable / "
     "healthy they are, using a machine-learning model. <b>Champions</b> = best; <b>Drifters / Need Attention</b> "
     "= weakest. It&rsquo;s a way to treat similar customers similarly."),
    ("Firmographics", "&lsquo;Demographics, but for companies&rsquo; &mdash; facts about the customer&rsquo;s "
     "business, like its size, industry and overall revenue."),
    ("D&amp;B (Dun &amp; Bradstreet)", "A company that sells business data. &lsquo;D&amp;B revenue&rsquo; / "
     "&lsquo;Global Ultimate revenue&rsquo; = the total revenue of the customer&rsquo;s <b>parent company</b> "
     "&mdash; useful to spot when several customers belong to one big group."),
    ("SBU / Business unit (AMO, APC, ACM, AMI&hellip;)", "Which part of Henkel&rsquo;s business the customer sits in "
     "&mdash; different product lines/divisions."),
]))
story.append(P("3.4&nbsp;&nbsp;Delivery (Customer Experience)", h2))
story.append(glo([
    ("POT-C", "&lsquo;On-time vs Communicated.&rsquo; Did we deliver by the date <b>we promised</b>? Measures how "
     "well our own process runs. ~1.0 = on time."),
    ("POT-AR", "&lsquo;On-time vs Actual Requested.&rsquo; Did we deliver by the date the customer <b>originally "
     "asked for</b>? Measures the customer&rsquo;s experience. If POT-C is high but POT-AR is low, we&rsquo;re "
     "hitting our own (later) promises but not what the customer really wanted."),
]))
story.append(P("3.5&nbsp;&nbsp;Marketing &amp; the funnel (needed for Task 2)", h2))
story.append(glo([
    ("Emails sent / opened, engagement", "How much marketing activity a customer has received and responded to. "
     "In this data it&rsquo;s mostly <b>missing or zero</b> &mdash; a coverage/recording gap."),
    ("Lead", "A potential customer / contact who might buy one day."),
    ("Funnel (or pipeline)", "The journey a lead takes from first contact to becoming a paying customer, split into "
     "<b>stages</b> that narrow like a funnel."),
    ("MQL (Marketing Qualified Lead)", "A lead <b>marketing</b> judges interested/ready enough to hand to sales."),
    ("SQL (Sales Qualified Lead)", "A lead <b>sales</b> has accepted as genuinely worth pursuing."),
    ("Known → MQL → SQL → Opportunity → Customer", "The five-stage funnel Task 2 proposes as the shared language: "
     "a known contact → marketing-ready → sales-accepted → a real deal → a won customer."),
    ("Entry / exit rule, owner, timestamp", "For each stage: what gets a lead <b>in</b>, what moves it <b>on</b>, "
     "<b>who</b> is accountable, and a <b>date</b> that can&rsquo;t be overwritten (so you can measure how long "
     "things take)."),
    ("System of record", "The one system treated as the &lsquo;source of truth&rsquo; for a piece of data."),
]))

story.append(PageBreak())

# 4 DATASET
story.append(sec("4&nbsp;&nbsp;The dataset, explained simply"))
story.append(P("Open the <b>Data</b> sheet and picture a giant table: <b>one row = one customer company</b> "
               "(3,056 of them), and <b>53 columns</b> of facts about each. The columns fall into groups:"))
dg = [["Column group", "What&rsquo;s in it", "Which team cares"],
      ["Sales by year", "Revenue (NES) for 2021, 2022, 2023, 2024, 2025, and Q1-2026; plus growth % and CAGR",
       "Sales / Finance"],
      ["Pipeline", "Counts of opportunities: won, lost, open, in-progress, stopped; a conversion rate", "Sales"],
      ["Marketing", "Emails sent / opened; a marketing rank (mostly missing)", "Marketing"],
      ["Firmographics", "D&amp;B parent-company revenue; firmographic rank", "Sales / Strategy"],
      ["Delivery (CX)", "POT-C and POT-AR delivery scores", "Customer Experience"],
      ["Segmentation", "The ML segment (Champions&hellip;Drifters) and business unit (SBU)", "Everyone"],
      ["Flags", "&lsquo;Missing data&rsquo; markers for sales / marketing / firmographics", "You (the analyst)"]]
story.append(Table([[Paragraph(c, cw if r == 0 else cell) for c in row] for r, row in enumerate(dg)],
                   colWidths=[USABLE * 0.22, USABLE * 0.56, USABLE * 0.22], repeatRows=1))
story[-1].setStyle(TableStyle([("VALIGN", (0, 0), (-1, -1), "TOP"), ("BACKGROUND", (0, 0), (-1, 0), NAVY),
                               ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
                               ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
                               ("LINEBELOW", (0, 0), (-1, -1), 0.4, MID), ("LINEBEFORE", (0, 0), (-1, -1), 0.4, MID),
                               ("LINEAFTER", (0, 0), (-1, -1), 0.4, MID), ("LINEABOVE", (0, 0), (-1, 0), 0.4, MID),
                               ("ROWBACKGROUNDS", (0, 1), (-1, -1), [white, LIGHT])]))
story.append(Spacer(1, 4))
story.append(P("The other sheets are helpers: <b>Definitions</b> explains each metric; <b>Analysis_Approach</b> "
               "lists the assumptions and data-quality issues; <b>Analysis_EDA</b> and <b>Analysis_Top10</b> hold "
               "the live formulas; <b>Case_Study_QA</b> and <b>Slide_Talk_Track</b> are interview prep."))
story.append(box([P("<b>The most important thing about this dataset: it&rsquo;s messy on purpose.</b> Lots of "
                    "columns are missing (marketing 86% missing, delivery 87%), and some definitions don&rsquo;t "
                    "match the actual numbers. Spotting and <i>stating</i> that &mdash; instead of trusting it "
                    "blindly &mdash; is the biggest thing they&rsquo;re testing.", co)], WARM, AMBER))

# 5 FORMULAS
story.append(sec("5&nbsp;&nbsp;The formulas, with the intuition behind them"))
story.append(P("You don&rsquo;t need to memorise Excel syntax &mdash; you need to explain <i>what each number "
               "means and why</i>. Here&rsquo;s each one in words, with a worked example."))
story.append(formula("Total sales (Total NES 2021&ndash;25)", "just add up a customer&rsquo;s five yearly sales figures.",
                     "Total NES = NES2021 + NES2022 + NES2023 + NES2024 + NES2025",
                     "€100m + €120m + €130m + €110m + €90m = €550m over five years.",
                     "the ready-made &lsquo;nes&rsquo; column secretly covers 2023&ndash;2026 (a partial year), so "
                     "it isn&rsquo;t the true total &mdash; the analyst rebuilt it from the yearly columns."))
story.append(formula("Year-on-year (YoY) growth", "how much this year changed versus last year.",
                     "YoY growth = (this year / last year) − 1",
                     "2025 = €90m, 2024 = €110m → 90/110 − 1 = −18% (down 18%)."))
story.append(formula("CAGR (smoothed yearly growth)", "the steady % per year that gets you from the first year to the last.",
                     "CAGR = (end value / start value)^(1 / number of years) − 1",
                     "€100m in 2021 → €150m in 2025 (4 years): (150/100)^(1/4) − 1 = 1.5^0.25 − 1 ≈ +10.7% a year.",
                     "&lsquo;number of years&rsquo; is the <i>gaps</i> between years (2021→2025 = 4), not 5."))
story.append(formula("Q1-2026 annualised", "turn one quarter into a rough full-year estimate to compare momentum.",
                     "Annualised 2026 = Q1-2026 × 4",
                     "Q1-2026 = €25m → ×4 = €100m implied for the year; compare that to 2025 to see the trend.",
                     "it&rsquo;s only <i>directional</i> &mdash; one quarter isn&rsquo;t a real trend, so label it."))
story.append(formula("Customer concentration", "how much of total sales sits with the biggest few customers.",
                     "Concentration = (sales of top N customers) / (sales of all customers)",
                     "Top 10 = €8.7bn, all customers = €48.4bn → 8.7 / 48.4 = 18% (10 names = 18% of the book)."))
story.append(formula("Segment share", "how much of total sales each customer segment contributes.",
                     "Segment share = (sales of that segment) / (sales of all segments)",
                     "Promising segment = €18bn of €48.4bn → 37% of sales."))
story.append(formula("Win rate", "of the deals that were decided, how many did we win.",
                     "Win rate = Won / (Won + Lost)      [open/in-progress deals excluded]",
                     "60 won, 40 lost → 60 / (60 + 40) = 60%."))
story.append(formula("Data completeness", "what share of customers actually have data for a field.",
                     "% complete = customers with data / total customers",
                     "2,051 of 3,057 have sales history → 67% complete (so 33% is missing)."))
story.append(P("<b>The clever guard:</b> a delivery score of <b>0.00</b> is treated as &lsquo;no data,&rsquo; not "
               "&lsquo;0% on time.&rsquo; Otherwise thousands of blank accounts would drag the average down and "
               "point the CX team at the wrong customers. In Excel: "
               "<font face=\"Courier\" size=\"8\">=IF(score=0,\"no data\", score)</font>.", body))

story.append(PageBreak())

# 6 STORY
story.append(sec("6&nbsp;&nbsp;The story the numbers tell (say it like this)"))
story.append(P("Once you understand the pieces, Task 1 is really one short story:"))
story.append(blist([
    "The business is <b>shrinking</b> &mdash; sales peaked in 2023 and have fallen since.",
    "It&rsquo;s <b>dangerously concentrated</b> &mdash; ~3% of customers make ~60% of revenue, and those big "
    "accounts are the ones declining fastest.",
    "We <b>lose more deals than we win</b> at the top accounts (win rate under 50%) &mdash; that&rsquo;s a "
    "<b>pricing/qualification</b> problem, not a lack of demand.",
    "<b>Marketing is barely present</b> &mdash; only ~12% of customers have ever been emailed, and the "
    "Promising segment (37% of sales) has had <b>zero</b> emails.",
    "And we can only half-trust the data, because so much is <b>missing</b> &mdash; so every recommendation is "
    "stated with that caveat.",
]))

# 7 TASK 2 FUNDAMENTALS
story.append(sec("7&nbsp;&nbsp;Task 2 fundamentals (the funnel problem)"))
story.append(P("Task 2 has no data &mdash; it&rsquo;s a thinking exercise. The problem: a global company&rsquo;s "
               "regions all track the same sales funnel (Known → MQL → SQL → Opportunity), but each defines and "
               "counts the stages differently and uses different systems &mdash; so leadership can&rsquo;t compare "
               "regions or trust the numbers."))
story.append(box([P("<b>The whole answer in one line:</b> <i>standardise the definition, not the process.</i> "
                    "Agree what each stage <i>means</i> (the entry rule, the owner, the date), but let each region "
                    "keep <i>how</i> they actually sell. That&rsquo;s what makes it acceptable to the regions "
                    "instead of a fight.", co)]))
story.append(P("Three ideas make it work: <b>core + local</b> (regions can add small steps inside a stage but "
               "can&rsquo;t invent new ones), <b>ownership</b> (one named owner per stage + a change process, or it "
               "drifts apart again), and <b>rules for messy reality</b> (leads skip stages and go backwards, so "
               "count skips as passed and log reversals instead of erasing dates). The killer evidence: the pack "
               "itself defines the funnel two different ways &mdash; proof the project is needed."))

# 8 HOW TO PREP
story.append(sec("8&nbsp;&nbsp;How to use this to prepare"))
story.append(blist([
    "<b>First</b>, be able to say what each keyword in &sect;3 means in one sentence, without notes.",
    "<b>Then</b>, be able to explain each formula in &sect;5 in words (not Excel) and why it&rsquo;s done that way.",
    "<b>Then</b>, tell the &sect;6 story out loud in 60 seconds.",
    "<b>Finally</b>, for Task 2, be able to say &lsquo;standardise the definition, not the process&rsquo; and "
    "explain the five stages.",
]))
story.append(P("Quick self-test (answers are all in this guide): What does POT-AR measure, and how does it differ "
               "from POT-C? Why is 18% concentration a <i>risk</i> here, not a strength? Why is a sub-50% win rate "
               "a pricing problem and not a demand problem? What&rsquo;s the difference between an MQL and an SQL? "
               "Why exclude 2026 from the rankings?", small))
story.append(Spacer(1, 5))
story.append(P("Next: once these fundamentals feel solid, move to the <b>Explainer &amp; Q&amp;A prep pack</b> "
               "(the deeper deck), and then do a mock interview. You&rsquo;ll be ready.", body))


def furn(canvas, doc):
    canvas.saveState(); canvas.setStrokeColor(MID); canvas.setLineWidth(0.5)
    if doc.page > 1:
        canvas.line(M, PAGE_H - M + 14, PAGE_W - M, PAGE_H - M + 14)
        canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
        canvas.drawString(M, PAGE_H - M + 18, "Amplify Analytix BA Case — Foundations & Fundamentals")
    canvas.line(M, M - 12, PAGE_W - M, M - 12)
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
    canvas.drawString(M, M - 22, "Start here — learn the basics first")
    canvas.drawRightString(PAGE_W - M, M - 22, "Page %d" % doc.page)
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M + 6,
                        title="Amplify Analytix BA Case — Foundations & Fundamentals", author="Juhi Bhalla")
doc.build(story, onFirstPage=furn, onLaterPages=furn)
print("PDF written to", OUT)
