"""Draw the Checkpoint 1 metric tree (docs/metric_tree.png)."""
from pathlib import Path

import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

OUT = Path(__file__).resolve().parents[1] / "docs" / "metric_tree.png"

NAVY, BLUE, TEAL, GREY, INK = "#172337", "#2874F0", "#0F9D8A", "#6B7280", "#111827"

# (key, label, sub-label, x, y, colour)
NODES = [
    ("goal", "Customer Retention", "North-star (not in data)", 56, 92, NAVY),
    ("csat", "Customer Satisfaction", "Avg CSAT · % Satisfied (≥8)\n% Dissatisfied (≤4)", 30, 72, BLUE),
    ("resp", "Feedback Coverage", "CSAT response rate", 72, 72, BLUE),
    ("exp", "Interaction Quality", "Sentiment mix\nAvg sentiment score", 12, 48, TEAL),
    ("speed", "Speed of Service", "SLA compliance\nSLA breach rate", 34, 48, TEAL),
    ("eff", "Efficiency", "Avg call duration (AHT)", 56, 48, TEAL),
    ("demand", "Contact Demand", "Volume by reason,\nchannel, day", 80, 48, TEAL),
    ("d_sent", "sentiment", "", 12, 24, GREY),
    ("d_resp", "response_time", "", 34, 24, GREY),
    ("d_dur", "call duration", "", 56, 24, GREY),
    ("d_reason", "reason · channel\ncall_timestamp", "", 80, 24, GREY),
    ("d_loc", "Cut every metric by: call_center · city · state · gender", "", 46, 7, GREY),
]
EDGES = [("goal", "csat"), ("goal", "resp"), ("csat", "exp"), ("csat", "speed"), ("csat", "eff"),
         ("resp", "demand"), ("csat", "demand"), ("exp", "d_sent"), ("speed", "d_resp"),
         ("eff", "d_dur"), ("demand", "d_reason")]
HYP = {"exp": "H2 · H6", "speed": "H1", "eff": "H3", "demand": "H5", "d_loc": "H4"}


def main():
    fig, ax = plt.subplots(figsize=(14, 8.5), dpi=150)
    ax.set_xlim(0, 100)
    ax.set_ylim(0, 100)
    ax.axis("off")
    pos = {k: (x, y) for k, _, _, x, y, _ in NODES}
    for a, b in EDGES:
        (x1, y1), (x2, y2) = pos[a], pos[b]
        ax.annotate("", xy=(x2, y2 + 6), xytext=(x1, y1 - 6),
                    arrowprops=dict(arrowstyle="-|>", color="#9CA3AF", lw=1.4))
    for key, label, sub, x, y, col in NODES:
        w = 62 if key == "d_loc" else (20 if key.startswith("d_") else 19)
        h = 6 if key.startswith("d_") else 11
        data = key.startswith("d_")
        ax.add_patch(FancyBboxPatch((x - w / 2, y - h / 2), w, h, boxstyle="round,pad=0.4,rounding_size=1.2",
                                    fc="white" if data else col, ec=col, lw=1.6))
        tc = INK if data else "white"
        if sub:
            ax.text(x, y + 2.2, label, ha="center", va="center", fontsize=11, weight="bold", color=tc)
            ax.text(x, y - 2.2, sub, ha="center", va="center", fontsize=8.5, color=tc, linespacing=1.3)
        else:
            ax.text(x, y, label, ha="center", va="center", fontsize=9, color=tc,
                    family="monospace" if key != "d_loc" else None)
        if key in HYP:
            ax.text(x + w / 2 - 0.5, y + h / 2 + 1.2, HYP[key], ha="right", va="bottom", fontsize=8.5,
                    weight="bold", color="#B45309")
    ax.text(1, 99, "Flipkart Customer Service: Metric Tree", fontsize=13, weight="bold", color=NAVY, va="top")
    legend = [(NAVY, "Business goal"), (BLUE, "Outcome metrics (L1)"), (TEAL, "Driver metrics (L2)"),
              ("white", "Dataset columns")]
    for i, (c, t) in enumerate(legend):
        ax.add_patch(FancyBboxPatch((83, 97 - i * 3.2), 2, 2, boxstyle="round,pad=0.1", fc=c, ec=GREY))
        ax.text(86, 98 - i * 3.2, t, fontsize=8.5, va="center", color=INK)
    ax.text(83, 97 - 4 * 3.2 + 1, "H# = hypothesis tested", fontsize=8.5, color="#B45309", weight="bold", va="center")
    fig.savefig(OUT, bbox_inches="tight", facecolor="white")
    print("saved", OUT)


if __name__ == "__main__":
    main()
