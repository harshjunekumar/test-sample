"""8. Teddy bear having a picnic."""
from lib import *


def teddy():
    return [
        # ears
        circle(-88, -138, 40), circle(88, -138, 40),
        circle(-88, -138, 21, sw=SW2), circle(88, -138, 21, sw=SW2),
        # body + arms
        ellipse(0, 120, 108, 115),
        ellipse(0, 140, 62, 76, sw=SW2),
        ellipse(-90, 105, 34, 60, rot=20), ellipse(90, 105, 34, 60, rot=-20),
        # feet with paw pads, soles facing us
        ellipse(-72, 225, 50, 54), ellipse(72, 225, 50, 54),
        ellipse(-72, 238, 24, 20, sw=SW2), ellipse(72, 238, 24, 20, sw=SW2),
        circle(-92, 202, 8, sw=SW2), circle(-72, 194, 8, sw=SW2), circle(-52, 202, 8, sw=SW2),
        circle(92, 202, 8, sw=SW2), circle(72, 194, 8, sw=SW2), circle(52, 202, 8, sw=SW2),
        # head
        ellipse(0, -60, 118, 100),
        ellipse(0, -22, 52, 40),
        ellipse(0, -40, 17, 12, fill=BLACK, sw=0),
        line("M0 -30 L0 -16 M-20 -16 Q-10 -4 0 -16 Q10 -4 20 -16", SW2),
        eye(-46, -78, 16), eye(46, -78, 16),
        cheek(-80, -30, 14), cheek(80, -30, 14),
        # bow tie
        path("M0 42 L-48 18 L-48 66 Z"), path("M0 42 L48 18 L48 66 Z"), circle(0, 42, 13),
    ]


def blanket():
    top, bot = 700, 975
    xl_t, xr_t, xl_b, xr_b = 170, 680, 80, 770
    items = [poly([(xl_t, top), (xr_t, top), (xr_b, bot), (xl_b, bot)])]
    d = ""
    for i in range(1, 6):
        t = i / 6
        d += f" M{xl_t + (xr_t - xl_t) * t:.1f} {top} L{xl_b + (xr_b - xl_b) * t:.1f} {bot}"
    for j in range(1, 4):
        t = j / 4
        y = top + (bot - top) * t
        d += f" M{xl_t + (xl_b - xl_t) * t:.1f} {y:.1f} L{xr_t + (xr_b - xr_t) * t:.1f} {y:.1f}"
    items.append(line(d, SW2))
    return items


def basket(x, y):
    return place([
        line("M-60 -10 C-60 -110 60 -110 60 -10", SW * 1.6), line("M-60 -10 C-60 -110 60 -110 60 -10", SW * 0.01),
        tube("M-58 -10 C-58 -105 58 -105 58 -10", 12),
        path("M-80 -15 L80 -15 L62 75 L-62 75 Z"),
        rect(-88, -28, 176, 26, r=10),
        line("M-70 22 L70 22 M-66 48 L66 48 M-35 -2 L-30 75 M0 -2 L0 75 M35 -2 L30 75", SW2 * 0.8),
    ], x, y)


def cupcake(x, y, s=1.0):
    return place([
        path("M-45 0 L45 0 L34 60 L-34 60 Z"),
        line("M-22 0 L-18 60 M0 0 L0 60 M22 0 L18 60", SW2 * 0.8),
        path("M-52 2 C-62 -30 -30 -40 -20 -38 C-15 -65 25 -65 25 -38 C45 -45 65 -20 52 2 Z"),
        circle(0, -62, 12),
    ], x, y, s)


def teacup(x, y):
    return place([
        ellipse(0, 40, 60, 14),
        path("M-40 -10 L40 -10 C40 30 20 40 0 40 C-20 40 -40 30 -40 -10 Z"),
        line("M40 0 C65 0 65 25 34 25", SW2),
        heart(0, 12, 14, sw=SW2),
        line("M-10 -25 Q-18 -38 -8 -50 M10 -25 Q2 -38 12 -50", SW2 * 0.8),
    ], x, y)


def draw():
    return [
        cloud(200, 190, 160), cloud(640, 230, 130),
        bush(150, 700, 190), bush(710, 700, 160),
        hills(690, amp=15, bumps=1),
        *blanket(),
        place(teddy(), 425, 575, 1.12),
        basket(665, 880), cupcake(185, 870, 1.0), teacup(425, 935),
    ]
