"""Regenerate seed.sql deterministically.

You normally don't need this: seed.sql is committed. Run it only if you want
to tweak the data (e.g. more customers) and rebuild:  python generate_seed.py
"""
import random
from datetime import date, datetime, timedelta

random.seed(42)

REGIONS = {1: "North", 2: "South", 3: "East", 4: "West"}
CITIES = {
    1: ["Chicago", "Minneapolis", "Detroit"],
    2: ["Atlanta", "Dallas", "Miami"],
    3: ["New York", "Boston", "Philadelphia"],
    4: ["Seattle", "San Francisco", "Denver"],
}
FIRST = ["Ava", "Liam", "Noah", "Emma", "Olivia", "Mason", "Sophia", "Lucas", "Mia", "Ethan",
         "Isabella", "Aiden", "Harper", "Elijah", "Amelia", "James", "Evelyn", "Benjamin",
         "Abigail", "Logan", "Ella", "Jackson", "Scarlett", "Leo", "Grace", "Mateo", "Chloe",
         "Ravi", "Aisha", "Kenji", "Fatima", "Diego", "Zara", "Omar", "Mei", "Arjun"]
LAST = ["Smith", "Johnson", "Brown", "Garcia", "Miller", "Davis", "Martinez", "Lopez", "Wilson",
        "Anderson", "Thomas", "Moore", "Lee", "Walker", "Hall", "Young", "King", "Patel", "Nguyen",
        "Kim", "Khan", "Singh", "Chen", "Rossi", "Silva", "Okafor"]
CHANNELS = ["Paid Search", "Social", "Email", "Affiliate", "Organic", "Referral"]
PAID_CHANNELS = ["Paid Search", "Social", "Email", "Affiliate"]

# id, name, category, price, cost, launch, popularity weight
PRODUCTS = [
    (1, "Laptop Pro 14", "Electronics", 1299.00, 850.00, "2023-01-15", 3),
    (2, "Laptop Air 13", "Electronics", 999.00, 680.00, "2023-01-15", 4),
    (3, "Monitor 27in", "Electronics", 329.00, 210.00, "2023-03-01", 6),
    (4, "Tablet 11", "Electronics", 549.00, 360.00, "2023-06-01", 3),
    (5, "Wireless Earbuds", "Electronics", 129.00, 55.00, "2023-02-01", 7),
    (6, "USB-C Hub", "Accessories", 49.00, 18.00, "2023-01-15", 10),
    (7, "Wireless Mouse", "Accessories", 29.00, 9.00, "2023-01-15", 12),
    (8, "Mechanical Keyboard", "Accessories", 119.00, 48.00, "2023-04-01", 6),
    (9, "Laptop Sleeve", "Accessories", 35.00, 11.00, "2023-01-15", 7),
    (10, "Webcam HD", "Accessories", 79.00, 32.00, "2023-05-01", 5),
    (11, "Standing Desk", "Furniture", 499.00, 260.00, "2023-02-01", 3),
    (12, "Ergonomic Chair", "Furniture", 379.00, 190.00, "2023-02-01", 4),
    (13, "Monitor Arm", "Furniture", 89.00, 37.00, "2023-07-01", 4),
    (14, "Desk Lamp", "Furniture", 45.00, 17.00, "2023-01-15", 5),
    (15, "Printer Paper (Box)", "Office", 42.00, 24.00, "2023-01-15", 8),
    (16, "Notebook 5-Pack", "Office", 18.00, 6.00, "2023-01-15", 7),
    (17, "Pen Set", "Office", 12.00, 3.00, "2023-01-15", 6),   # discontinued end of 2024
    (18, "Label Printer", "Office", 149.00, 85.00, "2023-09-01", 2),
    (19, "Office Suite Annual", "Software", 99.00, 10.00, "2023-01-15", 6),
    (20, "Antivirus Pro Annual", "Software", 59.00, 5.00, "2023-01-15", 5),
    (21, "Cloud Backup 1TB", "Software", 119.00, 30.00, "2024-03-01", 4),
    (22, "VR Headset", "Electronics", 699.00, 450.00, "2025-06-20", 0),  # never sold
]

# employee_id, name, title, manager, region, hire_date, salary
EMPLOYEES = [
    (1, "Morgan Blake", "CEO", None, None, "2019-02-01", 240000),
    (2, "Priya Shah", "VP Sales", 1, None, "2020-05-11", 175000),
    (3, "Daniel Cho", "Regional Sales Manager", 2, 1, "2021-03-15", 118000),
    (4, "Rosa Alvarez", "Regional Sales Manager", 2, 2, "2021-06-01", 115000),
    (5, "Tom Becker", "Regional Sales Manager", 2, 3, "2020-11-02", 121000),
    (6, "Nina Petrova", "Regional Sales Manager", 2, 4, "2022-01-10", 119000),
    (7, "Jake Turner", "Sales Rep", 3, 1, "2022-04-18", 68000),
    (8, "Lena Fischer", "Sales Rep", 3, 1, "2023-08-07", 64000),
    (9, "Marcus Reed", "Sales Rep", 4, 2, "2021-09-20", 71000),
    (10, "Sofia Romano", "Sales Rep", 4, 2, "2024-02-12", 62000),
    (11, "Hiro Tanaka", "Sales Rep", 5, 3, "2022-07-25", 70000),
    (12, "Grace Obi", "Sales Rep", 5, 3, "2023-01-09", 66000),
    (13, "Ben Carter", "Sales Rep", 6, 4, "2021-12-01", 72000),
    (14, "Chloe Martin", "Sales Rep", 6, 4, "2024-09-03", 61000),
    (15, "Sam Ortiz", "Sales Rep", 6, 4, "2025-06-16", 60000),  # too new: no orders
]

START, END = date(2024, 1, 1), date(2025, 6, 30)


def d(s):
    return date.fromisoformat(s)


def rand_date(a, b):
    return a + timedelta(days=random.randint(0, (b - a).days))


# ---------------------------------------------------------------- customers
customers = []
cust_meta = {}
N_CUST = 90
for cid in range(1, N_CUST + 1):
    fn, ln = random.choice(FIRST), random.choice(LAST)
    region = random.choice(list(REGIONS))
    segment = random.choices(["Consumer", "SMB", "Enterprise"], [55, 30, 15])[0]
    channel = random.choices(CHANNELS, [25, 20, 12, 10, 23, 10])[0]
    signup = rand_date(date(2023, 9, 1), date(2025, 5, 31))
    email = f"{fn.lower()}.{ln.lower()}{cid}@example.com"
    customers.append([cid, fn, ln, email, random.choice(CITIES[region]), region,
                      segment, channel, signup.isoformat()])
    weight = random.paretovariate(1.3)  # a few customers buy a lot
    if segment == "Enterprise":
        weight *= 2
    if random.random() < 0.08:
        weight = 0  # never orders
    churn = signup + timedelta(days=random.randint(120, 700)) if random.random() < 0.45 else None
    cust_meta[cid] = dict(region=region, segment=segment, signup=signup, weight=weight, churn=churn)

# ---------------------------------------------------------------- orders
orders, items = [], []
oid, iid = 1000, 1
month = date(2024, 1, 1)
m_index = 0
while month <= END:
    nxt = date(month.year + (month.month == 12), month.month % 12 + 1, 1)
    n = 22 + m_index * 1.6
    n *= {11: 1.35, 12: 1.6, 1: 0.85, 2: 0.9}.get(month.month, 1.0)
    for _ in range(int(n + random.uniform(-3, 3))):
        od = rand_date(month, nxt - timedelta(days=1))
        cands = [(c, m["weight"]) for c, m in cust_meta.items()
                 if m["weight"] > 0 and m["signup"] <= od and (m["churn"] is None or od < m["churn"])]
        if not cands:
            continue
        cid = random.choices([c for c, _ in cands], [w for _, w in cands])[0]
        meta = cust_meta[cid]
        status = random.choices(["completed", "cancelled", "returned"], [85, 8, 7])[0]
        reps = [e for e in EMPLOYEES if e[2] == "Sales Rep" and e[4] == meta["region"] and d(e[5]) <= od]
        rep_share = 0.85 if meta["segment"] == "Enterprise" else 0.55
        emp = random.choice(reps)[0] if reps and random.random() < rep_share else None
        ship = None if status == "cancelled" else (od + timedelta(days=random.randint(1, 6))).isoformat()
        oid += 1
        orders.append([oid, cid, emp, od.isoformat(), ship, status])

        avail = [p for p in PRODUCTS if p[6] > 0 and d(p[5]) <= od and not (p[0] == 17 and od.year >= 2025)]
        k = random.choices([1, 2, 3, 4], [45, 30, 17, 8])[0]
        chosen = set()
        while len(chosen) < k:
            chosen.add(random.choices(avail, [p[6] for p in avail])[0])
        for p in sorted(chosen):
            if meta["segment"] == "Enterprise":
                qty = random.randint(2, 12)
            elif meta["segment"] == "SMB":
                qty = random.randint(1, 5)
            else:
                qty = random.choices([1, 2, 3], [75, 20, 5])[0]
            price = p[3]
            if od < date(2025, 1, 1) and p[0] in (1, 2, 3):
                price = round(price * 1.05, 2)  # prices dropped at start of 2025
            disc = random.choices([0, 0.05, 0.10, 0.15, 0.20], [60, 15, 13, 8, 4])[0]
            if meta["segment"] == "Enterprise" and disc == 0 and random.random() < 0.5:
                disc = 0.10
            items.append([iid, oid, p[0], qty, price, disc])
            iid += 1
    month = nxt
    m_index += 1

# ---------------------------------------------------------------- data-quality issues (on purpose!)
customers[4][3] = None                                   # missing emails
customers[17][3] = None
customers[52][3] = None
customers[30][3] = "  " + customers[11][3].upper() + " "  # duplicate email w/ case + spaces
customers[63][3] = customers[40][3]                      # exact duplicate email
customers[8][4] = None                                   # missing cities
customers[71][4] = None
customers[22][4] = " new york"                           # messy city values
customers[45][4] = "CHICAGO "
completed = [o for o in orders if o[5] == "completed"]
completed[10][4] = None                                  # completed but never shipped?
completed[200][4] = None
bad = completed[120]                                     # shipped before it was ordered
bad[4] = (d(bad[3]) - timedelta(days=2)).isoformat()
for o in (completed[55], completed[301]):                # orders with no line items
    items[:] = [i for i in items if i[1] != o[0]]
for n, i in enumerate(items, start=1):
    i[0] = n

# ---------------------------------------------------------------- marketing spend
spend = []
m = date(2023, 9, 1)
base = {"Paid Search": 4200, "Social": 3100, "Email": 900, "Affiliate": 1600}
while m <= END:
    for ch in PAID_CHANNELS:
        seasonal = 1.4 if m.month in (11, 12) else 1.0
        spend.append([m.isoformat(), ch, round(base[ch] * seasonal * random.uniform(0.8, 1.25), 2)])
    m = date(m.year + (m.month == 12), m.month % 12 + 1, 1)

# ---------------------------------------------------------------- web events (funnel, 2025 H1)
events = []
eid = 1
steps = ["visit", "view_product", "add_to_cart", "checkout", "purchase"]
conv = {"desktop": [0.72, 0.38, 0.65, 0.78], "mobile": [0.64, 0.27, 0.52, 0.66], "tablet": [0.68, 0.32, 0.58, 0.72]}
for sid in range(50001, 51401):
    device = random.choices(["desktop", "mobile", "tablet"], [45, 45, 10])[0]
    cust = random.randint(1, N_CUST) if random.random() < 0.4 else None
    t = datetime.combine(rand_date(date(2025, 1, 1), END), datetime.min.time()) + timedelta(
        minutes=random.randint(6 * 60, 23 * 60))
    for s, step in enumerate(steps):
        if s > 0 and random.random() > conv[device][s - 1]:
            break
        events.append([eid, sid, cust, device, step, t.strftime("%Y-%m-%d %H:%M:%S")])
        eid += 1
        t += timedelta(minutes=random.randint(1, 9), seconds=random.randint(0, 59))


# ---------------------------------------------------------------- write
def lit(v):
    if v is None:
        return "NULL"
    if isinstance(v, str):
        return "'" + v.replace("'", "''") + "'"
    return repr(v)


def inserts(table, cols, rows, chunk=250):
    out = []
    for i in range(0, len(rows), chunk):
        vals = ",\n".join("(" + ", ".join(lit(v) for v in r) + ")" for r in rows[i:i + chunk])
        out.append(f"INSERT INTO {table} ({', '.join(cols)}) VALUES\n{vals};\n")
    return "\n".join(out)


with open("seed.sql", "w") as f:
    f.write("-- Generated by generate_seed.py (random.seed(42)). Load AFTER schema.sql.\n\n")
    f.write(inserts("regions", ["region_id", "region_name"], [[k, v] for k, v in REGIONS.items()]))
    f.write(inserts("customers", ["customer_id", "first_name", "last_name", "email", "city", "region_id",
                                  "segment", "acquisition_channel", "signup_date"], customers))
    f.write(inserts("products", ["product_id", "product_name", "category", "unit_price", "unit_cost",
                                 "launch_date"], [list(p[:6]) for p in PRODUCTS]))
    f.write(inserts("employees", ["employee_id", "full_name", "title", "manager_id", "region_id",
                                  "hire_date", "salary"], [list(e) for e in EMPLOYEES]))
    f.write(inserts("orders", ["order_id", "customer_id", "employee_id", "order_date", "ship_date",
                               "status"], orders))
    f.write(inserts("order_items", ["order_item_id", "order_id", "product_id", "quantity", "unit_price",
                                    "discount"], items))
    f.write(inserts("marketing_spend", ["month_start", "channel", "spend"], spend))
    f.write(inserts("web_events", ["event_id", "session_id", "customer_id", "device", "event_type",
                                   "event_time"], events))

print(f"customers={len(customers)} orders={len(orders)} items={len(items)} "
      f"spend={len(spend)} events={len(events)}")
