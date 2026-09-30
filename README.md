# Flipkart Customer Service & Retention Analysis

Analysis of 30,000 Flipkart customer-service contacts (Oct 2020): how customer-service factors affect CSAT and, through it, retention.

**Headline:** customer sentiment is the only strong driver of CSAT (r = 0.90; 2.5 → 9.5 from Very Negative to Very Positive). Response time, call duration, call-centre location and channel each move CSAT by less than 0.2 points. 52% of contacts are negative, 71% are billing questions, and 63% get no CSAT score.

## Deliverables

| Checkpoint | Deliverable | Location |
|---|---|---|
| 1 | Metric tree | [`docs/metric_tree.png`](docs/metric_tree.png) (+ Mermaid version in the doc) |
| 1 | Documented metrics & hypotheses | [`docs/Checkpoint1_Metrics_and_Hypotheses.md`](docs/Checkpoint1_Metrics_and_Hypotheses.md), `Metrics_Hypotheses` sheet |
| 2 | EDA in Excel: cleaning, descriptive stats, correlation, pivots, charts, hypothesis tests | [`excel/Flipkart_Customer_Service_EDA.xlsx`](excel/Flipkart_Customer_Service_EDA.xlsx) |
| 3 | Interactive dashboard (Excel) | `Dashboard` sheet: pick call centre / channel / reason in the yellow cells |
| 3 | Interactive dashboard (web) | [`dashboard/index.html`](dashboard/index.html), open in any browser (works offline) · [live link](https://claude.ai/artifact/Hn2WEHrNWsaBbAJL8SAirU) |
| 3 | Final presentation | [Slides deck](https://claude.ai/artifact/QZa6nTmd9hiSA1Lc1rpYSE) (download as PPTX/PDF from the deck) · sources in `presentation/deck_source/` |
| 3 | Final report with findings & recommendations | [`docs/Final_Report.md`](docs/Final_Report.md) |

## Workbook tour

`README` → `Dashboard` → `Metrics_Hypotheses` → `Hypothesis_Tests` → `Descriptive_Stats` → `Correlation` → `Pivots` → `Charts` → `Cleaning_Log` → `Clean_Data` → `Raw_Data`

All 738 summary cells are live Excel formulas (`COUNTIFS`, `AVERAGEIFS`, `CORREL`, `TDIST`…) on `Clean_Data`, so the workbook recalculates if the data changes. The significance level for the hypothesis tests is an input cell (`Hypothesis_Tests!B3`).

## Reproduce

```bash
pip install pandas openpyxl matplotlib
python scripts/build_metric_tree.py     # docs/metric_tree.png
python scripts/build_workbook.py        # data/…_clean.csv + excel workbook
python scripts/build_dashboard.py       # dashboard/index.html (from dashboard/template.html)
python scripts/build_deck_slides.py     # presentation/deck_source/
```

The committed workbook is already recalculated. A freshly built one has no cached values until you open it in Excel (or recalculate it with LibreOffice).

## Data

- `data/flipkart_customer_calls_raw.csv`: the provided dataset, unchanged
- `data/flipkart_customer_calls_clean.csv`: cleaned data with derived columns
