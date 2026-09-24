# SQL Practice for Business Analysts: Basic to Advanced

This is a practice kit you can run yourself. It has a realistic retail database, **63 questions**
written like stakeholder requests, and a tested reference solution for each one.

| File | What it is |
|---|---|
| [`sql-syntax-guide.md`](sql-syntax-guide.md) | **Start here if you're new.** Explains every keyword and piece of syntax, with real results and practice questions |
| [`exercises.md`](exercises.md) | The questions, from Level 1 (SELECT) to Level 8 (gaps and islands, recursive CTEs) |
| [`solutions.sql`](solutions.sql) | Reference solutions, each tagged `-- Q<level>.<n>` |
| `schema.sql` + `seed.sql` | Portable DDL and data (SQLite / PostgreSQL / MySQL 8) |
| `run.py` | A helper that builds a SQLite DB and runs queries. It needs only Python 3 |
| `generate_seed.py` | Rebuilds `seed.sql` if you want to change the data (deterministic) |

## Quick start (just Python, nothing to install)

```bash
cd sql-practice
python run.py setup                                   # builds practice.db
python run.py query "SELECT * FROM products LIMIT 5"  # ad-hoc query
python run.py file my_answer.sql                      # run your own file
python run.py solution 5.4                            # show + run a reference answer
python run.py check                                   # smoke-test all solutions
```

If you prefer a GUI, open `practice.db` in **DB Browser for SQLite**, **DBeaver** or the
VS Code *SQLite Viewer* extension.

**PostgreSQL / MySQL:** run `schema.sql` and then `seed.sql`. Most solutions work unchanged.
Swap in the date functions from the table below.

## What each level covers

| Level | Topic | Skills |
|---|---|---|
| 1 | Retrieving and filtering | `SELECT`, `WHERE`, `ORDER BY`, `LIMIT`, `DISTINCT`, `IN`, `BETWEEN`, `LIKE`, `IS NULL` |
| 2 | Aggregation | `COUNT/SUM/AVG/MIN/MAX`, `GROUP BY`, `HAVING`, `COUNT(DISTINCT)`, % of total |
| 3 | Joins | inner / left joins, multi-table joins, self-joins, anti-joins, "keep the zeros" |
| 4 | Subqueries, CTEs, CASE | scalar / correlated subqueries, `EXISTS`, `WITH`, bucketing, pivots |
| 5 | Window functions | `ROW_NUMBER`, `RANK`, `NTILE`, `LAG`, running totals, moving averages, top-N per group |
| 6 | Business case studies | new vs returning, cohort retention, funnels, RFM, Pareto, CAC, churn, YoY, market basket, median, SLA |
| 7 | Data quality | duplicates, NULLs, messy text, orphan records, dedupe with `ROW_NUMBER` |
| 8 | Stretch | gaps and islands, price-change detection, event timing, recursive CTEs |

The data contains **deliberate problems** for Level 7 to find: duplicate and missing emails,
messy city names, orders without line items, and ship dates before order dates.

## Dialect cheat sheet

| Task | SQLite (used here) | PostgreSQL | MySQL 8 |
|---|---|---|---|
| Year-month label | `strftime('%Y-%m', d)` | `to_char(d, 'YYYY-MM')` | `DATE_FORMAT(d, '%Y-%m')` |
| First of month | `date(d, 'start of month')` | `date_trunc('month', d)` | `DATE_FORMAT(d, '%Y-%m-01')` |
| Days between | `julianday(b) - julianday(a)` | `b::date - a::date` | `DATEDIFF(b, a)` |
| Add days | `date(d, '+7 days')` | `d + INTERVAL '7 days'` | `DATE_ADD(d, INTERVAL 7 DAY)` |
| Concatenate | `a \|\| b` | `a \|\| b` | `CONCAT(a, b)` |
| List aggregate | `GROUP_CONCAT(x)` | `STRING_AGG(x::text, ',')` | `GROUP_CONCAT(x)` |
| Median | window trick (Q6.11) | `PERCENTILE_CONT(0.5) WITHIN GROUP (ORDER BY x)` | window trick |
| Integer division | `5 / 2 = 2`, so use `* 1.0` or `100.0 *` | same | `5 / 2 = 2.5` |

## How to practise

1. Read the question and say out loud what one output row represents (its *grain*).
2. Write the query and check the row count makes sense.
3. Compare it with `python run.py solution <n>`. A different query with the same result is still right.
4. Write **one sentence of insight** for a non-technical manager.

Common mistakes to watch for: forgetting `status = 'completed'`; counting rows twice after a
join (count `DISTINCT order_id`); putting a LEFT JOIN filter in `WHERE` instead of `ON`; and
integer division.
