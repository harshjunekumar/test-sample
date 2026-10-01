-- E-commerce Sales Performance — business questions answered in SQL (SQLite dialect)
-- Each query is labelled with "-- name:" so analysis.py can run and export it.

-- name: kpi_summary
-- Q1. What are the headline KPIs for each year?
SELECT strftime('%Y', order_date)                         AS year,
       COUNT(DISTINCT order_id)                           AS orders,
       COUNT(DISTINCT customer_id)                        AS active_customers,
       ROUND(SUM(revenue), 0)                             AS revenue,
       ROUND(SUM(revenue) / COUNT(DISTINCT order_id), 2)  AS avg_order_value,
       ROUND(100.0 * SUM(revenue - cost) / SUM(revenue), 1) AS gross_margin_pct,
       ROUND(100.0 * AVG(returned), 1)                    AS return_rate_pct
FROM orders
GROUP BY year
ORDER BY year;

-- name: monthly_revenue
-- Q2. How does revenue trend month over month (with MoM growth)?
WITH m AS (
  SELECT strftime('%Y-%m', order_date) AS month, SUM(revenue) AS revenue
  FROM orders GROUP BY month
)
SELECT month,
       ROUND(revenue, 0) AS revenue,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
             / LAG(revenue) OVER (ORDER BY month), 1) AS mom_growth_pct
FROM m ORDER BY month;

-- name: category_performance
-- Q3. Which categories drive revenue, profit and returns?
SELECT category,
       COUNT(*)                                             AS orders,
       ROUND(SUM(revenue), 0)                               AS revenue,
       ROUND(100.0 * SUM(revenue) / (SELECT SUM(revenue) FROM orders), 1) AS revenue_share_pct,
       ROUND(SUM(revenue - cost), 0)                        AS gross_profit,
       ROUND(100.0 * SUM(revenue - cost) / SUM(revenue), 1) AS margin_pct,
       ROUND(100.0 * AVG(returned), 1)                      AS return_rate_pct
FROM orders
GROUP BY category
ORDER BY revenue DESC;

-- name: region_performance
-- Q4. How do regions compare?
SELECT region,
       COUNT(DISTINCT customer_id)                         AS customers,
       ROUND(SUM(revenue), 0)                              AS revenue,
       ROUND(SUM(revenue) / COUNT(DISTINCT customer_id), 2) AS revenue_per_customer,
       ROUND(SUM(revenue) / COUNT(*), 2)                   AS avg_order_value
FROM orders
GROUP BY region
ORDER BY revenue DESC;

-- name: discount_impact
-- Q5. Do discounts pay off? Margin and return rate by discount band.
SELECT CASE WHEN discount = 0     THEN '0%'
            WHEN discount <= 0.10 THEN '1-10%'
            WHEN discount <= 0.20 THEN '11-20%'
            ELSE '21-30%' END                               AS discount_band,
       COUNT(*)                                             AS orders,
       ROUND(SUM(revenue), 0)                               AS revenue,
       ROUND(100.0 * SUM(revenue - cost) / SUM(revenue), 1) AS margin_pct,
       ROUND(100.0 * AVG(returned), 1)                      AS return_rate_pct
FROM orders
GROUP BY discount_band
ORDER BY discount_band;

-- name: channel_ltv
-- Q6. Which acquisition channels bring the most valuable customers?
WITH per_customer AS (
  SELECT customer_id, COUNT(*) AS n_orders, SUM(revenue) AS revenue
  FROM orders GROUP BY customer_id
)
SELECT c.acquisition_channel,
       COUNT(*)                                          AS customers,
       ROUND(AVG(p.n_orders), 2)                         AS orders_per_customer,
       ROUND(AVG(p.revenue), 2)                          AS revenue_per_customer,
       ROUND(100.0 * AVG(CASE WHEN p.n_orders >= 2 THEN 1 ELSE 0 END), 1) AS repeat_rate_pct
FROM customers c
JOIN per_customer p ON p.customer_id = c.customer_id
GROUP BY c.acquisition_channel
ORDER BY revenue_per_customer DESC;

-- name: top_customers_pareto
-- Q7. How concentrated is revenue? (share of revenue from top 20% of customers)
WITH cust AS (
  SELECT customer_id, SUM(revenue) AS rev,
         NTILE(5) OVER (ORDER BY SUM(revenue) DESC) AS quintile
  FROM orders GROUP BY customer_id
)
SELECT quintile,
       COUNT(*) AS customers,
       ROUND(SUM(rev), 0) AS revenue,
       ROUND(100.0 * SUM(rev) / (SELECT SUM(rev) FROM cust), 1) AS revenue_share_pct
FROM cust GROUP BY quintile ORDER BY quintile;
