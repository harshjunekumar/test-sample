#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Amplify Analytix BA Case Study — Explainer & Interview Q&A prep (PDF).
Consolidates: what the case is, the dataset, Task 1 (analysis), Task 2 (funnel
proposal), what it tests, and the questions likely to be asked with sharp answers.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_JUSTIFY, TA_LEFT
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether, PageBreak, ListFlowable, ListItem)

NAVY = HexColor("#1F3A5F"); TEAL = HexColor("#0E7C86"); LIGHT = HexColor("#EEF2F7")
MID = HexColor("#C9D6E5"); GREY = HexColor("#555555")
OUT = "/home/user/test-sample/Amplify_Analytix_Case_Prep.pdf"
M = 0.75 * inch; PAGE_W, PAGE_H = A4; USABLE = PAGE_W - 2 * M

tt = ParagraphStyle("tt", fontName="Helvetica-Bold", fontSize=23, leading=27, textColor=NAVY, spaceAfter=3)
sub = ParagraphStyle("sub", fontName="Helvetica", fontSize=12.5, leading=16, textColor=GREY, spaceAfter=9)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=13.5, leading=16, textColor=NAVY, spaceBefore=11, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.6, leading=13.5, textColor=TEAL, spaceBefore=7, spaceAfter=1)
body = ParagraphStyle("b", fontName="Helvetica", fontSize=9.7, leading=13.1, textColor=black, alignment=TA_JUSTIFY, spaceAfter=5)
bl = ParagraphStyle("bl", parent=body, alignment=TA_LEFT)
bu = ParagraphStyle("bu", fontName="Helvetica", fontSize=9.5, leading=12.6, textColor=black, leftIndent=13, bulletIndent=3, spaceAfter=2.5)
cell = ParagraphStyle("c", fontName="Helvetica", fontSize=8.7, leading=11.1, textColor=black)
cb = ParagraphStyle("cb", fontName="Helvetica-Bold", fontSize=8.7, leading=11.1, textColor=NAVY)
cw = ParagraphStyle("cw", fontName="Helvetica-Bold", fontSize=8.7, leading=11.1, textColor=white)
small = ParagraphStyle("sm", fontName="Helvetica-Oblique", fontSize=8.2, leading=10.5, textColor=GREY, spaceAfter=4)
co = ParagraphStyle("co", fontName="Helvetica", fontSize=9.7, leading=13, textColor=NAVY, leftIndent=8, rightIndent=8, spaceBefore=2, spaceAfter=2)


def rule(c=TEAL, th=1.4, sb=1, sa=6):
    return HRFlowable(width="100%", thickness=th, color=c, spaceBefore=sb, spaceAfter=sa)


def sec(t):
    return KeepTogether([Paragraph(t, h1), rule()])


def P(t, st=body):
    return Paragraph(t, st)


def blist(items):
    return ListFlowable([ListItem(Paragraph(t, bu), leftIndent=13, value="•") for t in items],
                        bulletType="bullet", start="•", leftIndent=6)


def tbl(data, widths, hbg=NAVY):
    rows = []
    for r, row in enumerate(data):
        rows.append([c if isinstance(c, Paragraph) else Paragraph(str(c), cw if r == 0 else cell) for c in row])
    t = Table(rows, colWidths=widths, repeatRows=1)
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"), ("LEFTPADDING", (0, 0), (-1, -1), 5),
             ("RIGHTPADDING", (0, 0), (-1, -1), 5), ("TOPPADDING", (0, 0), (-1, -1), 3.5),
             ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5), ("BACKGROUND", (0, 0), (-1, 0), hbg),
             ("LINEBELOW", (0, 0), (-1, -1), 0.4, MID), ("LINEBEFORE", (0, 0), (-1, -1), 0.4, MID),
             ("LINEAFTER", (0, 0), (-1, -1), 0.4, MID), ("LINEABOVE", (0, 0), (-1, 0), 0.4, MID)]
    for r in range(1, len(rows)):
        if r % 2 == 0:
            style.append(("BACKGROUND", (0, r), (-1, r), LIGHT))
    t.setStyle(TableStyle(style))
    return t


def box(paras):
    inner = Table([[p] for p in paras], colWidths=[USABLE - 10])
    inner.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                               ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                               ("BACKGROUND", (0, 0), (-1, -1), LIGHT), ("LINEBEFORE", (0, 0), (0, -1), 3.5, TEAL)]))
    return KeepTogether(inner)


story = []
story.append(rule(TEAL, 3, 0, 9))
story.append(P("Amplify Analytix — Business Analyst Case Study", tt))
story.append(P("Explainer &amp; Interview Q&amp;A Prep · Two tasks: customer data analysis + global lead-funnel proposal", sub))
story.append(rule(NAVY, 1, 0, 8))
story.append(P("<b>What you&rsquo;re holding:</b> a plain-English walkthrough of the whole case, plus the "
               "questions you&rsquo;re most likely to be asked and how to answer them. The underlying data is a "
               "Henkel Adhesive Technologies&ndash;style customer file (3,056 customers, 53 fields).", bl))

# 1 OVERVIEW
story.append(sec("1&nbsp;&nbsp;What this case study is"))
story.append(P("It&rsquo;s a two-part Business Analyst assessment. Both parts test the same thing from two "
               "angles: can you turn messy data and an ambiguous brief into clear, defensible, business-ready "
               "recommendations &mdash; and can you defend them in a room."))
tv = [["Task", "What it is", "What you deliver"],
      ["Task 1 — Analysis", P("Analyse a customer dataset and recommend actions for the top 10 customers "
         "(for Sales, Marketing, Customer Experience, or overall).", cell),
       P("EDA findings in charts/tables + a PPT showing the <b>top 5</b> customers and recommendations + a list "
         "of assumptions.", cell)],
      ["Task 2 — Case study", P("A strategy proposal: how to <b>standardise a global lead funnel</b> across "
         "regions that define/measure the same stages differently, ahead of a CRM transformation.", cell),
       P("A 2&ndash;3 slide proposal: approach, methodology, future-state framework, roadmap, assumptions, "
         "risks, success metrics, and supporting visuals.", cell)]]
story.append(tbl(tv, [USABLE * 0.16, USABLE * 0.46, USABLE * 0.38]))
story.append(P("<b>The through-line:</b> Task 1 rewards analytical honesty (validate every definition against "
               "the data); Task 2 rewards structured problem-solving and stakeholder judgement. The best answers "
               "connect them: the customer data has <i>no lifecycle-stage field</i>, so today you can&rsquo;t "
               "link funnel activity to customer value &mdash; which is exactly what Task 2 would fix.", body))

# 2 DATASET
story.append(sec("2&nbsp;&nbsp;The dataset, in plain terms"))
story.append(P("One row per customer account (3,056 valid + 1 &lsquo;orphan&rsquo; row with no ID). 53 columns, "
               "which group into:"))
story.append(blist([
    "<b>Sales:</b> Net External Sales (NES) per year 2021&ndash;2026, growth %, CAGR, purchase counts, "
    "recency/tenure.",
    "<b>Pipeline:</b> opportunities won / lost / open / in-progress / stopped, and a conversion rate.",
    "<b>Marketing:</b> emails sent / opened, marketing rank (mostly missing).",
    "<b>Firmographics:</b> D&amp;B global-ultimate revenue, firmographic rank (D&amp;B = Dun &amp; Bradstreet).",
    "<b>Service (CX):</b> delivery scores &mdash; POT-C (actual vs <i>communicated</i> date) and POT-AR "
    "(actual vs date the customer <i>originally requested</i>).",
    "<b>Segmentation:</b> a cross-functional ML segment (Champions / Promising / Sustainers / Need Attention / "
    "Drifters) and business unit (SBU).",
]))
story.append(P("Two supporting sheets matter: <b>Definitions</b> (33 metrics) and a <b>data-quality reality</b> "
               "&mdash; several definitions don&rsquo;t match the actual data, which is the single richest source "
               "of &lsquo;rigour&rsquo; points (see &sect;3.4).", small))

# 3 TASK 1
story.append(sec("3&nbsp;&nbsp;Task 1 — the data analysis"))
story.append(P("3.1&nbsp;&nbsp;The approach (state it, don&rsquo;t assume it)", h2))
story.append(P("&lsquo;Top&rsquo; isn&rsquo;t defined, so you define it and say so: <b>rank on realised revenue "
               "(Total NES 2021&ndash;2025)</b> &mdash; the one measure every stakeholder already trusts &mdash; "
               "then <b>diagnose</b> each account on growth, pipeline (win rate), service (delivery) and marketing "
               "reach to decide what to <i>do</i> about it."))
story.append(P("3.2&nbsp;&nbsp;The five headline findings", h2))
ff = [["Finding", "The number", "So what"],
      ["Revenue is declining", "Peaked €10.6bn (2023) → €9.87bn (2025); Q1-26 annualises ~€9.3bn (&minus;5%)",
       P("The book is shrinking, not growing.", cell)],
      ["Heavy concentration", "Top 10 = 18.1% of 5-yr sales; top 100 = 58.6% (~3% of customers ≈ 60% of revenue)",
       P("Concentration is a <i>risk</i> here because the big accounts are the ones declining.", cell)],
      ["Segment concentration", "Champions (199) + Promising (413) = 89.7% of sales; other 2,444 = ~10%",
       P("Value sits in a handful of segments.", cell)],
      ["Win rate below 50% at the top", "Overall 53.7% on decided deals; top-10 ≈ 49% (won 4,889 / lost 5,073)",
       P("Qualification &amp; pricing problem, not a demand problem.", cell)],
      ["Marketing barely present", "Only 369 of 3,056 ever emailed (12%); Promising (37% of sales) = 0 emails",
       P("A <i>coverage</i> gap, not an engagement failure.", cell)],
      ["Data is incomplete", "Sales 67% complete; firmographics 38%; marketing 14%; delivery 13%",
       P("Every marketing/service finding applies to a minority &mdash; state that.", cell)]]
story.append(tbl(ff, [USABLE * 0.24, USABLE * 0.42, USABLE * 0.34]))

story.append(P("3.3&nbsp;&nbsp;The top 5 customers and recommended owners", h2))
t5 = [["Customer (SBU)", "NES 21-25", "Signal", "Recommendation &amp; owner"],
      ["abcd_2009 (AMO)", "€1,549m", P("Biggest account; sales &minus;13.6%; only 62% delivered by the date "
         "requested.", cell), P("<b>Sales + CX.</b> Fix service before setting any growth target.", cell)],
      ["abcd_2897 (AMO)", "€1,029m", P("Growing; near-perfect delivery; <b>never emailed once</b>.", cell),
       P("<b>Marketing.</b> Clearest untapped opportunity in the book.", cell)],
      ["abcd_1194 (APC)", "€916m", P("Best win rate of the five; almost no marketing.", cell),
       P("<b>Marketing.</b> Low-risk place to prove coverage works.", cell)],
      ["abcd_1717 (AMO)", "€878m", P("Only real growth story (+43.8%/yr) but delivery slipping to 73%.", cell),
       P("<b>CX.</b> Protect it before volume breaks service.", cell)],
      ["abcd_2496 (AMO)", "€871m", P("Perfect delivery but weakest win rate in the top ten.", cell),
       P("<b>Sales.</b> A pricing/qualification issue, not execution.", cell)]]
story.append(tbl(t5, [USABLE * 0.18, USABLE * 0.11, USABLE * 0.37, USABLE * 0.34]))

story.append(P("3.4&nbsp;&nbsp;The strongest move: validating definitions against the data", h2))
story.append(P("This is what separates a good candidate from a great one &mdash; you <b>raised issues rather than "
               "silently fixing them</b>:"))
story.append(blist([
    "<b>&lsquo;nes&rsquo; column is NOT total sales</b> &mdash; it equals 2023+2024+2025+2026 (a 3.25-yr window). "
    "You built your own 2021&ndash;25 total instead.",
    "<b>CAGR window</b> in the data is 4-year (2025/2021), not the &lsquo;3-year&rsquo; the Definitions claim &mdash; "
    "recalculated transparently.",
    "<b>Opportunity conversion</b> is won/(won+lost) in reality (96.7% match), not won/total as defined &mdash; "
    "documented, both shown.",
    "<b>Zero delivery score = missing data</b>, not 0% on-time (2,000+ rows) &mdash; otherwise you&rsquo;d "
    "mis-target CX.",
    "<b>8 defined metrics are absent</b> from the data (incl. Lifecycle Stage &mdash; the link to Task 2); a "
    "referenced &lsquo;Segment Overview&rsquo; tab doesn&rsquo;t exist.",
    "<b>Marketing 86% missing, one orphan row, a duplicate column</b> &mdash; all flagged, not hidden.",
]))
story.append(P("3.5&nbsp;&nbsp;The eight assumptions (each one moves a number)", h2))
story.append(P("2026 is one quarter (excluded from rankings/CAGR) · NES is EUR, already converted · negative NES "
               "= returns/credits, not errors · zero delivery = no data · win rate = won/(won+lost), open deals "
               "excluded · shared global-parent revenue = one parent group · the 5 <i>data</i> segment names "
               "supersede the Definitions&rsquo; 5 · every row in scope (no test/inactive filter available).", body))

story.append(PageBreak())

# 4 TASK 2
story.append(sec("4&nbsp;&nbsp;Task 2 — the global lead-funnel proposal"))
story.append(P("<b>The problem:</b> a global org where regions define and measure the same funnel stages "
               "(Known, MQL, SQL, Opportunity) differently, across multiple source systems &mdash; so leadership "
               "can&rsquo;t compare markets, spot bottlenecks, or benchmark. A CRM transformation is coming; they "
               "want the funnel standardised <i>while</i> respecting regional needs."))
story.append(box([P("<b>The core insight the whole proposal rests on:</b> standardise the <b>definition</b>, not "
                    "the <b>process</b>. A stage is a checkpoint with an entry criterion; <i>how</i> a region "
                    "gets a lead there stays local. Fix the stage names, entry/exit criteria, owner and timestamp "
                    "&mdash; leave routing, cadence and channel mix alone. That&rsquo;s what makes it acceptable "
                    "to the people who could block it.", co)]))
story.append(P("4.1&nbsp;&nbsp;Methodology &mdash; look, compare, sort", h2))
story.append(blist([
    "<b>Look:</b> inventory every system; ask the same questions in every region; <b>trace 30&ndash;50 real "
    "leads</b> end-to-end (the traced leads settle it when a region&rsquo;s story conflicts with its data).",
    "<b>Compare:</b> put every region side-by-side in one <b>definition matrix</b>.",
    "<b>Sort</b> each difference into three buckets &mdash; and only two need work (this is what keeps the "
    "project small).",
]))
gc = [["Gap type", "Meaning", "Fix"],
      ["Semantic", "Same checkpoint, different name", "Map it. No design work."],
      ["Criteria", "Genuinely different bar for the same stage", "Needs a global decision."],
      ["Systemic", "The data can&rsquo;t be produced today", "Needs a system change (and budget)."]]
story.append(tbl(gc, [USABLE * 0.18, USABLE * 0.5, USABLE * 0.32]))
story.append(P("4.2&nbsp;&nbsp;Future-state framework", h2))
story.append(P("Five common stages &mdash; <b>Known → MQL → SQL → Opportunity → Customer</b> &mdash; each fixing "
               "four things everywhere: <b>what gets a lead in, what moves it on, who&rsquo;s accountable, and a "
               "date stamp nobody can overwrite.</b> Three design principles keep it real:"))
story.append(blist([
    "<b>Core + local:</b> a region can add sub-steps <i>inside</i> a stage, but can&rsquo;t invent a new stage "
    "<i>between</i> two core ones.",
    "<b>Governance:</b> one named owner per stage + change control (proposed → assessed → signed off → "
    "versioned → dated) &mdash; or definitions drift apart within a year.",
    "<b>Messy reality:</b> a skipped stage still counts as passed (so the maths balances); a regression is "
    "logged with a reason, never by overwriting the original timestamp (or you lose velocity).",
]))
story.append(P("4.3&nbsp;&nbsp;Roadmap, risks, success metrics", h2))
story.append(P("<b>Four gated steps</b> (go/no-go at each): 1) Assess current state, 4&ndash;6 wks · 2) Design &amp; "
               "agree, ~4 wks · 3) Pilot one mid-sized, willing region (CRM-aligned; ≥1 quarter parallel run) · "
               "4) Phased rollout. <b>No final date is given until Step 1</b> &mdash; deliberately. The sequence "
               "is firm even though the durations are estimates.", body))
story.append(P("<b>Top risk = compensation.</b> If you change what counts as an SQL, you change what sales are "
               "paid on &mdash; where these projects usually die. Mitigate with parallel running + a published "
               "conversion factor + bringing comp owners into the design. <b>Success metrics in three tiers:</b> "
               "adoption (2 quarters) → comparability (2&ndash;3) → business outcomes (3&ndash;4). Don&rsquo;t "
               "promise business results in quarter one.", body))
story.append(box([P("<b>The single strongest card:</b> the pack contradicts itself &mdash; the Definitions sheet "
                    "says the pipeline is <b>Contact → MQL → SQL → Lead</b>, the problem statement says "
                    "<b>Known → MQL → SQL → Opportunity</b>. Two models, one organisation, one document. "
                    "That&rsquo;s undeniable internal evidence that the project is needed &mdash; lead with it if "
                    "the room is sceptical.", co)]))

# 5 WHAT IT TESTS
story.append(sec("5&nbsp;&nbsp;What the assessors are really testing"))
story.append(blist([
    "<b>Analytical honesty</b> &mdash; do you check definitions against the data, or take them on trust?",
    "<b>Business judgement</b> &mdash; rank on the measure everyone trusts; diagnose, don&rsquo;t just describe.",
    "<b>Communication</b> &mdash; one clear story, facts vs assumptions labelled.",
    "<b>Structured problem-solving</b> &mdash; the 3-bucket triage that stops the project sprawling.",
    "<b>Stakeholder savvy</b> &mdash; the comp risk, the politics of pilot choice, influence without authority.",
    "<b>Intellectual honesty under pressure</b> &mdash; refusing to invent a number or a date you can&rsquo;t "
    "support.",
]))

story.append(PageBreak())

# 6 Q&A TASK 1
story.append(sec("6&nbsp;&nbsp;Questions you&rsquo;ll be asked — Task 1 (the analysis)"))
q1 = [["They&rsquo;ll ask", "Say", "Testing"],
      ["&ldquo;Is &minus;6.5% actually bad?&rdquo;", P("Yes &mdash; it&rsquo;s worse than the &minus;4.9% for "
         "everyone else, and it&rsquo;s in the accounts we can least afford to lose.", cell), "Context, not just the number"],
      ["&ldquo;Why two delivery percentages?&rdquo;", P("One is vs the date the customer <i>requested</i> (POT-AR), "
         "one vs the date we <i>promised</i> (POT-C). A gap means we re-negotiate dates rather than miss our own.", cell),
       "Do you understand the metric"],
      ["&ldquo;Why exclude 2026?&rdquo;", P("Data ends 31-Mar-2026 &mdash; one quarter, not a year. Including it "
         "makes everyone look collapsed. Used only as an annualised, labelled momentum signal.", cell),
       "Rigour on time windows"],
      ["&ldquo;How is win rate calculated?&rdquo;", P("Won / (won + lost); open deals excluded. Reverse-engineered "
         "from the data &mdash; the Definitions sheet describes it differently.", cell), "Method + honesty"],
      ["&ldquo;Are they really the same parent?&rdquo;", P("They share an identical global-parent revenue figure "
         "&mdash; the only hierarchy field. I&rsquo;d confirm before acting, but it&rsquo;s worth confirming.", cell),
       "Inference vs fact"],
      ["&ldquo;Maybe sales handles those accounts directly?&rdquo;", P("Possibly &mdash; worth confirming. But 86% "
         "of customers have no marketing data at all, so it&rsquo;s a recording gap as much as a coverage one.", cell),
       "Absence vs non-capture"],
      ["&ldquo;Why rank on revenue?&rdquo;", P("It&rsquo;s the one measure every stakeholder already agrees on; "
         "I then diagnose each account on growth, pipeline, service and marketing.", cell), "Defensible choices"],
      ["&ldquo;Can we see the workings?&rdquo;", P("Yes &mdash; every figure is a live formula in the "
         "Analysis_EDA / Analysis_Top10 tabs; assumptions are in Analysis_Approach.", cell), "Reproducibility"]]
story.append(tbl(q1, [USABLE * 0.26, USABLE * 0.56, USABLE * 0.18]))

# 7 Q&A TASK 2
story.append(sec("7&nbsp;&nbsp;Questions you&rsquo;ll be asked — Task 2 (the proposal)"))
q2 = [["Who / question", "Say", "Testing"],
      ["CMO: &ldquo;Why standardise? Our regions are genuinely different.&rdquo;",
       P("Standardise the definition, not the process. Fix names, entry/exit criteria and timestamps; leave "
         "routing, cadence and channel local.", cell), "Semantics vs centralising ops"],
      ["CMO: &ldquo;What does success look like, and when?&rdquo;",
       P("Adoption (2 qtrs) → comparability (2&ndash;3) → business outcomes (3&ndash;4). No business results in "
         "Q1.", cell), "Not over-promising"],
      ["CFO: &ldquo;Cost and return?&rdquo;",
       P("I can&rsquo;t size the return until the assessment shows how much pipeline is invisible/double-counted. "
         "I&rsquo;ll commit to the cost of Step 1 and a decision gate &mdash; not a guessed number.", cell),
       "Won&rsquo;t invent numbers"],
      ["Regional Sales VP: &ldquo;My team is paid on SQLs.&rdquo;",
       P("Biggest risk, handled before go-live: run old + new definitions in parallel a quarter, publish the "
         "conversion factor, and put comp owners in the design so quotas are rebased, not broken.", cell),
       "Incentives (where projects die)"],
      ["Sales VP: &ldquo;Why absorb the disruption?&rdquo;",
       P("You keep your process &mdash; only the label and timestamp change. In return you finally get "
         "benchmarking you can trust.", cell), "Selling change to those who lose autonomy"],
      ["Mktg Ops: &ldquo;Assess without spending six months?&rdquo;",
       P("Three parallel tracks over 4&ndash;6 wks: systems &amp; data reconcile; structured workshops on a fixed "
         "template; trace 30&ndash;50 real leads that settle disputes.", cell), "A method, not just meetings"],
      ["Data/BI: &ldquo;Which model is right &mdash; Contact→MQL→SQL→Lead or Known→MQL→SQL→Opportunity?&rdquo;",
       P("Neither, until someone owns it &mdash; and that contradiction inside one pack is the clearest evidence "
         "the project is needed. I&rsquo;d open the assessment with it.", cell), "Did you spot it (strongest card)"],
      ["Data/BI: &ldquo;What about 3 years of old data?&rdquo;",
       P("Map and restate only where the mapping is defensible; mark the rest as a visible break in series. A "
         "visible break beats a silent wrong number.", cell), "Won&rsquo;t fake comparability"],
      ["CRM Director: &ldquo;Why not the vendor&rsquo;s out-of-the-box funnel?&rdquo;",
       P("Start there. But OOTB assumes one sales motion; if the assessment finds genuinely different motions it "
         "needs an extension, not a custom-field workaround.", cell), "Don&rsquo;t reinvent; know when config isn&rsquo;t enough"],
      ["Demand Gen: &ldquo;Leads that skip stages or go backwards?&rdquo;",
       P("Both are normal. Skips counted as passed so conversion maths balances; regressions logged with a reason "
         "code, never by overwriting the timestamp.", cell), "Real lead behaviour"],
      ["PM: &ldquo;How long / when finished?&rdquo;",
       P("Four gated phases; I won&rsquo;t commit a final date before Step 1 &mdash; until we see the gap, any "
         "date is a guess. I&rsquo;ll give you Step 1 firm and a sized plan at the end of it.", cell),
       "Won&rsquo;t commit dates you can&rsquo;t know"],
      ["PM: &ldquo;Which region do you pilot?&rdquo;",
       P("Not the biggest, not the most broken &mdash; a mid-sized, cooperative region with reasonable data. "
         "Pilot choice is political as much as technical.", cell), "Judgement on pilots"],
      ["Risk: &ldquo;What if the CRM programme is cancelled?&rdquo;",
       P("The definitional and governance work still stands on existing systems &mdash; designed to be "
         "system-agnostic so it doesn&rsquo;t die with a platform decision.", cell), "Not coupled to one dependency"],
      ["Sceptic: &ldquo;We tried this before and it failed.&rdquo;",
       P("I&rsquo;d ask <i>why</i> first &mdash; the usual causes (standardising process not definitions, no owner "
         "after go-live, no comp handling) are all addressed here, but the reason changes the design.", cell),
       "Will you ask or bluff (ask)"],
      ["CMO: &ldquo;How does this connect to Task 1?&rdquo;",
       P("The customer data has no lifecycle-stage field, so you can&rsquo;t join funnel performance to customer "
         "value today. Standardising the funnel is what makes that join possible.", cell), "One story, two tasks"]]
story.append(tbl(q2, [USABLE * 0.28, USABLE * 0.54, USABLE * 0.18]))

# 8 CLOSERS
story.append(sec("8&nbsp;&nbsp;Turn it around — and three reminders"))
story.append(P("<b>Three questions to ask <i>them</i></b> (shows seniority):", h2))
story.append(blist([
    "Which funnel stage is compensation actually tied to today, in each region? (Determines how hard this is.)",
    "Is there an existing data-governance forum to plug into, or must one be created?",
    "What&rsquo;s the immovable CRM date, and what&rsquo;s already locked in its data model? (That&rsquo;s your "
    "design space.)",
]))
story.append(P("<b>Three things to remember when presenting</b>", h2))
story.append(blist([
    "<b>Label facts vs assumptions.</b> Sales figures are facts; the parent grouping and win-rate formula are "
    "inferences. On Task 2, almost nothing is a finding yet &mdash; it&rsquo;s an approach.",
    "<b>If you don&rsquo;t know, say when you would.</b> &ldquo;I can&rsquo;t tell you until Step 1 is done "
    "&mdash; 4&ndash;6 weeks&rdquo; is a strong answer; an invented date is not.",
    "<b>Lead with the conflicting stage names</b> if the room doubts the project is needed &mdash; it&rsquo;s "
    "evidence from their own documents and takes fifteen seconds.",
]))
story.append(Spacer(1, 6))
story.append(P("Prep note: this pack synthesises the case brief, the dataset, the Analysis_Approach / EDA / "
               "Top-10 working, and the Case_Study_QA &amp; Slide talk-track from the workbook. Every Task-1 "
               "number is a live formula in those tabs &mdash; be ready to open them.", small))


def furn(canvas, doc):
    canvas.saveState(); canvas.setStrokeColor(MID); canvas.setLineWidth(0.5)
    if doc.page > 1:
        canvas.line(M, PAGE_H - M + 14, PAGE_W - M, PAGE_H - M + 14)
        canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
        canvas.drawString(M, PAGE_H - M + 18, "Amplify Analytix BA Case — Explainer & Interview Q&A")
    canvas.line(M, M - 12, PAGE_W - M, M - 12)
    canvas.setFont("Helvetica", 7.5); canvas.setFillColor(GREY)
    canvas.drawString(M, M - 22, "Interview prep")
    canvas.drawRightString(PAGE_W - M, M - 22, "Page %d" % doc.page)
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M + 6,
                        title="Amplify Analytix BA Case — Explainer & Q&A Prep", author="Juhi Bhalla")
doc.build(story, onFirstPage=furn, onLaterPages=furn)
print("PDF written to", OUT)
