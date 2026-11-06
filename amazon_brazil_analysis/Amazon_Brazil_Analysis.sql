-- =====================================================================
-- Amazon Brazil -> Amazon India : Database & schema setup
-- Run in pgAdmin. Step 1 (CREATE DATABASE) must run on its own while
-- connected to the default "postgres" database; then connect to
-- amazon_analysis and run the rest.
-- =====================================================================

-- CREATE DATABASE amazon_analysis;

CREATE SCHEMA IF NOT EXISTS amazon_brazil;

-- Customers: one row per customer_id (an order-level customer key);
-- customer_unique_id identifies the real person across orders.
CREATE TABLE amazon_brazil.customers (
    customer_id               VARCHAR(50) PRIMARY KEY,
    customer_unique_id        VARCHAR(50) NOT NULL,
    customer_zip_code_prefix  INT
);

-- Seller master data
CREATE TABLE amazon_brazil.seller (
    seller_id                 VARCHAR(50) PRIMARY KEY,
    seller_zip_code_prefix    INT
);

-- Product specifications
CREATE TABLE amazon_brazil.product (
    product_id                  VARCHAR(50) PRIMARY KEY,
    product_category_name       VARCHAR(100),
    product_name_lenght         INT,
    product_description_lenght  INT,
    product_photos_qty          INT,
    product_weight_g            INT,
    product_length_cm           INT,
    product_height_cm           INT,
    product_width_cm            INT
);

-- Orders: one row per order (1 customer_id -> 1 order)
CREATE TABLE amazon_brazil.orders (
    order_id                       VARCHAR(50) PRIMARY KEY,
    customer_id                    VARCHAR(50) REFERENCES amazon_brazil.customers(customer_id),
    order_status                   VARCHAR(20),
    order_purchase_timestamp       TIMESTAMP,
    order_approved_at              TIMESTAMP,
    order_delivered_carrier_date   TIMESTAMP,
    order_delivered_customer_date  TIMESTAMP,
    order_estimated_delivery_date  TIMESTAMP
);

-- Order items: one row per item line (1 order -> many items)
CREATE TABLE amazon_brazil.order_items (
    order_id             VARCHAR(50) REFERENCES amazon_brazil.orders(order_id),
    order_item_id        INT,
    product_id           VARCHAR(50) REFERENCES amazon_brazil.product(product_id),
    seller_id            VARCHAR(50) REFERENCES amazon_brazil.seller(seller_id),
    shipping_limit_date  TIMESTAMP,
    price                NUMERIC(10,2),
    freight_value        NUMERIC(10,2),
    PRIMARY KEY (order_id, order_item_id)
);

-- Payments: one row per payment instalment record (1 order -> many payments)
CREATE TABLE amazon_brazil.payments (
    order_id              VARCHAR(50) REFERENCES amazon_brazil.orders(order_id),
    payment_sequential    INT,
    payment_type          VARCHAR(20),
    payment_installments  INT,
    payment_value         NUMERIC(10,2),
    PRIMARY KEY (order_id, payment_sequential)
);

-- Import order (respect foreign keys): customers, seller, product,
-- orders, order_items, payments. In pgAdmin use Import/Export -> CSV,
-- delimiter ',', Header ON. psql equivalent:
-- \copy amazon_brazil.customers   FROM 'customers.csv'   CSV HEADER
-- \copy amazon_brazil.seller      FROM 'seller.csv'      CSV HEADER
-- \copy amazon_brazil.product     FROM 'product.csv'     CSV HEADER
-- \copy amazon_brazil.orders      FROM 'orders.csv'      CSV HEADER
-- \copy amazon_brazil.order_items FROM 'order_items.csv' CSV HEADER
-- \copy amazon_brazil.payments    FROM 'payments.csv'    CSV HEADER


-- =====================================================================
-- Amazon Brazil Data Analysis for Amazon India
-- Database: amazon_analysis   Schema: amazon_brazil
--
-- Conventions used throughout:
--   * "Sales" / "order value" at order level = payments.payment_value
--     (what the customer actually paid).
--   * "Revenue" at product / category level   = order_items.price
--     (payments cannot be split by product).
--   * All order statuses are included (as in the raw data).
--   * A "customer" for repeat-purchase analysis = customer_unique_id,
--     because customer_id is created afresh for every order.
-- =====================================================================

SET search_path TO amazon_brazil;


-- =====================================================================
-- ANALYSIS I
-- =====================================================================

-- I.1 Standardise payment values: average payment value per payment type,
--     rounded to an integer, sorted ascending.
SELECT payment_type,
       ROUND(AVG(payment_value)) AS rounded_avg_payment
FROM payments
GROUP BY payment_type
ORDER BY rounded_avg_payment ASC;


-- I.2 Distribution of orders by payment type: % of all orders that used
--     each payment type (1 decimal), descending. An order paid with two
--     methods counts for both, so the column can total slightly > 100%.
SELECT payment_type,
       ROUND(COUNT(DISTINCT order_id) * 100.0
             / (SELECT COUNT(DISTINCT order_id) FROM payments), 1) AS percentage_orders
FROM payments
GROUP BY payment_type
ORDER BY percentage_orders DESC;


-- I.3 Targeted promotion: products priced 100-500 BRL whose name contains
--     'Smart'. The product table has no free-text name, so the category
--     name is used (category 'smart'). Price comes from order_items.
SELECT DISTINCT oi.product_id,
       oi.price
FROM order_items oi
JOIN product p ON p.product_id = oi.product_id
WHERE p.product_category_name ILIKE '%smart%'
  AND oi.price BETWEEN 100 AND 500
ORDER BY oi.price DESC;


-- I.4 Seasonal patterns: top 3 calendar months (all years combined) by
--     total sales value, rounded to the nearest integer.
SELECT TO_CHAR(o.order_purchase_timestamp, 'FMMonth') AS month,
       ROUND(SUM(p.payment_value))                  AS total_sales
FROM orders o
JOIN payments p ON p.order_id = o.order_id
GROUP BY TO_CHAR(o.order_purchase_timestamp, 'FMMonth'),
         EXTRACT(MONTH FROM o.order_purchase_timestamp)
ORDER BY total_sales DESC
LIMIT 3;


-- I.5 Categories with large price variation: max - min price > 500 BRL.
SELECT p.product_category_name,
       MAX(oi.price) - MIN(oi.price) AS price_difference
FROM order_items oi
JOIN product p ON p.product_id = oi.product_id
WHERE p.product_category_name IS NOT NULL
GROUP BY p.product_category_name
HAVING MAX(oi.price) - MIN(oi.price) > 500
ORDER BY price_difference DESC;


-- I.6 Most consistent payment types: standard deviation of transaction
--     amounts, smallest first.
SELECT payment_type,
       ROUND(STDDEV(payment_value), 2) AS std_deviation
FROM payments
GROUP BY payment_type
ORDER BY std_deviation ASC;


-- I.7 Data quality: products whose category name is missing or is only a
--     single character.
SELECT product_id,
       product_category_name
FROM product
WHERE product_category_name IS NULL
   OR LENGTH(TRIM(product_category_name)) = 1;


-- =====================================================================
-- ANALYSIS II
-- =====================================================================

-- II.1 Popular payment types by order-value segment.
--      Order value = total paid for the order. Segments: Low (<200),
--      Medium (200-1000), High (>1000). Count of orders per payment type.
WITH order_value AS (
    SELECT order_id, SUM(payment_value) AS total_value
    FROM payments
    GROUP BY order_id
)
SELECT CASE
           WHEN ov.total_value < 200   THEN 'Low (<200)'
           WHEN ov.total_value <= 1000 THEN 'Medium (200-1000)'
           ELSE 'High (>1000)'
       END                         AS order_value_segment,
       p.payment_type,
       COUNT(DISTINCT p.order_id)  AS count
FROM payments p
JOIN order_value ov ON ov.order_id = p.order_id
GROUP BY order_value_segment, p.payment_type
ORDER BY count DESC;


-- II.2 Price range and average price per product category,
--      sorted by average price descending.
SELECT p.product_category_name,
       MIN(oi.price)           AS min_price,
       MAX(oi.price)           AS max_price,
       ROUND(AVG(oi.price), 2) AS avg_price
FROM order_items oi
JOIN product p ON p.product_id = oi.product_id
WHERE p.product_category_name IS NOT NULL
GROUP BY p.product_category_name
ORDER BY avg_price DESC;


-- II.3 Repeat customers: customers (customer_unique_id) with more than one order.
SELECT c.customer_unique_id,
       COUNT(o.order_id) AS total_orders
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_unique_id
HAVING COUNT(o.order_id) > 1
ORDER BY total_orders DESC;


-- II.4 Customer types via a temporary table:
--      New = 1 order, Returning = 2-4 orders, Loyal = >4 orders.
DROP TABLE IF EXISTS temp_customer_type;

CREATE TEMP TABLE temp_customer_type AS
SELECT c.customer_unique_id,
       COUNT(o.order_id)    AS order_count,
       NULL::VARCHAR(20)    AS customer_type
FROM customers c
JOIN orders o ON o.customer_id = c.customer_id
GROUP BY c.customer_unique_id;

UPDATE temp_customer_type
SET customer_type = CASE
                        WHEN order_count = 1            THEN 'New'
                        WHEN order_count BETWEEN 2 AND 4 THEN 'Returning'
                        ELSE 'Loyal'
                    END;

SELECT DISTINCT c.customer_unique_id,
       t.customer_type
FROM customers c
JOIN temp_customer_type t ON t.customer_unique_id = c.customer_unique_id
ORDER BY t.customer_type, c.customer_unique_id;

-- (summary used in the report)
SELECT customer_type, COUNT(*) AS customers
FROM temp_customer_type
GROUP BY customer_type
ORDER BY customers DESC;


-- II.5 Top 5 product categories by total revenue (sum of item prices).
SELECT p.product_category_name,
       SUM(oi.price) AS total_revenue
FROM order_items oi
JOIN product p ON p.product_id = oi.product_id
WHERE p.product_category_name IS NOT NULL
GROUP BY p.product_category_name
ORDER BY total_revenue DESC
LIMIT 5;


-- =====================================================================
-- ANALYSIS III
-- =====================================================================

-- III.1 Total sales by season using a subquery.
--       Spring = Mar-May, Summer = Jun-Aug, Autumn = Sep-Nov, Winter = Dec-Feb.
SELECT season,
       ROUND(SUM(payment_value), 2) AS total_sales
FROM (
    SELECT p.payment_value,
           CASE
               WHEN EXTRACT(MONTH FROM o.order_purchase_timestamp) IN (3, 4, 5)  THEN 'Spring'
               WHEN EXTRACT(MONTH FROM o.order_purchase_timestamp) IN (6, 7, 8)  THEN 'Summer'
               WHEN EXTRACT(MONTH FROM o.order_purchase_timestamp) IN (9, 10, 11) THEN 'Autumn'
               ELSE 'Winter'
           END AS season
    FROM orders o
    JOIN payments p ON p.order_id = o.order_id
) AS seasonal
GROUP BY season
ORDER BY total_sales DESC;


-- III.2 Products whose total quantity sold is above the average quantity
--       sold per product (each order_items row = 1 unit).
SELECT product_id,
       COUNT(*) AS total_quantity_sold
FROM order_items
GROUP BY product_id
HAVING COUNT(*) > (
    SELECT AVG(qty)
    FROM (SELECT COUNT(*) AS qty
          FROM order_items
          GROUP BY product_id) AS per_product
)
ORDER BY total_quantity_sold DESC;


-- III.3 Monthly revenue trend for 2018 (export to Excel and chart).
SELECT TO_CHAR(DATE_TRUNC('month', o.order_purchase_timestamp), 'YYYY-MM') AS month,
       ROUND(SUM(p.payment_value), 2)                                     AS total_revenue
FROM orders o
JOIN payments p ON p.order_id = o.order_id
WHERE EXTRACT(YEAR FROM o.order_purchase_timestamp) = 2018
GROUP BY DATE_TRUNC('month', o.order_purchase_timestamp)
ORDER BY month;


-- III.4 Loyalty segmentation with a CTE:
--       Occasional = 1-2 orders, Regular = 3-5, Loyal = >5.
WITH customer_orders AS (
    SELECT c.customer_unique_id,
           COUNT(o.order_id) AS order_count
    FROM customers c
    JOIN orders o ON o.customer_id = c.customer_id
    GROUP BY c.customer_unique_id
),
segmented AS (
    SELECT customer_unique_id,
           CASE
               WHEN order_count <= 2 THEN 'Occasional'
               WHEN order_count <= 5 THEN 'Regular'
               ELSE 'Loyal'
           END AS customer_type
    FROM customer_orders
)
SELECT customer_type,
       COUNT(*) AS count
FROM segmented
GROUP BY customer_type
ORDER BY count DESC;


-- III.5 Top 20 high-value customers ranked by average order value.
WITH order_value AS (
    SELECT o.customer_id,
           o.order_id,
           SUM(p.payment_value) AS order_value
    FROM orders o
    JOIN payments p ON p.order_id = o.order_id
    GROUP BY o.customer_id, o.order_id
),
customer_avg AS (
    SELECT customer_id,
           ROUND(AVG(order_value), 2) AS avg_order_value
    FROM order_value
    GROUP BY customer_id
)
SELECT customer_id,
       avg_order_value,
       customer_rank
FROM (
    SELECT customer_id,
           avg_order_value,
           RANK() OVER (ORDER BY avg_order_value DESC) AS customer_rank
    FROM customer_avg
) ranked
WHERE customer_rank <= 20
ORDER BY customer_rank;


-- III.6 Product lifecycle: monthly cumulative sales per product from its
--       first sale month, built month-by-month with a RECURSIVE CTE.
--       Months with no sales carry the running total forward.
WITH RECURSIVE monthly_sales AS (
    SELECT oi.product_id,
           DATE_TRUNC('month', o.order_purchase_timestamp)::DATE AS sale_month,
           SUM(oi.price) AS month_sales
    FROM order_items oi
    JOIN orders o ON o.order_id = oi.order_id
    GROUP BY oi.product_id, DATE_TRUNC('month', o.order_purchase_timestamp)
),
product_span AS (
    SELECT product_id,
           MIN(sale_month) AS first_month,
           MAX(sale_month) AS last_month
    FROM monthly_sales
    GROUP BY product_id
),
cumulative AS (
    -- anchor: first month of sale
    SELECT ps.product_id,
           ps.first_month AS sale_month,
           ps.last_month,
           ms.month_sales AS total_sales
    FROM product_span ps
    JOIN monthly_sales ms
      ON ms.product_id = ps.product_id
     AND ms.sale_month = ps.first_month
    UNION ALL
    -- recursive step: next month = previous cumulative + this month's sales
    SELECT c.product_id,
           (c.sale_month + INTERVAL '1 month')::DATE,
           c.last_month,
           c.total_sales + COALESCE(ms.month_sales, 0)
    FROM cumulative c
    LEFT JOIN monthly_sales ms
      ON ms.product_id = c.product_id
     AND ms.sale_month = (c.sale_month + INTERVAL '1 month')::DATE
    WHERE c.sale_month < c.last_month
)
SELECT product_id,
       TO_CHAR(sale_month, 'YYYY-MM') AS sale_month,
       total_sales
FROM cumulative
ORDER BY product_id, sale_month;


-- III.7 Month-over-month sales growth by payment method for 2018.
WITH monthly AS (
    SELECT p.payment_type,
           DATE_TRUNC('month', o.order_purchase_timestamp) AS month_start,
           SUM(p.payment_value)                            AS monthly_total
    FROM payments p
    JOIN orders o ON o.order_id = p.order_id
    WHERE EXTRACT(YEAR FROM o.order_purchase_timestamp) = 2018
    GROUP BY p.payment_type, DATE_TRUNC('month', o.order_purchase_timestamp)
)
SELECT payment_type,
       TO_CHAR(month_start, 'YYYY-MM') AS sale_month,
       ROUND(monthly_total, 2)         AS monthly_total,
       ROUND((monthly_total - LAG(monthly_total) OVER w) * 100.0
             / NULLIF(LAG(monthly_total) OVER w, 0), 2) AS monthly_change
FROM monthly
WINDOW w AS (PARTITION BY payment_type ORDER BY month_start)
ORDER BY payment_type, sale_month;
