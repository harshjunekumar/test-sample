"""A free, offline version of the persona chatbot: no API key, no AI model.

It understands questions with simple keyword rules ("intents"), looks up the
answer with the same tools the AI version uses (persona_tools.py), and fills
the numbers into ready-written answer templates. Every number comes from the data.

Run in the terminal:  python free_bot.py
Run as a web app:     streamlit run app.py
"""
import re

from persona_tools import compare_personas, get_persona_profile, list_personas, persona_breakdown, sample_customers

# Words people might use for each persona
ALIASES = {
    "Big-Ticket Tech Buyers": ["tech", "electronic", "gadget", "big-ticket", "big ticket", "laptop", "phone"],
    "Deal & Festive Shoppers": ["deal", "festive shopper", "bargain", "coupon hunter", "discount shopper", "discount hunter"],
    "Everyday Home & Kitchen Shoppers": ["home", "kitchen"],
    "Everyday Fashion Shoppers": ["fashion", "clothes", "apparel"],
    "Everyday Beauty Shoppers": ["beauty", "cosmetic", "skincare"],
}

# metric key -> (words that point to it, label, unit, True if "worse" means higher)
METRICS = {
    "median_days_since_last_order": (["churn", "inactive", "at risk", "at-risk", "lapsed", "dormant", "win back", "winback"],
                                     "median days since last order", " days", True),
    "return_rate_pct": (["return"], "return rate", "%", True),
    "avg_discount_pct": (["discount", "coupon", "deal", "price sensitive", "price-sensitive"], "average discount used", "%", False),
    "holiday_order_share_pct": (["holiday", "festive", "festival", "diwali", "season"], "share of orders in Nov-Dec", "%", False),
    "avg_order_value": (["order value", "aov", "basket", "expensive", "spend per order"], "average order value", "$", False),
    "avg_lifetime_spend": (["lifetime", "ltv", "clv"], "average lifetime spend", "$", False),
    "repeat_rate_pct": (["repeat"], "repeat purchase rate", "%", False),
    "avg_orders": (["frequent", "often", "loyal", "orders per"], "orders per customer", "", False),
    "revenue_share_pct": (["revenue", "valuable", "money", "sales", "important"], "share of revenue", "%", False),
    "customers": (["biggest", "largest", "most customers", "size"], "number of customers", "", False),
}


def _has(text: str, words) -> bool:
    return any(w in text for w in words)


def _has_word(text: str, words) -> bool:
    """Whole-word match, so 'hey' doesn't match 'they' and 'buy' doesn't match 'buyers'."""
    return any(re.search(rf"\b{re.escape(w)}\b", text) for w in words)


def _fmt(value, unit: str) -> str:
    if unit == "$":
        return f"${value:,.0f}"
    return f"{value:,}{unit}" if isinstance(value, int) else f"{value:,.1f}{unit}"


def find_personas(text: str) -> list[str]:
    """Personas mentioned in the text, in the order they appear."""
    hits = []
    for name, words in ALIASES.items():
        positions = [text.find(w) for w in words + [name.lower()] if w in text]
        if positions:
            hits.append((min(positions), name))
    return [name for _, name in sorted(hits)]


def find_metric(text: str):
    for key, (words, *_rest) in METRICS.items():
        if _has(text, words):
            return key
    return None


def ideas_for(p: dict) -> list[str]:
    """Rule-based recommendations from a persona's numbers."""
    ideas = []
    if p["avg_discount_pct"] >= 12:
        ideas.append("Very price-sensitive: use time-limited coupons and bundles instead of blanket discounts, to protect margin.")
    if p["return_rate_pct"] >= 10:
        ideas.append("High return rate: add better product content (specs, size guides, videos) and review return reasons by category.")
    if p["holiday_order_share_pct"] >= 30:
        ideas.append("Buys heavily in Nov-Dec: target this group first in festive campaigns, with early-access offers.")
    if p["avg_order_value"] >= 250:
        ideas.append("High basket value: offer no-cost EMI, exchange offers and extended warranty to lift conversion.")
    if p["repeat_rate_pct"] < 50:
        ideas.append("Low repeat rate: set up a post-purchase journey (day 7 / 30 / 60 nudges) to drive the second order.")
    if p["median_days_since_last_order"] >= 250:
        ideas.append("Many haven't ordered in a long time: run a win-back campaign and A/B test the offer size.")
    if not ideas:
        ideas.append("Steady, low-maintenance group: use cross-sell recommendations to grow basket size.")
    return ideas


class FreeBot:
    def __init__(self):
        self.last_persona = None   # remembers the persona being discussed, for follow-up questions

    def answer(self, question: str) -> str:
        q = question.lower().strip()
        personas = find_personas(q)
        if not personas and self.last_persona and re.search(r"\b(they|them|their|this persona|this group)\b", q):
            personas = [self.last_persona]
        asks_which = _has(q, ["which", "who ", "most", "highest", "lowest", "least", "best", "worst", "rank", "top "])

        if _has_word(q, ["hello", "hi", "hey", "help", "what can you"]):
            return self.help_text()
        if _has(q, ["list", "all persona", "what persona", "overview", "summary", "segments", "how many persona"]):
            return self.overview()
        if len(personas) >= 2 or (_has(q, ["compare", " vs", "versus", "difference"]) and personas):
            if len(personas) < 2:
                return f"Which persona should I compare **{personas[0]}** with? Options: " + ", ".join(
                    n for n in ALIASES if n != personas[0])
            return self.compare(personas[0], personas[1])
        if _has(q, ["target", "campaign"]) or (asks_which and _has(q, ["diwali", "festive sale", "sale", "festival"])):
            return self.campaign()
        if personas:
            self.last_persona = personas[0]
            if _has(q, ["region", "where", "location", "city", "state"]):
                return self.breakdown(personas[0], "region")
            if "categor" in q or _has_word(q, ["buy", "products", "purchase"]):
                return self.breakdown(personas[0], "category")
            if _has(q, ["example", "sample", "show me customer", "who are they"]):
                return self.examples(personas[0])
            return self.profile(personas[0])
        metric = find_metric(q)
        if metric:
            return self.rank(metric, lowest=_has(q, ["lowest", "least", "fewest", "smallest", "worst"]))
        return ("I'm not sure what you mean. I'm a simple rule-based bot, so I work best with short questions.\n\n"
                + self.examples_text())

    # ---- Answer templates --------------------------------------------------
    def help_text(self) -> str:
        return ("Hi! I answer questions about our 5 customer personas, using the customer data "
                "(no AI model, so it's free and runs offline).\n\n" + self.examples_text())

    @staticmethod
    def examples_text() -> str:
        return ("Try asking:\n- *List all personas*\n- *Tell me about the tech buyers*\n"
                "- *Which persona returns the most?*\n- *Which persona is most at risk of churning?*\n"
                "- *Compare deal shoppers vs fashion shoppers*\n- *Where are the beauty shoppers?*\n"
                "- *Which persona should we target for a Diwali campaign?*")

    def overview(self) -> str:
        d = list_personas()
        rows = "\n".join(f"| {p['name']} | {p['customers']:,} | {p['revenue_share_pct']}% | ${p['avg_order_value']:,.0f} | {p['tagline']} |"
                         for p in d["personas"])
        return (f"We have **{len(d['personas'])} personas** across {d['total_customers']:,} customers:\n\n"
                "| Persona | Customers | Revenue share | Avg order value | In short |\n|---|---:|---:|---:|---|\n" + rows
                + "\n\nAsk about any of them for the full profile.")

    def profile(self, name: str) -> str:
        p = get_persona_profile(name)
        cats = ", ".join(f"{c} {v}%" for c, v in list(p["category_mix_pct"].items())[:3])
        channel = next(iter(p["acquisition_channels_pct"]))
        lines = [
            f"### {p['name']}",
            f"*{p['tagline']}*",
            "",
            f"- **Size:** {p['customers']:,} customers ({p['customer_share_pct']}%), bringing in **{p['revenue_share_pct']}% of revenue**",
            f"- **Basket:** ${p['avg_order_value']:,.0f} per order, {p['avg_orders']} orders each, ${p['avg_lifetime_spend']:,.0f} lifetime spend",
            f"- **Loyalty:** {p['repeat_rate_pct']}% bought more than once; median {p['median_days_since_last_order']} days since last order",
            f"- **Deals and returns:** {p['avg_discount_pct']}% average discount, {p['return_rate_pct']}% return rate, "
            f"{p['holiday_order_share_pct']}% of orders in Nov-Dec",
            f"- **Buys:** {cats}",
            f"- **Most often acquired via:** {channel}",
            "",
            "**💡 Ideas**",
            *[f"- {i}" for i in ideas_for(p)],
        ]
        return "\n".join(lines)

    def compare(self, a: str, b: str) -> str:
        c = compare_personas(a, b)
        names = list(c["top_category"])
        labels = {"customers": ("Customers", ""), "revenue_share_pct": ("Revenue share", "%"),
                  "avg_order_value": ("Avg order value", "$"), "avg_orders": ("Orders per customer", ""),
                  "repeat_rate_pct": ("Repeat rate", "%"), "avg_discount_pct": ("Avg discount", "%"),
                  "return_rate_pct": ("Return rate", "%"), "median_days_since_last_order": ("Days since last order", "")}
        rows = "\n".join(f"| {lab} | {_fmt(c['comparison'][k][names[0]], u)} | {_fmt(c['comparison'][k][names[1]], u)} |"
                         for k, (lab, u) in labels.items())
        rows += f"\n| Top category | {c['top_category'][names[0]]} | {c['top_category'][names[1]]} |"
        return f"| | {names[0]} | {names[1]} |\n|---|---:|---:|\n{rows}"

    def rank(self, metric: str, lowest: bool = False) -> str:
        words, label, unit, worse_is_higher = METRICS[metric]
        ps = sorted((get_persona_profile(p["name"]) for p in list_personas()["personas"]),
                    key=lambda p: p[metric], reverse=not lowest)
        top = ps[0]
        rows = "\n".join(f"{i}. {p['name']}: {_fmt(p[metric], unit)}" for i, p in enumerate(ps, 1))
        verdict = f"**{top['name']}** has the {'lowest' if lowest else 'highest'} {label} ({_fmt(top[metric], unit)})."
        tip = f"\n\n💡 {ideas_for(top)[0]}" if (worse_is_higher and not lowest) else ""
        return f"{verdict}\n\n{rows}{tip}"

    def campaign(self) -> str:
        ps = [get_persona_profile(p["name"]) for p in list_personas()["personas"]]
        best = max(ps, key=lambda p: p["holiday_order_share_pct"] + p["avg_discount_pct"])
        value = max(ps, key=lambda p: p["avg_order_value"])
        return (f"For a festive campaign, start with **{best['name']}**: {best['holiday_order_share_pct']}% of their orders "
                f"come in Nov-Dec and they use an average {best['avg_discount_pct']}% discount, so offers move them.\n\n"
                f"Run a separate track for **{value['name']}** (${value['avg_order_value']:,.0f} per order): "
                "they respond to value-adds like no-cost EMI and exchange offers more than to deep discounts.\n\n"
                "💡 A/B test the offer: discount vs. bundle for the first group, measured on conversion **and** margin.")

    def breakdown(self, name: str, dim: str) -> str:
        d = persona_breakdown(name, dim)
        rows = "\n".join(f"| {r[dim]} | {r['orders']:,} | {r['revenue_share_pct']}% | {r['return_rate_pct']}% |" for r in d["rows"])
        return (f"**{d['persona']}** by {dim}:\n\n| {dim.title()} | Orders | Revenue share | Return rate |\n|---|---:|---:|---:|\n{rows}")

    def examples(self, name: str) -> str:
        d = sample_customers(name, 5)
        rows = "\n".join(f"| {c['customer_id']} | {c['orders']} | ${c['total_spend']:,.0f} | {c['days_since_last_order']} | {c['region']} |"
                         for c in d["customers"])
        return (f"Five example **{d['persona']}**:\n\n| Customer | Orders | Total spend | Days since last order | Region |\n"
                f"|---|---:|---:|---:|---|\n{rows}")


if __name__ == "__main__":
    bot = FreeBot()
    print("Free Persona Bot (no API key needed). Type 'quit' to exit.\n")
    print(bot.help_text() + "\n")
    while True:
        try:
            q = input("You: ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if q.lower() in {"quit", "exit"}:
            break
        if q:
            print(f"\nBot: {bot.answer(q)}\n")
