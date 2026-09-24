# SQL Syntax Guide: Every Keyword Explained, With Exercises

This guide teaches SQL from zero. Each section explains **what a piece of syntax means**,
shows a **real query** against the practice database with its **actual result**, lists the
**common mistakes**, and ends with **practice questions**. Answers are hidden: click
"Show answer" only after you've tried.

When you finish a section, go to the matching level in [`exercises.md`](exercises.md) for
harder, business-style questions.

**Setup:** run `python run.py setup` once. Then run any query with
`python run.py query "SELECT ..."`, or open `practice.db` in DB Browser for SQLite or DBeaver.
The examples use SQLite. See the dialect table in the [README](README.md) for PostgreSQL and MySQL.

## Contents

0. [Core ideas: tables, rows, NULL and how SQL runs](#0-core-ideas)
1. [SELECT and FROM: picking columns](#1-select-and-from)
2. [AS: aliases and calculated columns](#2-as-aliases-and-calculated-columns)
3. [WHERE: filtering rows](#3-where-filtering-rows)
4. [AND, OR, NOT, IN, BETWEEN, LIKE and IS NULL](#4-and-or-not-in-between-like-is-null)
5. [ORDER BY, LIMIT and OFFSET: sorting and top-N](#5-order-by-limit-offset)
6. [DISTINCT: removing duplicates](#6-distinct)
7. [Functions: text, numbers, dates and NULLs](#7-functions)
8. [CASE WHEN: if/then logic](#8-case-when)
9. [Aggregates: COUNT, SUM, AVG, MIN and MAX](#9-aggregate-functions)
10. [GROUP BY and HAVING](#10-group-by-and-having)
11. [JOINs: combining tables](#11-joins)
12. [UNION, INTERSECT and EXCEPT: stacking results](#12-set-operators)
13. [Subqueries: a query inside a query](#13-subqueries)
14. [WITH (CTEs): naming steps](#14-ctes-with)
15. [Window functions: OVER and PARTITION BY](#15-window-functions)
16. [Creating and changing data: CREATE, INSERT, UPDATE, DELETE and VIEW](#16-ddl-and-dml)
17. [Checklist for writing any query](#17-checklist)

---

## 0. Core ideas

### Tables, rows and columns
A **table** is like a spreadsheet tab. Each **row** is one record, such as one order. Each
**column** is one attribute, such as `order_date`. A **primary key** (for example `order_id`) is
a column whose value is unique for every row. A **foreign key** (for example `orders.customer_id`)
points to the primary key of another table. That link is how tables join together.

**Grain** means *what one row represents*. The grain of `orders` is one order. The grain of
`order_items` is one product within one order. Always ask "what is the grain?" before you
write a query. Most wrong answers come from mixing grains.

### A query is a question
```sql
SELECT product_name, unit_price   -- which columns to show
FROM products                     -- which table to read
WHERE category = 'Furniture'      -- which rows to keep
ORDER BY unit_price DESC;         -- how to sort the result
```
**Result:**

| product_name | unit_price |
|---|---|
| Standing Desk | 499 |
| Ergonomic Chair | 379 |
| Monitor Arm | 89 |
| Desk Lamp | 45 |

*(4 rows)*

### The order you write it vs the order SQL runs it
You **write** clauses in this order: `SELECT → FROM → WHERE → GROUP BY → HAVING → ORDER BY → LIMIT`.

The database **runs** them in this order:

| Step | Clause | What happens |
|---|---|---|
| 1 | `FROM` / `JOIN` | Get the tables and combine them |
| 2 | `WHERE` | Throw away rows that don't match |
| 3 | `GROUP BY` | Squash rows into groups |
| 4 | `HAVING` | Throw away groups that don't match |
| 5 | `SELECT` | Compute the output columns (and window functions) |
| 6 | `DISTINCT` | Remove duplicate output rows |
| 7 | `ORDER BY` | Sort |
| 8 | `LIMIT` / `OFFSET` | Keep only some rows |

This explains many error messages. For example, you usually **can't use a `SELECT` alias
inside `WHERE`**, because `WHERE` runs before `SELECT` has created the alias. SQLite is lenient
about this, but PostgreSQL and SQL Server are not.

### Grammar rules
| Rule | Example |
|---|---|
| Keywords are case-insensitive. Writing them in CAPITALS is a readability convention | `select` = `SELECT` |
| Text values go in **single quotes** | `'Furniture'` |
| Double quotes (or backticks in MySQL) are for **names** that contain spaces or odd characters | `"order date"` |
| A `;` ends a statement | `SELECT 1;` |
| `--` starts a comment that runs to the end of the line | `-- note` |
| `/* ... */` is a comment that can span several lines | `/* note */` |
| Whitespace and new lines don't matter | Put each clause on its own line so it's easy to read |

### NULL: "unknown", not zero, not empty
`NULL` means the value is missing or unknown. It follows special rules:
- Any arithmetic with NULL gives NULL: `5 + NULL` is `NULL`.
- **Any comparison with NULL is "unknown", which counts as not true.** `NULL = NULL` is not true,
  so `WHERE email = NULL` never matches anything. Write `WHERE email IS NULL` instead.
- Aggregates such as `SUM`, `AVG` and `COUNT(column)` **skip** NULLs.

```sql
SELECT 5 + NULL        AS plus_null,
       NULL = NULL     AS null_equals_null,
       NULL IS NULL    AS null_is_null;
```
**Result:**

| plus_null | null_equals_null | null_is_null |
|---|---|---|
| NULL | NULL | 1 |

*(1 row)*

SQLite shows true as `1` and false as `0`. `NULL = NULL` gives NULL ("unknown"), not true.

### Data types you'll meet
| Type | Holds | Example |
|---|---|---|
| `INTEGER` | whole numbers | `42` |
| `DECIMAL(10,2)` / `REAL` | numbers with decimals | `19.99` |
| `VARCHAR(n)` / `TEXT` | text | `'Chicago'` |
| `DATE` | a calendar date, written `'YYYY-MM-DD'` | `'2025-01-31'` |
| `TIMESTAMP` | date plus time | `'2025-01-31 14:05:00'` |
| `BOOLEAN` | true/false. SQLite stores these as 1/0 | `1` |

---

## 1. SELECT and FROM

**`SELECT`** lists the columns (or calculations) you want back. **`FROM`** names the table to read.

```text
SELECT column1, column2, ...
FROM table_name;
```

| Syntax | Meaning |
|---|---|
| `SELECT *` | every column. Handy for exploring, but avoid it in final queries |
| `SELECT a, b` | only columns a and b, in that order |
| `SELECT 'hello'`, `SELECT 2 * 3` | a constant or a calculation. `FROM` is optional here in SQLite, PostgreSQL and MySQL |

```sql
SELECT * FROM regions;
```
**Result:**

| region_id | region_name |
|---|---|
| 1 | North |
| 2 | South |
| 3 | East |
| 4 | West |

*(4 rows)*

```sql
SELECT first_name, last_name, segment
FROM customers
LIMIT 5;
```
**Result:**

| first_name | last_name | segment |
|---|---|---|
| Lucas | Smith | Consumer |
| Noah | Smith | Consumer |
| Amelia | Hall | SMB |
| Sophia | Brown | Consumer |
| Grace | Brown | SMB |

*(5 rows)*

**Tip:** to see a table's columns, run `SELECT * FROM table LIMIT 5;` or check the table list in [exercises.md](exercises.md).

### Practice 1
1. Show every column of `employees`.
2. Show only `product_name` and `category` from `products`.
3. Without using any table, show the number 100 and the text `'SQL'`.

<details><summary>Show answers</summary>

```sql
SELECT * FROM employees;
```
```sql
SELECT product_name, category FROM products;
```
```sql
SELECT 100, 'SQL';
```
</details>

---

## 2. AS: aliases and calculated columns

**`AS`** gives a column or table a new name, called an **alias**, for the rest of the query.
The word `AS` itself is optional (`price p` works too), but writing it is clearer.

### Arithmetic operators
| Operator | Meaning | Example |
|---|---|---|
| `+` `-` `*` `/` | add, subtract, multiply, divide | `unit_price - unit_cost` |
| `%` | remainder (modulo) | `10 % 3` → 1 |
| `\|\|` | join text together (concatenate). MySQL uses `CONCAT(a, b)` | `first_name \|\| ' ' \|\| last_name` |

```sql
SELECT product_name,
       unit_price - unit_cost              AS unit_margin,
       unit_price * 2                      AS price_for_two,
       product_name || ' (' || category || ')' AS label
FROM products
LIMIT 5;
```
**Result:**

| product_name | unit_margin | price_for_two | label |
|---|---|---|---|
| Laptop Pro 14 | 449 | 2598 | Laptop Pro 14 (Electronics) |
| Laptop Air 13 | 319 | 1998 | Laptop Air 13 (Electronics) |
| Monitor 27in | 119 | 658 | Monitor 27in (Electronics) |
| Tablet 11 | 189 | 1098 | Tablet 11 (Electronics) |
| Wireless Earbuds | 74 | 258 | Wireless Earbuds (Electronics) |

*(5 rows)*

### ⚠️ The integer division trap
When you divide **one whole number by another**, the answer is a whole number: `7 / 2 = 3`.
Multiply by `1.0` or `100.0` first to get decimals.
```sql
SELECT 7 / 2 AS int_div, 7 * 1.0 / 2 AS real_div, 100.0 * 3 / 4 AS pct;
```
**Result:**

| int_div | real_div | pct |
|---|---|---|
| 3 | 3.5 | 75 |

*(1 row)*

### Table aliases
`FROM products AS p` lets you write `p.product_name` instead of `products.product_name`.
Once you join several tables, this becomes essential (see section 11).

### Practice 2
1. For each product, show its name and its cost as a % of price, calling the column `cost_pct`.
2. Show each customer's full name as a single column called `customer`.
3. Show the price of every product after a 15% discount, calling the column `sale_price`.

<details><summary>Show answers</summary>

```sql
SELECT product_name, 100.0 * unit_cost / unit_price AS cost_pct FROM products;
```
```sql
SELECT first_name || ' ' || last_name AS customer FROM customers;
```
```sql
SELECT product_name, unit_price * (1 - 0.15) AS sale_price FROM products;
```
</details>

---

## 3. WHERE: filtering rows

**`WHERE`** keeps only the rows for which the condition is **true**. It runs **before**
grouping, so it filters individual rows.

### Comparison operators
| Operator | Meaning | Example |
|---|---|---|
| `=` | equals | `status = 'completed'` |
| `<>` or `!=` | not equal | `segment <> 'Consumer'` |
| `>` `>=` `<` `<=` | greater or less than (works for numbers, dates and text) | `unit_price >= 100` |

Text comparison is **case-sensitive** in SQLite and PostgreSQL. `'furniture'` does not equal
`'Furniture'`. Dates stored as `'YYYY-MM-DD'` compare correctly as text: `'2024-12-31' < '2025-01-01'`.

```sql
SELECT order_id, order_date, status
FROM orders
WHERE order_date >= '2025-06-25';
```
**Result:**

| order_id | order_date | status |
|---|---|---|
| 1616 | 2025-06-26 | completed |
| 1618 | 2025-06-29 | completed |
| 1626 | 2025-06-26 | returned |
| 1628 | 2025-06-28 | returned |
| 1642 | 2025-06-25 | completed |
| 1648 | 2025-06-29 | completed |
| 1650 | 2025-06-30 | completed |

*(7 rows)*

### Practice 3
1. Which products cost less than $30?
2. Which orders have the status `'returned'`?
3. Which customers are **not** in region 4?

<details><summary>Show answers</summary>

```sql
SELECT product_name, unit_price FROM products WHERE unit_price < 30;
```
```sql
SELECT * FROM orders WHERE status = 'returned';
```
```sql
SELECT * FROM customers WHERE region_id <> 4;
```
</details>

---

## 4. AND, OR, NOT, IN, BETWEEN, LIKE, IS NULL

| Syntax | Meaning | Example |
|---|---|---|
| `A AND B` | both must be true | `segment = 'SMB' AND region_id = 1` |
| `A OR B` | at least one must be true | `category = 'Office' OR category = 'Software'` |
| `NOT A` | reverses the condition | `NOT status = 'completed'` |
| `x IN (a, b, c)` | x equals any value in the list. It's shorthand for several ORs | `category IN ('Office','Software')` |
| `x NOT IN (...)` | x equals none of them. ⚠️ See the NULL trap in section 13 | |
| `x BETWEEN a AND b` | `x >= a AND x <= b`. **Both ends are included** | `unit_price BETWEEN 50 AND 100` |
| `x LIKE 'pattern'` | text pattern match. `%` = any number of characters, `_` = exactly one character | `email LIKE '%@example.com'` |
| `x IS NULL` / `x IS NOT NULL` | tests for missing values | `ship_date IS NULL` |

### Precedence: AND binds tighter than OR, so use parentheses
```sql
-- WRONG: this reads as  segment='Enterprise' OR (segment='SMB' AND region_id=1)
SELECT COUNT(*) AS wrong FROM customers
WHERE segment = 'Enterprise' OR segment = 'SMB' AND region_id = 1;
```
**Result:**

| wrong |
|---|
| 21 |

*(1 row)*
```sql
-- RIGHT: Enterprise or SMB customers who are in region 1
SELECT COUNT(*) AS right_answer FROM customers
WHERE (segment = 'Enterprise' OR segment = 'SMB') AND region_id = 1;
```
**Result:**

| right_answer |
|---|
| 9 |

*(1 row)*

### LIKE patterns
| Pattern | Matches |
|---|---|
| `'Laptop%'` | text that starts with "Laptop" |
| `'%Annual'` | text that ends with "Annual" |
| `'%Pro%'` | text that contains "Pro" anywhere |
| `'_ask%'` | any 1 character, then "ask", then anything |

In SQLite, `LIKE` ignores case for English letters. In PostgreSQL it doesn't, so use `ILIKE` there.

```sql
SELECT product_name FROM products WHERE product_name LIKE '%Pro%';
```
**Result:**

| product_name |
|---|
| Laptop Pro 14 |
| Antivirus Pro Annual |

*(2 rows)*

### BETWEEN with dates
`order_date BETWEEN '2025-01-01' AND '2025-01-31'` works because these are plain dates. If a
column holds **timestamps**, `'2025-01-31 15:00'` is *after* `'2025-01-31'` and would be missed.
The safe pattern is a half-open range:
`event_time >= '2025-01-01' AND event_time < '2025-02-01'`.

```sql
SELECT order_id, order_date, ship_date, status
FROM orders
WHERE status = 'completed' AND ship_date IS NULL;
```
**Result:**

| order_id | order_date | ship_date | status |
|---|---|---|---|
| 1015 | 2024-01-15 | NULL | completed |
| 1225 | 2024-09-28 | NULL | completed |

*(2 rows)*

### Practice 4
1. Which products are in the Electronics **or** Furniture category **and** cost more than $400?
2. Which customers signed up in March 2025 (use `BETWEEN`)?
3. Which customers' emails end in `@example.com`?
4. Which customers are **missing** a city?
5. Which orders are neither completed nor cancelled (use `NOT IN`)?

<details><summary>Show answers</summary>

```sql
SELECT product_name, category, unit_price FROM products
WHERE category IN ('Electronics', 'Furniture') AND unit_price > 400;
```
```sql
SELECT * FROM customers WHERE signup_date BETWEEN '2025-03-01' AND '2025-03-31';
```
```sql
SELECT email FROM customers WHERE email LIKE '%@example.com';
```
```sql
SELECT * FROM customers WHERE city IS NULL;
```
```sql
SELECT * FROM orders WHERE status NOT IN ('completed', 'cancelled');
```
</details>

---

## 5. ORDER BY, LIMIT, OFFSET

| Syntax | Meaning |
|---|---|
| `ORDER BY col` | sorts smallest first, A→Z, oldest first (`ASC` is the default) |
| `ORDER BY col DESC` | sorts largest first, Z→A, newest first |
| `ORDER BY a, b DESC` | sorts by a, then breaks ties with b (descending) |
| `ORDER BY 2` | sorts by the 2nd selected column. Short, but fragile if the columns change |
| `LIMIT n` | keeps only the first n rows |
| `LIMIT n OFFSET m` | skips m rows, then keeps n. Used for pages (rows 11–20 = `LIMIT 10 OFFSET 10`) |

Other databases write this differently: SQL Server uses `SELECT TOP 5 ...`, and standard SQL
and Oracle use `FETCH FIRST 5 ROWS ONLY`.

Without `ORDER BY`, **row order is not guaranteed**. `LIMIT` without `ORDER BY` returns
arbitrary rows. In SQLite, NULLs sort first in ascending order. In PostgreSQL they sort
last, and you can control this with `NULLS FIRST` or `NULLS LAST`.

```sql
SELECT category, product_name, unit_price
FROM products
ORDER BY category, unit_price DESC
LIMIT 6;
```
**Result:**

| category | product_name | unit_price |
|---|---|---|
| Accessories | Mechanical Keyboard | 119 |
| Accessories | Webcam HD | 79 |
| Accessories | USB-C Hub | 49 |
| Accessories | Laptop Sleeve | 35 |
| Accessories | Wireless Mouse | 29 |
| Electronics | Laptop Pro 14 | 1299 |

*(6 rows)*

### Practice 5
1. Show the 3 most recently hired employees.
2. Sort customers by segment (A→Z), then by signup date (newest first).
3. Show products ranked 6th to 10th by price (highest price first).

<details><summary>Show answers</summary>

```sql
SELECT full_name, hire_date FROM employees ORDER BY hire_date DESC LIMIT 3;
```
```sql
SELECT first_name, segment, signup_date FROM customers ORDER BY segment, signup_date DESC;
```
```sql
SELECT product_name, unit_price FROM products ORDER BY unit_price DESC LIMIT 5 OFFSET 5;
```
</details>

---

## 6. DISTINCT

**`DISTINCT`** removes duplicate rows from the **result**. It applies to the whole row, meaning
the *combination* of every selected column, not just the first column.

```sql
SELECT DISTINCT segment, acquisition_channel
FROM customers
ORDER BY segment, acquisition_channel
LIMIT 8;
```
**Result:**

| segment | acquisition_channel |
|---|---|
| Consumer | Affiliate |
| Consumer | Email |
| Consumer | Organic |
| Consumer | Paid Search |
| Consumer | Referral |
| Consumer | Social |
| Enterprise | Affiliate |
| Enterprise | Email |

*(8 rows)*

`COUNT(DISTINCT col)` counts the unique values in a column (see section 9).

⚠️ If you're adding `DISTINCT` to "fix" duplicate rows after a join, stop and check the
join. The duplicates usually mean the grain is wrong.

### Practice 6
1. Which distinct statuses exist in `orders`?
2. Which distinct cities are there in region 3?
3. Which distinct (device, event_type) pairs appear in `web_events`?

<details><summary>Show answers</summary>

```sql
SELECT DISTINCT status FROM orders;
```
```sql
SELECT DISTINCT city FROM customers WHERE region_id = 3;
```
```sql
SELECT DISTINCT device, event_type FROM web_events ORDER BY device, event_type;
```
</details>

---
## 7. Functions

A **function** takes input values in parentheses and returns a value: `UPPER('abc')` → `'ABC'`.
The functions in this section are **scalar** functions, meaning they work on one row at a time.
Aggregate functions, which combine many rows, come in section 9.

### Text functions
| Function | Meaning | Example → result |
|---|---|---|
| `UPPER(s)` / `LOWER(s)` | change the case | `LOWER('ABC')` → `abc` |
| `TRIM(s)` | removes spaces from both ends (`LTRIM` / `RTRIM` do one side only) | `TRIM('  hi ')` → `hi` |
| `LENGTH(s)` | number of characters | `LENGTH('SQL')` → 3 |
| `SUBSTR(s, start, len)` | cuts out part of the text. Positions start at 1 (PostgreSQL/MySQL also have `SUBSTRING`) | `SUBSTR('2025-06-30', 1, 4)` → `2025` |
| `REPLACE(s, from, to)` | find and replace | `REPLACE('a-b', '-', '/')` → `a/b` |
| `INSTR(s, find)` | position of `find` in `s`, or 0 if it isn't there (PostgreSQL: `STRPOS`) | `INSTR('a@b.com', '@')` → 2 |

```sql
SELECT email,
       SUBSTR(email, INSTR(email, '@') + 1)  AS email_domain,
       UPPER(last_name)                       AS last_upper,
       LENGTH(first_name)                     AS name_len
FROM customers
WHERE email IS NOT NULL
LIMIT 4;
```
**Result:**

| email | email_domain | last_upper | name_len |
|---|---|---|---|
| lucas.smith1@example.com | example.com | SMITH | 5 |
| noah.smith2@example.com | example.com | SMITH | 4 |
| amelia.hall3@example.com | example.com | HALL | 6 |
| sophia.brown4@example.com | example.com | BROWN | 6 |

*(4 rows)*

### Number functions
| Function | Meaning | Example → result |
|---|---|---|
| `ROUND(x, n)` | rounds to n decimal places | `ROUND(3.14159, 2)` → 3.14 |
| `ABS(x)` | absolute value | `ABS(-5)` → 5 |
| `CAST(x AS type)` | converts to another type | `CAST('42' AS INTEGER)` → 42 |
| `MAX(a, b)` / `MIN(a, b)` with 2+ arguments | largest or smallest of the values (SQLite. PostgreSQL/MySQL use `GREATEST` / `LEAST`) | `MAX(3, 7)` → 7 |

### Date functions (SQLite)
Dates are text in the form `'YYYY-MM-DD'`. SQLite has a few functions that understand them:

| Function | Meaning | Example → result |
|---|---|---|
| `date('now')` | today's date | |
| `date(d, '+7 days')` | adds or subtracts time. Other modifiers: `'-1 month'`, `'start of month'`, `'start of year'` | `date('2025-01-31', '+1 day')` → `2025-02-01` |
| `strftime(fmt, d)` | formats a date. `%Y` = year, `%m` = month, `%d` = day, `%W` = week number, `%w` = weekday (0 = Sunday) | `strftime('%Y-%m', '2025-06-30')` → `2025-06` |
| `julianday(d)` | the date as a day number. Subtract two of them to get the days between | `julianday('2025-01-10') - julianday('2025-01-01')` → 9 |

```sql
SELECT order_id, order_date, ship_date,
       strftime('%Y-%m', order_date)                    AS order_month,
       strftime('%w', order_date)                       AS weekday_0_sun,
       julianday(ship_date) - julianday(order_date)     AS days_to_ship,
       date(order_date, 'start of month')               AS month_start
FROM orders
LIMIT 4;
```
**Result:**

| order_id | order_date | ship_date | order_month | weekday_0_sun | days_to_ship | month_start |
|---|---|---|---|---|---|---|
| 1001 | 2024-01-28 | 2024-02-03 | 2024-01 | 0 | 6 | 2024-01-01 |
| 1002 | 2024-01-30 | 2024-02-05 | 2024-01 | 2 | 6 | 2024-01-01 |
| 1003 | 2024-01-02 | 2024-01-07 | 2024-01 | 2 | 5 | 2024-01-01 |
| 1004 | 2024-01-08 | 2024-01-12 | 2024-01 | 1 | 4 | 2024-01-01 |

*(4 rows)*

### NULL-handling functions
| Function | Meaning | Example → result |
|---|---|---|
| `COALESCE(a, b, c)` | returns the **first value that isn't NULL** | `COALESCE(NULL, 'Unknown')` → `Unknown` |
| `NULLIF(a, b)` | returns NULL if a = b, otherwise a. Used to **avoid dividing by zero**: `x / NULLIF(y, 0)` | `NULLIF(0, 0)` → NULL |
| `IFNULL(a, b)` | the same as `COALESCE` with 2 arguments (SQLite/MySQL) | |

```sql
SELECT customer_id,
       city,
       COALESCE(city, 'Unknown')   AS city_filled,
       10 / NULLIF(0, 0)           AS safe_divide
FROM customers
WHERE city IS NULL;
```
**Result:**

| customer_id | city | city_filled | safe_divide |
|---|---|---|---|
| 9 | NULL | Unknown | NULL |
| 72 | NULL | Unknown | NULL |

*(2 rows)*

### Practice 7
1. Show each customer's email in lower case with the spaces trimmed off.
2. How many days after signing up did customer 1 place each of their orders?
3. Show each employee's hire **year** only.
4. Show `ship_date`, but display `'Not shipped'` when it's NULL.

<details><summary>Show answers</summary>

```sql
SELECT LOWER(TRIM(email)) AS clean_email FROM customers;
```
```sql
SELECT o.order_id, julianday(o.order_date) - julianday(c.signup_date) AS days_after_signup
FROM orders o JOIN customers c ON c.customer_id = o.customer_id
WHERE c.customer_id = 1;
```
```sql
SELECT full_name, strftime('%Y', hire_date) AS hire_year FROM employees;
```
```sql
SELECT order_id, COALESCE(ship_date, 'Not shipped') AS ship_date FROM orders;
```
</details>

---

## 8. CASE WHEN

**`CASE`** is SQL's if/then/else. It checks conditions **from top to bottom** and returns
the value for the **first** one that's true. If none are true, it returns the `ELSE` value.
If there's no `ELSE`, it returns NULL.

```text
CASE
    WHEN condition1 THEN result1
    WHEN condition2 THEN result2
    ELSE fallback
END
```

There's also a short form for simple equality checks: `CASE status WHEN 'completed' THEN 1 WHEN 'returned' THEN -1 ELSE 0 END`.

```sql
SELECT product_name, unit_price,
       CASE
           WHEN unit_price >= 500 THEN 'Premium'
           WHEN unit_price >= 100 THEN 'Mid'
           ELSE 'Budget'
       END AS price_tier
FROM products
ORDER BY unit_price DESC
LIMIT 6;
```
**Result:**

| product_name | unit_price | price_tier |
|---|---|---|
| Laptop Pro 14 | 1299 | Premium |
| Laptop Air 13 | 999 | Premium |
| VR Headset | 699 | Premium |
| Tablet 11 | 549 | Premium |
| Standing Desk | 499 | Mid |
| Ergonomic Chair | 379 | Mid |

*(6 rows)*

⚠️ Order matters. If you put `WHEN unit_price >= 100` first, the $1,299 laptop would be labelled
"Mid", because that's the first condition it matches.

### CASE inside an aggregate (conditional aggregation)
This is one of the most useful tricks for a BA. It lets you count or sum *only some rows* inside
a single `GROUP BY`. That's how you pivot rows into columns:
```sql
SELECT segment,
       COUNT(*)                                                AS customers,
       SUM(CASE WHEN acquisition_channel = 'Organic' THEN 1 ELSE 0 END) AS organic,
       SUM(CASE WHEN acquisition_channel = 'Paid Search' THEN 1 ELSE 0 END) AS paid_search
FROM customers
GROUP BY segment;
```
**Result:**

| segment | customers | organic | paid_search |
|---|---|---|---|
| Consumer | 49 | 12 | 14 |
| Enterprise | 13 | 1 | 4 |
| SMB | 28 | 5 | 10 |

*(3 rows)*

### Practice 8
1. Label each order `'Shipped'`, `'Not shipped'` or `'Cancelled'`, using `status` and `ship_date`.
2. Tag each customer `'Early'` if they signed up before 2024, otherwise `'Recent'`.
3. In one query, count how many orders are completed, cancelled and returned, as three columns.

<details><summary>Show answers</summary>

```sql
SELECT order_id,
       CASE WHEN status = 'cancelled'   THEN 'Cancelled'
            WHEN ship_date IS NOT NULL THEN 'Shipped'
            ELSE 'Not shipped' END AS ship_state
FROM orders;
```
```sql
SELECT first_name, signup_date,
       CASE WHEN signup_date < '2024-01-01' THEN 'Early' ELSE 'Recent' END AS cohort
FROM customers;
```
```sql
SELECT SUM(CASE WHEN status = 'completed' THEN 1 ELSE 0 END) AS completed,
       SUM(CASE WHEN status = 'cancelled' THEN 1 ELSE 0 END) AS cancelled,
       SUM(CASE WHEN status = 'returned'  THEN 1 ELSE 0 END) AS returned
FROM orders;
```
</details>

---

## 9. Aggregate functions

An **aggregate** function turns **many rows into one value**.

| Function | Meaning | NULL handling |
|---|---|---|
| `COUNT(*)` | number of **rows** | counts every row |
| `COUNT(col)` | number of rows where `col` **is not NULL** | skips NULLs |
| `COUNT(DISTINCT col)` | number of **different** values, not counting NULL | skips NULLs |
| `SUM(col)` | total | skips NULLs. If every value is NULL, the result is NULL, not 0 |
| `AVG(col)` | average (mean) | skips NULLs, so NULLs are *not* counted as 0 |
| `MIN(col)` / `MAX(col)` | smallest or largest. Works for numbers, dates and text | skips NULLs |
| `GROUP_CONCAT(col, ',')` | joins the values into one text string (PostgreSQL: `STRING_AGG`) | skips NULLs |

```sql
SELECT COUNT(*)              AS all_rows,
       COUNT(email)          AS with_email,
       COUNT(DISTINCT city)  AS distinct_cities,
       MIN(signup_date)      AS first_signup,
       MAX(signup_date)      AS last_signup
FROM customers;
```
**Result:**

| all_rows | with_email | distinct_cities | first_signup | last_signup |
|---|---|---|---|---|
| 90 | 87 | 14 | 2023-09-02 | 2025-05-14 |

*(1 row)*

Notice `all_rows` ≠ `with_email`. The difference is the customers with a NULL email.

```sql
SELECT ROUND(SUM(quantity * unit_price * (1 - discount)), 2) AS gross_sales,
       ROUND(AVG(discount) * 100, 1)                          AS avg_discount_pct,
       MAX(quantity)                                          AS biggest_line_qty
FROM order_items;
```
**Result:**

| gross_sales | avg_discount_pct | biggest_line_qty |
|---|---|---|
| 724,789.78 | 4.8 | 12 |

*(1 row)*

⚠️ Without `GROUP BY`, an aggregate query returns **exactly one row**. You can't mix an
aggregate with a plain column (for example `SELECT city, COUNT(*) FROM customers`) unless you
group by that column. SQLite allows it and returns an arbitrary city, which is misleading.

### Practice 9
1. How many products are there, and what's the average list price?
2. How many **distinct customers** have placed an order?
3. What's the earliest and latest `order_date`?
4. What's the total quantity sold across all order lines?

<details><summary>Show answers</summary>

```sql
SELECT COUNT(*) AS products, ROUND(AVG(unit_price), 2) AS avg_price FROM products;
```
```sql
SELECT COUNT(DISTINCT customer_id) FROM orders;
```
```sql
SELECT MIN(order_date), MAX(order_date) FROM orders;
```
```sql
SELECT SUM(quantity) FROM order_items;
```
</details>

---

## 10. GROUP BY and HAVING

**`GROUP BY`** splits the rows into groups that share the same values, then runs the aggregates
**once per group**. The result has **one row per group**.

**The golden rule:** every column in `SELECT` must either appear in `GROUP BY` or be inside an
aggregate function.

**`HAVING`** filters **groups** after aggregation. **`WHERE`** filters **rows** before it.

| | `WHERE` | `HAVING` |
|---|---|---|
| Runs | before grouping | after grouping |
| Filters | individual rows | whole groups |
| Can use aggregates like `COUNT(*)`? | ❌ | ✅ |

```sql
SELECT category,
       COUNT(*)                  AS products,
       ROUND(AVG(unit_price), 2) AS avg_price
FROM products
WHERE launch_date < '2025-01-01'    -- row filter: drop products launched in 2025
GROUP BY category
HAVING COUNT(*) >= 4                -- group filter: keep categories with 4+ products
ORDER BY avg_price DESC;
```
**Result:**

| category | products | avg_price |
|---|---|---|
| Electronics | 5 | 661 |
| Furniture | 4 | 253 |
| Accessories | 5 | 62.2 |
| Office | 4 | 55.25 |

*(4 rows)*

You can group by **several columns**, which gives one row per combination. You can also group
by **an expression**, for example a month:
```sql
SELECT strftime('%Y', order_date) AS year,
       status,
       COUNT(*) AS orders
FROM orders
GROUP BY year, status
ORDER BY year, orders DESC;
```
**Result:**

| year | status | orders |
|---|---|---|
| 2024 | completed | 354 |
| 2024 | returned | 26 |
| 2024 | cancelled | 24 |
| 2025 | completed | 222 |
| 2025 | returned | 22 |
| 2025 | cancelled | 13 |

*(6 rows)*

### Practice 10
1. How many customers are there per region_id?
2. For each customer, count their orders. Show only customers with 15 or more orders.
3. How many orders were placed per month in 2025?
4. For each product_id, what's the total quantity sold? Show the top 5.

<details><summary>Show answers</summary>

```sql
SELECT region_id, COUNT(*) AS customers FROM customers GROUP BY region_id;
```
```sql
SELECT customer_id, COUNT(*) AS orders FROM orders
GROUP BY customer_id HAVING COUNT(*) >= 15 ORDER BY orders DESC;
```
```sql
SELECT strftime('%Y-%m', order_date) AS month, COUNT(*) AS orders
FROM orders WHERE order_date >= '2025-01-01' GROUP BY month ORDER BY month;
```
```sql
SELECT product_id, SUM(quantity) AS units FROM order_items
GROUP BY product_id ORDER BY units DESC LIMIT 5;
```
</details>

---
## 11. JOINs

A **JOIN** puts columns from two tables side by side, matching rows by a condition in `ON`.
The condition is usually "this table's foreign key = that table's primary key".

```text
SELECT ...
FROM left_table  AS l
JOIN right_table AS r ON r.key = l.key
```

### Join types
| Join | Keeps | Use it when |
|---|---|---|
| `INNER JOIN` (or just `JOIN`) | only rows that **match in both** tables | you only want records that have a partner |
| `LEFT JOIN` | **every row from the left** table, plus matches. Where nothing matches, the right side's columns are NULL | "all customers, **even those without orders**" |
| `RIGHT JOIN` | the mirror image of LEFT. Rarely used, because you can swap the tables and use LEFT | |
| `FULL OUTER JOIN` | every row from **both** tables, with NULLs where there's no match | reconciling two lists |
| `CROSS JOIN` | **every combination**: rows × rows | building a grid, such as every region × every month |
| self join | a table joined to **itself**, using two aliases | employee → manager |

Picture it with Venn diagrams. INNER is the overlap. LEFT is the whole left circle.
FULL is both circles.

```sql
-- INNER: each order next to its customer's name
SELECT o.order_id, o.order_date, c.first_name, c.last_name
FROM orders AS o
INNER JOIN customers AS c ON c.customer_id = o.customer_id
LIMIT 5;
```
**Result:**

| order_id | order_date | first_name | last_name |
|---|---|---|---|
| 1001 | 2024-01-28 | Olivia | Kim |
| 1002 | 2024-01-30 | Sophia | Johnson |
| 1003 | 2024-01-02 | Mateo | Singh |
| 1004 | 2024-01-08 | Lucas | Lee |
| 1005 | 2024-01-07 | James | Nguyen |

*(5 rows)*

`o.` and `c.` say **which table** a column comes from. They're required when both tables have
a column with the same name, such as `customer_id`.

### Joining 3 or more tables
Chain the joins. Each `ON` connects the new table to one that's already joined.
```sql
SELECT o.order_id, c.first_name, r.region_name, p.product_name, oi.quantity
FROM orders o
JOIN customers   c  ON c.customer_id = o.customer_id
JOIN regions     r  ON r.region_id   = c.region_id
JOIN order_items oi ON oi.order_id   = o.order_id
JOIN products    p  ON p.product_id  = oi.product_id
LIMIT 5;
```
**Result:**

| order_id | first_name | region_name | product_name | quantity |
|---|---|---|---|---|
| 1001 | Olivia | North | Printer Paper (Box) | 1 |
| 1001 | Olivia | North | Pen Set | 2 |
| 1002 | Sophia | West | Monitor 27in | 3 |
| 1002 | Sophia | West | Wireless Earbuds | 1 |
| 1003 | Mateo | East | Wireless Earbuds | 1 |

*(5 rows)*

### LEFT JOIN and the anti-join ("which ones have no match?")
```sql
SELECT c.customer_id, c.first_name, o.order_id
FROM customers c
LEFT JOIN orders o ON o.customer_id = c.customer_id
WHERE o.order_id IS NULL          -- no match, so this customer never ordered
LIMIT 5;
```
**Result:**

| customer_id | first_name | order_id |
|---|---|---|
| 4 | Sophia | NULL |
| 5 | Grace | NULL |
| 12 | Arjun | NULL |
| 18 | Amelia | NULL |
| 19 | James | NULL |

*(5 rows)*

### ⚠️ Filtering in ON vs in WHERE (with LEFT JOIN)
- A condition in **`ON`** controls *which rows get matched*. The left rows are always kept.
- A condition in **`WHERE`** runs *after* the join, and removes rows whose right-side columns are NULL.
  This quietly turns your LEFT JOIN into an INNER JOIN.

```sql
-- Keeps every Sales Rep. Reps with no completed orders show 0
SELECT e.full_name, COUNT(o.order_id) AS completed_orders
FROM employees e
LEFT JOIN orders o ON o.employee_id = e.employee_id AND o.status = 'completed'
WHERE e.title = 'Sales Rep'
GROUP BY e.full_name
ORDER BY completed_orders
LIMIT 3;
```
**Result:**

| full_name | completed_orders |
|---|---|
| Sam Ortiz | 0 |
| Chloe Martin | 33 |
| Sofia Romano | 37 |

*(3 rows)*
If you moved `o.status = 'completed'` into `WHERE`, Sam Ortiz (who has no orders) would disappear.

### Self join
```sql
SELECT e.full_name AS employee, m.full_name AS manager
FROM employees e
LEFT JOIN employees m ON m.employee_id = e.manager_id
LIMIT 5;
```
**Result:**

| employee | manager |
|---|---|
| Morgan Blake | NULL |
| Priya Shah | Morgan Blake |
| Daniel Cho | Priya Shah |
| Rosa Alvarez | Priya Shah |
| Tom Becker | Priya Shah |

*(5 rows)*

### CROSS JOIN
```sql
SELECT r.region_name, s.segment
FROM regions r
CROSS JOIN (SELECT DISTINCT segment FROM customers) s
ORDER BY r.region_name, s.segment
LIMIT 6;
```
**Result:**

| region_name | segment |
|---|---|
| East | Consumer |
| East | Enterprise |
| East | SMB |
| North | Consumer |
| North | Enterprise |
| North | SMB |

*(6 rows)*

### `USING` shortcut
When both columns have the **same name**, `JOIN orders USING (customer_id)` means the same as
`ON orders.customer_id = customers.customer_id`.

### ⚠️ Join fan-out (the #1 cause of inflated numbers)
Joining `orders` (one row per order) to `order_items` (many rows per order) **repeats each
order once per item**. `COUNT(*)` then counts items, not orders, and summing an order-level
value adds it up several times. The fix is `COUNT(DISTINCT o.order_id)`, or aggregate the
items first and then join.
```sql
SELECT COUNT(*)                   AS rows_after_join,
       COUNT(DISTINCT o.order_id) AS real_orders
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id;
```
**Result:**

| rows_after_join | real_orders |
|---|---|
| 1280 | 659 |

*(1 row)*

### Practice 11
1. List every order with the name of the sales rep who handled it. Online orders have no rep, so show `'Online'` for them.
2. Show revenue (`quantity * unit_price * (1 - discount)`) by product category, for completed orders only.
3. Which products have **never** been ordered? Use a LEFT JOIN.
4. List every employee whose manager is a `'Regional Sales Manager'`.

<details><summary>Show answers</summary>

```sql
SELECT o.order_id, COALESCE(e.full_name, 'Online') AS handled_by
FROM orders o
LEFT JOIN employees e ON e.employee_id = o.employee_id;
```
```sql
SELECT p.category, ROUND(SUM(oi.quantity * oi.unit_price * (1 - oi.discount)), 2) AS revenue
FROM order_items oi
JOIN orders o   ON o.order_id = oi.order_id
JOIN products p ON p.product_id = oi.product_id
WHERE o.status = 'completed'
GROUP BY p.category
ORDER BY revenue DESC;
```
```sql
SELECT p.product_name
FROM products p
LEFT JOIN order_items oi ON oi.product_id = p.product_id
WHERE oi.order_item_id IS NULL;
```
```sql
SELECT e.full_name, m.full_name AS manager
FROM employees e
JOIN employees m ON m.employee_id = e.manager_id
WHERE m.title = 'Regional Sales Manager';
```
</details>

---

## 12. Set operators

A **JOIN** adds columns side by side. **Set operators** stack results **on top of each other**,
adding rows. Both queries must return the **same number of columns**, with compatible types.

| Operator | Meaning |
|---|---|
| `UNION` | rows from both queries, **with duplicates removed** (slower) |
| `UNION ALL` | rows from both queries, **keeping duplicates** (faster). Use this by default |
| `INTERSECT` | rows that appear in **both** queries |
| `EXCEPT` (Oracle: `MINUS`) | rows in the first query that are **not** in the second |

```sql
SELECT 'customer' AS person_type, first_name || ' ' || last_name AS name FROM customers WHERE customer_id <= 2
UNION ALL
SELECT 'employee', full_name FROM employees WHERE employee_id <= 2;
```
**Result:**

| person_type | name |
|---|---|
| customer | Lucas Smith |
| customer | Noah Smith |
| employee | Morgan Blake |
| employee | Priya Shah |

*(4 rows)*

```sql
-- Customers who ordered in 2024 but not in 2025
SELECT customer_id FROM orders WHERE order_date <  '2025-01-01'
EXCEPT
SELECT customer_id FROM orders WHERE order_date >= '2025-01-01'
LIMIT 5;
```
**Result:**

| customer_id |
|---|
| 10 |
| 14 |
| 21 |
| 36 |
| 41 |

*(5 rows)*

### Practice 12
1. Which customer_ids ordered in **both** 2024 and 2025?
2. Build one list of every city in `customers` together with every `region_name`, with no duplicates.

<details><summary>Show answers</summary>

```sql
SELECT customer_id FROM orders WHERE order_date <  '2025-01-01'
INTERSECT
SELECT customer_id FROM orders WHERE order_date >= '2025-01-01';
```
```sql
SELECT city FROM customers WHERE city IS NOT NULL
UNION
SELECT region_name FROM regions;
```
</details>

---

## 13. Subqueries

A **subquery** is a `SELECT` in parentheses, used inside another query. Where you put it
decides what it must return:

| Where | Must return | Example |
|---|---|---|
| `WHERE x > (subquery)` | **one value** (a scalar subquery) | above-average prices |
| `WHERE x IN (subquery)` | **one column**, any number of rows | customers who bought X |
| `WHERE EXISTS (subquery)` | anything. It only checks whether **at least one row** comes back | has at least one order |
| `FROM (subquery) AS t` | a table (called a derived table), which **must** have an alias | aggregate, then filter |
| in `SELECT` | one value per row | a "total" column |

```sql
-- Scalar subquery: products above the average price
SELECT product_name, unit_price
FROM products
WHERE unit_price > (SELECT AVG(unit_price) FROM products)
ORDER BY unit_price DESC;
```
**Result:**

| product_name | unit_price |
|---|---|
| Laptop Pro 14 | 1299 |
| Laptop Air 13 | 999 |
| VR Headset | 699 |
| Tablet 11 | 549 |
| Standing Desk | 499 |
| Ergonomic Chair | 379 |
| Monitor 27in | 329 |

*(7 rows)*

```sql
-- IN subquery: customers who have ordered a Standing Desk
SELECT first_name, last_name
FROM customers
WHERE customer_id IN (
    SELECT o.customer_id
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE oi.product_id = 11
)
LIMIT 5;
```
**Result:**

| first_name | last_name |
|---|---|
| Amelia | Hall |
| Abigail | Brown |
| Amelia | Singh |
| Ethan | Khan |
| Evelyn | King |

*(5 rows)*

### Correlated subqueries
A **correlated** subquery refers to the **outer** row, so it's re-run for each row.
```sql
-- Each product compared with its own category's average price
SELECT p.product_name, p.category, p.unit_price,
       (SELECT ROUND(AVG(p2.unit_price), 2)
        FROM products p2
        WHERE p2.category = p.category) AS category_avg
FROM products p
LIMIT 5;
```
**Result:**

| product_name | category | unit_price | category_avg |
|---|---|---|---|
| Laptop Pro 14 | Electronics | 1299 | 667.33 |
| Laptop Air 13 | Electronics | 999 | 667.33 |
| Monitor 27in | Electronics | 329 | 667.33 |
| Tablet 11 | Electronics | 549 | 667.33 |
| Wireless Earbuds | Electronics | 129 | 667.33 |

*(5 rows)*

### EXISTS / NOT EXISTS
`EXISTS (...)` is true as soon as the subquery finds one row. It's usually written with `SELECT 1`, because the columns don't matter.
```sql
SELECT c.customer_id, c.first_name
FROM customers c
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.customer_id = c.customer_id)
LIMIT 5;
```
**Result:**

| customer_id | first_name |
|---|---|
| 4 | Sophia |
| 5 | Grace |
| 12 | Arjun |
| 18 | Amelia |
| 19 | James |

*(5 rows)*

### ⚠️ The `NOT IN` + NULL trap
If the subquery returns **any NULL**, `x NOT IN (subquery)` returns **no rows at all**.
That's because "x is not equal to NULL" is unknown, not true. Use `NOT EXISTS` instead, or
add `WHERE col IS NOT NULL` inside the subquery.
```sql
-- employee_id in orders contains NULLs, so this returns 0 rows
SELECT COUNT(*) AS not_in_result
FROM employees
WHERE employee_id NOT IN (SELECT employee_id FROM orders);
```
**Result:**

| not_in_result |
|---|
| 0 |

*(1 row)*
```sql
-- This correctly finds employees who never handled an order
SELECT COUNT(*) AS not_exists_result
FROM employees e
WHERE NOT EXISTS (SELECT 1 FROM orders o WHERE o.employee_id = e.employee_id);
```
**Result:**

| not_exists_result |
|---|
| 7 |

*(1 row)*

### Derived table (a subquery in FROM)
```sql
SELECT size, COUNT(*) AS orders
FROM (
    SELECT order_id,
           CASE WHEN SUM(quantity) >= 10 THEN 'Bulk' ELSE 'Normal' END AS size
    FROM order_items
    GROUP BY order_id
) AS t
GROUP BY size;
```
**Result:**

| size | orders |
|---|---|
| Bulk | 134 |
| Normal | 525 |

*(2 rows)*

### Practice 13
1. Which employees earn more than the average salary?
2. Which customers have placed at least one order handled by employee 9 (use `IN`)?
3. Using `EXISTS`, which products have been sold with a 20% discount at least once?
4. What's the average **number of orders per customer**? (Count per customer in a derived table, then average those counts.)

<details><summary>Show answers</summary>

```sql
SELECT full_name, salary FROM employees
WHERE salary > (SELECT AVG(salary) FROM employees);
```
```sql
SELECT * FROM customers
WHERE customer_id IN (SELECT customer_id FROM orders WHERE employee_id = 9);
```
```sql
SELECT p.product_name FROM products p
WHERE EXISTS (SELECT 1 FROM order_items oi WHERE oi.product_id = p.product_id AND oi.discount = 0.20);
```
```sql
SELECT ROUND(AVG(n), 2) AS avg_orders_per_customer
FROM (SELECT customer_id, COUNT(*) AS n FROM orders GROUP BY customer_id) t;
```
</details>

---

## 14. CTEs (WITH)

A **CTE** (Common Table Expression) gives a subquery a **name**, placed at the top of the query.
The query then reads like a list of steps. It's the BA's best tool for keeping complex queries readable.

```text
WITH step1 AS (
    SELECT ...
),
step2 AS (
    SELECT ... FROM step1 ...     -- a later CTE can use an earlier one
)
SELECT ... FROM step2;
```

- Separate multiple CTEs with **commas**. Write `WITH` only once.
- A CTE only exists for **this one statement**.
- Anything a CTE does, a derived table can do too. CTEs are just easier to read and can be reused within the query.

```sql
WITH order_value AS (             -- step 1: one row per order, with its value
    SELECT o.order_id, o.customer_id,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS value
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY o.order_id, o.customer_id
),
customer_value AS (               -- step 2: one row per customer
    SELECT customer_id, COUNT(*) AS orders, SUM(value) AS revenue
    FROM order_value
    GROUP BY customer_id
)
SELECT c.first_name, c.last_name, cv.orders, ROUND(cv.revenue, 2) AS revenue,
       ROUND(cv.revenue / cv.orders, 2) AS aov
FROM customer_value cv
JOIN customers c ON c.customer_id = cv.customer_id
ORDER BY cv.revenue DESC
LIMIT 5;
```
**Result:**

| first_name | last_name | orders | revenue | aov |
|---|---|---|---|---|
| Sophia | Nguyen | 38 | 113,298.36 | 2,981.54 |
| James | Garcia | 18 | 69,291.07 | 3,849.5 |
| Aisha | Hall | 11 | 42,587.64 | 3,871.6 |
| Evelyn | Rossi | 12 | 36,634.59 | 3,052.88 |
| Ravi | Khan | 8 | 33,689.15 | 4,211.14 |

*(5 rows)*

### Recursive CTE
`WITH RECURSIVE` lets a CTE refer to **itself**. You write a starting query, then
`UNION ALL`, then a step that builds on the previous rows. It's used for hierarchies (org
charts) and for generating series such as dates.
```sql
WITH RECURSIVE months(m) AS (
    SELECT '2025-01-01'                 -- starting row
    UNION ALL
    SELECT date(m, '+1 month')          -- step, repeated...
    FROM months
    WHERE m < '2025-06-01'              -- ...until this stops being true
)
SELECT m AS month_start FROM months;
```
**Result:**

| month_start |
|---|
| 2025-01-01 |
| 2025-02-01 |
| 2025-03-01 |
| 2025-04-01 |
| 2025-05-01 |
| 2025-06-01 |

*(6 rows)*

### Practice 14
1. Using a CTE, calculate the revenue for each region, then show only regions above the average region revenue.
2. With a recursive CTE, generate the numbers 1 to 10.

<details><summary>Show answers</summary>

```sql
WITH region_rev AS (
    SELECT c.region_id, SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN customers c    ON c.customer_id = o.customer_id
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed'
    GROUP BY c.region_id
)
SELECT * FROM region_rev
WHERE revenue > (SELECT AVG(revenue) FROM region_rev);
```
```sql
WITH RECURSIVE n(x) AS (SELECT 1 UNION ALL SELECT x + 1 FROM n WHERE x < 10)
SELECT x FROM n;
```
</details>

---
## 15. Window functions

A **window function** calculates across a set of related rows (the "window"), but unlike
`GROUP BY` it **keeps every row**. Think of it as "add a column holding a group total or a
rank, without collapsing the rows".

```text
function_name(...) OVER (
    PARTITION BY col      -- optional: restart the calculation for each group
    ORDER BY col          -- optional: the order inside each group (needed for ranks, LAG, running totals)
    ROWS BETWEEN ...      -- optional: the frame, i.e. which nearby rows to include
)
```

| Part | Meaning |
|---|---|
| `OVER ()` | the window is the **whole result** |
| `PARTITION BY x` | a separate window for each value of x. It's like GROUP BY, but the rows are not collapsed |
| `ORDER BY y` inside `OVER` | order within the window. Adding it makes `SUM`/`AVG` **running** (cumulative) |
| `ROWS BETWEEN 2 PRECEDING AND CURRENT ROW` | the frame: this row and the 2 rows before it (a moving window) |
| `UNBOUNDED PRECEDING` / `UNBOUNDED FOLLOWING` | from the start of the partition / to the end of it |

### GROUP BY vs window, side by side
```sql
SELECT product_name, category, unit_price,
       ROUND(AVG(unit_price) OVER (PARTITION BY category), 2) AS category_avg,
       ROUND(unit_price - AVG(unit_price) OVER (PARTITION BY category), 2) AS diff_from_avg
FROM products
WHERE category = 'Furniture';
```
**Result:**

| product_name | category | unit_price | category_avg | diff_from_avg |
|---|---|---|---|---|
| Standing Desk | Furniture | 499 | 253 | 246 |
| Ergonomic Chair | Furniture | 379 | 253 | 126 |
| Monitor Arm | Furniture | 89 | 253 | -164 |
| Desk Lamp | Furniture | 45 | 253 | -208 |

*(4 rows)*
Every product row is kept, and each row also gets its category's average.

### Ranking functions
| Function | What it does | Ties (e.g. values 100, 90, 90, 80) |
|---|---|---|
| `ROW_NUMBER()` | 1, 2, 3, ... always unique | 1, 2, 3, 4 (ties are broken arbitrarily) |
| `RANK()` | same value gets the same rank, then **skips** | 1, 2, 2, 4 |
| `DENSE_RANK()` | same value gets the same rank, **no gaps** | 1, 2, 2, 3 |
| `NTILE(n)` | splits the rows into n buckets of nearly equal size (quartiles = 4) | |

```sql
SELECT full_name, salary,
       ROW_NUMBER() OVER (ORDER BY salary DESC) AS row_num,
       RANK()       OVER (ORDER BY salary DESC) AS rnk,
       DENSE_RANK() OVER (ORDER BY salary DESC) AS dense_rnk,
       NTILE(3)     OVER (ORDER BY salary DESC) AS salary_band
FROM employees
LIMIT 8;
```
**Result:**

| full_name | salary | row_num | rnk | dense_rnk | salary_band |
|---|---|---|---|---|---|
| Morgan Blake | 240000 | 1 | 1 | 1 | 1 |
| Priya Shah | 175000 | 2 | 2 | 2 | 1 |
| Tom Becker | 121000 | 3 | 3 | 3 | 1 |
| Nina Petrova | 119000 | 4 | 4 | 4 | 1 |
| Daniel Cho | 118000 | 5 | 5 | 5 | 1 |
| Rosa Alvarez | 115000 | 6 | 6 | 6 | 2 |
| Ben Carter | 72000 | 7 | 7 | 7 | 2 |
| Marcus Reed | 71000 | 8 | 8 | 8 | 2 |

*(8 rows)*

### Top-N per group
You **can't** use a window function in `WHERE`, because `WHERE` runs before the window is
calculated. Instead, calculate the rank in a CTE or subquery, then filter in the outer query:
```sql
WITH ranked AS (
    SELECT category, product_name, unit_price,
           ROW_NUMBER() OVER (PARTITION BY category ORDER BY unit_price DESC) AS rn
    FROM products
)
SELECT category, product_name, unit_price
FROM ranked
WHERE rn = 1;          -- the most expensive product in each category
```
**Result:**

| category | product_name | unit_price |
|---|---|---|
| Accessories | Mechanical Keyboard | 119 |
| Electronics | Laptop Pro 14 | 1299 |
| Furniture | Standing Desk | 499 |
| Office | Label Printer | 149 |
| Software | Cloud Backup 1TB | 119 |

*(5 rows)*

### LAG / LEAD: look at the previous or next row
| Function | Meaning |
|---|---|
| `LAG(col)` | the value of `col` in the **previous** row of the window |
| `LAG(col, n, default)` | n rows back, returning `default` instead of NULL when there's no row |
| `LEAD(col)` | the value in the **next** row |
| `FIRST_VALUE(col)` / `LAST_VALUE(col)` | the first or last value in the window/frame |

```sql
SELECT customer_id, order_id, order_date,
       LAG(order_date)  OVER (PARTITION BY customer_id ORDER BY order_date) AS prev_order,
       LEAD(order_date) OVER (PARTITION BY customer_id ORDER BY order_date) AS next_order
FROM orders
WHERE customer_id = 2
LIMIT 5;
```
**Result:**

| customer_id | order_id | order_date | prev_order | next_order |
|---|---|---|---|---|
| 2 | 1016 | 2024-01-07 | NULL | 2024-02-13 |
| 2 | 1026 | 2024-02-13 | 2024-01-07 | 2024-04-04 |
| 2 | 1087 | 2024-04-04 | 2024-02-13 | 2024-12-02 |
| 2 | 1390 | 2024-12-02 | 2024-04-04 | 2025-01-03 |
| 2 | 1422 | 2025-01-03 | 2024-12-02 | NULL |

*(5 rows)*

### Running totals, moving averages and % of total
```sql
WITH monthly AS (
    SELECT strftime('%Y-%m', o.order_date) AS month,
           SUM(oi.quantity * oi.unit_price * (1 - oi.discount)) AS revenue
    FROM orders o
    JOIN order_items oi ON oi.order_id = o.order_id
    WHERE o.status = 'completed' AND o.order_date >= '2025-01-01'
    GROUP BY month
)
SELECT month,
       ROUND(revenue, 0)                                                              AS revenue,
       ROUND(SUM(revenue) OVER (ORDER BY month), 0)                                   AS running_total,
       ROUND(AVG(revenue) OVER (ORDER BY month ROWS BETWEEN 2 PRECEDING AND CURRENT ROW), 0) AS moving_avg_3m,
       ROUND(100.0 * revenue / SUM(revenue) OVER (), 1)                               AS pct_of_period,
       ROUND(100.0 * (revenue - LAG(revenue) OVER (ORDER BY month)) / LAG(revenue) OVER (ORDER BY month), 1) AS mom_pct
FROM monthly;
```
**Result:**

| month | revenue | running_total | moving_avg_3m | pct_of_period | mom_pct |
|---|---|---|---|---|---|
| 2025-01 | 29,795 | 29,795 | 29,795 | 12.6 | NULL |
| 2025-02 | 26,444 | 56,239 | 28,119 | 11.2 | -11.2 |
| 2025-03 | 47,953 | 104,192 | 34,731 | 20.4 | 81.3 |
| 2025-04 | 54,045 | 158,237 | 42,814 | 22.9 | 12.7 |
| 2025-05 | 35,039 | 193,275 | 45,679 | 14.9 | -35.2 |
| 2025-06 | 42,314 | 235,589 | 43,799 | 18 | 20.8 |

*(6 rows)*

**Tip:** if you use the same window several times, you can name it once:
`... OVER w ... WINDOW w AS (PARTITION BY customer_id ORDER BY order_date)`.

### Practice 15
1. Number each customer's orders 1, 2, 3, ... from oldest to newest.
2. For each employee, show their salary and the average salary for their title.
3. Show the 2 cheapest products in each category.
4. For each order of customer 5, how many days passed since their previous order?
5. Rank regions by number of customers using `DENSE_RANK`.

<details><summary>Show answers</summary>

```sql
SELECT customer_id, order_id, order_date,
       ROW_NUMBER() OVER (PARTITION BY customer_id ORDER BY order_date, order_id) AS order_number
FROM orders;
```
```sql
SELECT full_name, title, salary,
       AVG(salary) OVER (PARTITION BY title) AS title_avg
FROM employees;
```
```sql
SELECT * FROM (
    SELECT category, product_name, unit_price,
           ROW_NUMBER() OVER (PARTITION BY category ORDER BY unit_price) AS rn
    FROM products
) t WHERE rn <= 2;
```
```sql
SELECT order_id, order_date,
       julianday(order_date) - julianday(LAG(order_date) OVER (ORDER BY order_date)) AS days_since_prev
FROM orders WHERE customer_id = 5;
```
```sql
SELECT region_id, COUNT(*) AS customers,
       DENSE_RANK() OVER (ORDER BY COUNT(*) DESC) AS rnk
FROM customers GROUP BY region_id;
```
</details>

---

## 16. DDL and DML

As a BA you'll mostly *read* data. But you'll often need scratch tables, views and small fixes.
- **DDL** (Data Definition Language) changes the *structure*: `CREATE`, `ALTER`, `DROP`.
- **DML** (Data Manipulation Language) changes the *rows*: `INSERT`, `UPDATE`, `DELETE`.

⚠️ These **change the database**. Practise on a copy. Here, `python run.py setup` rebuilds
everything from scratch whenever you need it.

### CREATE TABLE
```sql
CREATE TABLE IF NOT EXISTS targets (
    region_id     INTEGER PRIMARY KEY,               -- unique ID for each row
    target_2025   DECIMAL(10,2) NOT NULL,            -- NOT NULL: a value is required
    owner         VARCHAR(50) DEFAULT 'TBD',         -- DEFAULT: used if no value is given
    FOREIGN KEY (region_id) REFERENCES regions(region_id)  -- must exist in regions
);
```
*Result: statement executed (no rows returned).*

| Keyword | Meaning |
|---|---|
| `PRIMARY KEY` | uniquely identifies each row. It can't be NULL or duplicated |
| `FOREIGN KEY ... REFERENCES` | the value must exist in the other table |
| `NOT NULL` | a value is required |
| `UNIQUE` | no duplicate values allowed |
| `DEFAULT x` | the value used when none is supplied |
| `CHECK (condition)` | the value must pass the condition, e.g. `CHECK (discount BETWEEN 0 AND 1)` |
| `IF NOT EXISTS` / `IF EXISTS` | skips the command instead of throwing an error |

### INSERT: add rows
```sql
INSERT INTO targets (region_id, target_2025, owner) VALUES
    (1, 150000, 'Daniel Cho'),
    (2, 140000, 'Rosa Alvarez'),
    (3, 160000, 'Tom Becker');
INSERT INTO targets (region_id, target_2025) VALUES (4, 155000);   -- owner gets its DEFAULT
SELECT * FROM targets;
```
**Result:**

| region_id | target_2025 | owner |
|---|---|---|
| 1 | 150000 | Daniel Cho |
| 2 | 140000 | Rosa Alvarez |
| 3 | 160000 | Tom Becker |
| 4 | 155000 | TBD |

*(4 rows)*

### UPDATE: change existing rows
```sql
UPDATE targets
SET target_2025 = target_2025 * 1.10,   -- new value, which can be calculated from the old one
    owner = 'Nina Petrova'
WHERE region_id = 4;                    -- ⚠️ without WHERE, EVERY row is updated
SELECT * FROM targets WHERE region_id = 4;
```
**Result:**

| region_id | target_2025 | owner |
|---|---|---|
| 4 | 170500 | Nina Petrova |

*(1 row)*

### DELETE: remove rows
```sql
DELETE FROM targets WHERE region_id = 3;   -- ⚠️ without WHERE, EVERY row is deleted
SELECT COUNT(*) AS remaining FROM targets;
```
**Result:**

| remaining |
|---|
| 3 |

*(1 row)*

**Safety habit:** before any `UPDATE` or `DELETE`, run `SELECT * FROM t WHERE <same condition>`
to check exactly which rows will change.

### ALTER TABLE and DROP TABLE
```sql
ALTER TABLE targets ADD COLUMN notes TEXT;      -- add a column
ALTER TABLE targets RENAME TO region_targets;    -- rename the table
SELECT * FROM region_targets;
```
**Result:**

| region_id | target_2025 | owner | notes |
|---|---|---|---|
| 1 | 150000 | Daniel Cho | NULL |
| 2 | 140000 | Rosa Alvarez | NULL |
| 4 | 170500 | Nina Petrova | NULL |

*(3 rows)*
```sql
DROP TABLE IF EXISTS region_targets;            -- delete the table and all its data
```
*Result: statement executed (no rows returned).*

`TRUNCATE TABLE t` (PostgreSQL/MySQL) removes all rows quickly but keeps the table.
SQLite doesn't have it, so use `DELETE FROM t` there.

### CREATE TABLE AS: save a query's result as a table
```sql
CREATE TEMP TABLE customer_summary AS          -- TEMP: disappears when you disconnect
SELECT customer_id, COUNT(*) AS orders, MAX(order_date) AS last_order
FROM orders
GROUP BY customer_id;
SELECT * FROM customer_summary ORDER BY orders DESC LIMIT 3;
```
**Result:**

| customer_id | orders | last_order |
|---|---|---|
| 40 | 48 | 2025-06-29 |
| 59 | 44 | 2025-06-17 |
| 84 | 44 | 2025-02-04 |

*(3 rows)*

### INSERT ... SELECT
```sql
CREATE TEMP TABLE vip (customer_id INTEGER, reason TEXT);
INSERT INTO vip (customer_id, reason)
SELECT customer_id, 'Many orders' FROM customer_summary WHERE orders >= 20;
SELECT COUNT(*) AS vips FROM vip;
```
**Result:**

| vips |
|---|
| 5 |

*(1 row)*

### VIEW: a saved query
A **view** stores the *query*, not the data. Each time you select from it, it re-runs against
the latest data. BAs use views so everyone shares one definition of a metric such as "revenue".
```sql
CREATE VIEW IF NOT EXISTS v_order_lines AS
SELECT o.order_id, o.order_date, o.customer_id, o.status,
       oi.product_id, oi.quantity,
       oi.quantity * oi.unit_price * (1 - oi.discount) AS line_revenue
FROM orders o
JOIN order_items oi ON oi.order_id = o.order_id;

SELECT status, ROUND(SUM(line_revenue), 2) AS revenue
FROM v_order_lines
GROUP BY status;
```
**Result:**

| status | revenue |
|---|---|
| cancelled | 27,803.8 |
| completed | 644,230.32 |
| returned | 52,755.65 |

*(3 rows)*
```sql
DROP VIEW IF EXISTS v_order_lines;
```
*Result: statement executed (no rows returned).*

### INDEX: make lookups faster
```sql
CREATE INDEX IF NOT EXISTS idx_orders_customer ON orders(customer_id);
```
*Result: statement executed (no rows returned).*
An index works like the index at the back of a book. It speeds up `WHERE`, `JOIN` and
`ORDER BY` on that column, at the cost of slightly slower writes. To see how the database
plans to run a query, put `EXPLAIN QUERY PLAN` (SQLite) or `EXPLAIN` (PostgreSQL/MySQL)
in front of it.

### Transactions: all or nothing
```text
BEGIN;                              -- start
UPDATE ... ;
DELETE ... ;
COMMIT;                             -- save every change
-- or ROLLBACK;                     -- undo every change since BEGIN
```
Use a transaction whenever several changes must succeed or fail together.

### Practice 16
1. Create a temp table `price_changes(product_id, old_price, new_price)`.
2. Insert a row saying product 3 changed from 345.45 to 329.00.
3. Update that row so the new price is 319.00.
4. Create a view `v_completed_orders` that shows only completed orders, then count its rows.

<details><summary>Show answers</summary>

```sql
CREATE TEMP TABLE price_changes (product_id INTEGER, old_price REAL, new_price REAL);
```
```sql
INSERT INTO price_changes VALUES (3, 345.45, 329.00);
```
```sql
UPDATE price_changes SET new_price = 319.00 WHERE product_id = 3;
```
```sql
CREATE TEMP VIEW v_completed_orders AS SELECT * FROM orders WHERE status = 'completed';
SELECT COUNT(*) FROM v_completed_orders;
```
</details>

---

## 17. Checklist

Work through these steps for any business question:

1. **Restate the question with its grain.** For example: "One row per region, with columns region and revenue."
2. **Find the tables.** Which tables hold the columns you need, and which keys link them?
3. **FROM + JOIN.** Start from the table whose grain matches the answer. Use LEFT JOIN when you must keep zero rows.
4. **WHERE.** Apply the business rules: `status = 'completed'`, the date range, and so on.
5. **GROUP BY + aggregates.** Watch for join fan-out, and use `COUNT(DISTINCT ...)` where needed.
6. **HAVING.** Filter on aggregated values.
7. **Window functions.** Add ranks, running totals and % of total. Wrap the query in a CTE if you need to filter on them.
8. **ORDER BY / LIMIT.** Present the result.
9. **Sanity-check it.** Does the row count make sense? Does the total match a simpler query? Look for NULLs and duplicates.
10. **Write the insight.** Say what the number means in one sentence for a manager.

### Which keyword do I need?

| I want to... | Use |
|---|---|
| pick columns | `SELECT` |
| filter rows | `WHERE` (`AND`/`OR`, `IN`, `BETWEEN`, `LIKE`, `IS NULL`) |
| sort / top N | `ORDER BY ... DESC LIMIT n` |
| remove duplicates | `DISTINCT` |
| if/then labels | `CASE WHEN` |
| totals per group | `GROUP BY` + `SUM`/`COUNT`/`AVG` |
| filter on a total | `HAVING` |
| add columns from another table | `JOIN` |
| keep rows with no match | `LEFT JOIN` |
| find rows with no match | `LEFT JOIN ... WHERE right.id IS NULL` or `NOT EXISTS` |
| stack results | `UNION ALL` |
| compare with an overall number | scalar subquery, or `AGG() OVER ()` |
| break a problem into steps | `WITH` (CTE) |
| rank / top N per group | `ROW_NUMBER() OVER (PARTITION BY ... ORDER BY ...)` |
| previous/next row, growth % | `LAG` / `LEAD` |
| running total / moving average | `SUM() OVER (ORDER BY ...)`, `ROWS BETWEEN` |
| fill in missing values | `COALESCE` |
| avoid dividing by zero | `NULLIF(x, 0)` |
| save a reusable query | `CREATE VIEW` |

**Next step:** work through [`exercises.md`](exercises.md) Levels 1–8. Every question there uses
only the syntax in this guide.
