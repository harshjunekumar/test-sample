"""22. Happy dinosaur family."""
import math
from lib import *


def dino():
    """Cute long-neck dinosaur facing right, feet at y=0, ~470 tall."""
    out = [
        path("M-120 -175 Q-230 -170 -272 -62 Q-262 -50 -246 -60 Q-200 -105 -118 -105 Z"),  # tail
        rect(-108, -115, 52, 112, r=22), rect(-48, -115, 52, 108, r=22),
        rect(40, -115, 52, 108, r=22), rect(92, -115, 50, 112, r=22),  # legs
    ]
    for t in (205, 228, 251, 274, 297):  # back plates
        a = math.radians(t)
        bx, by = 150 * math.cos(a), -155 + 95 * math.sin(a)
        nx, ny = math.cos(a) / 150, math.sin(a) / 95
        n = math.hypot(nx, ny); nx, ny = nx / n, ny / n
        tx, ty = -ny, nx
        out.append(path(f"M{bx - tx * 24} {by - ty * 24} Q{bx + nx * 44 - tx * 6} {by + ny * 44 - ty * 6} "
                        f"{bx + nx * 46} {by + ny * 46} Q{bx + nx * 44 + tx * 6} {by + ny * 44 + ty * 6} "
                        f"{bx + tx * 24} {by + ty * 24} Z"))
    out += [
        path("M60 -215 Q118 -300 112 -385 L198 -385 Q205 -270 130 -140 Z"),  # neck
        ellipse(0, -155, 152, 98),
        line("M-118 -100 Q0 -66 125 -105", SW2),  # belly line
        ellipse(-50, -185, 26, 17, sw=SW2), ellipse(15, -208, 18, 12, sw=SW2), ellipse(-95, -150, 16, 11, sw=SW2),
        ellipse(160, -405, 80, 58),
        line("M150 -365 Q185 -350 215 -372", SW2),  # smile
        eye(170, -420, 15), cheek(205, -390, 12), ellipse(225, -415, 5, 3.5, fill=BLACK, sw=0),
    ]
    for x in (-82, -22, 66, 117):
        out.append(line(f"M{x - 12} -4 L{x - 12} -18 M{x} -2 L{x} -18 M{x + 12} -4 L{x + 12} -18", SW2 * 0.7))
    return out


def baby_in_egg():
    return [
        circle(0, -175, 54),
        eye(-19, -182, 10), eye(19, -182, 10), open_smile(0, -158, 14, 8, tongue=False),
        cheek(-35, -163, 7), cheek(35, -163, 7),
        path("M-80 -110 L-56 -134 L-32 -108 L-8 -134 L16 -108 L40 -134 L62 -108 L82 -124 "
             "Q98 -18 0 0 Q-98 -18 -80 -110 Z"),
        ellipse(-36, -55, 15, 10, sw=SW2), ellipse(30, -40, 19, 12, sw=SW2),
        path("M-40 -220 L-20 -204 L0 -220 L20 -204 L40 -220 Q32 -264 0 -264 Q-32 -264 -40 -220 Z", sw=SW2),
    ]


def draw():
    return [
        sun(185, 205, 52, rays=10), cloud(470, 165, 150),
        # volcano with puffy smoke
        cloud(650, 300, 150),
        path("M500 900 L595 365 Q645 345 695 365 L790 900 Z"),
        path("M595 365 Q615 420 635 390 Q655 430 675 395 Q685 410 695 365", fill="none", sw=SW2),
        hills(860, amp=30, bumps=2),
        place(dino(), 330, 880, 0.95),
        place(dino(), 675, 945, 0.48, flip=True),
        place(baby_in_egg(), 500, 1000, 0.95),
        grass_tuft(110, 990), grass_tuft(755, 1000),
    ]
