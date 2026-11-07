"""Data preparation for the UK Savoury Snacks case study.

Reads the sales tab ('Name mapping') of the converted source workbook and builds the
summarised 'Data' table used by Savoury_Snacks_Analysis_Workbook.xlsx.

Steps
1. Keep weeks 1-47 of both years (like-for-like: 2025 has data only to week 47).
2. Period: 2025 -> TY, 2024 -> YA.
3. Channel: E-COMMERCE + PURE PLAY = Online; LARGE + SMALL FORMAT = In-store
   ('UNALLOCATED', ~GBP 5.5k over two years, is dropped).
4. Sum value and units by Period x Customer x Store format x Channel x Supplier x Brand
   x Segment x Sub segment x Pack format x Sub pack format (1.01m rows -> ~8.5k rows).

Usage: python prepare_data.py Case_Study_Commercial_Insights.xlsx data_summary.csv
(The same result can be produced in Excel with a PivotTable in tabular layout.)
"""
import sys
import pandas as pd

src, out = sys.argv[1], sys.argv[2]
d = pd.read_excel(src, sheet_name="Name mapping")
d = d[d["WEEK"] <= 47].copy()
d["Period"] = d["YEAR"].map({2024: "YA", 2025: "TY"})
d["Channel"] = d["STORE FORMAT"].map({"E-COMMERCE": "Online", "PURE PLAY": "Online",
                                      "LARGE FORMAT": "In-store", "SMALL FORMAT": "In-store"})
d = d.dropna(subset=["Channel"])
keys = ["Period", "Customer Name", "STORE FORMAT", "Channel", "SUPPLIER", "Brand Name",
        "Segment", "Sub segment", "Pack format", "Sub pack format"]
cube = d.groupby(keys, as_index=False)[["VALUE SALES", "UNIT SALES"]].sum()
cube.to_csv(out, index=False)
print(f"{len(d):,} source rows -> {len(cube):,} summary rows; "
      f"TY £{cube.loc[cube.Period == 'TY', 'VALUE SALES'].sum():,.0f}, "
      f"YA £{cube.loc[cube.Period == 'YA', 'VALUE SALES'].sum():,.0f}")
