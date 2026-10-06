"""Step 1: Turn raw orders into customer personas.

Reads the e-commerce data from Project 1, builds one feature row per customer,
clusters customers with K-Means, and gives each cluster a readable persona name
based on what makes it different from the average customer.

Outputs:
  data/customer_personas.csv  one row per customer with their persona
  data/personas.json          persona profiles the chatbot's tools read from
Run: python build_personas.py
"""
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).parent
SRC = ROOT.parent / "01-ecommerce-sales-analysis" / "data"
OUT = ROOT / "data"
OUT.mkdir(exist_ok=True)
N_PERSONAS = 5

orders = pd.read_csv(SRC / "orders.csv", parse_dates=["order_date"])
customers = pd.read_csv(SRC / "customers.csv")

# ---- 1. One row of behavioural features per customer -----------------------
snapshot = orders.order_date.max() + pd.Timedelta(days=1)
orders["is_holiday"] = orders.order_date.dt.month.isin([11, 12])
g = orders.groupby("customer_id")
feat = pd.DataFrame({
    "orders": g.size(),
    "total_spend": g.revenue.sum(),
    "avg_order_value": g.revenue.mean(),
    "days_since_last_order": (snapshot - g.order_date.max()).dt.days,
    "avg_discount": g.discount.mean(),
    "return_rate": g.returned.mean(),
    "holiday_share": g.is_holiday.mean(),
})
cat_share = pd.crosstab(orders.customer_id, orders.category, normalize="index")
feat = feat.join(cat_share.add_prefix("share_"))
feat = feat.join(customers.set_index("customer_id")[["region", "acquisition_channel"]])

# ---- 2. Cluster on the numeric behaviour ----------------------------------
cluster_cols = ["orders", "avg_order_value", "days_since_last_order", "avg_discount",
                "return_rate", "holiday_share", "share_Electronics", "share_Fashion",
                "share_Beauty", "share_Home & Kitchen"]
X = StandardScaler().fit_transform(np.log1p(feat[cluster_cols].clip(lower=0)))
feat["cluster"] = KMeans(n_clusters=N_PERSONAS, n_init=20, random_state=7).fit_predict(X)

# ---- 3. Name each cluster from its most distinctive traits ----------------
overall = feat[cluster_cols].mean()
std = feat[cluster_cols].std()

def describe(c: pd.DataFrame) -> tuple[str, str]:
    """Pick a persona name and tagline from the cluster's standout features."""
    z = (c[cluster_cols].mean() - overall) / std
    if z["orders"] > 0.8 and z["days_since_last_order"] < 0:
        return "Loyal Regulars", "Order often and recently; the core of repeat revenue"
    if z["share_Electronics"] > 0.8 and z["avg_order_value"] > 0.5:
        return "Big-Ticket Tech Buyers", "Few, expensive electronics orders; higher return risk"
    if z["avg_discount"] > 0.6 or z["holiday_share"] > 0.8:
        return "Deal & Festive Shoppers", "Buy when discounts or holiday sales are on"
    if z["days_since_last_order"] > 0.6:
        return "Drifting One-Timers", "Bought once or twice, then went quiet"
    top_cat = c[[col for col in feat.columns if col.startswith("share_")]].mean().idxmax()
    return f"Everyday {top_cat.removeprefix('share_')} Shoppers", "Regular, mid-value baskets in one main category"

names = {}
for k, c in feat.groupby("cluster"):
    name, tagline = describe(c)
    while name in [n for n, _ in names.values()]:   # keep names unique
        name += " II"
    names[k] = (name, tagline)
feat["persona"] = feat.cluster.map(lambda k: names[k][0])

# ---- 4. Build persona profiles for the chatbot ------------------------------
total_rev = feat.total_spend.sum()
personas = []
for k, c in feat.groupby("cluster"):
    cust_orders = orders[orders.customer_id.isin(c.index)]
    personas.append({
        "name": names[k][0],
        "tagline": names[k][1],
        "customers": int(len(c)),
        "customer_share_pct": round(100 * len(c) / len(feat), 1),
        "revenue_share_pct": round(100 * c.total_spend.sum() / total_rev, 1),
        "avg_orders": round(c.orders.mean(), 2),
        "avg_order_value": round(c.avg_order_value.mean(), 2),
        "avg_lifetime_spend": round(c.total_spend.mean(), 2),
        "median_days_since_last_order": int(c.days_since_last_order.median()),
        "avg_discount_pct": round(100 * c.avg_discount.mean(), 1),
        "return_rate_pct": round(100 * c.return_rate.mean(), 1),
        "holiday_order_share_pct": round(100 * c.holiday_share.mean(), 1),
        "repeat_rate_pct": round(100 * (c.orders >= 2).mean(), 1),
        "category_mix_pct": (100 * cust_orders.groupby("category").revenue.sum()
                             / cust_orders.revenue.sum()).round(1).sort_values(ascending=False).to_dict(),
        "top_regions_pct": (100 * c.region.value_counts(normalize=True)).round(1).to_dict(),
        "acquisition_channels_pct": (100 * c.acquisition_channel.value_counts(normalize=True)).round(1).to_dict(),
    })
personas.sort(key=lambda p: -p["revenue_share_pct"])

(OUT / "personas.json").write_text(json.dumps({
    "source": "Synthetic e-commerce data from project 01 (2024-2025)",
    "total_customers": int(len(feat)),
    "total_revenue": round(float(total_rev), 2),
    "personas": personas,
}, indent=2))
feat.reset_index().round(3).to_csv(OUT / "customer_personas.csv", index=False)

for p in personas:
    print(f"{p['name']:<28} {p['customers']:>5} customers  {p['revenue_share_pct']:>5}% of revenue  "
          f"AOV ${p['avg_order_value']:>7}  orders {p['avg_orders']}  discount {p['avg_discount_pct']}%  "
          f"returns {p['return_rate_pct']}%")
