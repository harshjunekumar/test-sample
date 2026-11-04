"""Build the coloring book: pages/*.py -> svg/*.svg -> output PNGs (300 DPI) + PDFs (Letter & A4).

Usage:  python3 build.py            # all pages
        python3 build.py 3 7        # only pages 03 and 07 (SVG + PNG; PDFs always rebuilt from all SVGs)
"""
import importlib.util, pathlib, subprocess, sys
from PIL import Image

ROOT = pathlib.Path(__file__).parent
sys.path.insert(0, str(ROOT))
import lib  # noqa: E402

SVG_DIR, OUT = ROOT / "svg", ROOT / "output"
PNG_DIR = OUT / "png-300dpi"
SVG_DIR.mkdir(exist_ok=True); PNG_DIR.mkdir(parents=True, exist_ok=True)

only = {int(a) for a in sys.argv[1:]}
built = []
for f in sorted((ROOT / "pages").glob("p[0-9][0-9]_*.py")):
    n = int(f.name[1:3])
    if only and n not in only:
        continue
    spec = importlib.util.spec_from_file_location(f.stem, f)
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    svg = lib.page(mod.draw())
    out = SVG_DIR / (f.stem[1:] + ".svg")
    out.write_text(svg)
    built.append(out)
    print("svg", out.name)

subprocess.run(["node", str(ROOT / "render.js"), str(SVG_DIR), str(OUT), *[b.name for b in built]], check=True)

# Stamp 300 DPI metadata and store as clean 8-bit grayscale.
for b in built:
    p = PNG_DIR / (b.stem + ".png")
    Image.open(p).convert("L").save(p, dpi=(300, 300), optimize=True)
print("done")
