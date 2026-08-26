#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Two companion PDFs for the Spotify India engagement BRD:
  1) Simplified BRD  - plain, human language you can walk stakeholders through.
  2) Explainer       - talking points / how to present it to stakeholders.
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
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=14, leading=17, textColor=NAVY, spaceBefore=13, spaceAfter=2)
body = ParagraphStyle("b", fontName="Helvetica", fontSize=10.4, leading=14.6, textColor=black, alignment=TA_JUSTIFY, spaceAfter=6)
body_l = ParagraphStyle("bl", parent=body, alignment=TA_LEFT)
bullet = ParagraphStyle("bu", fontName="Helvetica", fontSize=10.3, leading=14, textColor=black, leftIndent=13, bulletIndent=3, spaceAfter=3.5)
cell = ParagraphStyle("c", fontName="Helvetica", fontSize=9.4, leading=12.4, textColor=black)
cellw = ParagraphStyle("cw", fontName="Helvetica-Bold", fontSize=9.4, leading=12.4, textColor=white)
small = ParagraphStyle("sm", fontName="Helvetica-Oblique", fontSize=8.6, leading=11.5, textColor=GREY, spaceAfter=4)
callout = ParagraphStyle("co", fontName="Helvetica", fontSize=10.6, leading=14.6, textColor=NAVY, leftIndent=9, rightIndent=9, spaceBefore=2, spaceAfter=2)
calloutb = ParagraphStyle("cob", fontName="Helvetica-Bold", fontSize=11, leading=15, textColor=NAVY, leftIndent=9, rightIndent=9, spaceBefore=2, spaceAfter=2)


def rule(c=GREEN, th=1.4, sb=1, sa=7):
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
# 1) SIMPLIFIED BRD
# ==========================================================================
s = []
s.append(rule(GREEN, 3, 0, 9))
s.append(P("Spotify India — Getting People to Listen More", title_style))
s.append(P("Business Requirements Document (Simplified) · The engagement &amp; listening-time problem", subtitle_style))
s.append(rule(NAVY, 1, 0, 8))
s.append(P("<b>Version</b> 1.0 (Draft) &nbsp;&bull;&nbsp; <b>Date</b> August 2026 &nbsp;&bull;&nbsp; "
           "<b>By</b> Juhi Bhalla &nbsp;&bull;&nbsp; <b>For</b> Design, Engineering &amp; Strategy", body_l))
s.append(box([P("This is the plain-language version of our BRD. It defines the problem we&rsquo;re solving and "
                "why &mdash; <b>not</b> the solution. We&rsquo;ll get to ideas and features later; first we all "
                "need to agree on the problem.", callout)]))

s.append(sec("The short version"))
s.append(P("India is one of Spotify&rsquo;s <b>biggest audiences but smallest earners</b>. The single most "
           "powerful lever we have is <b>engagement</b> &mdash; how much time people actually spend listening. "
           "It&rsquo;s a simple chain: <b>more listening &rarr; people stick around &rarr; sticking around is "
           "what earns money</b> (ads for free users, subscriptions for premium)."))
s.append(P("Today, a lot of Indian listeners aren&rsquo;t building the daily habit. Often the music "
           "doesn&rsquo;t feel relevant enough (wrong language, mood, or moment), the app can feel heavy on "
           "data, or free options like YouTube already feel &lsquo;good enough.&rsquo; So people listen a "
           "little, drift away, and don&rsquo;t come back as often as they could."))
s.append(P("This document lays that problem out clearly so design, engineering, and strategy start from the "
           "same page. (The specific numbers come from our Milestone&nbsp;1 research &mdash; marked "
           "<b>[M1]</b> where they go.)"))

s.append(sec("What we&rsquo;re trying to achieve"))
s.append(blist([
    "<b>The business goal (the why):</b> earn more and lose fewer users, by getting more value out of a huge "
    "audience.",
    "<b>The product goal (what we&rsquo;ll actually move):</b> more <b>time spent listening</b> per person &mdash; "
    "more days active, longer sessions, more often.",
]))
s.append(P("In one line: <b>the product goal (listening time) is how we reach the business goal (revenue and "
           "retention).</b> If we only chase installs or sign-ups, we&rsquo;re measuring vanity, not value."))

s.append(sec("Who we&rsquo;re solving for"))
s.append(P("India isn&rsquo;t one audience &mdash; it&rsquo;s many. People differ by <b>city vs town, free vs "
           "paid, age, and language</b>, and each listens differently. Three quick stand-ins:"))
per = [["Person", "In plain words", "What they really want (their &lsquo;job&rsquo;)"],
       [P("<b>Aditya</b><br/>Gen&nbsp;Z, city, free", cell), P("College student, metro, budget phone, limited "
          "data, likes what&rsquo;s trending.", cell), P("&ldquo;On my commute or with friends, give me "
          "effortless, on-trend music &mdash; don&rsquo;t make me search.&rdquo;", cell)],
       [P("<b>Meera</b><br/>Millennial, Tier-2, free", cell), P("Working professional, smaller city, prefers "
          "her regional language, watches her data.", cell), P("&ldquo;While I work or do chores, play familiar "
          "regional music that just works and doesn&rsquo;t eat my data.&rdquo;", cell)],
       [P("<b>Rohan</b><br/>Millennial, city, premium", cell), P("Busy urban professional, several devices, "
          "playlists + podcasts.", cell), P("&ldquo;When I focus or relax, give me reliable, spot-on listening "
          "across my devices without fiddling.&rdquo;", cell)]]
s.append(tbl(per, [USABLE * 0.2, USABLE * 0.38, USABLE * 0.42]))

s.append(sec("What&rsquo;s getting in the way"))
s.append(P("Four honest reasons people don&rsquo;t listen as much as they could:"))
s.append(blist([
    "<b>Relevance</b> &mdash; the music we surface doesn&rsquo;t always match their language, mood, or the "
    "moment, so they lose interest or go elsewhere.",
    "<b>Access</b> &mdash; data cost, budget phones, and patchy internet make listening feel heavier than it "
    "should.",
    "<b>Habit</b> &mdash; without a relevant first experience, people don&rsquo;t build the daily habit, so "
    "they come back less.",
    "<b>Value</b> &mdash; free alternatives (especially YouTube) feel &lsquo;good enough,&rsquo; so both our "
    "free and premium experiences have to clearly earn their place.",
]))

s.append(sec("What we&rsquo;re NOT doing (yet)"))
s.append(P("So expectations stay clear:"))
s.append(blist([
    "We are <b>defining the problem</b>, not designing the fix &mdash; no features, screens, or ideas yet.",
    "No pricing, packaging, or content-licensing changes here.",
    "India only, mobile-first, both free and premium users.",
    "Solutions come later (Milestone&nbsp;4), <i>after</i> we&rsquo;ve tested our assumptions.",
]))

s.append(sec("What &lsquo;good&rsquo; looks like"))
s.append(P("Our <b>North Star</b> &mdash; the one number that best shows we&rsquo;re delivering value &mdash; is "
           "<b>time spent listening</b> (minutes per active user per day). It rolls up simply:"))
s.append(box([P("<b>More listening time &rarr; better retention (people stay) &rarr; more money (ad revenue + "
                "premium conversion, higher ARPU/LTV).</b>", calloutb)]))
s.append(P("The handful of things we&rsquo;ll watch:"))
s.append(blist([
    "<b>Listening time</b> per active user (our North Star), by segment.",
    "<b>Stickiness &amp; sessions:</b> daily vs monthly actives, sessions a day, how long each lasts.",
    "<b>Retention:</b> how many come back after 7 and 30 days; how many churn.",
    "<b>Money signals:</b> ad listening hours, free&rarr;premium conversion, revenue per user.",
]))
s.append(P("Actual starting points and targets come from Milestone&nbsp;1 <b>[M1]</b> &mdash; we&rsquo;ll set "
           "them together.", small))

s.append(sec("What we&rsquo;re assuming, and what&rsquo;s fixed"))
s.append(P("<b>We&rsquo;re assuming:</b> our Milestone&nbsp;1 findings hold; most Indian users start on free; "
           "language relevance and affordability really matter; and listening time is a fair early signal of "
           "retention and revenue.", body))
s.append(P("<b>What&rsquo;s fixed (constraints):</b> low willingness to pay, varied devices and connectivity, "
           "catalogue/licensing we can&rsquo;t change here, strong free competition, evolving Indian data "
           "rules, and a cross-team, multi-time-zone way of working.", body))

s.append(sec("Who&rsquo;s involved"))
s.append(P("Product (owns the framing), Design &amp; UX Research (users, personas, journeys), Engineering "
           "(what&rsquo;s feasible, performance &amp; data), Data/Analytics (the metrics and baselines), "
           "Marketing/Growth, Content &amp; Regional teams (language relevance), and Strategy/Leadership "
           "(the business goals)."))

s.append(sec("A few terms, in plain English"))
gl = [["Term", "Plain meaning"],
      ["Engagement", "How actively people use the app &mdash; here, mostly how much they listen."],
      ["North Star metric", "The one number that best shows we&rsquo;re delivering value: <b>listening time</b>."],
      ["KPI tree", "A simple map of how listening time rolls up into retention, then money."],
      ["Retention / churn", "How many people keep coming back vs how many leave."],
      ["ARPU / LTV", "How much money an average user brings in &mdash; per period, and over their whole time with us."],
      ["Job-to-be-Done", "The real reason someone plays music &mdash; the &lsquo;job&rsquo; they hire it for."]]
s.append(tbl(gl, [USABLE * 0.24, USABLE * 0.76]))
s.append(Spacer(1, 6))
s.append(P("<b>The bottom line:</b> if we help people listen a little more &mdash; by making it more relevant, "
           "easier to access, and worth the habit &mdash; retention and revenue follow. That&rsquo;s the whole "
           "game. Solutions come next; agreeing on this problem comes first.", body))

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
tp = [["BRD section", "Say this in one line", "Why it&rsquo;s there"],
      ["Executive summary", "&ldquo;Here&rsquo;s the problem and why it matters, in a paragraph.&rdquo;", "Sets the frame fast."],
      ["Scope (in/out)", "&ldquo;We&rsquo;re defining the problem, not the fix &mdash; here&rsquo;s what&rsquo;s in and out.&rdquo;", "Prevents scope creep."],
      ["Business drivers", "&ldquo;These forces make this urgent now.&rdquo;", "Answers &lsquo;why now.&rsquo;"],
      ["Current process", "&ldquo;This is how people listen today &mdash; and where we lose them.&rdquo;", "Grounded in reality (personas + journey)."],
      ["Proposed process", "&ldquo;We&rsquo;re reframing it as four problems: relevance, access, habit, value.&rdquo;", "Framing, not solutions."],
      ["Requirements", "&ldquo;These are the needs any solution must address &mdash; still no features.&rdquo;", "Problem-focused."],
      ["Success &amp; KPIs", "&ldquo;Our North Star is listening time; here&rsquo;s how it maps to money.&rdquo;", "How we&rsquo;ll know it worked."],
      ["Assumptions/constraints", "&ldquo;Here&rsquo;s what we&rsquo;re assuming and what&rsquo;s fixed.&rdquo;", "Honest about limits."],
      ["Stakeholders", "&ldquo;Here&rsquo;s who owns and informs each part.&rdquo;", "Clear roles."]]
e.append(tbl(tp, [USABLE * 0.24, USABLE * 0.5, USABLE * 0.26]))

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
