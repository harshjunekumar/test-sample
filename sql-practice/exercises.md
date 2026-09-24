# SQL Exercises: Basic to Advanced (Business Analyst Track)

There are 63 questions across 8 levels. Each one is a question a stakeholder might really ask.
New to SQL? Read [`sql-syntax-guide.md`](sql-syntax-guide.md) first.
Write your query first, then compare with `python run.py solution <n>` or `solutions.sql`.

## The business

**Northwind-lite** is an online retailer that sells electronics, accessories, furniture,
office supplies and software to consumers, small businesses (SMB) and enterprises. It
covers four US regions. Data runs from **Sep 2023 (first signups) to Jun 2025**.

```
regions ─┬─< customers ──< orders >── employees (self-ref manager_id)
         │                  │
         └─< employees      └──< order_items >── products

marketing_spend (month_start, channel)   web_events (session funnel, 2025 H1)
```

| Table | Grain | Key columns |
|---|---|---|
| `regions` | 1 row per region | `region_id`, `region_name` |
| `customers` | 1 row per customer | `segment`, `acquisition_channel`, `signup_date`, `region_id` |
| `products` | 1 row per product | `category`, `unit_price` (current list), `unit_cost` |
| `employees` | 1 row per employee | `manager_id` → `employees`, `title`, `region_id` |
| `orders` | 1 row per order | `customer_id`, `employee_id` (NULL = online self-serve), `status`, `order_date`, `ship_date` |
| `order_items` | 1 row per product in an order | `quantity`, `unit_price` (price charged), `discount` (0.10 = 10%) |
| `marketing_spend` | 1 row per month × paid channel | `spend` |
| `web_events` | 1 row per event in a session | `session_id`, `event_type`, `device`, `event_time` |

### Business rules (use these unless the question says otherwise)

- **Line revenue** = `quantity * unit_price * (1 - discount)` from `order_items`.
- **Revenue** counts only orders with `status = 'completed'`.
- **Gross profit** = line revenue − `quantity * products.unit_cost`.
- **AOV** (average order value) = revenue ÷ number of completed orders.
- The "as-of date" for recency and churn questions is **2025-06-30**.

> Dialect note: solutions are written for **SQLite**, which `run.py` uses. They also run on
> PostgreSQL and MySQL except for date functions. See the cheat sheet in the README.

---

## Level 1: Retrieving and filtering data
*SELECT, WHERE, ORDER BY, LIMIT, DISTINCT, IN, BETWEEN, LIKE, IS NULL, calculated columns*

**1.1** List every product's name, category and price, most expensive first.

**1.2** Which **Enterprise** customers signed up during **2024**? Show name, city and signup date, oldest first.

**1.3** Which distinct product categories do we sell? Sort them alphabetically.

**1.4** Show the 5 cheapest products in the `Accessories` or `Office` categories.

**1.5** Marketing wants to email everyone. Which customers have **no email address** on file?

**1.6** Find all products with "Laptop" anywhere in the name.

**1.7** List the orders **cancelled** in **Q1 2025** (Jan–Mar), newest first.

**1.8** For each product, show the unit margin (`unit_price - unit_cost`) and the margin %
(margin ÷ price × 100, rounded to 1 decimal). Sort by margin % from highest to lowest.

---

## Level 2: Aggregation
*COUNT, SUM, AVG, MIN, MAX, GROUP BY, HAVING, COUNT(DISTINCT)*

**2.1** How many customers are in each segment?

**2.2** How many orders are there in each status, and what % of all orders is each status?

**2.3** What is total **revenue** (see business rules) across all time?

**2.4** For each category, show the product count and the min, max and average list price.

**2.5** Which categories have **more than 4** products?

**2.6** How many orders were placed in each month of **2024**? (Hint: `strftime('%Y-%m', order_date)`)

**2.7** How many distinct customers placed at least one order in 2025?

**2.8** Which acquisition channels brought in more than 10 customers? Sort by customer count, highest first.

---

## Level 3: Joins
*INNER / LEFT JOIN, multi-table joins, self-joins, anti-joins*

**3.1** List each order with the customer's full name and region name. Show the 10 most recent orders.

**3.2** Show **revenue by region**, highest first.

**3.3** Show **revenue, gross profit and gross margin %** by product category.

**3.4** Which customers have **never placed an order**? (Solve it with a LEFT JOIN.)

**3.5** Show every employee next to the name of their manager. Keep the CEO in the list.

**3.6** Who are the **top 10 customers by lifetime revenue**? Include their segment.

**3.7** **Sales rep scorecard**: for every employee titled `Sales Rep`, show completed orders,
revenue and AOV. Reps with zero sales must still appear with 0.

**3.8** Which products sold **zero units in 2025** (completed orders)?

---

## Level 4: Subqueries, CTEs and CASE
*scalar/correlated subqueries, EXISTS, WITH, CASE WHEN, conditional aggregation*

**4.1** Which products are priced above the average product price?

**4.2** Which customers have lifetime revenue **above the average customer's** lifetime revenue?
Only count customers with at least one completed order. Use a CTE.

**4.3** Put completed orders into size bands: `Small` (< $100), `Medium` ($100–$499.99),
`Large` ($500–$1,999.99) and `Very Large` ($2,000+). For each band, show the order count and revenue.

**4.4** **Pivot**: show revenue by category (rows) with one column for 2024 and one for 2025.

**4.5** For each customer who has ordered, show their first order date, last order date, number of orders
(any status) and the days between their first and last order.

**4.6** Which customers have bought from **every category** we sell? Don't hard-code the number of categories. (Completed orders only.)

**4.7** **Cross-sell target list**: which customers bought a laptop (`Laptop Pro 14` or `Laptop Air 13`)
but have **never** bought a `Laptop Sleeve`? Use `EXISTS` / `NOT EXISTS`.

**4.8** Is there a price effect? Compare each product's average discount with its category's average
discount using a **correlated subquery**.

---

## Level 5: Window functions
*ROW_NUMBER, RANK, DENSE_RANK, NTILE, LAG/LEAD, running totals, moving averages, SUM() OVER ()*

**5.1** Rank products by revenue **within their category**.

**5.2** Show only the **top 2 products per category** by revenue.

**5.3** Show monthly revenue with a **running total** that resets each year.

**5.4** Show **month-over-month revenue growth %**.

**5.5** Show a **3-month moving average** of monthly revenue.

**5.6** For every order, show the customer's order sequence number (1st, 2nd, ...) and the **days since
their previous order**.

**5.7** Show each region's revenue **and its % share of the total**, without a subquery.

**5.8** Split customers into **quartiles** by lifetime revenue (`NTILE(4)`). For each quartile, show the
customer count, total revenue and share of revenue.

**5.9** For each month, which product had the most revenue? Break ties by product name.

---

## Level 6: Business analytics case studies
*The questions that come up in interviews and in real BA work*

**6.1** **New vs returning customers**: for each month, count active customers, split into *new*
(first ever completed order that month) and *returning*.

**6.2** **Cohort retention**: group customers by the month of their first completed order. For each
cohort, what % of customers ordered again 1, 2 and 3 months later? (Month 0 = cohort month.)

**6.3** **Conversion funnel** (web_events): how many sessions reached each step (visit → view_product →
add_to_cart → checkout → purchase)? Show conversion from the previous step and from visit.

**6.4** Same funnel, **by device**: show visit→purchase conversion for desktop, mobile and tablet.
Where should the product team focus?

**6.5** **RFM segmentation** as of 2025-06-30. Score each customer 1–4 on Recency (days since last order),
Frequency (number of orders) and Monetary (revenue) using `NTILE`, then label them:
`Champions` (R≥3 and F≥3 and M≥3), `At Risk` (R≤2 and F≥3), `New / Promising` (R≥3 and F≤2), otherwise `Needs Attention`.

**6.6** **Pareto analysis**: what % of customers generate 80% of revenue?

**6.7** **CAC by channel**: for each paid channel, divide total marketing spend by the number of customers
acquired through that channel. Also show the revenue per acquired customer and the ROI ratio.

**6.8** **Churn risk**: which customers with 2+ completed orders have not ordered in the last 120 days
(as of 2025-06-30)? Sort by lifetime revenue, because these are the ones to call first.

**6.9** **Year-over-year**: compare revenue by category for **Jan–Jun 2025 vs Jan–Jun 2024**, with YoY growth %.

**6.10** **Market basket**: which pairs of products are most often bought **in the same order**? Show the top 10.

**6.11** What is the **median** completed order value? SQLite has no `MEDIAN()`, so use window functions.

**6.12** **Fulfilment SLA**: for each region, show the average days from order to shipping and the % of
orders shipped within 3 days. Use completed orders with valid ship dates only.

---

## Level 7: Data quality and cleaning
*The unglamorous half of the job*

**7.1** Find **duplicate emails** in `customers`. Treat case and extra spaces as the same (`TRIM`, `LOWER`).

**7.2** Find **suspicious orders**: completed orders with no ship date, or a ship date before the order date.

**7.3** Build a **clean customer list**: trimmed, lower-case email; city in proper case with
`'Unknown'` when it is missing; full name in one column.

**7.4** Find orders that have **no line items**.

**7.5** **Deduplicate**: keep one row per cleaned email (the earliest signup) with `ROW_NUMBER()`.
Ignore rows with a NULL email.

**7.6** **Referential check**: find `web_events.customer_id` values that don't exist in `customers`, and
check every order line has a known product. Expect 0 rows. The point is to know how to check.

---

## Level 8: Stretch (interview-hard)

**8.1** **Consecutive-month streaks**: find each customer's longest streak of consecutive months with at
least one order. This is the classic "gaps and islands" problem.

**8.2** **Price change detection**: some products changed price on 2025-01-01. Find products whose
average charged `unit_price` in 2025 differs from 2024, and show the % change.

**8.3** **Time between funnel steps**: for sessions that purchased, what is the average number of minutes
from `visit` to `purchase`, by device?

**8.4** **Manager roll-up** (recursive CTE): for each employee, show their full management chain up to
the CEO, e.g. `Jake Turner > Daniel Cho > Priya Shah > Morgan Blake`.

---

### Suggested practice plan

| Week | Levels | Goal |
|---|---|---|
| 1 | 1–2 | Answer any "how many / how much" question from one table |
| 2 | 3–4 | Combine tables confidently. Know when to use LEFT JOIN vs EXISTS |
| 3 | 5 | Use window functions without looking anything up |
| 4 | 6–8 | Solve an open-ended business question end-to-end, then explain it in plain English |

**Tip:** for every answer, write one sentence a manager would understand, for example
"The West region brings in 31% of revenue but has only 2 reps." Turning numbers into
insight is the real BA skill.
