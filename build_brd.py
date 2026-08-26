#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Business Requirements Document (BRD) - Spotify India: User Engagement &
Listening Time. Problem-framing document (no solutions), Milestone 2.
Rendered as a clean, professional multi-page PDF via reportlab.
"""
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, mm
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.enums import TA_CENTER, TA_LEFT, TA_JUSTIFY
from reportlab.lib.styles import ParagraphStyle
from reportlab.platypus import (SimpleDocTemplate, Paragraph, Spacer, Table,
                                TableStyle, HRFlowable, KeepTogether, PageBreak,
                                ListFlowable, ListItem)

NAVY = HexColor("#1F3A5F")
GREEN = HexColor("#1DB954")   # Spotify-ish accent for rules only
LIGHT = HexColor("#EEF2F7")
MID = HexColor("#C9D6E5")
GREY = HexColor("#555555")
OUT = "/home/user/test-sample/BRD_Spotify_India_Engagement.pdf"

M = 0.8 * inch
PAGE_W, PAGE_H = A4
USABLE = PAGE_W - 2 * M

title_style = ParagraphStyle("t", fontName="Helvetica-Bold", fontSize=24, leading=28,
                             textColor=NAVY, alignment=TA_LEFT, spaceAfter=4)
subtitle_style = ParagraphStyle("st", fontName="Helvetica", fontSize=13, leading=17,
                                textColor=GREY, alignment=TA_LEFT, spaceAfter=10)
h1 = ParagraphStyle("h1", fontName="Helvetica-Bold", fontSize=13.5, leading=16, textColor=NAVY,
                    spaceBefore=12, spaceAfter=2)
h2 = ParagraphStyle("h2", fontName="Helvetica-Bold", fontSize=10.8, leading=13.5, textColor=HexColor("#2b4a72"),
                    spaceBefore=7, spaceAfter=1)
body = ParagraphStyle("b", fontName="Helvetica", fontSize=9.7, leading=13.2, textColor=black,
                      alignment=TA_JUSTIFY, spaceAfter=5)
body_l = ParagraphStyle("bl", parent=body, alignment=TA_LEFT)
bullet = ParagraphStyle("bu", fontName="Helvetica", fontSize=9.6, leading=12.8, textColor=black,
                        leftIndent=13, bulletIndent=3, spaceAfter=2.5)
cell = ParagraphStyle("c", fontName="Helvetica", fontSize=8.9, leading=11.4, textColor=black)
cellb = ParagraphStyle("cb", fontName="Helvetica-Bold", fontSize=8.9, leading=11.4, textColor=NAVY)
cellw = ParagraphStyle("cw", fontName="Helvetica-Bold", fontSize=8.9, leading=11.4, textColor=white)
small = ParagraphStyle("sm", fontName="Helvetica-Oblique", fontSize=8.2, leading=10.5, textColor=GREY,
                       spaceAfter=4)
callout = ParagraphStyle("co", fontName="Helvetica", fontSize=9.6, leading=13, textColor=NAVY,
                         leftIndent=8, rightIndent=8, spaceBefore=2, spaceAfter=2)


def rule(c=NAVY, th=1.1, sb=2, sa=8):
    return HRFlowable(width="100%", thickness=th, color=c, spaceBefore=sb, spaceAfter=sa)


def sec(num, title):
    return KeepTogether([Spacer(1, 2), Paragraph(f"{num}&nbsp;&nbsp;{title}", h1),
                         rule(GREEN, 1.4, 1, 6)])


def blist(items):
    return ListFlowable([ListItem(Paragraph(t, bullet), leftIndent=13, value="•") for t in items],
                        bulletType="bullet", start="•", leftIndent=6)


def P(t, st=body):
    return Paragraph(t, st)


def tbl(data, widths, header=True, zebra=True, hbg=NAVY):
    rows = []
    for r, row in enumerate(data):
        rr = []
        for cval in row:
            if isinstance(cval, Paragraph):
                rr.append(cval)
            else:
                rr.append(Paragraph(str(cval), cellw if (header and r == 0) else cell))
        rows.append(rr)
    t = Table(rows, colWidths=widths, repeatRows=1 if header else 0)
    style = [("VALIGN", (0, 0), (-1, -1), "TOP"),
             ("LEFTPADDING", (0, 0), (-1, -1), 5), ("RIGHTPADDING", (0, 0), (-1, -1), 5),
             ("TOPPADDING", (0, 0), (-1, -1), 3.5), ("BOTTOMPADDING", (0, 0), (-1, -1), 3.5),
             ("LINEBELOW", (0, 0), (-1, -1), 0.4, MID),
             ("LINEBEFORE", (0, 0), (-1, -1), 0.4, MID), ("LINEAFTER", (0, 0), (-1, -1), 0.4, MID),
             ("LINEABOVE", (0, 0), (-1, 0), 0.4, MID)]
    if header:
        style += [("BACKGROUND", (0, 0), (-1, 0), hbg)]
    if zebra:
        for r in range(1, len(rows)):
            if r % 2 == 0:
                style.append(("BACKGROUND", (0, r), (-1, r), LIGHT))
    t.setStyle(TableStyle(style))
    return t


def box(paras):
    inner = Table([[p] for p in paras], colWidths=[USABLE - 10])
    inner.setStyle(TableStyle([("LEFTPADDING", (0, 0), (-1, -1), 9), ("RIGHTPADDING", (0, 0), (-1, -1), 9),
                               ("TOPPADDING", (0, 0), (-1, -1), 7), ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
                               ("BACKGROUND", (0, 0), (-1, -1), LIGHT),
                               ("LINEBEFORE", (0, 0), (0, -1), 3, GREEN)]))
    return KeepTogether(inner)


story = []

# ---------------------------------------------------------------- COVER
story.append(Spacer(1, 8))
story.append(rule(GREEN, 3, 0, 10))
story.append(P("Business Requirements Document (BRD)", title_style))
story.append(P("User Engagement &amp; Listening Time &mdash; Spotify India", subtitle_style))
story.append(rule(NAVY, 1, 0, 10))
dc = [["Field", "Detail"],
      ["Document", "Business Requirements Document (BRD) &mdash; Problem Definition"],
      ["Initiative", "Increasing user engagement and time spent listening in the Indian market"],
      ["Milestone", "Milestone 2 (builds on Milestone 1: market, competitor &amp; user research)"],
      ["Version", "1.0 &mdash; Draft for Review"],
      ["Date", "August 2026"],
      ["Prepared by", "Juhi Bhalla &mdash; Business Analyst / Product"],
      ["Audience", "Design, Engineering, Data/Analytics, Strategy &amp; Leadership"],
      ["Status", "Problem framing only &mdash; no solutions or features proposed at this stage"]]
story.append(tbl(dc, [USABLE * 0.24, USABLE * 0.76]))
story.append(Spacer(1, 8))
story.append(P("Note on data: Quantitative market context below is directional and drawn from public "
               "industry sources (see &sect;15 References). Specific baselines, targets, and figures marked "
               "<b>[M1]</b> should be populated from the reader&rsquo;s Milestone&nbsp;1 research and cited "
               "accordingly. This document defines the problem, scope, and business framing only; it does "
               "<b>not</b> propose solutions or features.", small))
story.append(PageBreak())

# ---------------------------------------------------------------- 1 EXEC SUMMARY
story.append(sec("1", "Executive Summary (Snapshot)"))
story.append(P("India is one of Spotify&rsquo;s largest markets by users yet among its lowest by revenue per "
               "user, making <b>engagement</b> &mdash; specifically <b>time spent listening</b> &mdash; the "
               "pivotal lever for the business. Time spent listening is a leading indicator of retention and, "
               "in turn, of monetization: on the free/ad-supported tier it determines ad inventory and "
               "impressions, and on premium it shapes perceived value, conversion, and lifetime value (LTV)."))
story.append(P("Despite rapid growth in India&rsquo;s streaming ecosystem, Spotify India faces a distinct "
               "engagement challenge shaped by price sensitivity, deep regional-language diversity, "
               "data-cost and device constraints, heavy reliance on the free tier, and intense competition "
               "(JioSaavn, Wynk Music, YouTube Music, Apple Music, Amazon Music, and free YouTube itself). "
               "The result is listening time and stickiness that under-index against the market&rsquo;s "
               "potential (IFPI; FICCI&ndash;EY; RedSeer). <b>[M1: insert Spotify India engagement / "
               "listening-time findings]</b>"))
story.append(box([P("<b>Problem statement (framing).</b> Spotify India is not fully converting its large, "
                    "young, mobile-first audience into <i>habitual, high-time listeners</i>. This BRD defines "
                    "the engagement / listening-time problem space &mdash; goals, target users, challenges, "
                    "requirements, success measures, and constraints &mdash; so that design, engineering, and "
                    "strategy teams can align on <i>what</i> must be solved and <i>why</i>, before any "
                    "solution is designed.", callout)]))
story.append(P("This document applies business-outcome vs product-outcome thinking, a KPI tree linking "
               "listening time to retention and monetization, user segmentation and personas "
               "(urban/rural, free/premium, Gen&nbsp;Z/millennial, language), Jobs-to-be-Done, journey "
               "mapping, and explicit assumption/hypothesis framing.", body))

# ---------------------------------------------------------------- 2 PROJECT DESCRIPTION
story.append(sec("2", "Project Description"))
story.append(P("<b>Purpose.</b> To structure the understanding gathered in Milestone&nbsp;1 into a shared "
               "problem definition for Spotify India&rsquo;s user engagement and listening-time challenge, "
               "enabling cross-functional alignment before solutioning.", body))
story.append(P("<b>Background.</b> Spotify launched in India in February&nbsp;2019 into a market transformed "
               "by cheap mobile data (post-2016) and a mobile-first, video-and-audio consumption culture in "
               "which free platforms &mdash; notably YouTube &mdash; are dominant music-discovery surfaces. "
               "India&rsquo;s recorded-music consumption is overwhelmingly streaming-led and heavily "
               "ad-supported, with comparatively low paid-subscription penetration and low ARPU (IFPI Global "
               "Music Report; FICCI&ndash;EY M&amp;E Report). Regional-language repertoire (Hindi and a wide "
               "range of regional languages) drives the majority of consumption.", body))
story.append(P("<b>The problem in focus.</b> Engagement &mdash; and its clearest proxy, <i>time spent "
               "listening</i> per active user &mdash; is under-realized relative to the size and youth of the "
               "audience. Because engagement feeds retention, and retention feeds monetization, small "
               "improvements in listening time compound into meaningful business impact.", body))
story.append(P("<b>Business outcomes vs product outcomes.</b> The two must be distinguished so teams optimise "
               "the right things:", body))
bo = [["Business Outcomes (the &lsquo;why&rsquo;)", "Product Outcomes (the measurable &lsquo;how&rsquo;)"],
      [P("Revenue growth (ad + subscription); higher ARPU; reduced churn; increased customer lifetime value "
         "(LTV); market-share gains; stronger unit economics in a low-ARPU market.", cell),
       P("Higher time spent listening per active user; DAU/MAU stickiness; more sessions/day and longer "
         "sessions; higher discovery&rarr;save&rarr;repeat rates; stronger D1/D7/D30 retention; free&rarr;"
         "premium conversion.", cell)]]
story.append(tbl(bo, [USABLE * 0.5, USABLE * 0.5]))
story.append(Spacer(1, 3))
story.append(P("<b>Guiding principle.</b> Product outcomes (e.g., listening time) are the instruments; "
               "business outcomes (e.g., LTV, retained revenue) are the goals. This BRD keeps the two "
               "explicitly linked via the KPI tree in &sect;10.", body))

# ---------------------------------------------------------------- 3 SCOPE
story.append(sec("3", "Project Scope"))
sc = [["In-Scope", "Out-of-Scope"],
      [P("&bull; Defining the engagement / listening-time problem for the <b>Indian</b> market.<br/>"
         "&bull; Both <b>free/ad-supported</b> and <b>premium</b> tiers.<br/>"
         "&bull; Mobile-first experience (the dominant access mode).<br/>"
         "&bull; User segmentation, personas, journeys &amp; Jobs-to-be-Done.<br/>"
         "&bull; Problem-focused functional &amp; non-functional requirements.<br/>"
         "&bull; Success criteria, KPI tree, assumptions &amp; constraints.", cell),
       P("&bull; Designing solutions, features, or UI (deferred to later PRD/design phases).<br/>"
         "&bull; Pricing/packaging changes and content-licensing negotiations.<br/>"
         "&bull; Markets outside India.<br/>"
         "&bull; Backend re-architecture or platform build decisions.<br/>"
         "&bull; Marketing-campaign creative or media planning.<br/>"
         "&bull; Vendor/tooling selection.", cell)]]
story.append(tbl(sc, [USABLE * 0.5, USABLE * 0.5]))
story.append(Spacer(1, 3))
story.append(P("<b>Scope rationale.</b> Per the brief, this milestone deliberately stops at problem "
               "definition. Constraining scope to &lsquo;what and why&rsquo; prevents premature solutioning "
               "and keeps design, engineering, and strategy anchored to the same problem statement.", body))

# ---------------------------------------------------------------- 4 BUSINESS DRIVERS
story.append(sec("4", "Business Drivers"))
story.append(P("The following forces make the engagement / listening-time problem urgent and strategically "
               "important now:", body))
bd = [["Driver", "Why it matters"],
      ["Market size &amp; growth", P("India offers one of the largest addressable streaming audiences "
         "globally, expanding with smartphone and data penetration &mdash; a strategic growth market for "
         "Spotify. <b>[M1: market size / growth figures]</b>", cell)],
      ["Low ARPU / monetization pressure", P("A predominantly free, ad-supported, price-sensitive base means "
         "revenue per user is low; engagement (listening time) is the primary way to grow both ad inventory "
         "and premium value (IFPI; FICCI&ndash;EY).", cell)],
      ["Retention economics", P("Acquisition is comparatively cheap but fragile; without habitual listening, "
         "users churn to free alternatives. Retained, engaged users are the compounding source of LTV.", cell)],
      ["Competitive intensity", P("JioSaavn, Wynk, YouTube Music, Apple/Amazon Music and free YouTube compete "
         "for the same attention and time. Time spent is effectively a share-of-ear battle. <b>[M1: "
         "competitor benchmarks]</b>", cell)],
      ["Ad + subscription revenue linkage", P("Ad revenue scales with time spent (impressions/fill); "
         "subscription value and conversion scale with perceived, habitual usefulness &mdash; both hinge on "
         "listening time.", cell)],
      ["Strategic importance of India", P("India is central to Spotify&rsquo;s long-term user-growth story; "
         "solving engagement here materially affects global scale narratives.", cell)]]
story.append(tbl(bd, [USABLE * 0.26, USABLE * 0.74]))

story.append(PageBreak())

# ---------------------------------------------------------------- 5 CURRENT PROCESS
story.append(sec("5", "Current Process &mdash; Engagement Patterns &amp; Listening Behaviors"))
story.append(P("This section describes the <i>current state</i> of how Indian users engage with Spotify "
               "(and streaming broadly), synthesised from Milestone&nbsp;1 and public sources. It is "
               "descriptive, not evaluative of solutions.", body))
story.append(P("5.1&nbsp;&nbsp;Observed engagement patterns", h2))
story.append(blist([
    "<b>Free-tier dominance &amp; price sensitivity</b> &mdash; a large majority of Indian listeners use "
    "free/ad-supported tiers; willingness to pay is constrained by disposable income and abundant free "
    "alternatives. <b>[M1: free vs premium split]</b>",
    "<b>Mobile-first, budget-device reality</b> &mdash; usage is overwhelmingly on Android smartphones "
    "spanning a wide range of price/performance, often on constrained data plans and variable connectivity.",
    "<b>Background &amp; context-driven listening</b> &mdash; commuting, working/studying, chores, workouts, "
    "sleep, and social/sharing moments; music is frequently a companion activity rather than the focus.",
    "<b>Regional-language centrality</b> &mdash; consumption skews to Hindi and regional-language repertoire; "
    "relevance of recommendations to a user&rsquo;s language(s) strongly shapes satisfaction.",
    "<b>Discovery friction</b> &mdash; when recommendations/editorial do not reflect local tastes, moods, or "
    "languages, users fall back to manual search, known songs, or competitors, shortening sessions.",
    "<b>Competition with free video/audio</b> &mdash; YouTube&rsquo;s free, ad-supported catalogue is a "
    "default music surface for many, setting a high bar for &lsquo;free enough, relevant enough&rsquo;.",
]))
story.append(P("5.2&nbsp;&nbsp;User segments (Indian market)", h2))
seg = [["Segment axis", "Sub-segments &amp; engagement implications"],
       ["Geography", P("Urban (higher connectivity, English + Hindi + regional, more premium propensity) vs "
          "Rural / Tier&nbsp;2&ndash;3 (data-cost sensitive, regional-language-first, offline needs).", cell)],
       ["Tier", P("Free/ad-supported (majority; interruption-tolerant, conversion-cautious) vs Premium "
          "(expect frictionless, high-relevance, offline).", cell)],
       ["Generation", P("Gen&nbsp;Z (short-form, social, trend- and mood-led) vs Millennials (playlist- and "
          "habit-led, nostalgia, podcasts).", cell)],
       ["Language", P("Hindi-first, Regional-language-first (e.g., Tamil, Telugu, Punjabi, Bengali, etc.), and "
          "English/global &mdash; each with distinct discovery expectations.", cell)],
       ["Usage context (JTBD)", P("Commute, focus/work, workout, devotional, party/social, sleep &mdash; each "
          "a &lsquo;job&rsquo; the user hires music for.", cell)]]
story.append(tbl(seg, [USABLE * 0.2, USABLE * 0.8]))

story.append(P("5.3&nbsp;&nbsp;Representative personas (illustrative; refine with M1 data)", h2))
per = [["Persona", "Profile", "Job-to-be-Done (JTBD)", "Key engagement pain points"],
       [P("<b>Aditya</b><br/>Gen&nbsp;Z, Urban, Free", cell),
        P("21, college, metro; budget Android; capped data; Hindi + English + trending.", cell),
        P("&ldquo;When I&rsquo;m commuting or hanging out, I want effortless, trend-right music so I can vibe "
          "without searching.&rdquo;", cell),
        P("Recos feel generic/global; free-tier friction; discovery effort; drifts to YouTube/Reels.", cell)],
       [P("<b>Meera</b><br/>Millennial, Tier-2, Free&rarr;?", cell),
        P("29, working professional, Tier-2 city; regional-language-first; data-cost aware.", cell),
        P("&ldquo;When I work or do chores, I want familiar regional music that just plays, using little "
          "data.&rdquo;", cell),
        P("Regional relevance gaps; data/offline concerns; unclear premium value; short sessions.", cell)],
       [P("<b>Rohan</b><br/>Millennial, Urban, Premium", cell),
        P("34, urban professional; multi-device; podcasts + curated playlists; time-poor.", cell),
        P("&ldquo;When I focus or unwind, I want reliable, high-relevance listening across my devices without "
          "fiddling.&rdquo;", cell),
        P("Relevance drift lowers stickiness; cross-context continuity; perceived value vs price.", cell)]]
story.append(tbl(per, [USABLE * 0.16, USABLE * 0.26, USABLE * 0.3, USABLE * 0.28]))

story.append(P("5.4&nbsp;&nbsp;User journey &amp; pain points (where listening time leaks)", h2))
jm = [["Journey stage", "What happens today", "Engagement pain / leak"],
      ["Acquisition &amp; onboarding", P("User installs, signs up (often free); minimal taste/ language "
         "capture.", cell), P("Weak early personalisation &rarr; low first-session relevance.", cell)],
      ["First-session discovery", P("User seeks something to play; relies on search or generic recos.", cell),
       P("Effort &amp; mismatch &rarr; short first session, weak habit seed.", cell)],
      ["Habitual listening", P("Returns for specific contexts (commute, work); expects effortless relevance.",
         cell), P("Relevance/continuity gaps &rarr; fewer, shorter sessions.", cell)],
      ["Free-tier experience", P("Encounters ads/limits; compares with free alternatives.", cell),
       P("Friction vs &lsquo;good-enough free&rsquo; elsewhere &rarr; substitution.", cell)],
      ["Retention / churn", P("Continues, lapses, or switches based on accumulated value.", cell),
       P("Low accumulated listening time &rarr; churn &amp; weak conversion.", cell)]]
story.append(tbl(jm, [USABLE * 0.22, USABLE * 0.4, USABLE * 0.38]))

story.append(PageBreak())

# ---------------------------------------------------------------- 6 PROPOSED PROCESS (framing)
story.append(sec("6", "Proposed Process &mdash; Framing the Engagement Problem"))
story.append(P("Per the brief, this section reframes the challenge as a problem to be solved &mdash; it does "
               "<b>not</b> prescribe features or solutions. The intent is to give teams a shared, testable "
               "framing.", body))
story.append(box([P("<b>Reframe.</b> The objective is not &lsquo;add features&rsquo; but to <i>increase "
                    "meaningful time spent listening</i> by reducing friction across four problem dimensions: "
                    "<b>(1) Relevance</b> (right content for language, mood, context), <b>(2) Access</b> "
                    "(data-, device-, and connectivity-friendly), <b>(3) Habit</b> (frequency and continuity "
                    "of listening), and <b>(4) Value</b> (worth of free and premium experiences).", callout)]))
story.append(P("6.1&nbsp;&nbsp;Problem statements by segment (to be validated)", h2))
story.append(blist([
    "<b>Free / Gen&nbsp;Z / Urban:</b> effort and generic relevance suppress session length and frequency, "
    "ceding time to free video/social alternatives.",
    "<b>Free / Regional / Tier-2&ndash;3:</b> regional-language relevance and data/connectivity concerns "
    "limit habitual, low-friction listening.",
    "<b>Premium / Urban:</b> relevance drift and cross-context continuity gaps weaken stickiness and the "
    "felt value that justifies paying.",
]))
story.append(P("6.2&nbsp;&nbsp;Assumptions &amp; hypotheses (framing, not conclusions)", h2))
hy = [["ID", "Hypothesis (to test)", "If true, we&rsquo;d expect&hellip;"],
      ["H1", P("Higher recommendation relevance to language/mood/context increases session length.", cell),
       P("&uarr; avg session minutes; &uarr; discovery&rarr;save&rarr;repeat.", cell)],
      ["H2", P("Lower access friction (data/offline/low-end performance) increases session frequency.", cell),
       P("&uarr; sessions/day; &uarr; D7/D30 retention in Tier-2&ndash;3.", cell)],
      ["H3", P("Stronger early-session personalisation seeds durable habit.", cell),
       P("&uarr; week-1 listening time; &uarr; D30 retention.", cell)],
      ["H4", P("Perceived value gaps (free and premium) cap conversion and listening time.", cell),
       P("&uarr; free&rarr;premium conversion when value is felt; &darr; churn.", cell)]]
story.append(tbl(hy, [USABLE * 0.08, USABLE * 0.52, USABLE * 0.4]))
story.append(Spacer(1, 2))
story.append(P("These hypotheses are the bridge to Milestone&nbsp;3 discovery/validation; they are stated "
               "here only to make the problem framing explicit and falsifiable.", small))

# ---------------------------------------------------------------- 7 FUNCTIONAL REQUIREMENTS
story.append(sec("7", "Functional Requirements (Problem-Focused)"))
story.append(P("Stated as <i>capability needs / problems the eventual solution must address</i> &mdash; not "
               "as features. Each is a requirement of the problem space.", body))
fr = [["ID", "Problem-focused functional requirement", "Relates to"],
      ["FR1", P("The experience must address users&rsquo; need to find content relevant to their "
         "<b>language(s), mood, and context</b> with minimal effort.", cell), "Relevance"],
      ["FR2", P("The experience must address the need to <b>sustain and resume</b> listening across "
         "contexts and devices (continuity).", cell), "Habit / Access"],
      ["FR3", P("The experience must address <b>data-, connectivity-, and device-efficiency</b> needs of "
         "cost-sensitive, budget-device users.", cell), "Access"],
      ["FR4", P("The experience must address the need for a <b>free-tier value proposition</b> competitive "
         "with &lsquo;good-enough free&rsquo; alternatives.", cell), "Value"],
      ["FR5", P("The experience must address the need for <b>relevant discovery at first session</b> to seed "
         "habit (early personalisation).", cell), "Habit / Relevance"],
      ["FR6", P("The business must be able to <b>measure engagement</b> (listening time, sessions, retention) "
         "reliably by segment to manage the problem.", cell), "Measurement"],
      ["FR7", P("The experience must address the need for content <b>breadth &amp; freshness</b> across "
         "regional languages and use-case contexts.", cell), "Relevance"]]
story.append(tbl(fr, [USABLE * 0.08, USABLE * 0.72, USABLE * 0.2]))

story.append(PageBreak())

# ---------------------------------------------------------------- 8 NON-FUNCTIONAL
story.append(sec("8", "Non-Functional Requirements"))
nfr = [["Category", "Requirement (problem constraint)"],
       ["Performance", P("Smooth playback, fast search/recommendation response, and low startup latency on "
          "<b>low-to-mid-range Android devices</b>.", cell)],
       ["Data efficiency", P("Efficient streaming and caching to respect <b>constrained/expensive data</b>; "
          "graceful behaviour on low bandwidth.", cell)],
       ["Reliability / availability", P("High availability and resilience under variable connectivity; "
          "consistent behaviour offline/online.", cell)],
       ["Localization", P("Multi-language UI and content metadata across Hindi and major regional languages; "
          "culturally relevant editorial.", cell)],
       ["Scalability", P("Handle very large, multi-source datasets and peak concurrency (festivals, releases, "
          "sale events) without degradation.", cell)],
       ["Accessibility &amp; inclusivity", P("Usable across literacy levels, device classes, and "
          "first-time-internet users.", cell)],
       ["Privacy &amp; compliance", P("Adhere to applicable Indian data-protection and content regulations; "
          "transparent data use.", cell)],
       ["Measurability", P("Instrumentation to capture engagement metrics accurately and consistently by "
          "segment for ongoing management.", cell)]]
story.append(tbl(nfr, [USABLE * 0.24, USABLE * 0.76]))

# ---------------------------------------------------------------- 9 ASSUMPTIONS & CONSTRAINTS
story.append(sec("9", "Assumptions &amp; Constraints"))
story.append(P("9.1&nbsp;&nbsp;Assumptions", h2))
story.append(blist([
    "Milestone&nbsp;1 findings on the Indian market, competitors, and user behaviour are valid inputs to this "
    "framing. <b>[M1]</b>",
    "The free/ad-supported tier will remain the primary entry point for most Indian users in the near term.",
    "Regional-language relevance and data/device affordability are material drivers of engagement.",
    "Time spent listening is an accepted leading indicator of retention and monetization for this business.",
    "Mobile (Android) remains the dominant access mode.",
]))
story.append(P("9.2&nbsp;&nbsp;Constraints", h2))
story.append(blist([
    "<b>Commercial:</b> low ARPU and price sensitivity limit monetization headroom.",
    "<b>Technical:</b> device, bandwidth, and connectivity variability across geographies.",
    "<b>Content/licensing:</b> catalogue depth/rights vary by language and label (out of scope to change here).",
    "<b>Competitive:</b> free alternatives (esp. YouTube) set a high &lsquo;good-enough&rsquo; baseline.",
    "<b>Regulatory:</b> evolving Indian data-protection and content norms.",
    "<b>Organisational:</b> cross-functional, matrixed delivery across time zones; this milestone is framing-only.",
]))

# ---------------------------------------------------------------- 10 SUCCESS CRITERIA & KPIs
story.append(sec("10", "Success Criteria &amp; KPIs (KPI Tree)"))
story.append(P("Success is framed around a <b>North Star</b> product metric that is causally linked to "
               "business outcomes. Targets are directional and must be baselined from Milestone&nbsp;1 "
               "<b>[M1]</b>.", body))
story.append(box([P("<b>North Star Metric:</b> <b>Time Spent Listening</b> &mdash; average meaningful "
                    "listening minutes per active user per day (by segment).", callout)]))
story.append(P("10.1&nbsp;&nbsp;KPI tree (listening time &rarr; retention &rarr; monetization)", h2))
kt = [["Level", "Metric", "Links to"],
      [P("<b>North Star</b>", cellb), P("Time spent listening / active user / day (by segment)", cell),
       "Retention &amp; monetization"],
      [P("Input drivers", cell), P("Sessions per user/day &bull; Avg session length &bull; "
         "Discovery&rarr;play&rarr;save&rarr;repeat rate &bull; Continuity (resume, cross-device, offline)",
         cell), "North Star"],
      [P("Engagement / retention", cell), P("DAU/MAU stickiness &bull; D1 / D7 / D30 retention &bull; "
         "active days/month &bull; churn rate", cell), "Product outcome"],
      [P("Monetization (Free)", cell), P("Ad-supported listening hours &bull; ad impressions / fill &bull; "
         "ad revenue per active user", cell), "Business outcome"],
      [P("Monetization (Premium)", cell), P("Free&rarr;premium conversion &bull; premium retention &bull; "
         "ARPU &bull; LTV", cell), "Business outcome"]]
story.append(tbl(kt, [USABLE * 0.2, USABLE * 0.55, USABLE * 0.25]))
story.append(Spacer(1, 3))
story.append(P("10.2&nbsp;&nbsp;Success criteria (directional; baseline &amp; target from M1)", h2))
sccrit = [["Success criterion", "Measured by", "Target"],
          ["Increased listening time", "North Star minutes/active user/day, by segment",
           P("&uarr; vs baseline <b>[M1]</b>", cell)],
          ["Improved stickiness", "DAU/MAU; sessions/day; session length", P("&uarr; vs baseline <b>[M1]</b>", cell)],
          ["Stronger retention", "D7 / D30 retention; churn", P("&uarr; retention; &darr; churn <b>[M1]</b>", cell)],
          ["Healthier monetization", "Ad hours/impressions; free&rarr;premium conversion; ARPU/LTV",
           P("&uarr; vs baseline <b>[M1]</b>", cell)],
          ["Segment equity", "Engagement gap across urban/rural, language, tier",
           P("Narrowing gaps <b>[M1]</b>", cell)]]
story.append(tbl(sccrit, [USABLE * 0.3, USABLE * 0.46, USABLE * 0.24]))

story.append(PageBreak())

# ---------------------------------------------------------------- 11 TIMELINE
story.append(sec("11", "Timeline &amp; Milestones"))
story.append(P("High-level phasing. This BRD is the deliverable for Milestone&nbsp;2; downstream phases are "
               "indicative and out of scope to detail here.", body))
tl = [["Milestone", "Focus", "Status"],
      ["M1 &mdash; Research", "Market, competitor &amp; user-behaviour analysis; engagement rationale",
       P("<b>Complete</b>", cell)],
      ["M2 &mdash; BRD (this)", "Problem definition, scope, business framing, KPIs, personas",
       P("<b>In review</b>", cell)],
      ["M3 &mdash; Discovery &amp; validation", "Test hypotheses (H1&ndash;H4); user research; opportunity sizing",
       "Upcoming"],
      ["M4 &mdash; PRD &amp; design", "Solution requirements &amp; design (solutions begin here)", "Upcoming"],
      ["M5 &mdash; Build &amp; measure", "Delivery, experimentation, KPI-tree instrumentation", "Upcoming"]]
story.append(tbl(tl, [USABLE * 0.26, USABLE * 0.54, USABLE * 0.2]))

# ---------------------------------------------------------------- 12 STAKEHOLDERS
story.append(sec("12", "Stakeholders"))
story.append(P("RACI is indicative for the problem-definition phase (R = Responsible, A = Accountable, "
               "C = Consulted, I = Informed).", body))
sh = [["Stakeholder", "Interest in the engagement problem", "RACI (M2)"],
      ["Product Management", "Owns problem framing, KPIs, prioritisation", "A / R"],
      ["Design / UX Research", "User needs, personas, journeys, JTBD", "C / R"],
      ["Engineering", "Feasibility, data efficiency, performance constraints", "C"],
      ["Data / Analytics (BI/DE)", "Metrics, KPI-tree instrumentation, baselines", "C / R"],
      ["Marketing / Growth", "Acquisition-to-engagement handoff, segments", "C"],
      ["Content &amp; Label Partnerships", "Regional-language catalogue &amp; relevance", "C"],
      ["Regional / Localization", "Language and cultural relevance", "C"],
      ["Strategy / Leadership", "Business outcomes, market strategy, funding", "A / I"],
      ["Customer Support / Ops", "Voice-of-customer, friction signals", "I"]]
story.append(tbl(sh, [USABLE * 0.28, USABLE * 0.56, USABLE * 0.16]))

# ---------------------------------------------------------------- 13 COST & BENEFIT
story.append(sec("13", "Cost &amp; Benefit (Optional, Qualitative)"))
cbt = [["Cost of inaction", "Benefit of solving the engagement problem"],
       [P("Continued low listening time &rarr; weak retention &rarr; churn to free alternatives; suppressed ad "
          "inventory and premium conversion; eroding share-of-ear; under-realised value from a strategic "
          "growth market.", cell),
        P("Compounding gains: more listening time &rarr; stronger retention &rarr; higher ad revenue and "
          "premium conversion &rarr; improved ARPU/LTV and a defensible position in India. Detailed financials "
          "to be modelled post-validation <b>[M1/M3]</b>.", cell)]]
story.append(tbl(cbt, [USABLE * 0.5, USABLE * 0.5]))

# ---------------------------------------------------------------- 14 GLOSSARY
story.append(sec("14", "Glossary"))
gl = [["Term", "Definition"],
      ["ARPU", "Average Revenue Per User &mdash; revenue divided by active users."],
      ["BRD", "Business Requirements Document &mdash; defines the business problem, scope and needs (not solutions)."],
      ["Churn", "Rate at which users stop using the service over a period."],
      ["DAU / MAU", "Daily / Monthly Active Users; DAU&divide;MAU is a common &lsquo;stickiness&rsquo; measure."],
      ["JTBD", "Jobs-to-be-Done &mdash; the underlying &lsquo;job&rsquo; a user &lsquo;hires&rsquo; the product to do."],
      ["KPI", "Key Performance Indicator."],
      ["KPI tree", "Hierarchy linking a North Star metric to its input drivers and business outcomes."],
      ["LTV", "Lifetime Value &mdash; total value a user generates over their relationship with the product."],
      ["North Star Metric", "The single product metric best capturing delivered value (here, time spent listening)."],
      ["Retention (D1/D7/D30)", "Share of users returning 1 / 7 / 30 days after a reference event."],
      ["Time spent listening", "Cumulative meaningful listening minutes per user over a period."]]
story.append(tbl(gl, [USABLE * 0.22, USABLE * 0.78]))

story.append(PageBreak())

# ---------------------------------------------------------------- 15 REFERENCES
story.append(sec("15", "References"))
story.append(P("Directional market context in this BRD draws on the public sources below and on the "
               "reader&rsquo;s Milestone&nbsp;1 research. <b>Specific data points should be cited to the exact "
               "report/edition and year used in Milestone&nbsp;1.</b>", small))
story.append(blist([
    "IFPI &mdash; <i>Global Music Report</i> (annual): recorded-music revenue, streaming and ad-supported "
    "shares, market rankings.",
    "FICCI&ndash;EY &mdash; <i>Indian Media &amp; Entertainment (M&amp;E) Report</i> (annual): India music/"
    "audio streaming trends, subscriptions, digital consumption.",
    "RedSeer / Redseer Strategy Consultants &mdash; India OTT audio / music-streaming market reports.",
    "Spotify Technology S.A. &mdash; investor materials, quarterly shareholder letters and annual reports "
    "(engagement, MAU/premium, ARPU context).",
    "Spotify Newsroom / press &mdash; India launch (February&nbsp;2019) and market announcements.",
    "Industry/press coverage of Indian streaming competition (JioSaavn, Wynk Music, YouTube Music, Apple "
    "Music, Amazon Music).",
    "<b>[M1]</b> Milestone&nbsp;1 primary/secondary research (the reader&rsquo;s own sources &mdash; insert "
    "citations).",
]))

# ---------------------------------------------------------------- 16 APPENDIX
story.append(sec("16", "Appendix"))
story.append(P("A. Data to validate / populate from Milestone&nbsp;1", h2))
story.append(blist([
    "Spotify India engagement / listening-time baselines by segment.",
    "Free vs premium split; urban/rural and language mix; device/data profiles.",
    "Competitor engagement benchmarks (share-of-ear, session metrics).",
    "Market size, growth, and ARPU figures with citations.",
]))
story.append(P("B. Framework mapping (how this BRD applies the required methods)", h2))
fm = [["Method", "Where applied in this BRD"],
      ["Business vs Product Outcomes", "&sect;2 (table) and &sect;10 (KPI tree links product&rarr;business)"],
      ["KPI Trees", "&sect;10.1 &mdash; listening time &rarr; retention &rarr; monetization"],
      ["Product Discovery", "&sect;6.2 hypotheses &amp; &sect;11 (M3 discovery/validation)"],
      ["Design Thinking", "&sect;5 empathy (personas/journeys) &amp; &sect;6 problem reframing"],
      ["Persona &amp; Journey Mapping", "&sect;5.3 personas; &sect;5.4 journey &amp; pain points"],
      ["Segmenting Users", "&sect;5.2 segment axes (geography/tier/generation/language/context)"],
      ["Jobs-to-be-Done", "&sect;5.2&ndash;5.3 (JTBD per persona)"],
      ["Assumptions &amp; Hypothesis Framing", "&sect;6.2 (H1&ndash;H4) and &sect;9.1"]]
story.append(tbl(fm, [USABLE * 0.34, USABLE * 0.66]))
story.append(Spacer(1, 6))
story.append(P("End of document &mdash; BRD v1.0 (Draft for Review). This document intentionally defines the "
               "problem space only; solutions and features are addressed in later milestones.", small))


# ---------------------------------------------------------------- PAGE FURNITURE
def furniture(canvas, doc):
    canvas.saveState()
    # header rule
    canvas.setStrokeColor(MID)
    canvas.setLineWidth(0.5)
    if doc.page > 1:
        canvas.line(M, PAGE_H - M + 14, PAGE_W - M, PAGE_H - M + 14)
        canvas.setFont("Helvetica", 7.5)
        canvas.setFillColor(GREY)
        canvas.drawString(M, PAGE_H - M + 18, "BRD — User Engagement & Listening Time — Spotify India")
        canvas.drawRightString(PAGE_W - M, PAGE_H - M + 18, "v1.0 — Draft for Review")
    # footer
    canvas.line(M, M - 12, PAGE_W - M, M - 12)
    canvas.setFont("Helvetica", 7.5)
    canvas.setFillColor(GREY)
    canvas.drawString(M, M - 22, "Problem framing only — no solutions proposed")
    canvas.drawRightString(PAGE_W - M, M - 22, "Page %d" % doc.page)
    canvas.restoreState()


doc = SimpleDocTemplate(OUT, pagesize=A4, leftMargin=M, rightMargin=M, topMargin=M, bottomMargin=M + 6,
                        title="BRD - Spotify India User Engagement & Listening Time",
                        author="Juhi Bhalla", subject="Business Requirements Document (Problem Definition)")
doc.build(story, onFirstPage=furniture, onLaterPages=furniture)
print("PDF written to", OUT)
