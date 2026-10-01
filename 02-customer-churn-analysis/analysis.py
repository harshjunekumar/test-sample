"""Customer Churn Analysis & Retention Business Case.

1. Descriptive: churn rate and revenue at risk by segment
2. Diagnostic: which factors drive churn (segment lift + logistic regression)
3. Predictive: score every customer's churn risk
4. Prescriptive: ROI of a targeted retention campaign vs. blanket campaign
Run: python generate_data.py && python analysis.py
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

ROOT = Path(__file__).parent
OUT = ROOT / "outputs"
OUT.mkdir(exist_ok=True)
plt.rcParams.update({"figure.dpi": 130, "axes.spines.top": False, "axes.spines.right": False,
                     "axes.titleweight": "bold", "font.size": 10})
BLUE, GREY, RED = "#2563eb", "#9ca3af", "#dc2626"

df = pd.read_csv(ROOT / "data/subscribers.csv")
overall = df.churned.mean()
df["annual_revenue"] = df.monthly_charge * 12
df["tenure_band"] = pd.cut(df.tenure_months, [0, 6, 12, 24, 48, 72],
                           labels=["0-6m", "7-12m", "13-24m", "25-48m", "49-72m"])
df["ticket_band"] = pd.cut(df.support_tickets_90d, [-1, 0, 2, 4, 100],
                           labels=["0", "1-2", "3-4", "5+"])

# ---- 1. Headline numbers ---------------------------------------------------
lost_rev = df.loc[df.churned == 1, "annual_revenue"].sum()
print(f"Customers: {len(df):,} | churn rate: {overall:.1%} | "
      f"annualised revenue lost: ${lost_rev:,.0f} ({lost_rev / df.annual_revenue.sum():.1%} of base)")

# ---- 2. Segment churn & lift ----------------------------------------------
dims = ["contract", "tenure_band", "ticket_band", "payment_method", "plan",
        "completed_onboarding", "region"]
seg_rows = []
for d in dims:
    g = df.groupby(d, observed=True).agg(customers=("churned", "size"), churn_rate=("churned", "mean"))
    for k, r in g.iterrows():
        seg_rows.append((d, str(k), r.customers, round(100 * r.churn_rate, 1),
                         round(r.churn_rate / overall, 2)))
seg = pd.DataFrame(seg_rows, columns=["dimension", "segment", "customers", "churn_rate_pct", "lift_vs_avg"])
seg.to_csv(OUT / "segment_churn.csv", index=False)
print("\n=== Churn by segment ===\n" + seg.to_string(index=False))

fig, axes = plt.subplots(2, 2, figsize=(11, 7))
for ax, d, title in zip(axes.flat, ["contract", "tenure_band", "ticket_band", "payment_method"],
                        ["Contract type", "Tenure", "Support tickets (90 days)", "Payment method"]):
    s = seg[seg.dimension == d]
    ax.bar(s.segment, s.churn_rate_pct, color=[RED if v > 100 * overall * 1.3 else BLUE for v in s.churn_rate_pct])
    ax.axhline(100 * overall, color=GREY, ls="--", lw=1)
    ax.set_title(f"Churn rate by {title.lower()}")
    ax.set_ylabel("Churn %")
    ax.tick_params(axis="x", rotation=15)
fig.suptitle(f"Where churn concentrates (dashed line = {overall:.1%} average; red = 30%+ above average)",
             fontweight="bold")
fig.tight_layout(); fig.savefig(OUT / "01_churn_by_segment.png"); plt.close(fig)

# ---- 3. Driver model -------------------------------------------------------
features = ["tenure_months", "monthly_charge", "support_tickets_90d", "monthly_usage_hours",
            "completed_onboarding"]
X = pd.get_dummies(df[features + ["contract", "payment_method"]],
                   columns=["contract", "payment_method"], drop_first=False, dtype=float)
X = X.drop(columns=["contract_Two year", "payment_method_Credit card"])  # reference levels
y = df.churned
X_tr, X_te, y_tr, y_te = train_test_split(X, y, test_size=0.3, random_state=0, stratify=y)
scaler = StandardScaler().fit(X_tr)
model = LogisticRegression(max_iter=1000).fit(scaler.transform(X_tr), y_tr)
auc = roc_auc_score(y_te, model.predict_proba(scaler.transform(X_te))[:, 1])
print(f"\nLogistic regression test AUC: {auc:.3f}")

coef = pd.Series(model.coef_[0], index=X.columns).sort_values()
labels = {"tenure_months": "Tenure (months)", "monthly_charge": "Monthly charge",
          "support_tickets_90d": "Support tickets (90d)", "monthly_usage_hours": "Usage hours",
          "completed_onboarding": "Completed onboarding", "contract_Month-to-month": "Month-to-month contract",
          "contract_One year": "One-year contract", "payment_method_Electronic check": "Pays by e-check",
          "payment_method_Bank transfer": "Pays by bank transfer", "payment_method_PayPal": "Pays by PayPal"}
coef.rename(labels).round(3).to_csv(OUT / "churn_drivers.csv", header=["std_coefficient"])
print("\n=== Standardised drivers (+ raises churn) ===\n" + coef.rename(labels).round(3).to_string())

fig, ax = plt.subplots(figsize=(8, 4.5))
ax.barh(coef.rename(labels).index, coef.values, color=[RED if v > 0 else BLUE for v in coef.values])
ax.axvline(0, color="black", lw=0.8)
ax.set_title(f"Churn drivers (standardised logistic coefficients, AUC = {auc:.2f})")
ax.set_xlabel("← reduces churn        raises churn →")
fig.tight_layout(); fig.savefig(OUT / "02_churn_drivers.png"); plt.close(fig)

# ---- 4. Risk scoring & targeting -----------------------------------------
active = df[df.churned == 0].copy()   # customers we can still save
Xa = X.loc[active.index]
active["churn_risk"] = model.predict_proba(scaler.transform(Xa))[:, 1]
active["risk_tier"] = pd.cut(active.churn_risk, [0, 0.15, 0.35, 1], labels=["Low", "Medium", "High"])
tiers = active.groupby("risk_tier", observed=True).agg(
    customers=("customer_id", "size"), avg_risk=("churn_risk", "mean"),
    annual_revenue=("annual_revenue", "sum"))
tiers["expected_revenue_at_risk"] = (active.churn_risk * active.annual_revenue).groupby(
    active.risk_tier, observed=True).sum()
tiers = tiers.round(2)
tiers.to_csv(OUT / "risk_tiers.csv")
active[["customer_id", "plan", "contract", "churn_risk", "risk_tier", "annual_revenue"]] \
    .sort_values("churn_risk", ascending=False).round(3).to_csv(OUT / "customer_risk_scores.csv", index=False)
print("\n=== Active customers by risk tier ===\n" + tiers.to_string())

# ---- 5. Retention campaign business case ----------------------------------
# Assumptions (documented in README): offer costs $60/customer, saves 30% of would-be churners.
COST, SAVE_RATE = 60, 0.30
def campaign(target):
    cost = len(target) * COST
    saved = (target.churn_risk * target.annual_revenue).sum() * SAVE_RATE
    return len(target), cost, saved, saved - cost, (saved - cost) / cost

scen = pd.DataFrame(
    [("Blanket: all active customers", *campaign(active)),
     ("Targeted: High risk only", *campaign(active[active.risk_tier == "High"])),
     ("Targeted: High + Medium risk", *campaign(active[active.risk_tier != "Low"]))],
    columns=["scenario", "customers_contacted", "cost", "revenue_retained", "net_benefit", "roi"])
scen = scen.round(2)
scen.to_csv(OUT / "campaign_scenarios.csv", index=False)
print("\n=== Retention campaign scenarios ===\n" + scen.to_string(index=False))

fig, ax = plt.subplots(figsize=(8, 4))
x = np.arange(len(scen))
ax.bar(x - 0.2, scen.cost / 1000, 0.4, color=GREY, label="Campaign cost")
ax.bar(x + 0.2, scen.revenue_retained / 1000, 0.4, color=BLUE, label="Revenue retained")
for i, r in scen.iterrows():
    ax.text(i, max(r.cost, r.revenue_retained) / 1000 + 3, f"ROI {r.roi:.0%}", ha="center", fontweight="bold")
ax.set_xticks(x, ["Blanket\n(all)", "High risk\nonly", "High + Medium\nrisk"])
ax.set_ylabel("$K (annualised)")
ax.set_title("Retention campaign business case")
ax.legend(frameon=False)
fig.tight_layout(); fig.savefig(OUT / "03_campaign_roi.png"); plt.close(fig)
print("\nOutputs written to", OUT)
