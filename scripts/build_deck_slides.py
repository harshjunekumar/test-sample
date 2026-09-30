"""Generate the final-presentation slide files (Slides deck format)."""
import json, datetime
from pathlib import Path

# Slide sources for the published Slides deck (one HTML section per slide).
ROOT = Path(__file__).resolve().parents[1] / "presentation" / "deck_source"
(ROOT / "project" / "slides").mkdir(parents=True, exist_ok=True)

BG1, BG2, DARK, INK2, ACC, WARN, LINE = "#F7F8FA", "#ECF0F6", "#14213D", "#4A5568", "#2A6FDB", "#B8430F", "#D5DCE6"
NEU = "#9AA3B2"
SERIF = "'Source Serif 4', Georgia, serif"
SANS = "'IBM Plex Sans', Arial, sans-serif"
TREE = "/_blob/eeee8ac17268ac37a29b32a0b38b8566"
DASH = "https://claude.ai/artifact/Hn2WEHrNWsaBbAJL8SAirU"

slides = []


def sec(sid, body, notes, bg=BG1, color=DARK, extra="", num=True):
    n = len(slides) + 1
    foot = (f'<p style="position:absolute;left:128px;bottom:64px;width:1664px;font-size:24px;color:#5F6B7D">'
            f'Flipkart customer-service analysis · Oct 2020 data · {n}</p>') if num else ""
    html = (f'<section id="{sid}" data-transition="fade" style="background:{bg};color:{color};font-family:{SANS};'
            f'padding:128px 128px 160px;display:flex;flex-direction:column;gap:48px{extra}">\n{body}\n{foot}\n<aside>{notes}</aside>\n</section>\n')
    slides.append((sid, html))


def head(eyebrow, title, color=DARK, eb=ACC):
    return (f'<div style="display:flex;flex-direction:column;gap:16px">'
            f'<p style="font-size:24px;letter-spacing:3px;text-transform:uppercase;color:{eb};font-weight:600">{eyebrow}</p>'
            f'<h2 style="font-family:{SERIF};font-size:64px;font-weight:600;line-height:1.1;color:{color}">{title}</h2></div>')


def bars(rows, vmax, fmt, track=1100, label_w=340):
    out = '<div style="display:flex;flex-direction:column;gap:20px">'
    for label, v, col in rows:
        w = max(4, round(v / vmax * track))
        out += (f'<div style="display:flex;flex-direction:row;align-items:center;gap:24px">'
                f'<p style="width:{label_w}px;font-size:28px;color:{INK2}">{label}</p>'
                f'<div style="width:{w}px;height:44px;background:{col};border-radius:0px 6px 6px 0px"></div>'
                f'<p style="font-size:28px;font-weight:600;font-variant-numeric:tabular-nums">{fmt(v)}</p></div>')
    return out + "</div>"


def table(header, rows, widths, size=26):
    t = f'<table style="font-size:{size}px;color:{DARK};width:1664px">'
    t += "<tr>" + "".join(f'<th style="width:{w}%;text-align:left">{h}</th>' for h, w in zip(header, widths)) + "</tr>"
    for i, r in enumerate(rows):
        bg = ' style="background:#FFFFFF"' if i % 2 == 0 else ""
        t += f"<tr{bg}>" + "".join(f"<td>{c}</td>" for c in r) + "</tr>"
    return t + "</table>"


# 1 cover
sec("cover", f'''<div style="flex:1"></div>
<p style="font-size:28px;letter-spacing:4px;text-transform:uppercase;color:#9CC0F5;font-weight:600">Customer service &amp; retention analysis</p>
<h1 style="font-family:{SERIF};font-size:112px;font-weight:600;line-height:1.05;color:#F4F6FA">What really moves<br>Flipkart's CSAT?</h1>
<p style="font-size:36px;color:#C9D3E3;line-height:1.4;width:1300px">Findings and recommendations from 30,000 customer-service contacts, 1–31 October 2020</p>
<div style="flex:1"></div>
<p style="font-size:24px;color:#9FB0C8">Checkpoints 1–3 · Metrics &amp; hypotheses · EDA · Dashboard &amp; recommendations</p>''',
    "Flipkart has seen customer retention fall. This deck looks at customer-service data to see whether service performance explains it and where to act.",
    bg=DARK, color="#F4F6FA", num=False)

# 2 context
cards = [
    ("The problem", "Customer retention is falling. Customer service is one of the few places Flipkart talks directly to customers, so it is a likely cause and an easy place to act."),
    ("The data", "30,000 contacts · 13 columns: sentiment, CSAT (1–10), reason, channel, response time vs SLA, call duration, call centre, city/state. No retention or repeat-order field."),
    ("The approach", "Use CSAT as the stand-in for retention. Build a metric tree, test 6 hypotheses in Excel (stats, correlation, pivots), then build an interactive dashboard."),
]
c = '<div style="display:flex;flex-direction:row;gap:32px">'
for i, (t, b) in enumerate(cards):
    c += (f'<div style="flex:1;display:flex;flex-direction:column;gap:20px;background:#FFFFFF;padding:48px;border:1px solid {LINE};border-radius:16px">'
          f'<p style="font-size:24px;color:{ACC};font-weight:600">0{i+1}</p>'
          f'<h3 style="font-family:{SERIF};font-size:44px;font-weight:600">{t}</h3>'
          f'<p style="font-size:28px;line-height:1.45;color:{INK2}">{b}</p></div>')
c += "</div>"
sec("context", head("Business context", "Can customer service explain the drop in retention?") + c,
    "Retention is not in the dataset, so every conclusion links service to CSAT, and CSAT to retention by assumption. We will come back to this in the recommendations.")

# 3 metric tree
sec("tree", head("Checkpoint 1 · Metric tree", "From retention down to the columns we can measure") +
    f'<img src="{TREE}" alt="Metric tree: Customer Retention splits into Customer Satisfaction (avg CSAT, % satisfied, % dissatisfied) and Feedback Coverage (CSAT response rate). Satisfaction is driven by Interaction Quality (sentiment), Speed of Service (SLA), Efficiency (call duration) and Contact Demand (reason, channel, date). Every metric is cut by call centre, city, state and gender. Hypotheses H1-H6 are tagged on the branches." style="width:1664px;height:580px;object-fit:contain;background:#FFFFFF;border-radius:16px">',
    "L1 outcomes: average CSAT, % satisfied, % dissatisfied, CSAT response rate. L2 drivers: sentiment, SLA, handle time, contact demand. Location is a cut applied to every metric.", bg=BG2, extra=";gap:32px")

# 4 hypotheses
hyp_rows = [
    ("H1", "Faster response (fewer Above-SLA contacts) raises CSAT", "response_time, csat_score", "Welch t-test"),
    ("H2", "Better handling of negative sentiment raises CSAT", "sentiment, csat_score", "Pearson r"),
    ("H3", "Shorter calls raise CSAT", "call duration, csat_score", "Pearson r"),
    ("H4", "CSAT and SLA differ by call-centre location", "call_center, csat_score", "Group spread"),
    ("H5", "Chatbot gives lower CSAT than other channels", "channel, csat_score", "Welch t-test"),
    ("H6", "Unhappy customers skip the CSAT survey", "sentiment, csat_score", "Response-rate gap"),
]
sec("hyp", head("Checkpoint 1 · Hypotheses", "Six hypotheses, each tied to data columns and a test") +
    table(["ID", "Hypothesis", "Columns used", "Test"], hyp_rows, [7, 50, 26, 17], size=28),
    "H1 to H3 are the three example hypotheses from the brief. H4 to H6 add location, channel and survey coverage.")

# 5 data prep
prep = [
    ("Duplicates (all columns / call id)", "0 / 0", "No action needed"),
    ("CSAT score blank", "18,786 (62.6%)", "Kept blank: non-response is a metric, not imputed"),
    ("City / state blank", "132", "Set to 'Unknown'"),
    ("Customer name / gender blank", "3 / 3", "Set to 'Unknown'; f/m → Female/Male"),
    ("call_timestamp (text)", "30,000", "Converted to a real date; 31 Oct has only 1 contact"),
    ("Derived columns", "11 added", "Day, sentiment score 1–5, CSAT band, SLA-breach flag, duration band…"),
]
sec("prep", head("Checkpoint 2 · Data preparation", "Clean data, one deliberate choice: blank CSAT stays blank") +
    table(["Step", "Rows affected", "Treatment"], prep, [34, 20, 46], size=28),
    "Filling the 62.6% blank CSAT scores with a mean would invent data and hide the survey-coverage problem, so averages use rated contacts only (n = 11,214).", bg=BG2)

# 6 KPIs
kpis = [("5.54", "Average CSAT (1–10)", DARK), ("23.7%", "Satisfied (8–10)", DARK), ("34.8%", "Dissatisfied (1–4)", WARN),
        ("37.4%", "Contacts with a CSAT score", WARN), ("51.8%", "Negative or very negative sentiment", WARN), ("87.3%", "Within or below SLA", DARK)]
g = '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:32px">'
for v, l, col in kpis:
    g += (f'<div style="display:flex;flex-direction:column;gap:8px;background:#FFFFFF;padding:40px 48px;border:1px solid {LINE};border-radius:16px">'
          f'<p style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1.1;color:{col}">{v}</p>'
          f'<p style="font-size:28px;color:{INK2}">{l}</p></div>')
g += "</div>"
sec("kpi", head("Checkpoint 2 · Descriptive statistics", "Satisfaction is mediocre, and most customers are never asked") + g +
    f'<p style="font-size:24px;color:{INK2}">CSAT: mean 5.54 · median 5 · std dev 2.37 (n = 11,214 rated). Call duration: mean 25.0 min · median 25 · std dev 11.8. Orange = needs attention.</p>',
    "More customers are dissatisfied than satisfied: net satisfaction is -11 points. Fewer than 4 in 10 contacts get a CSAT score, so most of the customer voice is missing.")

# 7 statement
drv = [("Sentiment", 7.04, "#9CC0F5"), ("Call centre", 0.17, "#6B7A93"), ("Channel", 0.15, "#6B7A93"),
       ("Call duration", 0.15, "#6B7A93"), ("Contact reason", 0.13, "#6B7A93"), ("Response time (SLA)", 0.08, "#6B7A93")]
b = '<div style="display:flex;flex-direction:column;gap:18px">'
for l, v, col in drv:
    w = max(6, round(v / 7.04 * 1000))
    b += (f'<div style="display:flex;flex-direction:row;align-items:center;gap:24px">'
          f'<p style="width:380px;font-size:28px;color:#C9D3E3">{l}</p>'
          f'<div style="width:{w}px;height:40px;background:{col};border-radius:0px 6px 6px 0px"></div>'
          f'<p style="font-size:28px;font-weight:600;color:#F4F6FA">{v:.2f} pts</p></div>')
b += "</div>"
sec("lever", f'''<div style="display:flex;flex-direction:column;gap:16px">
<p style="font-size:24px;letter-spacing:3px;text-transform:uppercase;color:#9CC0F5;font-weight:600">The key finding</p>
<h2 style="font-family:{SERIF};font-size:72px;font-weight:600;line-height:1.1;color:#F4F6FA;width:1600px">Sentiment moves CSAT by 7 points. Nothing else moves it by more than 0.2.</h2></div>
<p style="font-size:28px;color:#C9D3E3">Gap between the best and worst group's average CSAT, for each factor</p>
{b}''',
    "This is the headline. How the customer feels during the contact decides the score. Speed, call length, location and channel barely matter in this data.",
    bg=DARK, color="#F4F6FA")

# 8 sentiment
sent = [("Very Negative", 2.46, WARN), ("Negative", 4.52, "#E39A7A"), ("Neutral", 6.47, NEU), ("Positive", 8.00, "#7FA9EC"), ("Very Positive", 9.49, "#1F57B3")]
sec("sent", head("H2 · Supported", "Every step up in sentiment adds about 1.75 CSAT points") +
    '<div style="display:flex;flex-direction:row;gap:64px;align-items:center">' +
    '<div style="flex:1;display:flex;flex-direction:column;gap:24px"><p style="font-size:28px;color:#4A5568">Average CSAT by customer sentiment (1–10)</p>' + bars(sent, 10, lambda v: f"{v:.2f}", track=640, label_w=260) + '</div>' +
    f'<div style="width:520px;display:flex;flex-direction:column;gap:24px;background:#FFFFFF;padding:48px;border:1px solid {LINE};border-radius:16px">'
    f'<p style="font-family:{SERIF};font-size:96px;font-weight:600;line-height:1.1">r = 0.90</p>'
    f'<p style="font-size:28px;line-height:1.45;color:{INK2}">Sentiment explains <b>80%</b> of CSAT variance (R² = 0.80, p &lt; 0.001).<br><br><b>52%</b> of contacts are negative or very negative. Those contacts average 3.8.</p></div></div>',
    "Very negative contacts score between 1 and 4, very positive ones 9 or 10. Moving a contact from negative to neutral is worth about 2 CSAT points.", bg=BG2)

# 9 what didn't matter
nm = [
    ("Response time (H1)", "Above SLA 5.60 · Within/Below 5.53", "0.07", "0.31", "No"),
    ("Call duration (H3)", "r = −0.007 · bands 5.47 to 5.61", "0.15", "0.49", "No"),
    ("Call centre (H4)", "Chennai 5.63 · Kolkata 5.46", "0.17", "–", "No (tiny)"),
    ("Channel (H5)", "Chatbot 5.46 · other channels 5.57", "0.11", "0.03", "Yes, but small"),
    ("Contact reason", "Payments 5.63 · Service Outage 5.51", "0.13", "–", "No (tiny)"),
]
sec("nomatter", head("H1 · H3 · H4 · H5", "Speed, call length and location barely change CSAT") +
    table(["Factor", "Evidence", "Gap (pts)", "p-value", "Real effect?"], nm, [24, 40, 12, 10, 14], size=28) +
    f'<p style="font-size:28px;color:{INK2};line-height:1.45;width:1500px">SLA breach is 12.3–12.9% at every centre and 12.4–13.4% on every channel. The weak spots are spread across the whole company, not one site.</p>',
    "With 11,000 rated contacts even a 0.11-point gap can pass a significance test (Chatbot, p = 0.03). On a 10-point scale it makes no practical difference. SLA is still worth holding as a hygiene metric.")

# 10 verdicts
ver = [
    ("H1", "Faster response raises CSAT", "Not supported", "t = 1.01, p = 0.31"),
    ("H2", "Negative sentiment lowers CSAT", "Supported", "r = 0.90, p < 0.001"),
    ("H3", "Shorter calls raise CSAT", "Not supported", "r = −0.007, p = 0.49"),
    ("H4", "Call centres differ", "Not supported", "0.17-pt spread"),
    ("H5", "Chatbot scores lower", "Supported (small)", "−0.11 pts, p = 0.03"),
    ("H6", "Unhappy customers skip survey", "Not supported", "38.1% vs 35.8% response"),
]
sec("verdicts", head("Checkpoint 2 · Results", "Hypothesis scorecard") +
    table(["ID", "Hypothesis", "Verdict", "Evidence"], ver, [8, 42, 22, 28], size=30),
    "Only sentiment is a strong driver. The brief's example hypotheses about response time and call duration are not supported by this data.", bg=BG2)

# 11 demand & feedback
two = '<div style="display:flex;flex-direction:row;gap:32px">'
for big, t, body in [
    ("71%", "of contacts are billing questions", "21,410 of 30,000 contacts. Payments and service outages are 14% each. Every billing contact the product prevents is a frustrated customer who never needs to call."),
    ("63%", "of contacts never get a CSAT score", "Response rate is 36–38% for every sentiment, so the gap is not caused by angry customers staying quiet (H6). The survey process itself misses most customers."),
]:
    two += (f'<div style="flex:1;display:flex;flex-direction:column;gap:16px;background:#FFFFFF;padding:56px;border:1px solid {LINE};border-radius:16px">'
            f'<p style="font-family:{SERIF};font-size:120px;font-weight:600;line-height:1.05;color:{WARN}">{big}</p>'
            f'<h3 style="font-family:{SERIF};font-size:44px;font-weight:600;line-height:1.2">{t}</h3>'
            f'<p style="font-size:28px;line-height:1.45;color:{INK2}">{body}</p></div>')
two += "</div>"
sec("demand", head("Beyond the hypotheses", "Two more problems: why people contact us, and how little we hear back") + two,
    "Daily volume is flat at about 1,000 contacts a day. The Thursday/Friday bump in raw counts comes from October 2020 having five Thursdays and five Fridays.")

# 12 recommendations
recs = [
    ("Train for de-escalation", "Empathy and recovery coaching; call-back for very-negative contacts."),
    ("Fix billing at the source", "Clearer invoices and in-app payment and refund status."),
    ("Close the feedback gap", "One-tap in-app survey right after the contact; aim for 60% response."),
    ("Tune the chatbot hand-off", "Send negative-sentiment chats to a human agent sooner."),
    ("Keep SLA and AHT as hygiene", "Hold 87% SLA; never cut call time at the cost of a fix."),
    ("Measure retention directly", "Link contact IDs to each customer's next-90-day orders."),
]
gr = '<div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:28px">'
for i, (t, body) in enumerate(recs):
    top = ACC if i < 3 else NEU
    gr += (f'<div style="display:flex;flex-direction:column;gap:12px;background:#FFFFFF;padding:36px 40px;border:1px solid {LINE};border-top:6px solid {top};border-radius:12px">'
           f'<h3 style="font-family:{SERIF};font-size:34px;font-weight:600;line-height:1.2">{t}</h3>'
           f'<p style="font-size:26px;line-height:1.4;color:{INK2}">{body}</p></div>')
gr += "</div>"
sec("recs", head("Checkpoint 3 · Recommendations", "Act on the conversation, not the clock") + gr +
    f'<p style="font-size:24px;color:{INK2}">Blue top edge = top priority (biggest impact on CSAT). Grey = supporting.</p>',
    "Priority order: 1 de-escalation training, 2 billing fixes, 3 survey coverage. The response-rate target of 60% is a proposed goal, not a figure from the data.",
    extra=";gap:36px")

# 13 scorecard to track
track = [
    ("Negative-sentiment share", "51.8%", "Below 45%", "Weekly, by centre and agent"),
    ("Average CSAT", "5.54", "6.0 or higher", "Weekly"),
    ("% Dissatisfied (1–4)", "34.8%", "Below 30%", "Weekly"),
    ("CSAT response rate", "37.4%", "60%", "Monthly"),
    ("Billing share of contacts", "71.4%", "Below 60%", "Monthly"),
    ("SLA compliance (guardrail)", "87.3%", "Hold at 87% or higher", "Daily"),
]
sec("track", head("How we'll know it worked", "A scorecard to track in the dashboard") +
    table(["Metric", "Oct 2020 baseline", "Proposed target", "Review"], track, [34, 20, 22, 24], size=28) +
    f'<p style="font-size:24px;color:{INK2}">Baselines come from the dataset. Targets are proposals for management to agree, not forecasts.</p>',
    "Once contact IDs are linked to repeat orders, add 90-day repeat-purchase rate as the true outcome metric at the top of the tree.", bg=BG2)

# 14 close
sec("close", f'''<div style="flex:1"></div>
<h2 style="font-family:{SERIF};font-size:80px;font-weight:600;line-height:1.1;color:#F4F6FA;width:1500px">Retention is won in how a contact feels, not how fast it ends.</h2>
<div style="display:flex;flex-direction:column;gap:14px">
<p style="font-size:30px;color:#C9D3E3">Interactive dashboard: <a href="{DASH}" style="color:#9CC0F5">open the live dashboard</a></p>
<p style="font-size:30px;color:#C9D3E3">Excel workbook: stats, correlation, pivots, charts, hypothesis tests, Excel dashboard</p>
<p style="font-size:30px;color:#C9D3E3">Metric tree, hypotheses and final report in the project repository</p></div>
<div style="flex:1"></div>''',
    "Thank you. Questions.", bg=DARK, color="#F4F6FA", num=False)

order = [s for s, _ in slides]
for sid, html in slides:
    (ROOT / "project" / "slides" / f"{sid}.html").write_text(html)
deck = {
    "v": 4, "createdOnFiles": {"v": 1, "at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")},
    "lists": "css", "title": "Flipkart Service & Retention Findings", "order": order,
    "sections": {
        "s1": {"description": "Context, metric tree and hypotheses (Checkpoint 1)", "start": "cover"},
        "s2": {"description": "Data preparation, statistics and hypothesis results (Checkpoint 2)", "start": "prep"},
        "s3": {"description": "Recommendations and tracking (Checkpoint 3)", "start": "recs"},
    },
    "faces": {
        "source-serif-4": {"family": "Source Serif 4", "href": "https://fonts.googleapis.com/css2?family=Source+Serif+4:wght@400..700&display=swap"},
        "ibm-plex-sans": {"family": "IBM Plex Sans", "href": "https://fonts.googleapis.com/css2?family=IBM+Plex+Sans:wght@400;500;600&display=swap"},
    },
    "designSystems": [],
}
(ROOT / "project" / "deck.json").write_text(json.dumps(deck, indent=1))
print(order)
