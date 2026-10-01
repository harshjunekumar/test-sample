"""E-commerce Sales Performance Analysis.

Loads the CSVs into SQLite, runs every query in sql/queries.sql, then adds
Python-side analysis (RFM segmentation, cohort retention) and saves charts.
Run: python generate_data.py && python analysis.py
"""
import re
import sqlite3
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"figure.dpi": 130, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.titleweight": "bold", "font.size": 10})
BLUE, GREY, RED = "#2563eb", "#9ca3af", "#dc2626"

orders = pd.read_csv(ROOT / "data/orders.csv", parse_dates=["order_date"])
customers = pd.read_csv(ROOT / "data/customers.csv", parse_dates=["signup_date"])

con = sqlite3.connect(":memory:")
orders.assign(order_date=orders.order_date.dt.strftime("%Y-%m-%d")).to_sql("orders", con, index=False)
customers.to_sql("customers", con, index=False)

# ---- 1. Run the SQL business questions ------------------------------------
sql = (ROOT / "sql/queries.sql").read_text()
results = {}
for name, body in re.findall(r"-- name: (\w+)\n(.*?)(?=\n-- name:|\Z)", sql, re.S):
    results[name] = pd.read_sql_query(body, con)
    results[name].to_csv(OUT / f"{name}.csv", index=False)
    print(f"\n=== {name} ===\n{results[name].to_string(index=False)}")

# ---- 2. Charts from SQL results -------------------------------------------
m = results["monthly_revenue"]
fig, ax = plt.subplots(figsize=(10, 4))
colors = [RED if mo[-2:] in ("11", "12") else BLUE for mo in m.month]
ax.bar(m.month, m.revenue / 1000, color=colors)
ax.set_title("Monthly revenue ($K) — Q4 holiday months highlighted")
ax.set_ylabel("$K")
ax.tick_params(axis="x", rotation=60)
fig.tight_layout(); fig.savefig(OUT / "01_monthly_revenue.png"); plt.close(fig)

c = results["category_performance"]
fig, ax1 = plt.subplots(figsize=(9, 4))
ax1.bar(c.category, c.revenue / 1000, color=BLUE)
ax1.set_ylabel("Revenue ($K)")
ax2 = ax1.twinx()
ax2.plot(c.category, c.return_rate_pct, color=RED, marker="o", lw=2)
ax2.set_ylabel("Return rate (%)", color=RED)
ax2.spines["top"].set_visible(False)
ax1.set_title("Revenue vs. return rate by category")
fig.tight_layout(); fig.savefig(OUT / "02_category_revenue_returns.png"); plt.close(fig)

d = results["discount_impact"]
fig, ax = plt.subplots(figsize=(7, 4))
ax.bar(d.discount_band, d.margin_pct, color=[BLUE, BLUE, GREY, RED])
for x, y in zip(d.discount_band, d.margin_pct):
    ax.text(x, y + 0.5, f"{y:.1f}%", ha="center")
ax.set_title("Gross margin by discount band")
ax.set_ylabel("Gross margin %")
fig.tight_layout(); fig.savefig(OUT / "03_discount_margin.png"); plt.close(fig)

ch = results["channel_ltv"]
fig, ax = plt.subplots(figsize=(8, 4))
ax.barh(ch.acquisition_channel[::-1], ch.revenue_per_customer[::-1], color=BLUE)
ax.set_title("Revenue per customer by acquisition channel")
ax.set_xlabel("$ per customer")
fig.tight_layout(); fig.savefig(OUT / "04_channel_value.png"); plt.close(fig)

# ---- 3. RFM segmentation ---------------------------------------------------
snapshot = orders.order_date.max() + pd.Timedelta(days=1)
rfm = orders.groupby("customer_id").agg(
    recency=("order_date", lambda s: (snapshot - s.max()).days),
    frequency=("order_id", "count"),
    monetary=("revenue", "sum"))
rfm["R"] = pd.qcut(rfm.recency, 4, labels=[4, 3, 2, 1]).astype(int)
rfm["F"] = pd.qcut(rfm.frequency.rank(method="first"), 4, labels=[1, 2, 3, 4]).astype(int)
rfm["M"] = pd.qcut(rfm.monetary, 4, labels=[1, 2, 3, 4]).astype(int)

def segment(r):
    if r.R >= 3 and r.F >= 3 and r.M >= 3: return "Champions"
    if r.R >= 3 and r.F >= 2:              return "Loyal"
    if r.R >= 3:                           return "New / Promising"
    if r.F >= 3 or r.M >= 3:               return "At Risk (high value)"
    return "Hibernating"

rfm["segment"] = rfm.apply(segment, axis=1)
seg = (rfm.groupby("segment")
          .agg(customers=("monetary", "size"), revenue=("monetary", "sum"),
               avg_recency_days=("recency", "mean"), avg_orders=("frequency", "mean"))
          .sort_values("revenue", ascending=False))
seg["customer_share_pct"] = (100 * seg.customers / seg.customers.sum()).round(1)
seg["revenue_share_pct"] = (100 * seg.revenue / seg.revenue.sum()).round(1)
seg = seg.round(1)
seg.to_csv(OUT / "rfm_segments.csv")
print(f"\n=== RFM segments ===\n{seg.to_string()}")

fig, ax = plt.subplots(figsize=(8, 4))
x = range(len(seg))
ax.bar([i - 0.2 for i in x], seg.customer_share_pct, 0.4, label="% of customers", color=GREY)
ax.bar([i + 0.2 for i in x], seg.revenue_share_pct, 0.4, label="% of revenue", color=BLUE)
ax.set_xticks(list(x), seg.index, rotation=15)
ax.set_title("RFM segments: share of customers vs. share of revenue")
ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(OUT / "05_rfm_segments.png"); plt.close(fig)

# ---- 4. Cohort retention ---------------------------------------------------
o = orders.copy()
o["order_month"] = o.order_date.dt.to_period("M")
o["cohort"] = o.groupby("customer_id").order_month.transform("min")
o["age"] = (o.order_month - o.cohort).apply(lambda p: p.n)
cohort = o.groupby(["cohort", "age"]).customer_id.nunique().unstack(fill_value=0)
retention = cohort.div(cohort[0], axis=0)
# Blank out months that haven't happened yet for recent cohorts
last = o.order_month.max()
for coh in retention.index:
    retention.loc[coh, retention.columns > (last - coh).n] = float("nan")
q = retention.loc[: "2024-12", [1, 3, 6, 12]]
retention.round(3).to_csv(OUT / "cohort_retention.csv")
print(f"\n=== Avg retention (2024 cohorts) at month 1/3/6/12 ===\n{(100 * q.mean()).round(1).to_string()}")

view = retention.loc[: "2025-06", :12]
fig, ax = plt.subplots(figsize=(10, 6))
im = ax.imshow(view.values, cmap=matplotlib.colormaps["Blues"].with_extremes(bad="#f3f4f6"), vmin=0, vmax=0.2, aspect="auto")
ax.set_xticks(range(view.shape[1]), view.columns)
ax.set_yticks(range(view.shape[0]), [str(p) for p in view.index])
ax.set_xlabel("Months since first purchase")
ax.set_title("Monthly cohort retention (month 0 = 100%, scale capped at 20%)")
fig.colorbar(im, ax=ax, format=lambda v, _: f"{v:.0%}")
fig.tight_layout(); fig.savefig(OUT / "06_cohort_retention.png"); plt.close(fig)

print("\nCharts and tables written to", OUT)
