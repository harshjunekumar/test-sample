"""Tiny SVG line-art toolkit for the coloring book.

Coordinate system: viewBox 0 0 850 1100 (1 unit = 0.01 inch, US Letter portrait).
Safe drawing area (generous margins): x 75..775, y 90..1010.

Every closed shape is filled pure white (#FFFFFF) and stroked pure black (#000000),
so shapes are layered back-to-front (painter's algorithm): later items hide earlier ones.
Only pupils/noses are solid black; no greys, gradients or textures anywhere.
"""
import math

W, H = 850, 1100
MARGIN_X, MARGIN_TOP, MARGIN_BOTTOM = 75, 90, 1010
SW = 8      # main outline weight  (0.08 in ~ 5.8 pt)
SW2 = 5.5   # inner detail weight
BLACK, WHITE = "#000000", "#FFFFFF"


def _fmt(v):
    return f"{v:.2f}".rstrip("0").rstrip(".") if isinstance(v, float) else str(v)


def _attrs(fill=WHITE, sw=SW, extra=""):
    s = f'fill="{fill}"'
    if sw:
        s += f' stroke="{BLACK}" stroke-width="{_fmt(sw)}" stroke-linejoin="round" stroke-linecap="round"'
    else:
        s += ' stroke="none"'
    return s + (" " + extra if extra else "")


def circle(cx, cy, r, fill=WHITE, sw=SW):
    return f'<circle cx="{_fmt(cx)}" cy="{_fmt(cy)}" r="{_fmt(r)}" {_attrs(fill, sw)}/>'


def ellipse(cx, cy, rx, ry, rot=0, fill=WHITE, sw=SW):
    t = f'transform="rotate({_fmt(rot)} {_fmt(cx)} {_fmt(cy)})"' if rot else ""
    return f'<ellipse cx="{_fmt(cx)}" cy="{_fmt(cy)}" rx="{_fmt(rx)}" ry="{_fmt(ry)}" {_attrs(fill, sw, t)}/>'


def rect(x, y, w, h, r=0, fill=WHITE, sw=SW, rot=0):
    t = f'transform="rotate({_fmt(rot)} {_fmt(x + w / 2)} {_fmt(y + h / 2)})"' if rot else ""
    return (f'<rect x="{_fmt(x)}" y="{_fmt(y)}" width="{_fmt(w)}" height="{_fmt(h)}" '
            f'rx="{_fmt(r)}" {_attrs(fill, sw, t)}/>')


def path(d, fill=WHITE, sw=SW):
    """Closed/filled shape from raw SVG path data."""
    return f'<path d="{d}" {_attrs(fill, sw)}/>'


def line(d, sw=SW2):
    """Open stroke only (no fill) from raw SVG path data."""
    return f'<path d="{d}" {_attrs("none", sw)}/>'


def poly(points, fill=WHITE, sw=SW, closed=True):
    d = "M" + " L".join(f"{_fmt(x)} {_fmt(y)}" for x, y in points) + (" Z" if closed else "")
    return path(d, fill, sw) if closed else line(d, sw)


def g(items, transform=""):
    body = "\n".join(items) if isinstance(items, (list, tuple)) else items
    return f'<g transform="{transform}">\n{body}\n</g>' if transform else f"<g>\n{body}\n</g>"


def place(items, x=0, y=0, s=1.0, rot=0, flip=False):
    """Move/scale/rotate/flip a group of items drawn around origin (0,0)."""
    t = f"translate({_fmt(x)} {_fmt(y)})"
    if rot:
        t += f" rotate({_fmt(rot)})"
    if flip:
        t += f" scale({_fmt(-s)} {_fmt(s)})"
    elif s != 1:
        t += f" scale({_fmt(s)})"
    return g(items, t)


# ---------------------------------------------------------------- face parts
def eye(cx, cy, r=14, look=(0, 0)):
    """Big shiny cartoon eye: solid black oval with a white sparkle."""
    lx, ly = look
    return "\n".join([
        ellipse(cx, cy, r, r * 1.15, fill=BLACK, sw=0),
        circle(cx - r * 0.32 + lx, cy - r * 0.38 + ly, r * 0.36, fill=WHITE, sw=0),
    ])


def closed_eye(cx, cy, w=16, sw=SW2):
    """Happy closed eye (upside-down U)."""
    return line(f"M{cx - w} {cy + w * 0.3} Q{cx} {cy - w * 0.9} {cx + w} {cy + w * 0.3}", sw)


def smile(cx, cy, w=20, depth=None, sw=SW2):
    d = depth if depth is not None else w * 0.7
    return line(f"M{cx - w} {cy} Q{cx} {cy + d * 2} {cx + w} {cy}", sw)


def open_smile(cx, cy, w=22, h=18, tongue=True):
    """Open happy mouth (white inside, with optional tongue)."""
    out = [path(f"M{cx - w} {cy} Q{cx} {cy + h * 2.2} {cx + w} {cy} Z", sw=SW2)]
    if tongue:
        out.append(path(f"M{cx - w * 0.45} {cy + h * 0.85} Q{cx} {cy + h * 0.35} {cx + w * 0.45} {cy + h * 0.85} "
                        f"Q{cx} {cy + h * 1.35} {cx - w * 0.45} {cy + h * 0.85} Z", sw=SW2 * 0.8))
    return "\n".join(out)


def cheek(cx, cy, r=11):
    return ellipse(cx, cy, r, r * 0.65, sw=SW2 * 0.8)


def nose(cx, cy, r=8):
    return ellipse(cx, cy, r, r * 0.7, fill=BLACK, sw=0)


# ---------------------------------------------------------------- props / scenery
def heart(cx, cy, s=30, sw=SW, rot=0):
    """Smooth classic heart, about 2s wide, centred on (cx, cy)."""
    d = (f"M0 {0.5 * s} C{-0.95 * s} {-0.05 * s} {-0.65 * s} {-0.95 * s} 0 {-0.45 * s} "
         f"C{0.65 * s} {-0.95 * s} {0.95 * s} {-0.05 * s} 0 {0.5 * s} Z")
    return place([path(d, sw=sw)], cx, cy, rot=rot)


def star(cx, cy, r=30, points=5, inner=0.5, rot=0, sw=SW):
    pts = []
    for i in range(points * 2):
        a = math.radians(-90 + rot + i * 180 / points)
        rr = r if i % 2 == 0 else r * inner
        pts.append((cx + rr * math.cos(a), cy + rr * math.sin(a)))
    return poly(pts, sw=sw)


def flower(cx, cy, r=30, petals=5, sw=SW, rot=0):
    out = []
    for i in range(petals):
        a = math.radians(rot + i * 360 / petals)
        px, py = cx + r * 0.62 * math.cos(a), cy + r * 0.62 * math.sin(a)
        out.append(ellipse(px, py, r * 0.5, r * 0.36, rot=math.degrees(a), sw=sw))
    out.append(circle(cx, cy, r * 0.36, sw=sw))
    return "\n".join(out)


def stem_flower(x, ground_y, h=90, r=26, petals=5, rot=0):
    return "\n".join([
        line(f"M{x} {ground_y} Q{x - 8} {ground_y - h / 2} {x} {ground_y - h}", SW),
        leaf(x - 2, ground_y - h * 0.4, max(30, r * 1.3), -35, sw=SW2),
        flower(x, ground_y - h, r, petals, rot=rot),
    ])


def leaf(x, y, size=30, angle=0, sw=SW2):
    """Pointed leaf whose base is at (x,y), pointing in `angle` degrees (0 = right)."""
    s = size
    d = f"M0 0 Q{s * 0.5} {-s * 0.45} {s} 0 Q{s * 0.5} {s * 0.45} 0 0 Z"
    return place([path(d, sw=sw), line(f"M{s * 0.1} 0 L{s * 0.75} 0", sw * 0.7)], x, y, rot=angle)


def cloud(cx, cy, w=160, sw=SW):
    s = w / 160
    d = ("M-70 20 C-95 20 -95 -15 -65 -15 C-65 -45 -25 -50 -15 -30 C-5 -60 45 -60 50 -25 "
         "C80 -30 90 15 65 20 Z")
    return place([path(d, sw=sw / s)], cx, cy, s)


def sun(cx, cy, r=60, rays=10, face=True):
    out = []
    for i in range(rays):
        a = math.radians(i * 360 / rays)
        a1, a2 = a - math.radians(9), a + math.radians(9)
        p = [(cx + (r + 8) * math.cos(a1), cy + (r + 8) * math.sin(a1)),
             (cx + (r + r * 0.55) * math.cos(a), cy + (r + r * 0.55) * math.sin(a)),
             (cx + (r + 8) * math.cos(a2), cy + (r + 8) * math.sin(a2))]
        out.append(poly(p))
    out.append(circle(cx, cy, r))
    if face:
        out += [eye(cx - r * 0.33, cy - r * 0.12, r * 0.13), eye(cx + r * 0.33, cy - r * 0.12, r * 0.13),
                smile(cx, cy + r * 0.22, r * 0.3), cheek(cx - r * 0.55, cy + r * 0.2, r * 0.14),
                cheek(cx + r * 0.55, cy + r * 0.2, r * 0.14)]
    return "\n".join(out)


def tree(x, ground_y, h=300, crown=120):
    """Simple cartoon tree: trunk + bumpy crown."""
    tw = crown * 0.32
    out = [path(f"M{x - tw / 2} {ground_y} L{x - tw / 2 + 6} {ground_y - h * 0.55} "
                f"L{x + tw / 2 - 6} {ground_y - h * 0.55} L{x + tw / 2} {ground_y} Z")]
    cy = ground_y - h + crown * 0.85
    for dx, dy, r in [(-0.55, 0.15, 0.55), (0.55, 0.15, 0.55), (-0.3, -0.35, 0.6), (0.3, -0.35, 0.6),
                      (0, 0.25, 0.65)]:
        out.append(circle(x + dx * crown, cy + dy * crown, r * crown))
    return "\n".join(out)


def bush(cx, ground_y, w=120):
    r = w / 4
    return "\n".join([circle(cx - r * 1.2, ground_y - r * 0.7, r), circle(cx + r * 1.2, ground_y - r * 0.7, r),
                      circle(cx, ground_y - r * 1.1, r * 1.25),
                      line(f"M{cx - w / 2 - 6} {ground_y} L{cx + w / 2 + 6} {ground_y}", SW)])


def grass_tuft(x, y, s=1.0):
    return place([line("M-14 0 Q-12 -14 -18 -26 M0 0 Q2 -18 -2 -34 M14 0 Q12 -14 20 -26", SW2)], x, y, s)


def hills(y, amp=40, x0=MARGIN_X - 5, x1=W - MARGIN_X + 5, bumps=2, bottom=H):
    """Rolling ground: white shape from y down past the frame (clipped by the frame)."""
    seg = (x1 - x0) / bumps
    d = f"M{x0} {bottom} L{x0} {y}"
    for i in range(bumps):
        sx = x0 + i * seg
        d += f" Q{sx + seg / 2} {y - amp} {sx + seg} {y}"
    d += f" L{x1} {bottom} Z"
    return path(d)


def frame():
    """Rounded border around the drawing area — gives every page a finished, book-like look."""
    return rect(MARGIN_X - 5, MARGIN_TOP - 15, (W - 2 * MARGIN_X) + 10, (MARGIN_BOTTOM - MARGIN_TOP) + 30,
                r=36, fill="none", sw=SW)


def clip_to_frame(items):
    """Clip scene items to the rounded frame so nothing spills into the margins."""
    x, y = MARGIN_X - 5, MARGIN_TOP - 15
    w, h = (W - 2 * MARGIN_X) + 10, (MARGIN_BOTTOM - MARGIN_TOP) + 30
    return (f'<clipPath id="frameclip"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="36"/></clipPath>\n'
            f'<g clip-path="url(#frameclip)">\n' + "\n".join(items) + "\n</g>")


def page(items, framed=True):
    body = clip_to_frame(items) + "\n" + frame() if framed else "\n".join(items)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="8.5in" height="11in">\n'
            f'<rect x="0" y="0" width="{W}" height="{H}" fill="{WHITE}"/>\n{body}\n</svg>\n')


# ---------------------------------------------------------------- helpers added for pages 02-11
def tube(d, w, sw=SW):
    """Outlined thick tube along an open path (arms, tails, trunks, branches)."""
    a = 'fill="none" stroke-linecap="round" stroke-linejoin="round"'
    return (f'<path d="{d}" {a} stroke="{BLACK}" stroke-width="{_fmt(w + 2 * sw)}"/>\n'
            f'<path d="{d}" {a} stroke="{WHITE}" stroke-width="{_fmt(w)}"/>')


def drop(cx, cy, s=20, rot=0, sw=SW2):
    """Water drop / teardrop, point up."""
    d = (f"M0 {-s} C{s * 0.55} {-s * 0.2} {s * 0.7} {s * 0.3} 0 {s * 0.65} "
         f"C{-s * 0.7} {s * 0.3} {-s * 0.55} {-s * 0.2} 0 {-s} Z")
    return place([path(d, sw=sw)], cx, cy, rot=rot)


def butterfly(cx, cy, s=1.0, rot=0):
    """Cute butterfly centred on its body, about 220 x 180 units at s=1."""
    half = [
        path("M0 -8 C-30 -95 -125 -100 -110 -25 C-102 12 -45 10 0 0 Z"),
        path("M0 2 C-45 10 -95 35 -75 75 C-58 102 -15 70 0 12 Z"),
        circle(-62, -40, 17, sw=SW2), circle(-48, 45, 11, sw=SW2),
    ]
    return place([
        place(half), place(half, flip=True),
        line("M-3 -48 Q-12 -82 -32 -92 M3 -48 Q12 -82 32 -92", SW2),
        circle(-34, -93, 7, sw=SW2), circle(34, -93, 7, sw=SW2),
        ellipse(0, 10, 11, 45), circle(0, -45, 15),
    ], cx, cy, s, rot)


def scallop(cx, cy, r, n=14, bump=0.32, sw=SW):
    """Scalloped round shape (lion mane, fluffy edges) as one clean outline."""
    pts = [(cx + r * math.cos(2 * math.pi * i / n), cy + r * math.sin(2 * math.pi * i / n)) for i in range(n)]
    chord = 2 * r * math.sin(math.pi / n)
    rb = chord / 2 * 1.08
    d = f"M{pts[0][0]:.1f} {pts[0][1]:.1f}"
    for i in range(1, n + 1):
        x, y = pts[i % n]
        d += f" A{rb:.1f} {rb:.1f} 0 0 1 {x:.1f} {y:.1f}"
    return path(d + " Z", sw=sw)


def big_leaf(x, y, size=150, angle=0, sw=SW):
    """Large jungle leaf with central vein + side veins, base at (x,y)."""
    s = size
    d = f"M0 0 C{s * 0.25} {-s * 0.42} {s * 0.75} {-s * 0.42} {s} 0 C{s * 0.75} {s * 0.42} {s * 0.25} {s * 0.42} 0 0 Z"
    veins = f"M{s * 0.08} 0 L{s * 0.85} 0"
    for t in (0.3, 0.5, 0.7):
        veins += f" M{s * t} 0 L{s * (t + 0.12)} {-s * 0.17} M{s * t} 0 L{s * (t + 0.12)} {s * 0.17}"
    return place([path(d, sw=sw), line(veins, SW2 * 0.8)], x, y, rot=angle)


# ---------------------------------------------------------------- helpers added for pages 12-21
def ringed_planet(cx, cy, r=80, rot=-15):
    """Planet with a ring that passes behind and in front of it."""
    ro, ri = r * 1.75, r * 1.35
    hro, hri = r * 0.45, r * 0.3
    front_fill = (f"M{-ro} 0 A{ro} {hro} 0 0 0 {ro} 0 L{ri} 0 A{ri} {hri} 0 0 1 {-ri} 0 Z")
    return place([
        ellipse(0, 0, ro, hro), ellipse(0, 0, ri, hri),
        circle(0, 0, r),
        line(f"M{-r * 0.8} {-r * 0.45} Q0 {-r * 0.6} {r * 0.8} {-r * 0.45}", SW2),
        path(front_fill, sw=0),
        line(f"M{-ro} 0 A{ro} {hro} 0 0 0 {ro} 0", SW),
        line(f"M{-ri} 0 A{ri} {hri} 0 0 0 {ri} 0", SW),
    ], cx, cy, rot=rot)


def fish_char(cx, cy, s=1.0, flip=False):
    """Cute round fish facing left (flip=True faces right)."""
    return place([
        path("M38 0 L82 -34 Q70 0 82 34 Z"),
        path("M-5 -30 Q10 -58 35 -40 L20 -25 Z", sw=SW2),
        ellipse(0, 0, 52, 36),
        line("M10 -22 Q22 0 10 22", SW2),
        eye(-24, -6, 8), smile(-36, 12, 8, sw=SW2 * 0.8),
    ], cx, cy, s, flip=flip)


def blob_shape(cx, cy, rx, ry, n=7, wobble=0.18, seed=1, sw=SW2, fill=WHITE):
    """Irregular rounded blob (giraffe spots, continents, rocks)."""
    import random
    rnd = random.Random(seed)
    pts = []
    for i in range(n):
        a = 2 * math.pi * i / n
        k = 1 + rnd.uniform(-wobble, wobble)
        pts.append((cx + rx * k * math.cos(a), cy + ry * k * math.sin(a)))
    d = ""
    for i in range(n):
        p0, p1, p2, p3 = pts[i - 1], pts[i], pts[(i + 1) % n], pts[(i + 2) % n]
        c1 = (p1[0] + (p2[0] - p0[0]) / 6, p1[1] + (p2[1] - p0[1]) / 6)
        c2 = (p2[0] - (p3[0] - p1[0]) / 6, p2[1] - (p3[1] - p1[1]) / 6)
        if i == 0:
            d += f"M{p1[0]:.1f} {p1[1]:.1f} "
        d += f"C{c1[0]:.1f} {c1[1]:.1f} {c2[0]:.1f} {c2[1]:.1f} {p2[0]:.1f} {p2[1]:.1f} "
    return path(d + "Z", fill=fill, sw=sw)


def water_drop(cx, cy, s=20, sw=SW2, rot=0):
    d = f"M0 {-s} C{s * 0.3} {-s * 0.4} {s * 0.7} 0 {s * 0.7} {s * 0.35} A{s * 0.7} {s * 0.7} 0 0 1 {-s * 0.7} {s * 0.35} C{-s * 0.7} 0 {-s * 0.3} {-s * 0.4} 0 {-s} Z"
    return place([path(d, sw=sw)], cx, cy, rot=rot)


def bubble_ring(cx, cy, r=14):
    return "\n".join([circle(cx, cy, r, sw=SW2),
                      line(f"M{cx - r * 0.55} {cy - r * 0.1} Q{cx - r * 0.5} {cy - r * 0.5} {cx - r * 0.1} {cy - r * 0.55}", SW2 * 0.7)])


def bfly(cx, cy, s=1.0, rot=0, face=True):
    """Cute butterfly: 4 wings with spots, round body, smiling head, curly antennae."""
    items = [
        line("M-8 -78 Q-20 -115 -38 -122", SW2), line("M8 -78 Q20 -115 38 -122", SW2),
        circle(-40, -124, 7, sw=SW2), circle(40, -124, 7, sw=SW2),
        path("M-6 -30 C-40 -110 -150 -120 -140 -40 C-135 0 -60 10 -6 0 Z"),
        path("M6 -30 C40 -110 150 -120 140 -40 C135 0 60 10 6 0 Z"),
        path("M-6 0 C-60 5 -120 40 -95 85 C-70 120 -20 80 -6 30 Z"),
        path("M6 0 C60 5 120 40 95 85 C70 120 20 80 6 30 Z"),
        ellipse(-78, -50, 28, 22, sw=SW2), ellipse(78, -50, 28, 22, sw=SW2),
        circle(-62, 52, 15, sw=SW2), circle(62, 52, 15, sw=SW2),
        ellipse(0, 10, 16, 62),
        circle(0, -62, 26),
    ]
    if face:
        items += [eye(-9, -65, 5), eye(9, -65, 5), smile(0, -52, 7, sw=SW2 * 0.7)]
    return place(items, cx, cy, s, rot=rot)


def tulip(x, ground_y, h=120, r=34):
    head = (f"M{x - r} {ground_y - h} C{x - r} {ground_y - h - r * 1.6} {x - r * 0.5} {ground_y - h - r * 1.2} "
            f"{x - r * 0.45} {ground_y - h - r * 1.7} L{x} {ground_y - h - r * 1.1} L{x + r * 0.45} {ground_y - h - r * 1.7} "
            f"C{x + r * 0.5} {ground_y - h - r * 1.2} {x + r} {ground_y - h - r * 1.6} {x + r} {ground_y - h} "
            f"C{x + r} {ground_y - h + r * 0.9} {x - r} {ground_y - h + r * 0.9} {x - r} {ground_y - h} Z")
    return "\n".join([
        line(f"M{x} {ground_y} L{x} {ground_y - h}", SW),
        place([path("M0 0 C30 -20 50 -50 48 -80 C20 -60 5 -30 0 0 Z", sw=SW2)], x, ground_y - 10),
        path(head),
    ])


def puff_cluster(circles, sw=SW):
    """Union of overlapping circles drawn as ONE outline (tree crowns, bushes, smoke, fluffy clouds).
    circles: list of (cx, cy, r)."""
    out = [circle(cx, cy, r, sw=sw) for cx, cy, r in circles]
    out += [circle(cx, cy, r - sw / 2 + 0.3, sw=0) for cx, cy, r in circles]
    return "\n".join(out)


def heart2(cx, cy, s=30, sw=SW, rot=0):
    """Classic smooth heart, about 2s wide, centred on (cx, cy)."""
    d = (f"M0 {0.5 * s} C{-0.95 * s} {-0.05 * s} {-0.65 * s} {-0.95 * s} 0 {-0.45 * s} "
         f"C{0.65 * s} {-0.95 * s} {0.95 * s} {-0.05 * s} 0 {0.5 * s} Z")
    return place([path(d, sw=sw)], cx, cy, rot=rot)


def rainbow_bands(cx, cy, radii):
    """Rainbow made of separate arched bands (ends sit on cy; hide them behind clouds)."""
    out = []
    for r1, r2 in zip(radii, radii[1:]):
        out.append(path(f"M{cx - r1} {cy} A{r1} {r1} 0 0 1 {cx + r1} {cy} L{cx + r2} {cy} "
                        f"A{r2} {r2} 0 0 0 {cx - r2} {cy} Z"))
    return out
