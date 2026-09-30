# Flipkart Customer Service & Retention: Final Report

**Data:** 30,000 customer-service contacts, 1–31 Oct 2020 · **Outcome proxy:** CSAT (1–10), because the data has no retention field.
**Deliverables:** [Excel EDA workbook](../excel/Flipkart_Customer_Service_EDA.xlsx) · [Interactive dashboard](../dashboard/index.html) ([live version](https://claude.ai/artifact/Hn2WEHrNWsaBbAJL8SAirU)) · [Presentation](https://claude.ai/artifact/QZa6nTmd9hiSA1Lc1rpYSE) · [Checkpoint 1](Checkpoint1_Metrics_and_Hypotheses.md)

## 1. Summary

1. **Sentiment is the only real driver of CSAT.** Very Negative contacts average **2.46**, Very Positive **9.49** (r = 0.90, R² = 0.80). Every other factor moves CSAT by **less than 0.2 points**.
2. **52% of contacts are negative or very negative**, and more rated customers are dissatisfied (34.8%) than satisfied (23.7%).
3. **Response time, call duration and call-centre location do not explain CSAT.** Two of the brief's three example hypotheses (H1, H3) are not supported.
4. **71% of contacts are billing questions.** Most of the demand comes from one product area.
5. **63% of contacts get no CSAT score.** This is true for every sentiment level, so the survey process itself misses most customers.

## 2. Data preparation (Checkpoint 2)

| Step | Rows | Treatment |
|---|---|---|
| Exact duplicates / duplicate IDs | 0 / 0 | none needed |
| `csat_score` blank | 18,786 (62.6%) | **left blank**: non-response is a metric; averages use the 11,214 rated contacts |
| `city`/`state` blank | 132 | "Unknown" |
| `customer_name` / `Gender` blank | 3 / 3 | "Unknown"; f/m → Female/Male; names Title Case |
| `call_timestamp` text | 30,000 | converted to a real date. 31 Oct has a single contact (partial day) |
| Derived columns | 11 | day, sentiment score 1–5, CSAT response flag, CSAT band, SLA-breach flag, response rank, duration band, satisfied flag, negative-sentiment flag, CSAT² (for t-tests) |

## 3. Descriptive statistics

| | CSAT (rated) | Call duration (min) |
|---|---|---|
| n | 11,214 | 30,000 |
| Mean | 5.54 | 25.0 |
| Median | 5 | 25 |
| Std dev | 2.37 | 11.8 |
| Min / Max | 1 / 10 | 5 / 45 |
| IQR | 4 – 7 | 15 – 35 |

| KPI | Value |
|---|---|
| CSAT response rate | 37.4% |
| % Satisfied (8–10) / % Dissatisfied (1–4) | 23.7% / 34.8% (net −11.2 pts) |
| Negative-sentiment share | 51.8% |
| SLA compliance / breach | 87.3% / 12.7% |
| Billing share of contacts | 71.4% |

## 4. Correlation analysis (Pearson r with CSAT, n = 11,214)

| Driver | r | p-value | Reading |
|---|---|---|---|
| Sentiment score (1–5) | **0.895** | < 0.001 | Strong driver |
| Call duration | −0.007 | 0.49 | No link |
| Response rank (Below→Above SLA) | 0.000 | 0.99 | No link |
| SLA-breach flag | 0.010 | 0.31 | No link |
| Day of week | 0.002 | 0.82 | No link |

Spread of average CSAT between the best and worst group: sentiment **7.04**, call centre 0.17, channel 0.15, duration band 0.15, reason 0.13, response time 0.08.

## 5. Hypothesis results

| ID | Hypothesis | Evidence | Verdict |
|---|---|---|---|
| H1 | Faster response raises CSAT | Above SLA 5.60 vs rest 5.53; t = 1.01, p = 0.31 | **Not supported** |
| H2 | Negative sentiment lowers CSAT | r = 0.90; Very Neg 2.46 → Very Pos 9.49 | **Supported (strong)** |
| H3 | Shorter calls raise CSAT | r = −0.007, p = 0.49; bands 5.47–5.61 | **Not supported** |
| H4 | CSAT/SLA differ by centre | CSAT 5.46 (Kolkata) – 5.63 (Chennai); SLA breach 12.3–12.9% | **Not supported** (differences too small to matter) |
| H5 | Chatbot scores lower | 5.46 vs 5.57; t = −2.21, p = 0.03 | **Supported, small effect** (0.11 pts) |
| H6 | Unhappy customers skip the survey | Response rate 38.1% (Very Neg) vs 35.8% (Very Pos) | **Not supported** (non-response is spread evenly) |

With over 11,000 rated contacts, very small differences can pass a significance test, so effect size is reported next to every p-value.

**Two notes.** Daily volume is flat at ~1,000 contacts a day. The Thu/Fri/Sat bump in raw day-of-week totals comes from October 2020 having five of each of those days. The call centre × channel heatmap shows some variation (e.g. Kolkata–Email 5.17, Chennai–Call-Center 5.83), but these cells hold a few hundred rated contacts each and fall within the overall noise.

## 6. How service affects retention

This data has no retention field, so the link from CSAT to retention is an assumption. Within it:

- The **experience** of the contact (sentiment) decides satisfaction, and satisfaction is where retention comes from. Half of all contacts end negative, a large and fixable churn risk.
- **Operational speed metrics are healthy and not the constraint.** 87% of contacts meet SLA, and missing SLA does not lower CSAT here.
- **Demand is concentrated.** Billing drives 7 in 10 contacts, so product fixes in billing would remove friction before it reaches customer service.

## 7. Recommendations

| Priority | Recommendation | Why (evidence) | KPI to move |
|---|---|---|---|
| 1 | **De-escalation & empathy training**; supervisor call-back for very-negative contacts; measure sentiment at the start and end of each contact | Sentiment explains 80% of CSAT variance; 52% of contacts are negative | Negative-sentiment share 51.8% → < 45%; Avg CSAT 5.54 → ≥ 6.0 |
| 2 | **Fix billing at the source**: clearer invoices, in-app payment/refund status, self-serve billing FAQ | 71% of contacts are billing questions | Billing share 71% → < 60% |
| 3 | **Close the feedback gap**: one-tap in-app survey sent right after the contact | Only 37% of contacts are rated | Response rate 37% → 60% |
| 4 | **Tune the chatbot hand-off**: send negative-sentiment chats to a human agent sooner | Chatbot is 0.11 pts lower (p = 0.03) | Chatbot CSAT gap → 0 |
| 5 | **Keep SLA and AHT as hygiene metrics.** Don't cut call time at the cost of solving the problem | No link between SLA/duration and CSAT | SLA compliance ≥ 87% |
| 6 | **Measure retention directly**: link contact IDs to each customer's orders over the next 90 days | CSAT is only a proxy | 90-day repeat-purchase rate |

Targets are proposed goals for management to agree. They are not forecasts from the data.

## 8. Limitations

- One month of data, no retention outcome, and CSAT is missing for 63% of contacts.
- Sentiment and CSAT are both recorded after the contact, so their strong link is partly two measures of the same experience. Sentiment is where to act, but training impact should be tested (e.g. an A/B test by agent group).
- Response time is recorded only as an SLA band, not in minutes.
