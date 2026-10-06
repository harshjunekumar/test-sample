"""Step 2: The tools the chatbot can call.

Each tool is a plain Python function that reads the persona data and returns
JSON. Claude never sees the raw data directly; it decides which tool to call,
we run the function, and Claude writes its answer from the result. This is
what keeps the answers grounded in real numbers instead of made-up ones.
"""
import json
from pathlib import Path

import pandas as pd

DATA = Path(__file__).parent / "data"
ORDERS_CSV = Path(__file__).parent.parent / "01-ecommerce-sales-analysis" / "data" / "orders.csv"

_profiles = json.loads((DATA / "personas.json").read_text())
_customers = pd.read_csv(DATA / "customer_personas.csv")
_orders = pd.read_csv(ORDERS_CSV).merge(_customers[["customer_id", "persona"]], on="customer_id")
PERSONA_NAMES = [p["name"] for p in _profiles["personas"]]


def _find(name: str) -> dict:
    """Match a persona by exact or partial name, e.g. 'tech' -> 'Big-Ticket Tech Buyers'."""
    exact = [p for p in _profiles["personas"] if name.lower() == p["name"].lower()]
    matches = exact or [p for p in _profiles["personas"] if name.lower() in p["name"].lower()]
    if len(matches) != 1:
        raise ValueError(f"Unknown or ambiguous persona '{name}'. Valid names: {PERSONA_NAMES}")
    return matches[0]


# ---- Tool implementations ---------------------------------------------------
def list_personas() -> dict:
    keys = ["name", "tagline", "customers", "customer_share_pct", "revenue_share_pct",
            "avg_order_value", "avg_orders"]
    return {"total_customers": _profiles["total_customers"],
            "total_revenue": _profiles["total_revenue"],
            "personas": [{k: p[k] for k in keys} for p in _profiles["personas"]]}


def get_persona_profile(persona_name: str) -> dict:
    return _find(persona_name)


def compare_personas(persona_a: str, persona_b: str) -> dict:
    a, b = _find(persona_a), _find(persona_b)
    metrics = ["customers", "revenue_share_pct", "avg_orders", "avg_order_value", "avg_lifetime_spend",
               "median_days_since_last_order", "avg_discount_pct", "return_rate_pct",
               "holiday_order_share_pct", "repeat_rate_pct"]
    return {"comparison": {m: {a["name"]: a[m], b["name"]: b[m]} for m in metrics},
            "top_category": {a["name"]: next(iter(a["category_mix_pct"])),
                             b["name"]: next(iter(b["category_mix_pct"]))}}


def persona_breakdown(persona_name: str, dimension: str) -> dict:
    p = _find(persona_name)
    o = _orders[_orders.persona == p["name"]]
    t = o.groupby(dimension).agg(orders=("order_id", "count"), revenue=("revenue", "sum"),
                                 avg_discount=("discount", "mean"), return_rate=("returned", "mean"))
    t["revenue_share_pct"] = 100 * t.revenue / t.revenue.sum()
    t["avg_discount_pct"] = 100 * t.pop("avg_discount")
    t["return_rate_pct"] = 100 * t.pop("return_rate")
    return {"persona": p["name"], "dimension": dimension,
            "rows": t.round(1).sort_values("revenue", ascending=False).reset_index().to_dict("records")}


def sample_customers(persona_name: str, n: int) -> dict:
    p = _find(persona_name)
    cols = ["customer_id", "orders", "total_spend", "avg_order_value", "days_since_last_order",
            "avg_discount", "region", "acquisition_channel"]
    rows = _customers[_customers.persona == p["name"]].sample(min(max(n, 1), 10), random_state=0)
    return {"persona": p["name"], "customers": rows[cols].to_dict("records")}


# ---- Tool definitions sent to Claude ----------------------------------------
# The description is what Claude reads to decide when to use each tool, so it
# says what the tool returns and when it's useful.
_name_param = {"type": "string", "description": f"Persona name or a distinctive part of it. One of: {PERSONA_NAMES}"}

TOOLS = [
    {"name": "list_personas",
     "description": "List every customer persona with its size, revenue share, average order value and "
                    "order frequency. Call this first when you don't yet know which personas exist.",
     "input_schema": {"type": "object", "properties": {}, "additionalProperties": False, "required": []}},
    {"name": "get_persona_profile",
     "description": "Full profile of one persona: spend, frequency, recency, discount use, return rate, "
                    "holiday share, repeat rate, category mix, regions and acquisition channels.",
     "input_schema": {"type": "object", "properties": {"persona_name": _name_param},
                      "additionalProperties": False, "required": ["persona_name"]}},
    {"name": "compare_personas",
     "description": "Side-by-side comparison of two personas on the key metrics.",
     "input_schema": {"type": "object",
                      "properties": {"persona_a": _name_param, "persona_b": _name_param},
                      "additionalProperties": False, "required": ["persona_a", "persona_b"]}},
    {"name": "persona_breakdown",
     "description": "Break one persona's orders down by region, product category, or basket size (quantity), "
                    "with orders, revenue, revenue share, average discount and return rate per group.",
     "input_schema": {"type": "object",
                      "properties": {"persona_name": _name_param,
                                     "dimension": {"type": "string", "enum": ["region", "category", "quantity"],
                                                   "description": "What to group the persona's orders by"}},
                      "additionalProperties": False, "required": ["persona_name", "dimension"]}},
    {"name": "sample_customers",
     "description": "Return up to 10 example customers from a persona, to make the persona concrete.",
     "input_schema": {"type": "object",
                      "properties": {"persona_name": _name_param,
                                     "n": {"type": "integer", "description": "How many customers, 1-10"}},
                      "additionalProperties": False, "required": ["persona_name", "n"]}},
]
for t in TOOLS:
    t["strict"] = True   # guarantees Claude's tool inputs match the schema exactly

_FUNCTIONS = {"list_personas": list_personas, "get_persona_profile": get_persona_profile,
              "compare_personas": compare_personas, "persona_breakdown": persona_breakdown,
              "sample_customers": sample_customers}


def run_tool(name: str, tool_input: dict) -> tuple[str, bool]:
    """Run a tool by name. Returns (json_result, is_error)."""
    try:
        return json.dumps(_FUNCTIONS[name](**tool_input), default=str), False
    except Exception as e:  # send the error back to Claude so it can correct itself
        return f"Error: {e}", True
