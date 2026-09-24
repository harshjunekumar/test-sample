-- =====================================================================
-- Reference solutions (SQLite). There is usually more than one correct
-- answer: if your result matches, your query is fine.
-- Run one:   python run.py solution 3.4
-- =====================================================================

-- =============================== LEVEL 1 ===============================

-- Q1.1 Products by price
SELECT product_name, category, unit_price
FROM products
ORDER BY unit_price DESC;

-- Q1.2 Enterprise customers who signed up in 2024
SELECT first_name, last_name, city, signup_date
FROM customers
WHERE segment = 'Enterprise'
  AND signup_date BETWEEN '2024-01-01' AND '2024-12-31'
ORDER BY signup_date;

-- Q1.3 Distinct categories
SELECT DISTINCT category
FROM products
ORDER BY category;

-- Q1.4 Five cheapest Accessories / Office products
SELECT product_name, category, unit_price
FROM products
WHERE category IN ('Accessories', 'Office')
ORDER BY unit_price
LIMIT 5;

-- Q1.5 Customers with no email (use IS NULL, never "= NULL")
SELECT customer_id, first_name, last_name
FROM customers
WHERE email IS NULL;

-- Q1.6 Products with "Laptop" in the name
SELECT product_id, product_name
FROM products
WHERE product_name LIKE '%Laptop%';

-- Q1.7 Cancelled orders in Q1 2025
SELECT order_id, customer_id, order_date
FROM orders
WHERE status = 'cancelled'
  AND order_date >= '2025-01-01' AND order_date < '2025-04-01'
ORDER BY order_date DESC;

-- Q1.8 Unit margin and margin %
SELECT product_name,
       unit_price,
       unit_cost,
       unit_price - unit_cost                               AS unit_margin,
       ROUND((unit_price - unit_cost) * 100.0 / unit_price, 1) AS margin_pct
FROM products
ORDER BY margin_pct DESC;

-- =============================== LEVEL 2 ===============================

-- Q2.1 Customers per segment
SELECT segment, COUNT(*) AS customers
FROM customers
GROUP BY segment
ORDER BY customers DESC;

-- Q2.2 Orders by status with % of total
SELECT status,
       COUNT(*) AS orders,
       ROUND(COUNT(*) * 100.0 / (SELECT COUNT(*) FROM orders), 1) AS pct_of_orders
FROM orders
GROUP BY status
ORDER BY orders DESC;

-- Q2.3 Total revenue
SELECT ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
FROM order_items oi
JOIN orders o ON o.order_id = oi.order_id
WHERE o.status = 'completed';

-- Q2.4 Price stats per category
SELECT category,
       COUNT(*)                  AS products,
       MIN(unit_price)           AS min_price,
       MAX(unit_price)           AS max_price,
       ROUND(AVG(unit_price), 2) AS avg_price
FROM products
GROUP BY category
ORDER BY avg_price DESC;

-- Q2.5 Categories with more than 4 products (HAVING filters groups, WHERE filters rows)
SELECT category, COUNT(*) AS products
FROM products
GROUP BY category
HAVING COUNT(*) > 4;

-- Q2.6 Orders per month in 2024
SELECT strftime('%Y-%m', order_date) AS month, COUNT(*) AS orders
FROM orders
WHERE order_date BETWEEN '2024-01-01' AND '2024-12-31'
GROUP BY month
ORDER BY month;

-- Q2.7 Distinct ordering customers in 2025
SELECT COUNT(DISTINCT customer_id) AS customers_2025
FROM orders
WHERE order_date >= '2025-01-01';

-- Q2.8 Acquisition channels with > 10 customers
SELECT acquisition_channel, COUNT(*) AS customers
FROM customers
GROUP BY acquisition_channel
HAVING COUNT(*) > 10
ORDER BY customers DESC;

-- =============================== LEVEL 3 ===============================

-- Q3.1 Orders with customer + region
SELECT o.order_id, o.order_date, o.status,
       c.first_name || ' ' || c.last_name AS customer,
       r.region_name
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN regions   r ON r.region_id   = c.region_id
ORDER BY o.order_date DESC, o.order_id DESC
LIMIT 10;

-- Q3.2 Revenue by region
SELECT r.region_name,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
FROM orders o
JOIN order_items oi ON oi.order_id   = o.order_id
JOIN customers c    ON c.customer_id = o.customer_id
JOIN regions r      ON r.region_id   = c.region_id
WHERE o.status = 'completed'
GROUP BY r.region_name
ORDER BY revenue DESC;

-- Q3.3 Revenue, gross profit and margin by category
SELECT p.category,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)
                 - oi.quantity * p.unit_cost), 2)                   AS gross_profit,
       ROUND(100.0 * SUM(oi.quantity * oi.unit_price * (1 - oi.discount) - oi.quantity * p.unit_cost)
                   / SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 1) AS gross_margin_pct
FROM order_items oi
JOIN orders o   ON o.order_id   = oi.order_id
JOIN products p ON p.product_id = oi.product_id
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY revenue DESC;

-- Q3.4 Customers who never ordered (anti-join)
SELECT c.customer_id, c.first_name, c.last_name, c.signup_date, c.acquisition_channel
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL
ORDER BY c.signup_date;

-- Q3.5 Employee -> manager (self-join; LEFT keeps the CEO)
SELECT e.full_name AS employee, e.title, m.full_name AS manager
FROM employees e
LEFT JOIN employees m ON m.employee_id = e.manager_id
ORDER BY e.employee_id;

-- Q3.6 Top 10 customers by lifetime revenue
SELECT c.customer_id,
       c.first_name || ' ' || c.last_name AS customer,
       c.segment,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS lifetime_revenue
FROM customers c
JOIN orders o       ON o.customer_id = c.customer_id AND o.status = 'completed'
JOIN order_items oi ON oi.order_id   = o.order_id
GROUP BY c.customer_id, customer, c.segment
ORDER BY lifetime_revenue DESC
LIMIT 10;

-- Q3.7 Sales rep scorecard (the filter goes in the ON clause so reps with zero sales survive the LEFT JOIN)
WITH order_value AS (
    SELECT order_id, SUM(quantity * unit_price * (1 - discount)) AS value
    FROM order_items
    GROUP BY order_id
)
SELECT e.full_name,
       r.region_name,
       COUNT(o.order_id)                                   AS completed_orders,
       ROUND(COALESCE(SUM(ov.value), 0), 2)                AS revenue,
       ROUND(COALESCE(SUM(ov.value) / COUNT(o.order_id), 0), 2) AS aov
FROM employees e
JOIN regions r            ON r.region_id = e.region_id
LEFT JOIN orders o        ON o.employee_id = e.employee_id AND o.status = 'completed'
LEFT JOIN order_value ov  ON ov.order_id = o.order_id
WHERE e.title = 'Sales Rep'
GROUP BY e.employee_id, e.full_name, r.region_name
ORDER BY revenue DESC;

-- Q3.8 Products with no completed sales in 2025
SELECT p.product_id, p.product_name, p.launch_date
FROM products p
WHERE p.product_id NOT IN (
    SELECT oi.product_id
    FROM order_items oi
    JOIN orders o ON o.order_id = oi.order_id
    WHERE o.status = 'completed' AND o.order_date >= '2025-01-01'
);

-- =============================== LEVEL 4 ===============================

-- Q4.1 Products priced above average (scalar subquery)
SELECT product_name, unit_price,
       ROUND((SELECT AVG(unit_price) FROM products), 2) AS avg_price
FROM products
WHERE unit_price > (SELECT AVG(unit_price) FROM products)
ORDER BY unit_price DESC;

-- Q4.2 Customers above average lifetime revenue
WITH customer_revenue AS (
    SELECT o.customer_id,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id
)
SELECT c.first_name || ' ' || c.last_name AS customer,
       ROUND(cr.revenue, 2) AS revenue,
       ROUND((SELECT AVG(revenue) FROM customer_revenue), 2) AS avg_customer_revenue
FROM customer_revenue cr
JOIN customers c ON c.customer_id = cr.customer_id
WHERE cr.revenue > (SELECT AVG(revenue) FROM customer_revenue)
ORDER BY cr.revenue DESC;

-- Q4.3 Order size bands
WITH order_value AS (
    SELECT o.order_id, SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS value
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY o.order_id
)
SELECT CASE
           WHEN value < 100  THEN '1. Small'
           WHEN value < 500  THEN '2. Medium'
           WHEN value < 2000 THEN '3. Large'
           ELSE                   '4. Very Large'
       END AS size_band,
       COUNT(*)            AS orders,
       ROUND(SUM(value), 2) AS revenue
FROM order_value
GROUP BY size_band
ORDER BY size_band;

-- Q4.4 Pivot: category x year (conditional aggregation)
SELECT p.category,
       ROUND(SUM(CASE WHEN o.order_date <  '2025-01-01' THEN oi.quantity * oi.unit_price * (1 - oi.discount) ELSE 0 END), 2) AS revenue_2024,
       ROUND(SUM(CASE WHEN o.order_date >= '2025-01-01' THEN oi.quantity * oi.unit_price * (1 - oi.discount) ELSE 0 END), 2) AS revenue_2025_h1
FROM order_items oi
JOIN orders o   ON o.order_id   = oi.order_id
JOIN products p ON p.product_id = oi.product_id
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY revenue_2024 DESC;

-- Q4.5 Customer order history summary
SELECT customer_id,
       MIN(order_date) AS first_order,
       MAX(order_date) AS last_order,
       COUNT(*)        AS orders,
       CAST(julianday(MAX(order_date)) - julianday(MIN(order_date)) AS INTEGER) AS days_first_to_last
FROM orders
GROUP BY customer_id
ORDER BY orders DESC;

-- Q4.6 Customers who bought from every category (relational division)
SELECT c.customer_id, c.first_name || ' ' || c.last_name AS customer,
       COUNT(DISTINCT p.category) AS categories
FROM customers c
JOIN orders o       ON o.customer_id = c.customer_id AND o.status = 'completed'
JOIN order_items oi ON oi.order_id   = o.order_id
JOIN products p     ON p.product_id  = oi.product_id
GROUP BY c.customer_id, customer
HAVING COUNT(DISTINCT p.category) = (SELECT COUNT(DISTINCT category) FROM products)
ORDER BY c.customer_id;

-- Q4.7 Bought a laptop, never bought a sleeve
SELECT c.customer_id, c.first_name || ' ' || c.last_name AS customer, c.email
FROM customers c
WHERE EXISTS (
        SELECT 1
        FROM orders o
        JOIN order_items oi ON oi.order_id = o.order_id
        JOIN products p     ON p.product_id = oi.product_id
        WHERE o.customer_id = c.customer_id
          AND o.status = 'completed'
          AND p.product_name IN ('Laptop Pro 14', 'Laptop Air 13'))
  AND NOT EXISTS (
        SELECT 1
        FROM orders o
        JOIN order_items oi ON oi.order_id = o.order_id
        JOIN products p     ON p.product_id = oi.product_id
        WHERE o.customer_id = c.customer_id
          AND p.product_name = 'Laptop Sleeve')
ORDER BY c.customer_id;

-- Q4.8 Product avg discount vs its category avg (correlated subquery)
SELECT p.product_name,
       p.category,
       ROUND(AVG(oi.discount) * 100, 1) AS avg_discount_pct,
       ROUND((SELECT AVG(oi2.discount) * 100
              FROM order_items oi2
              JOIN products p2 ON p2.product_id = oi2.product_id
              WHERE p2.category = p.category), 1) AS category_avg_discount_pct
FROM products p
JOIN order_items oi ON oi.product_id = p.product_id
GROUP BY p.product_id, p.product_name, p.category
ORDER BY p.category, avg_discount_pct DESC;

-- =============================== LEVEL 5 ===============================

-- Q5.1 Rank products by revenue within category
WITH product_revenue AS (
    SELECT p.category, p.product_name,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM order_items oi
    JOIN orders o   ON o.order_id   = oi.order_id
    JOIN products p ON p.product_id = oi.product_id
    WHERE o.status = 'completed'
    GROUP BY p.category, p.product_name
)
SELECT category, product_name, ROUND(revenue, 2) AS revenue,
       RANK() OVER (PARTITION BY category ORDER BY revenue DESC) AS rank_in_category
FROM product_revenue
ORDER BY category, rank_in_category;

-- Q5.2 Top 2 products per category (you can't filter a window function in WHERE, so wrap it)
WITH product_revenue AS (
    SELECT p.category, p.product_name,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM order_items oi
    JOIN orders o   ON o.order_id   = oi.order_id
    JOIN products p ON p.product_id = oi.product_id
    WHERE o.status = 'completed'
    GROUP BY p.category, p.product_name
),
ranked AS (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY category ORDER BY revenue DESC) AS rn
    FROM product_revenue
)
SELECT category, product_name, ROUND(revenue, 2) AS revenue, rn
FROM ranked
WHERE rn <= 2
ORDER BY category, rn;

-- Q5.3 Monthly revenue + running total by year
WITH monthly AS (
    SELECT strftime('%Y-%m', o.order_date) AS month,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY month
)
SELECT month,
       ROUND(revenue, 2) AS revenue,
       ROUND(SUM(revenue) OVER (PARTITION BY substr(month, 1, 4) ORDER BY month), 2) AS ytd_revenue
FROM monthly
ORDER BY month;

-- Q5.4 Month-over-month growth %
WITH monthly AS (
    SELECT strftime('%Y-%m', o.order_date) AS month,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY month
)
SELECT month,
       ROUND(revenue, 2) AS revenue,
       ROUND(LAG(revenue) OVER (ORDER BY month), 2) AS prev_month,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month))
                   / LAG(revenue) OVER (ORDER BY month), 1) AS mom_growth_pct
FROM monthly
ORDER BY month;

-- Q5.5 3-month moving average
WITH monthly AS (
    SELECT strftime('%Y-%m', o.order_date) AS month,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY month
)
SELECT month,
       ROUND(revenue, 2) AS revenue,
       ROUND(AVG(revenue) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 2) AS moving_avg_3m
FROM monthly
ORDER BY month;

-- Q5.6 Order sequence and days since previous order
SELECT customer_id, order_id, order_date,
       ROW_NUMBER() OVER w AS order_number,
       CAST(julianday(order_date) - julianday(LAG(order_date) OVER w) AS INTEGER) AS days_since_prev
FROM orders
WINDOW w AS (PARTITION BY customer_id ORDER BY order_date, order_id)
ORDER BY customer_id, order_number;

-- Q5.7 Region share of revenue (aggregate inside a window: SUM(SUM(x)) OVER ())
SELECT r.region_name,
       ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue,
       ROUND(100.0 * SUM(oi.quantity * oi.unit_price * (1 - oi.discount))
             / SUM(SUM(oi.quantity * oi.unit_price * (1 - oi.discount))) OVER (), 1) AS pct_of_total
FROM orders o
JOIN order_items oi ON oi.order_id   = o.order_id
JOIN customers c    ON c.customer_id = o.customer_id
JOIN regions r      ON r.region_id   = c.region_id
WHERE o.status = 'completed'
GROUP BY r.region_name
ORDER BY revenue DESC;

-- Q5.8 Revenue quartiles
WITH customer_revenue AS (
    SELECT o.customer_id, SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id
),
q AS (
    SELECT *, NTILE(4) OVER (ORDER BY revenue DESC) AS quartile
    FROM customer_revenue
)
SELECT quartile,
       COUNT(*) AS customers,
       ROUND(SUM(revenue), 2) AS revenue,
       ROUND(100.0 * SUM(revenue) / SUM(SUM(revenue)) OVER (), 1) AS pct_of_revenue
FROM q
GROUP BY quartile
ORDER BY quartile;

-- Q5.9 Best-selling product each month
WITH monthly_product AS (
    SELECT strftime('%Y-%m', o.order_date) AS month, p.product_name,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id   = o.order_id
    JOIN products p     ON p.product_id  = oi.product_id
    WHERE o.status = 'completed'
    GROUP BY month, p.product_name
)
SELECT month, product_name, ROUND(revenue, 2) AS revenue
FROM (
    SELECT *, ROW_NUMBER() OVER (PARTITION BY month ORDER BY revenue DESC, product_name) AS rn
    FROM monthly_product
) t
WHERE rn = 1
ORDER BY month;

-- =============================== LEVEL 6 ===============================

-- Q6.1 New vs returning active customers per month
WITH completed AS (
    SELECT customer_id, strftime('%Y-%m', order_date) AS month
    FROM orders
    WHERE status = 'completed'
),
first_month AS (
    SELECT customer_id, MIN(month) AS first_month
    FROM completed
    GROUP BY customer_id
)
SELECT c.month,
       COUNT(DISTINCT c.customer_id) AS active_customers,
       COUNT(DISTINCT CASE WHEN c.month =  f.first_month THEN c.customer_id END) AS new_customers,
       COUNT(DISTINCT CASE WHEN c.month >  f.first_month THEN c.customer_id END) AS returning_customers
FROM completed c
JOIN first_month f ON f.customer_id = c.customer_id
GROUP BY c.month
ORDER BY c.month;

-- Q6.2 Cohort retention (months since first order)
WITH activity AS (
    SELECT DISTINCT customer_id, strftime('%Y-%m', order_date) AS month
    FROM orders
    WHERE status = 'completed'
),
cohort AS (
    SELECT customer_id, MIN(month) AS cohort_month
    FROM activity
    GROUP BY customer_id
),
offsets AS (
    SELECT c.cohort_month, a.customer_id,
           (CAST(substr(a.month, 1, 4) AS INTEGER) - CAST(substr(c.cohort_month, 1, 4) AS INTEGER)) * 12
         + (CAST(substr(a.month, 6, 2) AS INTEGER) - CAST(substr(c.cohort_month, 6, 2) AS INTEGER)) AS month_n
    FROM activity a
    JOIN cohort c ON c.customer_id = a.customer_id
)
SELECT cohort_month,
       COUNT(DISTINCT CASE WHEN month_n = 0 THEN customer_id END) AS cohort_size,
       ROUND(100.0 * COUNT(DISTINCT CASE WHEN month_n = 1 THEN customer_id END)
                   / COUNT(DISTINCT CASE WHEN month_n = 0 THEN customer_id END), 1) AS m1_pct,
       ROUND(100.0 * COUNT(DISTINCT CASE WHEN month_n = 2 THEN customer_id END)
                   / COUNT(DISTINCT CASE WHEN month_n = 0 THEN customer_id END), 1) AS m2_pct,
       ROUND(100.0 * COUNT(DISTINCT CASE WHEN month_n = 3 THEN customer_id END)
                   / COUNT(DISTINCT CASE WHEN month_n = 0 THEN customer_id END), 1) AS m3_pct
FROM offsets
GROUP BY cohort_month
ORDER BY cohort_month;
-- Note: recent cohorts haven't had 3 months yet, so their later columns read 0 because there is no data yet, not because customers churned.

-- Q6.3 Funnel with step and overall conversion
WITH steps AS (
    SELECT event_type,
           CASE event_type WHEN 'visit' THEN 1 WHEN 'view_product' THEN 2 WHEN 'add_to_cart' THEN 3
                           WHEN 'checkout' THEN 4 WHEN 'purchase' THEN 5 END AS step_no,
           COUNT(DISTINCT session_id) AS sessions
    FROM web_events
    GROUP BY event_type
)
SELECT step_no, event_type, sessions,
       ROUND(100.0 * sessions / LAG(sessions) OVER (ORDER BY step_no), 1)     AS pct_of_prev_step,
       ROUND(100.0 * sessions / FIRST_VALUE(sessions) OVER (ORDER BY step_no), 1) AS pct_of_visits
FROM steps
ORDER BY step_no;

-- Q6.4 Funnel by device (one row per device, steps pivoted)
WITH s AS (
    SELECT session_id, device,
           MAX(event_type = 'visit')        AS visited,
           MAX(event_type = 'view_product') AS viewed,
           MAX(event_type = 'add_to_cart')  AS carted,
           MAX(event_type = 'checkout')     AS checked_out,
           MAX(event_type = 'purchase')     AS purchased
    FROM web_events
    GROUP BY session_id, device
)
SELECT device,
       SUM(visited)   AS visits,
       SUM(viewed)    AS views,
       SUM(carted)    AS carts,
       SUM(checked_out) AS checkouts,
       SUM(purchased) AS purchases,
       ROUND(100.0 * SUM(carted)    / SUM(viewed), 1) AS view_to_cart_pct,
       ROUND(100.0 * SUM(purchased) / SUM(visited), 2) AS visit_to_purchase_pct
FROM s
GROUP BY device
ORDER BY visit_to_purchase_pct DESC;
-- Insight: mobile converts worst, and the biggest drop is view -> add_to_cart.

-- Q6.5 RFM segmentation
WITH base AS (
    SELECT o.customer_id,
           CAST(julianday('2025-06-30') - julianday(MAX(o.order_date)) AS INTEGER) AS recency_days,
           COUNT(DISTINCT o.order_id) AS frequency,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS monetary
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id
),
scored AS (
    SELECT *,
           NTILE(4) OVER (ORDER BY recency_days DESC) AS r,   -- more recent = higher score
           NTILE(4) OVER (ORDER BY frequency)         AS f,
           NTILE(4) OVER (ORDER BY monetary)          AS m
    FROM base
)
SELECT customer_id, recency_days, frequency, ROUND(monetary, 2) AS monetary, r, f, m,
       CASE
           WHEN r >= 3 AND f >= 3 AND m >= 3 THEN 'Champions'
           WHEN r <= 2 AND f >= 3            THEN 'At Risk'
           WHEN r >= 3 AND f <= 2            THEN 'New / Promising'
           ELSE 'Needs Attention'
       END AS rfm_segment
FROM scored
ORDER BY r + f + m DESC, monetary DESC;

-- Q6.6 Pareto: share of customers producing 80% of revenue
WITH customer_revenue AS (
    SELECT o.customer_id, SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id
),
cum AS (
    SELECT customer_id, revenue,
           SUM(revenue) OVER (ORDER BY revenue DESC ROWS UNBOUNDED PRECEDING) / SUM(revenue) OVER () AS cum_share,
           ROW_NUMBER() OVER (ORDER BY revenue DESC) AS rn,
           COUNT(*) OVER () AS n_customers
    FROM customer_revenue
)
SELECT MIN(rn) AS customers_needed_for_80pct,
       MAX(n_customers) AS total_customers,
       ROUND(100.0 * MIN(rn) / MAX(n_customers), 1) AS pct_of_customers
FROM cum
WHERE cum_share >= 0.8;

-- Q6.7 CAC and ROI by paid channel
WITH spend AS (
    SELECT channel, SUM(spend) AS total_spend
    FROM marketing_spend
    GROUP BY channel
),
acquired AS (
    SELECT acquisition_channel AS channel, COUNT(*) AS customers
    FROM customers
    GROUP BY acquisition_channel
),
rev AS (
    SELECT c.acquisition_channel AS channel,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM customers c
    JOIN orders o       ON o.customer_id = c.customer_id AND o.status = 'completed'
    JOIN order_items oi ON oi.order_id   = o.order_id
    GROUP BY c.acquisition_channel
)
SELECT s.channel,
       ROUND(s.total_spend, 2)                        AS total_spend,
       a.customers,
       ROUND(s.total_spend / a.customers, 2)          AS cac,
       ROUND(COALESCE(r.revenue, 0) / a.customers, 2) AS revenue_per_customer,
       ROUND(COALESCE(r.revenue, 0) / s.total_spend, 2) AS revenue_to_spend_ratio
FROM spend s
JOIN acquired a  ON a.channel = s.channel
LEFT JOIN rev r  ON r.channel = s.channel
ORDER BY cac;
-- Caveat to mention in an interview: revenue is not profit, and attribution is last-touch only.

-- Q6.8 High-value churn risk
WITH stats AS (
    SELECT o.customer_id,
           COUNT(DISTINCT o.order_id) AS orders,
           MAX(o.order_date)          AS last_order,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY o.customer_id
)
SELECT c.customer_id, c.first_name || ' ' || c.last_name AS customer, c.segment,
       s.orders, s.last_order,
       CAST(julianday('2025-06-30') - julianday(s.last_order) AS INTEGER) AS days_inactive,
       ROUND(s.revenue, 2) AS lifetime_revenue
FROM stats s
JOIN customers c ON c.customer_id = s.customer_id
WHERE s.orders >= 2
  AND s.last_order < date('2025-06-30', '-120 days')
ORDER BY s.revenue DESC;

-- Q6.9 YoY H1 growth by category
WITH h1 AS (
    SELECT p.category,
           SUM(CASE WHEN o.order_date BETWEEN '2024-01-01' AND '2024-06-30'
                    THEN oi.quantity * oi.unit_price * (1 - oi.discount) ELSE 0 END) AS h1_2024,
           SUM(CASE WHEN o.order_date BETWEEN '2025-01-01' AND '2025-06-30'
                    THEN oi.quantity * oi.unit_price * (1 - oi.discount) ELSE 0 END) AS h1_2025
    FROM orders o
    JOIN order_items oi ON oi.order_id   = o.order_id
    JOIN products p     ON p.product_id  = oi.product_id
    WHERE o.status = 'completed'
    GROUP BY p.category
)
SELECT category,
       ROUND(h1_2024, 2) AS h1_2024,
       ROUND(h1_2025, 2) AS h1_2025,
       ROUND(100.0 * (h1_2025 - h1_2024) / NULLIF(h1_2024, 0), 1) AS yoy_growth_pct
FROM h1
ORDER BY yoy_growth_pct DESC;

-- Q6.10 Products bought together (a.product_id < b.product_id avoids duplicates and self-pairs)
SELECT pa.product_name AS product_a,
       pb.product_name AS product_b,
       COUNT(*)        AS orders_together
FROM order_items a
JOIN order_items b ON b.order_id = a.order_id AND a.product_id < b.product_id
JOIN products pa   ON pa.product_id = a.product_id
JOIN products pb   ON pb.product_id = b.product_id
GROUP BY pa.product_name, pb.product_name
ORDER BY orders_together DESC, product_a, product_b
LIMIT 10;

-- Q6.11 Median order value
WITH order_value AS (
    SELECT o.order_id, SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS value
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY o.order_id
),
ranked AS (
    SELECT value,
           ROW_NUMBER() OVER (ORDER BY value) AS rn,
           COUNT(*) OVER () AS n
    FROM order_value
)
SELECT ROUND(AVG(value), 2) AS median_order_value,
       (SELECT ROUND(AVG(value), 2) FROM order_value) AS mean_order_value
FROM ranked
WHERE rn IN ((n + 1) / 2, (n + 2) / 2);
-- Postgres: PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY value). Mean > median means a right-skewed distribution.

-- Q6.12 Fulfilment SLA by region
SELECT r.region_name,
       COUNT(*) AS shipped_orders,
       ROUND(AVG(julianday(o.ship_date) - julianday(o.order_date)), 2) AS avg_days_to_ship,
       ROUND(100.0 * SUM(CASE WHEN julianday(o.ship_date) - julianday(o.order_date) <= 3 THEN 1 ELSE 0 END)
             / COUNT(*), 1) AS pct_within_3_days
FROM orders o
JOIN customers c ON c.customer_id = o.customer_id
JOIN regions r   ON r.region_id   = c.region_id
WHERE o.status = 'completed'
  AND o.ship_date IS NOT NULL
  AND o.ship_date >= o.order_date
GROUP BY r.region_name
ORDER BY avg_days_to_ship;

-- =============================== LEVEL 7 ===============================

-- Q7.1 Duplicate emails (normalised)
SELECT LOWER(TRIM(email)) AS clean_email,
       COUNT(*) AS occurrences,
       GROUP_CONCAT(customer_id) AS customer_ids   -- Postgres: STRING_AGG(customer_id::text, ',')
FROM customers
WHERE email IS NOT NULL
GROUP BY clean_email
HAVING COUNT(*) > 1;

-- Q7.2 Suspicious orders
SELECT order_id, order_date, ship_date, status,
       CASE WHEN ship_date IS NULL THEN 'completed but no ship date'
            ELSE 'shipped before ordered' END AS issue
FROM orders
WHERE status = 'completed'
  AND (ship_date IS NULL OR ship_date < order_date);

-- Q7.3 Clean customer list
SELECT customer_id,
       first_name || ' ' || last_name AS full_name,
       LOWER(TRIM(email))             AS email,
       COALESCE(UPPER(substr(TRIM(city), 1, 1)) || LOWER(substr(TRIM(city), 2)), 'Unknown') AS city
FROM customers
ORDER BY customer_id;
-- Note: this simple proper-case turns "new york" into "New york". Proper word casing needs a lookup table or INITCAP (Postgres).

-- Q7.4 Orders with no line items
SELECT o.order_id, o.order_date, o.status
FROM orders o
WHERE NOT EXISTS (SELECT 1 FROM order_items oi WHERE oi.order_id = o.order_id);

-- Q7.5 Deduplicate customers by email, keeping the earliest signup
WITH ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY LOWER(TRIM(email)) ORDER BY signup_date, customer_id) AS rn
    FROM customers
    WHERE email IS NOT NULL
)
SELECT customer_id, first_name, last_name, LOWER(TRIM(email)) AS email, signup_date
FROM ranked
WHERE rn = 1
ORDER BY customer_id;

-- Q7.6 Referential integrity checks (both should return 0 rows)
SELECT 'web_events' AS source, we.customer_id AS missing_key
FROM web_events we
LEFT JOIN customers c ON c.customer_id = we.customer_id
WHERE we.customer_id IS NOT NULL AND c.customer_id IS NULL
UNION ALL
SELECT 'order_items', oi.product_id
FROM order_items oi
LEFT JOIN products p ON p.product_id = oi.product_id
WHERE p.product_id IS NULL;

-- =============================== LEVEL 8 ===============================

-- Q8.1 Longest consecutive-month ordering streak (gaps and islands)
WITH months AS (
    SELECT DISTINCT customer_id,
           CAST(strftime('%Y', order_date) AS INTEGER) * 12 + CAST(strftime('%m', order_date) AS INTEGER) AS month_idx
    FROM orders
    WHERE status = 'completed'
),
islands AS (
    -- consecutive months share the same (month_idx - row_number) value
    SELECT customer_id, month_idx,
           month_idx - ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY month_idx) AS grp
    FROM months
),
streaks AS (
    SELECT customer_id, grp, COUNT(*) AS streak_len
    FROM islands
    GROUP BY customer_id, grp
)
SELECT customer_id, MAX(streak_len) AS longest_streak_months
FROM streaks
GROUP BY customer_id
HAVING MAX(streak_len) >= 3
ORDER BY longest_streak_months DESC, customer_id;

-- Q8.2 Charged price change 2024 -> 2025
WITH prices AS (
    SELECT p.product_name,
           AVG(CASE WHEN o.order_date <  '2025-01-01' THEN oi.unit_price END) AS avg_price_2024,
           AVG(CASE WHEN o.order_date >= '2025-01-01' THEN oi.unit_price END) AS avg_price_2025
    FROM order_items oi
    JOIN orders o   ON o.order_id   = oi.order_id
    JOIN products p ON p.product_id = oi.product_id
    GROUP BY p.product_name
)
SELECT product_name,
       ROUND(avg_price_2024, 2) AS avg_price_2024,
       ROUND(avg_price_2025, 2) AS avg_price_2025,
       ROUND(100.0 * (avg_price_2025 - avg_price_2024) / avg_price_2024, 1) AS pct_change
FROM prices
WHERE ABS(avg_price_2025 - avg_price_2024) > 0.005;

-- Q8.3 Minutes from visit to purchase, by device
WITH t AS (
    SELECT session_id, device,
           MIN(CASE WHEN event_type = 'visit'    THEN event_time END) AS visit_time,
           MIN(CASE WHEN event_type = 'purchase' THEN event_time END) AS purchase_time
    FROM web_events
    GROUP BY session_id, device
)
SELECT device,
       COUNT(*) AS purchasing_sessions,
       ROUND(AVG((julianday(purchase_time) - julianday(visit_time)) * 24 * 60), 1) AS avg_minutes_to_purchase
FROM t
WHERE purchase_time IS NOT NULL
GROUP BY device
ORDER BY avg_minutes_to_purchase;

-- Q8.4 Management chain (recursive CTE)
WITH RECURSIVE chain AS (
    SELECT employee_id, manager_id, full_name AS path, 0 AS depth
    FROM employees
    UNION ALL
    SELECT c.employee_id, m.manager_id, c.path || ' > ' || m.full_name, c.depth + 1
    FROM chain c
    JOIN employees m ON m.employee_id = c.manager_id
)
SELECT e.full_name, e.title, c.depth AS levels_below_ceo, c.path AS management_chain
FROM chain c
JOIN employees e ON e.employee_id = c.employee_id
WHERE c.manager_id IS NULL          -- keep only the row that reached the top
ORDER BY c.depth, e.employee_id;
