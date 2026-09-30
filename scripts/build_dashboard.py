"""Build the interactive HTML dashboard (dashboard/index.html) from the clean data.

Each call is packed into compact per-column strings so the page can filter all
30,000 rows in the browser without any server.
"""
import json
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
CLEAN = ROOT / "data" / "flipkart_customer_calls_clean.csv"
TEMPLATE = ROOT / "dashboard" / "template.html"
OUT = ROOT / "dashboard" / "index.html"

DIMS = {
    "center": ("call_center", ["Delhi", "Mumbai", "Kolkata", "Chennai"]),
    "channel": ("channel", ["Call-Center", "Chatbot", "Email", "Web"]),
    "reason": ("reason", ["Billing Question", "Payments", "Service Outage"]),
    "sentiment": ("sentiment", ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]),
    "resp": ("response_time", ["Below SLA", "Within SLA", "Above SLA"]),
}


def main():
    df = pd.read_csv(CLEAN, parse_dates=["call_date"])
    packed = {"n": len(df), "labels": {k: v[1] for k, v in DIMS.items()}}
    for key, (col, labels) in DIMS.items():
        idx = {v: str(i) for i, v in enumerate(labels)}
        packed[key] = "".join(df[col].map(idx))
    packed["dur"] = "".join(f"{d:02d}" for d in df["call_duration_min"])
    packed["day"] = "".join(f"{d:02d}" for d in df["call_date"].dt.day)
    # csat: "0" = no rating, "1"-"9", "A" = 10
    packed["csat"] = "".join("0" if pd.isna(c) else ("A" if c == 10 else str(int(c))) for c in df["csat_score"])
    html = TEMPLATE.read_text().replace("/*__DATA__*/null", json.dumps(packed, separators=(",", ":")))
    OUT.write_text(html)
    print("saved", OUT, f"{OUT.stat().st_size/1024:.0f} KB")


if __name__ == "__main__":
    main()
