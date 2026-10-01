"""Generate a synthetic subscription (telecom/SaaS-style) customer base with churn labels.

Churn probability is driven by a known logistic function, so the analysis can be
validated: month-to-month contracts, short tenure, many support tickets, low
usage and electronic-check payments all raise churn risk.
"""
import numpy as np
import pandas as pd
from pathlib import Path

rng = np.random.default_rng(7)
N = 8000
OUT = Path(__file__).parent / "data"
OUT.mkdir(exist_ok=True)

contract = rng.choice(["Month-to-month", "One year", "Two year"], N, p=[0.52, 0.27, 0.21])
plan = rng.choice(["Basic", "Standard", "Premium"], N, p=[0.40, 0.40, 0.20])
base_fee = pd.Series(plan).map({"Basic": 29, "Standard": 59, "Premium": 99}).to_numpy()
monthly_charge = np.round(base_fee + rng.normal(0, 6, N), 2)
tenure = np.where(contract == "Month-to-month", rng.integers(1, 40, N),
         np.where(contract == "One year", rng.integers(6, 60, N), rng.integers(12, 72, N)))
payment = rng.choice(["Credit card", "Bank transfer", "Electronic check", "PayPal"], N,
                     p=[0.32, 0.24, 0.26, 0.18])
tickets = rng.poisson(1.2, N) + (rng.random(N) < 0.15) * rng.poisson(3, N)
usage_hrs = np.clip(rng.normal(32, 12, N), 1, None).round(1)
onboarding = rng.random(N) < 0.45
region = rng.choice(["North", "South", "East", "West"], N)

logit = (-2.3
         + 1.5 * (contract == "Month-to-month") + 0.35 * (contract == "One year")
         - 0.035 * tenure
         + 0.38 * tickets
         - 0.03 * (usage_hrs - 32)
         + 0.55 * (payment == "Electronic check")
         + 0.010 * (monthly_charge - 55)
         - 0.6 * onboarding)
churn = rng.random(N) < 1 / (1 + np.exp(-logit))

df = pd.DataFrame({
    "customer_id": [f"S{i:05d}" for i in range(1, N + 1)],
    "region": region, "plan": plan, "contract": contract, "payment_method": payment,
    "tenure_months": tenure, "monthly_charge": monthly_charge,
    "support_tickets_90d": tickets, "monthly_usage_hours": usage_hrs,
    "completed_onboarding": onboarding.astype(int), "churned": churn.astype(int),
})
df.to_csv(OUT / "subscribers.csv", index=False)
print(f"subscribers: {N:,}  churn rate: {churn.mean():.1%}")
