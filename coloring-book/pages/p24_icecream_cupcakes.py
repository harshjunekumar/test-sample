"""24. Ice cream and cupcakes."""
from lib import *
from pages.f3_helpers import face


def cone():
    tri = "M-95 0 L95 0 L0 330 Z"
    lines = ""
    for i in range(-4, 5):
        x = i * 48
        lines += f"M{x - 200} -10 L{x + 200} 390 M{x + 200} -10 L{x - 200} 390 "
    return [
        path(tri),
        f'<clipPath id="conec"><path d="{tri}"/></clipPath>',
        f'<g clip-path="url(#conec)">{line(lines, SW2)}</g>',
        path(tri, fill="none"),
    ]


def scoop(r, drips=True):
    d = f"M{-r} 0 A{r} {r} 0 0 1 {r} 0"
    if drips:
        d += (f" Q{r} {r * 0.25} {r * 0.75} {r * 0.25} Q{r * 0.55} {r * 0.25} {r * 0.5} {r * 0.5} "
              f"Q{r * 0.38} {r * 0.7} {r * 0.26} {r * 0.5} Q{r * 0.2} {r * 0.25} 0 {r * 0.25} "
              f"Q{-r * 0.25} {r * 0.25} {-r * 0.35} {r * 0.42} Q{-r * 0.47} {r * 0.6} {-r * 0.58} {r * 0.38} "
              f"Q{-r * 0.65} {r * 0.25} {-r * 0.8} {r * 0.25} Q{-r} {r * 0.25} {-r} 0 Z")
    else:
        d += f" Q{r} {r * 0.25} 0 {r * 0.25} Q{-r} {r * 0.25} {-r} 0 Z"
    return path(d)


def cupcake(topper="cherry"):
    out = [
        # frosting swirl (back to front)
        ellipse(0, -175, 120, 48), ellipse(0, -222, 92, 40), ellipse(0, -262, 60, 32),
    ]
    if topper == "cherry":
        out += [line("M0 -290 Q8 -330 30 -342", SW2), circle(0, -300, 26)]
    else:
        out += [star(0, -312, 36, sw=SW)]
    out += [path("M-110 -150 L110 -150 L84 0 L-84 0 Z")]  # wrapper
    out += [line("M-75 -150 L-60 0 M75 -150 L60 0", SW2)]
    out += [ellipse(-60, -205, 10, 6, rot=30, sw=SW2 * 0.8), ellipse(52, -200, 10, 6, rot=-30, sw=SW2 * 0.8),
            ellipse(-20, -248, 10, 6, rot=-20, sw=SW2 * 0.8), ellipse(30, -262, 10, 6, rot=40, sw=SW2 * 0.8),
            ellipse(5, -180, 10, 6, rot=10, sw=SW2 * 0.8)]
    return out


def draw():
    items = [
        heart(150, 200, 48, rot=-12), star(700, 190, 46, rot=10), star(160, 470, 30), heart(705, 440, 36, rot=12),
        star(430, 135, 28, rot=-8),
        line("M75 950 L775 950", SW),  # table edge
    ]
    ice = cone() + [
        place([scoop(105)], 0, -5),
    ]
    items += [place(cone(), 425, 560)]
    items += [place([scoop(108)], 425, 540)]
    items += [place([scoop(92)], 425, 420)]
    items += [line("M425 290 Q440 245 468 232", SW2), circle(425, 305, 30)]
    items += face(425, 395, 1.2)
    items += [rect(395, 470, 22, 9, r=4, rot=30, sw=SW2 * 0.8), rect(455, 480, 22, 9, r=4, rot=-25, sw=SW2 * 0.8)]
    items += face(425, 640, 0.9) if False else []
    items += [place(cupcake("cherry"), 200, 950, 0.88)]
    items += face(200, 880, 0.9, open_mouth=True)
    items += [place(cupcake("star"), 650, 950, 0.88)]
    items += face(650, 880, 0.9)
    return items
