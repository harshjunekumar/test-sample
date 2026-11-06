# UK Savoury Snacks – analysis guide

## Files
| File | What it is |
|---|---|
| `PepsiCo_Savoury_Case_Study_Deck.pptx` | 10 slides + appendix, real numbers, speaker notes give source tab + talk track |
| `Savoury_Snacks_Analysis_Workbook.xlsx` | All analysis, formula-driven (SUMIFS on the `Data` tab). Orange "INSIGHT" rows = the takeaway |
| `prepare_data.py` | How 1.01m sales rows were summarised into the `Data` tab (same as an Excel PivotTable) |
| `Case_Study_Commercial_Insights.xlsx` | Source data converted from .xlsb (local only, not in git) |

## Method (how to explain it)
1. **Frame:** Sales = Shoppers × Penetration × AWOP. Every action moves one of these levers.
2. **Clean & align:** 2025 only has weeks 1–47, so compare 2025 wk1–47 (TY) vs 2024 wk1–47 (YA).
   Online = E-COMMERCE + PURE PLAY (Acadia); In-store = Large + Small format.
3. **Summarise:** pivot 1.01m rows to 8.5k (Period × Customer × Format × Supplier × Brand × Segment × Sub-segment × Pack).
4. **Analyse:** growth and contribution, PepsiCo share, Fair Share Index by sub-segment × pack,
   online vs in-store gaps, Acadia vs other online retailers, shopper/basket data, cross-buying.
5. **Size & prioritise:** £ headroom to a benchmark share; score = impact 50% + ease 30% + fit 20%.

## Key findings (all in the workbook)
| # | Finding | Tab |
|---|---|---|
| 1 | Market £1.08bn, +1.2%. PepsiCo £398m, −1.2%, share 36.9% (−0.9pts) | 1_Market |
| 2 | Online +5.8% delivers ~81% of category growth; in-store +0.3% | 1_Market |
| 3 | Potato Crisps −£12.9m; ~£20m growth from Crackers, Bread snacks, Nuts, F&V crisps where PepsiCo <10% share | 2_SubSegment |
| 4 | SHARING = 38% of market, +2.5% (+10.5% online); PepsiCo share 26% and falling | 4_PackFormat |
| 5 | Potato Crisps × Sharing = £163m cell, PepsiCo 20% vs 46% in crisps → £42.9m headroom | 5_Whitespace |
| 6 | Multipacks over-trade online (index 144–228), PepsiCo strong there (47–73%) → AWOP lever | 4_PackFormat |
| 7 | Online PepsiCo trails its in-store share in Tortilla sharing and Nuts → £2.5m | 6_Online_Gaps |
| 8 | Acadia +15.5% (fastest), PepsiCo 24.8% vs 38.6% at other online retailers → £4.2m | 7_Acadia |
| 9 | Acadia shoppers over-index on Nuts (173), Rice cakes (237), F&V crisps (464) | 7_Acadia |
| 10 | Online baskets: 62% > £60; nuts & snacks in 49% of online baskets vs 23% offline; £4.20 vs £2.80 spend | 8_Shopper_Basket |
| 11 | Online shoppers skew to families with kids (index 127) and main shop (79% vs 43%) | 8_Shopper_Basket |
| 12 | 80% of nuts buyers also buy PC sharing; strong PepsiCo-to-PepsiCo cross-buy (51–55%) | 9_CrossBuy |

## Before presenting
- Put your name/date on slide 1.
- Re-check 3–4 numbers yourself in the workbook (e.g. 1_Market total row, 5_Whitespace block F, 7_Acadia KPIs).
- Be ready for: *Why 47 weeks?* · *Why is £ "headroom" not forecast?* · *How do you know penetration without panel data?*
  (CSN basket penetration + share as proxy; recommend panel validation) · *Why sharing before crackers?* (PepsiCo already has brands; quicker, lower risk).
