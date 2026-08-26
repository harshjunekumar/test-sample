#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two companion PDFs for the Spotify India engagement BRD:
  1) Simplified BRD - plain, human language, using the official checklist
     headers from the problem statement (all 16 sections).
  2) Explainer      - talking points / how to present it to stakeholders.
Problem framing only; no solutions.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_LEFT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether, ListFlowable, ListItem)

NAVY = HexColor("#1F3A5F")
GREEN = HexColor("#1DB954")
LIGHT = HexColor("#EEF2F7")
MID = HexColor("#C9D6E5")
GREY = HexColor("#555555")
M = 0.85 * inch
PAGE_W, PAGE_H = A4
USABLE = PAGE_W - 2 * M

title_style = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=23, leading=27, textColor=NAVY, spaceAfter=3)
subtitle_style = ParagraphStyle("st", fontName="Helvetica", fontSize=12.5, leading=16, textColor=GREY, spaceAfter=9)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=13, leading=16, textColor=NAVY, spaceBefore=11, spaceAfter=2)
body = ParagraphStyle("b", fontName="Helvetica", fontSize=10.2, leading=14.2, textColor=black, alignment=TA_JUSTIFY, spaceAfter=5.5)
body_l = ParagraphStyle("bl", parent=body, alignment=TA_LEFT)
bullet = ParagraphStyle("bu", fontName="Helvetica", fontSize=10.1, leading=13.6, textColor=black, leftIndent=13, bulletIndent=3, spaceAfter=3)
cell = ParagraphStyle("c", fontName="Helvetica", fontSize=9.3, leading=12.2, textColor=black)
cellw = ParagraphStyle("cw", fontName="Helvetica-Bold", fontSize=9.3, leading=12.2, textColor=white)
small = ParagraphStyle("sm", fontName="Helvetica-Oblique", fontSize=8.6, leading=11.5, textColor=GREY, spaceAfter=4)
callout = ParagraphStyle("co", fontName="Helvetica", fontSize=10.4, leading=14.2, textColor=NAVY, leftIndent=9, rightIndent=9, spaceBefore=2, spaceAfter=2)
calloutb = ParagraphStyle("cob", fontName="Helvetica-Bold", fontSize=10.8, leading=14.6, textColor=NAVY, leftIndent=9, rightIndent=9, spaceBefore=2, spaceAfter=2)


def rule(c=GREEN, th=1.4, sb=1, sa=6):
    return HRFlowable(width="100%", thickness=th, color=c, spaceBefore=sb, spaceAfter=sa)


def sec(title):
    return KeepTogether([Paragraph(title, h1), rule()])


def P(t, st=body):
    return Paragraph(t, st)


def blist(items):
    return ListFlowable([ListItem(Paragraph(t, bullet), leftIndent=13, value="•") for t in items],
                        bulletType="bullet", start="•", leftIndent=6)


def tbl(data, widths, hbg=NAVY):
    rows = []
    for r, row in enumerate(data):
        rr = [c if isinstance(c, Paragraph) else Paragraph(str(c), cellw if r == 0 else cell) for c in row]
        rows.append(rr)
    t = Table(rows, colWidths=widths, repeatRows=1)
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 6), ("RIGHTPADDING", (0, 0), (-1, -1), 6),
             ("TOPPADDING", (0, 0), (-1, -1), 4), ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
             ("BACKGROUND", (0, 0), (-1, 0), hbg),
             ("LINEBELOW", (0, 0), (-1, -1), 0.4, MID), ("LINEBEFORE", (0, 0), (-1, -1), 0.4, MID),
             ("LINEAFTER", (0, 0), (-1, -1), 0.4, MID), ("LINEABOVE", (0, 0), (-1, 0), 0.4, MID)]
    for r in range(1, len(rows)):
        if r % 2 == 0:
            style.append(("BACKGROUND", (0, r), (-1, r), LIGHT))
    t.setStyle(TableStyle(style))
    return t


def box(paras):
    inner = Table([[p] for p in paras], colWidths=[USABLE - 10])
    inner.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 10), ("RIGHTPADDING", (0, 0), (-1, -1), 10),
                               ("TOPPADDING", (0, 0), (-1, -1), 8), ("BOTTOMPADDING", (0, 0), (-1, -1), 8),
                               ("BACKGROUND", (0, 0), (-1, -1), LIGHT), ("LINEBEFORE", (0, 0), (0, -1), 3.5, GREEN)]))
    return KeepTogether(inner)


def make_furniture(header_text):
    def f(canvas, doc):
        canvas.saveState()
        canvas.setStrokeColor(MID)
        canvas.setLineWidth(0.5)
        if doc.page > 1:
            canvas.line(M, PAGE_H - M + 14, PAGE_W - M, PAGE_H - M + 14)
            canvas.setFont("Helvetica", 7.5)
            canvas.setFillColor(GREY)
            canvas.drawString(M, PAGE_H - M + 18, header_text)
        canvas.line(M, M - 12, PAGE_W - M, M - 12)
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(GREY)
        canvas.drawString(M, M - 22, "Spotify India — Engagement & Listening Time • Problem framing only")
        canvas.drawRightString(PAGE_W - M, M - 22, "Page %d" % doc.page)
        canvas.restoreState()
    return f


def build(path, title, header, story):
    doc = SimpleDocTemplate(path, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M + 6,
                            title=title, author="Juhi Bhalla")
    fur = make_furniture(header)
    doc.build(story, onFirstPage=fur, onLaterPages=fur)
    print("PDF written to", path)


# ==========================================================================
# 1) SIMPLIFIED BRD  (official checklist headers, plain content, all sections)
# ==========================================================================
s = []
s.append(rule(GREEN, 3, 0, 9))
s.append(P("Spotify India — User Engagement &amp; Listening Time", title_style))
s.append(P("Business Requirements Document (Simplified) · Problem framing only — no solutions", subtitle_style))
s.append(rule(NAVY, 1, 0, 8))
s.append(P("<b>Version</b> 1.0 (Draft) &nbsp;&bull;&nbsp; <b>Date</b> August 2026 &nbsp;&bull;&nbsp; "
           "<b>By</b> Juhi Bhalla &nbsp;&bull;&nbsp; <b>For</b> Design, Engineering &amp; Strategy", body_l))
s.append(box([P("This is the plain-language version of the BRD. It follows the same sections as the full "
                "document and defines the problem we&rsquo;re solving and why &mdash; <b>not</b> the solution. "
                "Ideas and features come later; first we agree on the problem. Figures marked <b>[M1]</b> come "
                "from Milestone&nbsp;1 research.", callout)]))

s.append(sec("1&nbsp;&nbsp;Executive Summary Snapshot"))
s.append(P("India is one of Spotify&rsquo;s <b>biggest audiences but smallest earners</b>. Our strongest lever "
           "is <b>engagement</b> &mdash; how much time people spend listening. It&rsquo;s a simple chain: "
           "<b>more listening &rarr; people stay &rarr; staying is what earns money</b> (ads for free users, "
           "subscriptions for premium)."))
s.append(P("Today, many Indian listeners aren&rsquo;t building the daily habit &mdash; the music can feel off "
           "(wrong language, mood, or moment), the app heavy on data, or free options like YouTube "
           "&lsquo;good enough.&rsquo; This document defines that problem so design, engineering, and strategy "
           "start from the same page. <b>[M1: Spotify India listening-time findings]</b>"))

s.append(sec("2&nbsp;&nbsp;Project Description"))
s.append(P("<b>What this is:</b> a shared, plain-language definition of Spotify India&rsquo;s engagement / "
           "listening-time problem, building on Milestone&nbsp;1 research."))
s.append(P("<b>What we&rsquo;re trying to achieve.</b> The <b>business goal</b>: earn more and lose fewer users "
           "from a huge audience. The <b>product goal</b>: more <b>time spent listening</b> per person (more "
           "active days, longer sessions, more often). In one line: the product goal (listening time) is how we "
           "reach the business goal (revenue + retention). Chasing installs or sign-ups alone measures vanity, "
           "not value."))

s.append(sec("3&nbsp;&nbsp;Project Scope (In-Scope / Out-of-Scope)"))
sc = [["In-scope", "Out-of-scope"],
      [P("&bull; Defining the engagement / listening-time problem for <b>India</b>.<br/>"
         "&bull; <b>Free</b> and <b>premium</b> users; mobile-first.<br/>"
         "&bull; Segments, personas, journeys and Jobs-to-be-Done.<br/>"
         "&bull; Problem-focused requirements, KPIs, assumptions.", cell),
       P("&bull; Solutions, features, or UI (later milestones).<br/>"
         "&bull; Pricing / packaging or content-licensing changes.<br/>"
         "&bull; Markets outside India; backend re-architecture.<br/>"
         "&bull; Marketing creative or vendor/tool selection.", cell)]]
s.append(tbl(sc, [USABLE * 0.5, USABLE * 0.5]))

s.append(sec("4&nbsp;&nbsp;Business Drivers"))
s.append(P("Why this is urgent now:"))
s.append(blist([
    "A <b>large but low-earning audience</b> &mdash; growth needs engagement, not just sign-ups.",
    "<b>Retention economics:</b> without a listening habit, cheaply-acquired users churn to free rivals.",
    "<b>Competition for attention</b> (JioSaavn, Wynk, YouTube Music, Apple/Amazon, and free YouTube) &mdash; "
    "it&rsquo;s a share-of-ear battle.",
    "<b>Revenue is tied to listening:</b> ad income scales with time spent; premium value and conversion depend "
    "on habitual usefulness.",
]))

s.append(sec("5&nbsp;&nbsp;Current Process (Spotify Engagement Patterns and Listening Behaviors)"))
s.append(P("How people listen today:"))
s.append(blist([
    "Mostly on the <b>free tier</b>, on <b>budget Android phones</b>, often on limited data / patchy internet.",
    "Music is usually a <b>companion</b> to something else &mdash; commute, work, chores, workouts, sleep.",
    "<b>Regional-language</b> repertoire drives a lot of listening; relevance to a user&rsquo;s language matters.",
    "When recommendations miss (language / mood / moment), people fall back to search, known songs, or "
    "competitors &mdash; and sessions get shorter.",
]))
s.append(P("India isn&rsquo;t one audience &mdash; it differs by <b>city vs town, free vs paid, age, and "
           "language</b>. Three quick stand-ins:"))
per = [["Person", "In plain words", "What they really want (their &lsquo;job&rsquo;)"],
       [P("<b>Aditya</b><br/>Gen&nbsp;Z, city, free", cell), P("College student, metro, budget phone, limited "
          "data, likes what&rsquo;s trending.", cell), P("&ldquo;On my commute or with friends, effortless, "
          "on-trend music &mdash; don&rsquo;t make me search.&rdquo;", cell)],
       [P("<b>Meera</b><br/>Millennial, Tier-2, free", cell), P("Working professional, smaller city, prefers her "
          "regional language, watches data.", cell), P("&ldquo;While I work or do chores, familiar regional "
          "music that just works and saves data.&rdquo;", cell)],
       [P("<b>Rohan</b><br/>Millennial, city, premium", cell), P("Busy urban professional, several devices, "
          "playlists + podcasts.", cell), P("&ldquo;When I focus or relax, reliable, spot-on listening across "
          "my devices without fiddling.&rdquo;", cell)]]
s.append(tbl(per, [USABLE * 0.2, USABLE * 0.38, USABLE * 0.42]))
s.append(P("<b>Where we lose them:</b> weak first-session relevance &rarr; no habit; relevance / continuity "
           "gaps &rarr; fewer, shorter sessions; friction vs &lsquo;good-enough free&rsquo; &rarr; they switch.",
           small))

s.append(sec("6&nbsp;&nbsp;Proposed Process (Framing the Engagement Problem without Prescribing Solutions)"))
s.append(box([P("<b>Reframe (no solutions).</b> The goal is to <i>increase meaningful listening time</i> by "
                "reducing friction across four problem areas: <b>Relevance</b> (right content for language, "
                "mood, moment), <b>Access</b> (data-, device-, network-friendly), <b>Habit</b> (coming back "
                "and continuing), and <b>Value</b> (free and premium clearly worth it).", callout)]))
s.append(P("These four become the <b>hypotheses we&rsquo;ll test</b> in Milestone&nbsp;3 &mdash; stated here "
           "only to make the problem clear and testable, not to pick a solution.", body))

s.append(sec("7&nbsp;&nbsp;Functional Requirements (Problem-Focused)"))
s.append(P("The <i>needs</i> any future solution must meet (not features):"))
s.append(blist([
    "Help users <b>find relevant content easily</b> &mdash; by language, mood, and context.",
    "Let users <b>keep and resume</b> listening across contexts and devices (continuity).",
    "Work well for <b>cheap phones, low data, and weak networks</b>.",
    "Offer a <b>free experience worth choosing</b> over &lsquo;good-enough&rsquo; alternatives.",
    "Deliver a <b>relevant first session</b> to seed the habit early.",
    "Let the business <b>measure engagement reliably</b> (listening time, sessions, retention) by segment.",
]))

s.append(sec("8&nbsp;&nbsp;Non-Functional Requirements"))
s.append(blist([
    "<b>Fast</b> and smooth on low-to-mid-range Android devices.",
    "<b>Light on data</b> and graceful on weak / intermittent connectivity.",
    "<b>Reliable</b> and available; consistent offline / online.",
    "<b>Multilingual</b> UI and content across Hindi and major regional languages.",
    "<b>Scales</b> for peaks (festivals, releases, sale events).",
    "<b>Private &amp; compliant</b> with Indian data / content rules; well-instrumented for metrics.",
]))

s.append(sec("9&nbsp;&nbsp;Assumptions and Constraints"))
s.append(P("<b>Assumptions:</b> Milestone&nbsp;1 findings hold; most users start on free; language relevance and "
           "affordability matter; listening time is a fair early signal of retention and revenue; usage is "
           "mobile-first.", body))
s.append(P("<b>Constraints:</b> low willingness to pay; varied devices and connectivity; catalogue / licensing "
           "we can&rsquo;t change here; strong free competition; evolving Indian data rules; cross-team, "
           "multi-time-zone working.", body))

s.append(sec("10&nbsp;&nbsp;Success Criteria &amp; KPIs"))
s.append(box([P("<b>North Star:</b> <b>Time spent listening</b> (minutes per active user per day). It rolls up: "
                "<b>more listening &rarr; better retention &rarr; more money</b> (ad revenue + premium "
                "conversion, higher ARPU / LTV).", calloutb)]))
s.append(P("The few things we&rsquo;ll watch:"))
s.append(blist([
    "<b>Listening time</b> per active user (North Star), by segment.",
    "<b>Stickiness &amp; sessions:</b> daily vs monthly actives, sessions/day, session length.",
    "<b>Retention:</b> return after 7 and 30 days; churn.",
    "<b>Money signals:</b> ad listening hours, free&rarr;premium conversion, revenue per user.",
]))
s.append(P("Baselines and targets come from Milestone&nbsp;1 <b>[M1]</b> &mdash; set together.", small))

s.append(sec("11&nbsp;&nbsp;Timeline &amp; Milestones"))
tl = [["Milestone", "Focus", "Status"],
      ["M1 — Research", "Market, competitor &amp; user research; why engagement matters", P("<b>Done</b>", cell)],
      ["M2 — BRD (this)", "Problem definition, scope, framing, KPIs", P("<b>In review</b>", cell)],
      ["M3 — Discovery", "Test the four hypotheses; user research; sizing", "Upcoming"],
      ["M4 — PRD &amp; design", "Solution requirements &amp; design (solutions start here)", "Upcoming"]]
s.append(tbl(tl, [USABLE * 0.26, USABLE * 0.54, USABLE * 0.2]))

s.append(sec("12&nbsp;&nbsp;Stakeholders"))
s.append(P("<b>Product</b> (owns the framing), <b>Design &amp; UX Research</b> (users, personas, journeys), "
           "<b>Engineering</b> (feasibility, performance, data), <b>Data / Analytics</b> (metrics, baselines), "
           "<b>Marketing / Growth</b>, <b>Content &amp; Regional</b> teams (language relevance), and "
           "<b>Strategy / Leadership</b> (business goals)."))

s.append(sec("13&nbsp;&nbsp;(Optional) Cost &amp; Benefit"))
s.append(P("<b>Cost of doing nothing:</b> continued low listening time &rarr; weak retention &rarr; churn to "
           "free rivals; suppressed ad inventory and premium conversion; lost ground in a strategic market. "
           "<b>Benefit of solving it:</b> more listening &rarr; stronger retention &rarr; more ad and "
           "subscription revenue &rarr; better ARPU / LTV and a defensible position in India. Detailed "
           "financials to be modelled after validation <b>[M1 / M3]</b>."))

s.append(sec("14&nbsp;&nbsp;Glossary"))
gl = [["Term", "Plain meaning"],
      ["Engagement", "How actively people use the app &mdash; here, mostly how much they listen."],
      ["North Star metric", "The one number that best shows we&rsquo;re delivering value: <b>listening time</b>."],
      ["KPI tree", "A simple map of how listening time rolls up into retention, then money."],
      ["Retention / churn", "How many people keep coming back vs how many leave."],
      ["ARPU / LTV", "Revenue from an average user &mdash; per period, and over their whole time with us."],
      ["Job-to-be-Done", "The real reason someone plays music &mdash; the &lsquo;job&rsquo; they hire it for."]]
s.append(tbl(gl, [USABLE * 0.24, USABLE * 0.76]))

s.append(sec("15&nbsp;&nbsp;References"))
s.append(P("Directional market context draws on public sources &mdash; IFPI <i>Global Music Report</i>, "
           "FICCI&ndash;EY <i>Indian M&amp;E Report</i>, RedSeer streaming reports, and Spotify investor / "
           "press materials &mdash; plus the reader&rsquo;s Milestone&nbsp;1 research. <b>Cite the exact "
           "reports / editions used in Milestone&nbsp;1 for every specific figure.</b>", body))

s.append(sec("16&nbsp;&nbsp;Appendix"))
s.append(P("<b>Data to fill from Milestone&nbsp;1 [M1]:</b> Spotify India listening-time baselines by segment; "
           "free vs premium split; urban/rural and language mix; competitor engagement benchmarks; market size, "
           "growth and ARPU. Every <b>[M1]</b> marker in this document shows where your numbers and citations "
           "go.", body))
s.append(Spacer(1, 4))
s.append(P("<b>The bottom line:</b> if we help people listen a little more &mdash; more relevant, easier to "
           "access, worth the habit &mdash; retention and revenue follow. That&rsquo;s the whole game. "
           "Solutions come next; agreeing on this problem comes first.", body))

build("/home/user/test-sample/BRD_Spotify_India_Simplified.pdf",
      "Spotify India BRD (Simplified)", "BRD (Simplified) — Spotify India Engagement", s)


# ==========================================================================
# 2) EXPLAINER / TALKING POINTS
# ==========================================================================
e = []
e.append(rule(GREEN, 3, 0, 9))
e.append(P("How to Explain This BRD", title_style))
e.append(P("A simple walkthrough &amp; talking points · Spotify India engagement &amp; listening time", subtitle_style))
e.append(rule(NAVY, 1, 0, 8))
e.append(P("Use this to <b>present</b> the BRD with confidence. It gives you the pitch, the story, one-line "
           "talking points for each section, the &lsquo;fancy words&rsquo; in plain English, and answers to the "
           "questions people usually ask.", body_l))

e.append(sec("The 30-second pitch (say this first)"))
e.append(box([P("&ldquo;India is a <b>massive audience but low on revenue</b>. The best lever we have is "
                "<b>listening time</b> &mdash; the more people listen, the more they stay, and the more they "
                "stay, the more we earn. This document defines that problem clearly, so we all agree on "
                "<b>what</b> to solve and <b>why</b> &mdash; before we design anything.&rdquo;", calloutb)]))

e.append(sec("The story in four beats"))
e.append(P("People remember stories, not sections. Walk them through this arc:"))
e.append(blist([
    "<b>1. Why India matters:</b> huge, young, fast-growing audience &mdash; but among our lowest revenue per "
    "user. Big opportunity, real pressure.",
    "<b>2. The problem:</b> people aren&rsquo;t listening enough or building the daily habit &mdash; often "
    "because of relevance, data/device cost, or &lsquo;good-enough&rsquo; free rivals.",
    "<b>3. Why it matters to the business:</b> listening time &rarr; retention &rarr; revenue. It&rsquo;s a "
    "chain, and listening time is the first link.",
    "<b>4. What this document does:</b> it defines the problem so everyone aligns &mdash; it deliberately does "
    "<i>not</i> jump to solutions.",
]))

e.append(sec("One-line talking points, section by section"))
tp = [["BRD section (as in the brief)", "Say this in one line", "Why it&rsquo;s there"],
      ["Executive Summary Snapshot", "&ldquo;The problem and why it matters, in a paragraph.&rdquo;", "Sets the frame fast."],
      ["Project Description", "&ldquo;What this is, and the goal we&rsquo;re after.&rdquo;", "Business + product goal."],
      ["Project Scope (In/Out)", "&ldquo;We&rsquo;re defining the problem, not the fix.&rdquo;", "Prevents scope creep."],
      ["Business Drivers", "&ldquo;These forces make it urgent now.&rdquo;", "Answers &lsquo;why now.&rsquo;"],
      ["Current Process", "&ldquo;How people listen today &mdash; and where we lose them.&rdquo;", "Grounded (personas + journey)."],
      ["Proposed Process", "&ldquo;Reframed as four problems: relevance, access, habit, value.&rdquo;", "Framing, not solutions."],
      ["Functional / Non-Functional Requirements", "&ldquo;The needs any solution must meet &mdash; no features yet.&rdquo;", "Problem-focused."],
      ["Success Criteria &amp; KPIs", "&ldquo;North Star is listening time; here&rsquo;s how it maps to money.&rdquo;", "How we&rsquo;ll know it worked."],
      ["Assumptions and Constraints", "&ldquo;What we&rsquo;re assuming and what&rsquo;s fixed.&rdquo;", "Honest about limits."],
      ["Stakeholders", "&ldquo;Who owns and informs each part.&rdquo;", "Clear roles."]]
e.append(tbl(tp, [USABLE * 0.28, USABLE * 0.46, USABLE * 0.26]))

e.append(sec("The &lsquo;fancy words,&rsquo; in plain English"))
e.append(P("If someone looks puzzled, here&rsquo;s how to explain each term simply:"))
fw = [["Term", "How to explain it"],
      ["Business vs product outcomes", "&ldquo;The goal (money, retention) vs the thing we can actually move (listening time).&rdquo;"],
      ["North Star metric", "&ldquo;The one number that best shows we&rsquo;re delivering value &mdash; here, time spent listening.&rdquo;"],
      ["KPI tree", "&ldquo;A simple map: listening time at the top, rolling up into retention, then revenue.&rdquo;"],
      ["Job-to-be-Done (JTBD)", "&ldquo;The real reason someone plays music &mdash; e.g. &lsquo;something effortless for my commute.&rsquo;&rdquo;"],
      ["Persona / journey map", "&ldquo;A stand-in user and their path, so we design for real people, not averages.&rdquo;"],
      ["Functional vs non-functional", "&ldquo;What it must do vs how well it must do it (fast, light on data, reliable).&rdquo;"],
      ["Hypothesis", "&ldquo;A smart guess we&rsquo;ll test next &mdash; not a conclusion.&rdquo;"]]
e.append(tbl(fw, [USABLE * 0.28, USABLE * 0.72]))

e.append(sec("If someone asks&hellip; (quick answers)"))
qa = [["You might hear&hellip;", "You can say&hellip;"],
      ["&ldquo;Why not just build features?&rdquo;", P("&ldquo;Because we haven&rsquo;t agreed on the problem "
         "yet. Solving the wrong problem quickly is expensive &mdash; this aligns us first.&rdquo;", cell)],
      ["&ldquo;Where&rsquo;s the hard data?&rdquo;", P("&ldquo;Market context is cited; the specific baselines "
         "come from our Milestone&nbsp;1 research &mdash; marked <b>[M1]</b> to slot in.&rdquo;", cell)],
      ["&ldquo;Why listening time, not installs?&rdquo;", P("&ldquo;Installs are vanity; listening time is the "
         "value people actually get, and it predicts retention and revenue.&rdquo;", cell)],
      ["&ldquo;Is this just about premium users?&rdquo;", P("&ldquo;No &mdash; free users matter too. Their "
         "listening drives ad revenue and future conversion.&rdquo;", cell)],
      ["&ldquo;What happens after this?&rdquo;", P("&ldquo;Milestone&nbsp;3: we test the assumptions; then a "
         "PRD and design. Solutions start there.&rdquo;", cell)],
      ["&ldquo;Isn&rsquo;t engagement too vague?&rdquo;", P("&ldquo;That&rsquo;s why we anchor it to one clear "
         "number &mdash; time spent listening &mdash; and a KPI tree tying it to the business.&rdquo;", cell)]]
e.append(tbl(qa, [USABLE * 0.34, USABLE * 0.66]))

e.append(sec("Presenting tips"))
e.append(P("<b>Do:</b>", body_l))
e.append(blist([
    "Start with the business <b>why</b>, then the problem.",
    "Use a persona (like Aditya or Meera) to make it real &mdash; people connect with a person, not a metric.",
    "Keep pulling the conversation back to the <b>problem</b>, not the fix.",
    "Point to the KPI tree when someone worries &lsquo;engagement&rsquo; is fuzzy.",
]))
e.append(P("<b>Don&rsquo;t:</b>", body_l))
e.append(blist([
    "Jump to features or solutions &mdash; that&rsquo;s a later milestone.",
    "Drown people in metrics &mdash; lead with the one North Star.",
    "Over-claim numbers you can&rsquo;t cite &mdash; use the <b>[M1]</b> placeholders honestly.",
]))

e.append(sec("Leave them with this"))
e.append(box([P("&ldquo;If we get people to listen just a little more &mdash; by making it more relevant, "
                "easier to access, and worth the habit &mdash; retention, ads, and subscriptions all follow. "
                "That&rsquo;s the whole game. Today, we&rsquo;re just agreeing on the problem.&rdquo;", calloutb)]))

build("/home/user/test-sample/BRD_Spotify_India_Explainer.pdf",
      "How to Explain the BRD — Spotify India", "Explainer & Talking Points — Spotify India", e)
