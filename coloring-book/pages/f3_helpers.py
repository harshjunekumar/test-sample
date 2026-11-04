"""Shared helpers for pages 22-30 (not a page itself: build.py only loads pNN_*.py)."""
import math
from lib import *


def face(cx, cy, s=1.0, open_mouth=False):
    out = [eye(cx - 22 * s, cy, 11 * s), eye(cx + 22 * s, cy, 11 * s)]
    if open_mouth:
        out.append(open_smile(cx, cy + 18 * s, 15 * s, 10 * s))
    else:
        out.append(smile(cx, cy + 20 * s, 13 * s, sw=SW2))
    out += [cheek(cx - 40 * s, cy + 18 * s, 9 * s), cheek(cx + 40 * s, cy + 18 * s, 9 * s)]
    return out


def arm_end(sx, sy, angle, length=80):
    a = math.radians(angle)
    return sx - length * math.sin(a), sy + length * math.cos(a)


def arm(sx, sy, angle):
    """Arm from shoulder (sx,sy); angle 0 = straight down, +90 = pointing left, -90 = right, 180 = up."""
    return place([rect(-14, -8, 28, 88, r=14), circle(0, 80, 17)], sx, sy, rot=angle)


def child(girl=True, arms=(30, -30), hair_style=0):
    """Cartoon child, feet at (0,0), ~350 units tall. Shoulders at (+-40, -195)."""
    out = []
    if girl:
        if hair_style == 0:   # pigtails
            out += [circle(-78, -292, 30), circle(78, -292, 30)]
        else:                 # long hair
            out.append(path("M-82 -270 Q-90 -356 0 -356 Q90 -356 82 -270 L88 -196 Q66 -176 50 -200 "
                            "L-50 -200 Q-66 -176 -88 -196 Z"))
    out += [rect(-36, -112, 28, 100, r=13), rect(8, -112, 28, 100, r=13),
            ellipse(-27, -10, 29, 16), ellipse(27, -10, 29, 16)]
    out += [arm(-42, -192, arms[0]), arm(42, -192, arms[1])]
    if girl:
        out += [path("M-38 -214 Q0 -226 38 -214 L80 -96 Q0 -78 -80 -96 Z"),
                line("M-60 -126 Q0 -112 60 -126", SW2)]
    else:
        out += [path("M-44 -100 L-46 -140 L46 -140 L44 -100 Q0 -92 -44 -100 Z"),
                rect(-50, -214, 100, 86, r=26), line("M0 -126 L0 -100", SW2)]
    out.append(circle(0, -272, 66))
    if girl:
        out.append(path("M-66 -268 Q-70 -350 0 -350 Q70 -350 66 -268 Q62 -304 36 -306 Q20 -288 0 -306 "
                        "Q-20 -288 -36 -306 Q-62 -304 -66 -268 Z"))
        if hair_style == 0:
            out.append(heart(50, -326, 14, sw=SW2))
    else:
        out.append(path("M-66 -272 Q-66 -350 0 -348 Q66 -350 66 -272 Q50 -300 28 -294 "
                        "Q8 -312 -12 -296 Q-36 -310 -66 -272 Z"))
    out += face(0, -258, 1.0, open_mouth=True)
    return out


def bunny():
    """Small sitting bunny, base at (0,0), ~200 tall."""
    return [
        ellipse(0, -55, 62, 58), ellipse(-30, -8, 30, 14), ellipse(30, -8, 30, 14),
        ellipse(-28, -195, 18, 55, rot=-12), ellipse(-28, -195, 8, 38, rot=-12, sw=SW2),
        ellipse(28, -195, 18, 55, rot=12), ellipse(28, -195, 8, 38, rot=12, sw=SW2),
        circle(0, -125, 52),
        eye(-20, -132, 9), eye(20, -132, 9), nose(0, -114, 6),
        line("M0 -110 Q-10 -96 -16 -102 M0 -110 Q10 -96 16 -102", SW2 * 0.8),
        cheek(-34, -110, 8), cheek(34, -110, 8),
    ]
