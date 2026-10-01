"""Generate a realistic synthetic e-commerce dataset (2024-2025).

Patterns deliberately embedded so the analysis has something real to find:
- Q4 seasonality (Nov/Dec peaks)
- Heavy discounts lift volume but erode margin
- Electronics has high revenue but the highest return rate
- Customers acquired via Referral are more loyal than Paid Social
"""
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(42)
OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

N_CUSTOMERS = 6000
regions = ["North", "South", "East", "West"]
channels = ["Organic Search", "Paid Social", "Referral", "Email", "Marketplace"]
channel_loyalty = {"Organic Search": 1.0, "Paid Social": 0.6, "Referral": 1.6, "Email": 1.3, "Marketplace": 0.8}

signup = pd.to_datetime("2024-01-01") + pd.to_timedelta(rng.integers(0, 700, N_CUSTOMERS), unit="D")
customers = pd.DataFrame({
    "customer_id": [f"C{i:05d}" for i in range(1, N_CUSTOMERS + 1)],
    "signup_date": signup,
    "region": rng.choice(regions, N_CUSTOMERS, p=[0.28, 0.22, 0.30, 0.20]),
    "acquisition_channel": rng.choice(channels, N_CUSTOMERS, p=[0.30, 0.25, 0.12, 0.15, 0.18]),
})

products = pd.DataFrame([
    # category, base price range, unit cost ratio, return rate
    ("Electronics", 120, 600, 0.72, 0.14),
    ("Home & Kitchen", 25, 180, 0.55, 0.06),
    ("Fashion", 20, 140, 0.45, 0.11),
    ("Beauty", 10, 70, 0.40, 0.03),
    ("Sports", 30, 250, 0.58, 0.05),
    ("Books", 8, 40, 0.50, 0.02),
], columns=["category", "price_min", "price_max", "cost_ratio", "return_rate"])
cat_weights = np.array([0.14, 0.22, 0.24, 0.16, 0.12, 0.12])

end = pd.to_datetime("2025-12-31")

rows = []
oid = 100000
for c in customers.itertuples():
    loyalty = channel_loyalty[c.acquisition_channel]
    n_orders = 1 + rng.poisson(1.6 * loyalty)
    # Gap between orders: loyal customers come back sooner
    date = c.signup_date + pd.Timedelta(days=int(rng.integers(0, 20)))
    for _ in range(n_orders):
        if date > end:
            break
        oid += 1
        cat_idx = rng.choice(len(products), p=cat_weights)
        p = products.iloc[cat_idx]
        unit_price = round(rng.uniform(p.price_min, p.price_max), 2)
        qty = int(rng.choice([1, 1, 1, 2, 2, 3]))
        discount = float(rng.choice([0, 0, 0, 0.05, 0.10, 0.15, 0.20, 0.30],
                                    p=[0.3, 0.15, 0.1, 0.12, 0.13, 0.08, 0.07, 0.05]))
        if date.month in (11, 12):  # holiday promos
            discount = max(discount, float(rng.choice([0.10, 0.15, 0.20, 0.30])))
        gross = unit_price * qty
        revenue = round(gross * (1 - discount), 2)
        cost = round(gross * p.cost_ratio, 2)
        returned = rng.random() < p.return_rate * (1.3 if discount >= 0.2 else 1.0)
        rows.append((f"O{oid}", c.customer_id, date.date(), p.category, c.region,
                     qty, unit_price, discount, revenue, cost, int(returned)))
        gap = rng.exponential(120 / loyalty)
        date = date + pd.Timedelta(days=int(gap) + 1)

orders = pd.DataFrame(rows, columns=["order_id", "customer_id", "order_date", "category", "region",
                                     "quantity", "unit_price", "discount", "revenue", "cost", "returned"])

# Inject seasonality by adding extra holiday orders from existing customers
holiday = orders[pd.to_datetime(orders.order_date).dt.month.isin([11, 12])]
extra = holiday.sample(frac=0.6, random_state=1).copy()
extra["order_id"] = [f"O{oid + i + 1}" for i in range(len(extra))]
orders = pd.concat([orders, extra]).sort_values("order_date").reset_index(drop=True)

customers.to_csv(OUT / "customers.csv", index=False)
orders.to_csv(OUT / "orders.csv", index=False)
print(f"customers: {len(customers):,}  orders: {len(orders):,}")
