"""Tiny helper to practise SQL with nothing but Python installed (uses SQLite).

  python run.py setup                  # (re)build practice.db from schema.sql + seed.sql
  python run.py query "SELECT ..."     # run an ad-hoc query and print a table
  python run.py file my_answer.sql     # run every statement in a file
  python run.py solution 5.4           # show + run the reference solution for Q5.4
  python run.py check                  # run all reference solutions (smoke test)

Prefer a GUI? Open practice.db in DB Browser for SQLite, DBeaver, or VS Code's
SQLite extension after running `setup`.
"""
import os
import re
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DB = os.path.join(HERE, "practice.db")
MAX_ROWS = 50


def setup():
    if os.path.exists(DB):
        os.remove(DB)
    con = sqlite3.connect(DB)
    for name in ("schema.sql", "seed.sql"):
        with open(os.path.join(HERE, name)) as f:
            con.executescript(f.read())
    con.commit()
    tables = [r[0] for r in con.execute("SELECT name FROM sqlite_master WHERE type='table' ORDER BY name")]
    for t in tables:
        print(f"  {t:<16} {con.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0]:>6} rows")
    con.close()
    print(f"Built {DB}")


def connect():
    if not os.path.exists(DB):
        setup()
    return sqlite3.connect(DB)


def show(cur, max_rows=MAX_ROWS):
    if cur.description is None:
        print("(ok)")
        return
    cols = [c[0] for c in cur.description]
    rows = cur.fetchall()
    fmt = lambda v: "NULL" if v is None else (f"{v:,.2f}" if isinstance(v, float) else str(v))
    shown = [[fmt(v) for v in r] for r in rows[:max_rows]]
    widths = [max(len(c), *(len(r[i]) for r in shown)) if shown else len(c) for i, c in enumerate(cols)]
    print(" | ".join(c.ljust(w) for c, w in zip(cols, widths)))
    print("-+-".join("-" * w for w in widths))
    for r in shown:
        print(" | ".join(v.ljust(w) for v, w in zip(r, widths)))
    extra = f", showing first {max_rows}" if len(rows) > max_rows else ""
    print(f"({len(rows)} rows{extra})\n")


def run_sql(sql, con=None):
    con = con or connect()
    statements = [s for s in split_statements(sql) if s.strip()]
    for s in statements:
        show(con.execute(s))


def split_statements(sql):
    # good enough for practice files: split on ';' outside of quotes and -- comments
    out, buf, q, comment = [], [], None, False
    for i, ch in enumerate(sql):
        if comment:
            comment = ch != "\n"
        elif q:
            q = None if ch == q else q
        elif ch in "'\"":
            q = ch
        elif sql.startswith("--", i):
            comment = True
        elif ch == ";":
            out.append("".join(buf))
            buf = []
            continue
        buf.append(ch)
    out.append("".join(buf))
    strip = lambda s: re.sub(r"--[^\n]*", "", s).strip()
    return [s for s in out if strip(s)]


def solutions():
    with open(os.path.join(HERE, "solutions.sql")) as f:
        text = f.read()
    parts = re.split(r"^-- (Q\d+\.\d+)\b", text, flags=re.M)
    return {parts[i][1:]: ("-- " + parts[i] + parts[i + 1]).strip() for i in range(1, len(parts), 2)}


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 0
    cmd, args = argv[1], argv[2:]
    if cmd == "setup":
        setup()
    elif cmd == "query":
        run_sql(" ".join(args))
    elif cmd == "file":
        with open(args[0]) as f:
            run_sql(f.read())
    elif cmd == "solution":
        sol = solutions().get(args[0])
        if not sol:
            print(f"No solution {args[0]!r}")
            return 1
        print(sol, "\n")
        run_sql(sol)
    elif cmd == "check":
        con, failed = connect(), 0
        for key, sql in solutions().items():
            try:
                for s in split_statements(sql):
                    rows = con.execute(s).fetchall()
                print(f"ok    Q{key:<5} {len(rows):>4} rows")
            except sqlite3.Error as e:
                failed += 1
                print(f"FAIL  Q{key:<5} {e}")
        print(f"\n{failed} failed")
        return 1 if failed else 0
    else:
        print(__doc__)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
