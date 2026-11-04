"""Amazon KDP paperback files for "Color Me Happy!" (8.5 x 11 in, no bleed, black & white interior).

Run after ../build.py:   python3 kdp/build_kdp.py
Outputs (kdp/output/):
  Color-Me-Happy-KDP-Interior.pdf  - 64 pages: title, copyright, "belongs to", blank, then 30 single-sided pages
  Color-Me-Happy-KDP-Cover.pdf     - full wrap (back + spine + front) with 0.125 in bleed
  cover-front-preview.png          - front cover image for listings / social posts
"""
import glob, importlib.util, pathlib, re, subprocess, sys

KDP = pathlib.Path(__file__).resolve().parent
ROOT = KDP.parent
sys.path.insert(0, str(ROOT))
from lib import *  # noqa: E402,F403
import lib  # noqa: E402

OUT = KDP / "output"; OUT.mkdir(exist_ok=True)
TITLE, SUBTITLE, AUTHOR, YEAR = "Color Me Happy!", "Easy Coloring Book for Kids Ages 3–8", "Happy Crayon Press", 2026
SVGS = sorted((ROOT / "svg").glob("*.svg"))
assert len(SVGS) == 30, len(SVGS)

FONT_CSS = """@font-face{font-family:Fredoka;font-weight:500;src:url(fonts/Fredoka-Medium.ttf)}
@font-face{font-family:Fredoka;font-weight:700;src:url(fonts/Fredoka-Bold.ttf)}"""


def load(n):
    f = glob.glob(str(ROOT / f"pages/p{n:02d}_*.py"))[0]
    s = importlib.util.spec_from_file_location(f"pg{n}", f)
    m = importlib.util.module_from_spec(s); s.loader.exec_module(m); return m


def colorize(items, colors):
    """colors: {item_index: color | [color, ...]} -> replace white fills/strokes of those items."""
    out = []
    for i, it in enumerate(items):
        c = colors.get(i)
        if c is None:
            out.append(it); continue
        seq = c if isinstance(c, list) else None
        k = [0]

        def rep(m):
            col = seq[min(k[0], len(seq) - 1)] if seq else c
            k[0] += 1
            return f'{m.group(1)}="{col}"'
        out.append(re.sub(r'(fill|stroke)="#FFFFFF"', rep, it))
    return out


def inner_svg(svg_text):
    return re.sub(r"^.*?<svg[^>]*>|</svg>\s*$", "", svg_text, flags=re.S)


# ------------------------------------------------------------------ interior
def title_page():
    pup = load(1).puppy()
    items = [
        cloud(200, 470, 170), cloud(650, 440, 140),
        place(pup, 425, 720, 0.95),
        star(150, 640, 34), star(700, 620, 30), star(735, 760, 22), heart(120, 790, 26),
    ]
    big = ('font-family="Fredoka" font-weight="700" text-anchor="middle" fill="#FFFFFF" stroke="#000000" '
           'stroke-width="7" stroke-linejoin="round" paint-order="stroke"')
    text = [
        f'<text x="425" y="215" font-size="118" {big}>Color Me</text>',
        f'<text x="425" y="355" font-size="150" {big}>Happy!</text>',
        f'<text x="425" y="1015" font-size="30" font-family="Fredoka" font-weight="500" text-anchor="middle">{AUTHOR}</text>',
    ]
    return lib.page(items, framed=False).replace("</svg>", "\n".join(text) + "\n</svg>")


def belongs_page():
    items = [
        lib.frame(),
        rect(165, 330, 520, 300, r=40),
        star(170, 190, 40), star(680, 190, 40), heart(425, 170, 40),
        line("M235 520 L615 520", SW),
        flower(160, 900, 46), flower(690, 900, 46, petals=6), place(load(1).ball(0, 0, 70), 425, 880),
    ]
    t = ('<text x="425" y="425" font-size="44" font-family="Fredoka" font-weight="700" text-anchor="middle" '
         'fill="#FFFFFF" stroke="#000000" stroke-width="5" paint-order="stroke">This book belongs to</text>')
    return lib.page(items, framed=False).replace("</svg>", t + "\n</svg>")


COPYRIGHT = f"""<div class="copy"><p><b>{TITLE}</b><br>{SUBTITLE}</p>
<p>Copyright © {YEAR} {AUTHOR}. All rights reserved.</p>
<p>No part of this book may be reproduced, distributed or transmitted in any form without written
permission from the publisher, except that parents and teachers may photocopy pages for personal or
classroom coloring use.</p>
<p><b>Coloring tips:</b> every picture is printed on its own page with a blank back, so markers won't spoil
the next picture. Slip a sheet of card behind the page when using markers or paint.</p></div>"""


def build_interior():
    pages = [title_page(), COPYRIGHT, belongs_page(), ""]
    for s in SVGS:
        pages += [s.read_text(), ""]          # picture on the right-hand page, blank back
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}
@page{{size:8.5in 11in;margin:0}} html,body{{margin:0;background:#fff}}
.pg{{width:8.5in;height:11in;overflow:hidden;break-after:page;position:relative}} .pg:last-child{{break-after:auto}}
.pg svg{{display:block;width:8.5in;height:11in}}
.copy{{position:absolute;left:1.1in;right:1.1in;bottom:1.3in;font:12pt/1.5 Fredoka;color:#000}}
</style></head><body>
{''.join(f'<div class="pg">{p}</div>' for p in pages)}
</body></html>"""
    (KDP / "interior.html").write_text(html)
    subprocess.run(["node", str(KDP / "render.js"), str(KDP / "interior.html"),
                    str(OUT / "Color-Me-Happy-KDP-Interior.pdf"), "8.5", "11"], check=True)
    return len(pages)


# ------------------------------------------------------------------ cover
TAN, BROWN, CREAM, RED, GOLD, PINK, MOUTH = "#F5B971", "#A86A3D", "#FFF3DC", "#EF476F", "#FFD166", "#FFA6C1", "#8E2C3A"
ORANGE, LILAC, GREEN, SKY = "#FF9F43", "#D7C4F7", "#7BD389", "#9AD8FF"


def cover_front():
    pup = colorize(load(1).puppy(), {0: TAN, 1: TAN, 2: CREAM, 3: TAN, 4: TAN, 5: TAN, 6: TAN, 7: CREAM, 8: CREAM,
                                    10: RED, 11: GOLD, 12: RED, 13: TAN, 14: BROWN, 15: BROWN, 16: BROWN,
                                    17: CREAM, 20: MOUTH, 21: PINK, 25: PINK, 26: PINK})
    kit = colorize(load(2).kitten(), {0: ORANGE, 1: ORANGE, 2: CREAM, 3: ORANGE, 4: ORANGE, 5: ORANGE, 6: CREAM,
                                     8: ORANGE, 9: ORANGE, 11: ORANGE, 12: ORANGE, 13: PINK, 14: PINK, 15: ORANGE,
                                     19: PINK, 20: PINK})
    bun = colorize(load(6).bunny(), {0: LILAC, 1: LILAC, 2: PINK, 3: PINK, 4: LILAC, 5: CREAM, 6: LILAC, 7: LILAC,
                                    8: LILAC, 11: PINK, 12: PINK, 18: [ORANGE, GREEN, GREEN, GREEN],
                                    19: LILAC, 20: LILAC, 21: LILAC, 22: LILAC})
    bands = colorize(rainbow_bands(425, 860, [420, 375, 330, 285, 240]), {0: RED, 1: GOLD, 2: GREEN, 3: "#5DADE2"})
    ball = colorize(load(1).ball(0, 0, 52), {0: GOLD})
    items = [
        f'<rect x="-20" y="-20" width="890" height="1140" fill="{SKY}"/>',
        *bands,
        cloud(95, 860, 190), cloud(755, 860, 190),
        colorize([sun(745, 470, 46, rays=9, face=True)], {0: GOLD})[0],
        cloud(110, 470, 150),
        hills(840, amp=45, bumps=2, x0=-20, x1=870, bottom=1130).replace('fill="#FFFFFF"', f'fill="{GREEN}"'),
        place(bun, 690, 790, 0.66), place(kit, 165, 800, 0.66),
        place(pup, 425, 720, 0.98),
        place(ball, 575, 922),
    ]
    letters = [("C", RED), ("o", ORANGE), ("l", GOLD), ("o", GREEN), ("r", "#4D96FF"), (" ", None),
               ("M", "#9B5DE5"), ("e", "#F15BB5")]
    def word(txt_cols, y, size):
        spans = "".join(f'<tspan fill="{c or "#fff"}">{ch}</tspan>' for ch, c in txt_cols)
        base = f'x="425" y="{y}" font-size="{size}" font-family="Fredoka" font-weight="700" text-anchor="middle"'
        return (f'<text {base} fill="#fff" stroke="#fff" stroke-width="34" stroke-linejoin="round">{spans}</text>'
                f'<text {base} stroke="#22223B" stroke-width="9" stroke-linejoin="round" paint-order="stroke">{spans}</text>')
    happy = [("H", "#4D96FF"), ("a", RED), ("p", GOLD), ("p", GREEN), ("y", ORANGE), ("!", "#F15BB5")]
    text = [
        word(letters, 190, 132), word(happy, 345, 170),
        f'<rect x="135" y="380" width="580" height="64" rx="32" fill="#fff" stroke="#22223B" stroke-width="6"/>',
        f'<text x="425" y="424" font-size="31" font-family="Fredoka" font-weight="700" text-anchor="middle" fill="#22223B">{SUBTITLE}</text>',
        f'<path d="M90 975 L760 975 L735 1008 L760 1041 L90 1041 L115 1008 Z" fill="{GOLD}" stroke="#22223B" stroke-width="6" stroke-linejoin="round"/>',
        '<text x="425" y="1019" font-size="33" font-family="Fredoka" font-weight="700" text-anchor="middle" fill="#22223B">30 Fun Adventures &amp; Cute Animals</text>',
        f'<text x="425" y="1078" font-size="24" font-family="Fredoka" font-weight="700" text-anchor="middle" fill="#22223B">{AUTHOR}</text>',
    ]
    return items + text


def cover_back():
    thumbs = [SVGS[i] for i in (8, 11, 15, 29)]   # unicorn, rocket, panda, castle
    pos = [(160, 255, -3), (450, 255, 3), (160, 595, 3), (450, 595, -3)]
    out = [f'<rect x="-20" y="-20" width="890" height="1140" fill="{SKY}"/>',
           hills(1000, amp=35, bumps=2, x0=-20, x1=870, bottom=1130).replace('fill="#FFFFFF"', f'fill="{GREEN}"')]
    for (x, y, r), s in zip(pos, thumbs):
        w, h = 240, 310
        out.append(f'<g transform="rotate({r} {x + w / 2} {y + h / 2})"><rect x="{x - 10}" y="{y - 10}" width="{w + 20}" '
                   f'height="{h + 20}" rx="14" fill="#fff" stroke="#22223B" stroke-width="5"/>'
                   f'<svg x="{x}" y="{y}" width="{w}" height="{h}" viewBox="0 0 850 1100">{inner_svg(s.read_text())}</svg></g>')
    return out


BACK_HTML = """<div class="blurb"><h2>Grab your crayons &mdash; adventure awaits!</h2>
<p>Puppies, unicorns, dinosaurs, rockets, mermaids, castles and more: 30 cheerful pictures made just for little hands.</p></div>
<ul class="feat"><li>30 big, one-sided pages &ndash; no bleed-through</li><li>Thick, bold lines &amp; simple shapes</li>
<li>Perfect for ages 3&ndash;8</li><li>Large 8.5 &times; 11 in pages</li></ul>"""


def build_cover(page_count):
    spine = page_count * 0.002252            # KDP white paper
    bleed = 0.125
    W, H = 2 * bleed + 2 * 8.5 + spine, 11 + 2 * bleed
    u = lambda inch: inch * 100
    front_x, back_x = u(bleed + 8.5 + spine), u(bleed)
    svg = (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {u(W):.2f} {u(H)}" width="{W:.4f}in" height="{H}in">'
           f'<rect width="100%" height="100%" fill="{SKY}"/>'
           f'<clipPath id="cb"><rect x="{-u(bleed)}" y="{-u(bleed)}" width="{u(bleed + 8.5 + spine / 2):.2f}" height="{u(H)}"/></clipPath>'
           f'<clipPath id="cf"><rect x="{-u(spine / 2):.2f}" y="{-u(bleed)}" width="{u(spine / 2 + 8.5 + bleed):.2f}" height="{u(H)}"/></clipPath>'
           f'<g transform="translate({back_x} {u(bleed)})"><g clip-path="url(#cb)">{"".join(cover_back())}</g></g>'
           f'<g transform="translate({front_x:.2f} {u(bleed)})"><g clip-path="url(#cf)">{"".join(cover_front())}</g></g></svg>')
    html = f"""<!doctype html><html><head><meta charset="utf-8"><style>{FONT_CSS}
@page{{size:{W:.4f}in {H}in;margin:0}} html,body{{margin:0}} body{{position:relative;width:{W:.4f}in;height:{H}in;overflow:hidden}}
svg{{display:block}} .back{{position:absolute;left:{bleed + 0.5}in;top:{bleed + 0.45}in;width:7.5in;font-family:Fredoka;color:#22223B}}
.blurb{{background:#fff;border:0.05in solid #22223B;border-radius:0.25in;padding:0.12in 0.3in;text-align:center}}
.blurb h2{{margin:0.05in 0;font-size:25pt;font-weight:700}} .blurb p{{margin:0.04in 0 0.06in;font:500 15pt/1.35 Fredoka}}
.feat{{position:absolute;left:{bleed + 0.5}in;top:{bleed + 9.3}in;margin:0;padding:0.1in 0.3in;list-style:none;font:700 14pt/1.45 Fredoka;color:#22223B;background:#fff;border:0.05in solid #22223B;border-radius:0.25in}}
.feat li::before{{content:"\\2605  ";color:#EF476F}}
</style></head><body>{svg}<div class="back">{BACK_HTML.split('<ul')[0]}</div>
<ul class="feat">{BACK_HTML.split('<ul class="feat">')[1].replace('</ul>', '')}</ul></body></html>"""
    (KDP / "cover.html").write_text(html)
    subprocess.run(["node", str(KDP / "render.js"), str(KDP / "cover.html"), str(OUT / "Color-Me-Happy-KDP-Cover.pdf"),
                    f"{W:.4f}", str(H), str(OUT / "cover-full-preview.png")], check=True)
    # Chromium rounds page sizes; trim the (bleed-only) right edge so the PDF matches KDP's exact cover width.
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import RectangleObject
    pdf = OUT / "Color-Me-Happy-KDP-Cover.pdf"
    r = PdfReader(pdf); wtr = PdfWriter()
    pg = r.pages[0]; box = RectangleObject([0, 0, round(W * 72, 3), round(H * 72, 3)])
    pg.mediabox = box; pg.cropbox = box; pg.trimbox = box; pg.bleedbox = box
    wtr.add_page(pg); wtr.write(pdf)
    # front-only preview (trimmed, no bleed) for listing images
    from PIL import Image
    im = Image.open(OUT / "cover-full-preview.png"); sx = im.width / W
    fx0 = (bleed + 8.5 + spine) * sx
    im.crop((round(fx0), round(bleed * sx), round(fx0 + 8.5 * sx), round((bleed + 11) * sx))).save(OUT / "cover-front-preview.png")
    print(f"cover {W:.4f} x {H} in, spine {spine:.4f} in")


if __name__ == "__main__":
    n = build_interior()
    print("interior pages:", n)
    build_cover(n)
