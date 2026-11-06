# Amazon Brazil → Amazon India: SQL Analysis

| File | What it is |
|---|---|
| `01_setup_schema.sql` | Creates `amazon_analysis` / `amazon_brazil`, all 6 tables with PKs & FKs, and import steps |
| `02_analysis_queries.sql` | All 19 queries (Analysis I, II, III) with context comments — **upload this to the portal** |
| `Amazon_Brazil_Analysis_Report.docx` | Word report: context, query + output screenshot, analysis and recommendation per question |
| `Amazon_Brazil_Analysis_Results.xlsx` | Every query output; III.3 line chart and III.4 pie chart (Excel-native) on the first two sheets |
| `screenshots/` | Query/output screenshots (`I.1.png` …) and report charts (`chart_*.png`) |

Run order in pgAdmin: create database `amazon_analysis` → run `01_setup_schema.sql` → import CSVs
(customers, seller, product, orders, order_items, payments) → run `02_analysis_queries.sql`.

Key assumptions: order-level sales = `payments.payment_value`; product/category revenue = `order_items.price`;
repeat-customer questions use `customer_unique_id`; the 'Smart' filter (I.3) uses `product_category_name`
because the product table has no name column.
