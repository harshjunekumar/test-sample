"""11. Cute farm animals."""
from lib import *


def cow():
    return [
        rect(-72, 50, 42, 100, r=14), rect(30, 50, 42, 100, r=14),
        line("M-72 128 L-30 128 M30 128 L72 128", SW2),
        line("M95 20 C130 30 130 80 120 105", SW2), ellipse(120, 112, 10, 14, sw=SW2),
        ellipse(0, 35, 105, 82),
        path("M-80 60 C-75 30 -35 30 -35 60 C-30 90 -70 100 -78 80 Z", sw=SW2),
        path("M35 40 C45 20 80 25 78 50 C78 75 42 78 36 62 Z", sw=SW2),
        # horns + ears
        path("M-45 -150 C-60 -175 -55 -195 -40 -205 C-38 -185 -25 -170 -20 -158 Z", sw=SW2),
        path("M45 -150 C60 -175 55 -195 40 -205 C38 -185 25 -170 20 -158 Z", sw=SW2),
        ellipse(-100, -110, 42, 20, rot=20), ellipse(100, -110, 42, 20, rot=-20),
        ellipse(0, -95, 86, 80),
        ellipse(38, -122, 30, 26, sw=SW2),
        ellipse(0, -45, 70, 42),
        ellipse(-25, -50, 8, 11, fill=BLACK, sw=0), ellipse(25, -50, 8, 11, fill=BLACK, sw=0),
        smile(0, -25, 20, 7),
        eye(-36, -110, 14), eye(38, -112, 14),
        cheek(-66, -75, 11), cheek(66, -75, 11),
    ]


def pig():
    return [
        rect(-62, 60, 36, 62, r=12), rect(26, 60, 36, 62, r=12),
        line("M-44 106 L-44 122 M44 106 L44 122", SW2 * 0.8),
        line("M92 10 C125 0 128 -28 110 -30 C95 -32 96 -10 116 -14", SW2),
        ellipse(0, 20, 100, 74),
        path("M-72 -120 L-95 -185 L-28 -150 Z"), path("M72 -120 L95 -185 L28 -150 Z"),
        circle(0, -80, 80),
        ellipse(0, -55, 36, 26),
        ellipse(-12, -55, 6, 9, fill=BLACK, sw=0), ellipse(12, -55, 6, 9, fill=BLACK, sw=0),
        smile(0, -22, 16, 6),
        eye(-32, -100, 13), eye(32, -100, 13),
        cheek(-56, -60, 11), cheek(56, -60, 11),
    ]


def chick():
    return [
        line("M-15 50 L-18 72 M-30 74 L-18 72 L-8 78 M15 50 L18 72 M8 78 L18 72 L30 74", SW2),
        circle(0, 0, 56),
        ellipse(36, 18, 22, 13, rot=-35, sw=SW2),
        line("M-4 -56 Q-10 -78 4 -84 M4 -56 Q10 -74 22 -72", SW2),
        path("M-12 -2 L0 -14 L12 -2 L0 10 Z", sw=SW2),
        line("M-12 -2 L12 -2", SW2 * 0.6),
        eye(-20, -22, 9), eye(20, -22, 9),
        cheek(-34, 4, 8), cheek(34, 4, 8),
    ]


def barn():
    return [
        path("M300 660 L300 455 L430 365 L560 455 L560 660 Z"),
        poly([(278, 468), (430, 345), (582, 468), (562, 482), (430, 380), (298, 482)]),
        rect(372, 520, 116, 140),
        line("M372 520 L488 660 M488 520 L372 660 M430 520 L430 660", SW2),
        circle(430, 445, 26), line("M404 445 L456 445 M430 419 L430 471", SW2),
    ]


def fence(y0, y1, x0=70, x1=780, step=78):
    out = [rect(x0, y0 + 18, x1 - x0, 22), rect(x0, y0 + 62, x1 - x0, 22)]
    x = x0 + 10
    while x < x1:
        out.append(path(f"M{x} {y1} L{x} {y0} L{x + 14} {y0 - 16} L{x + 28} {y0} L{x + 28} {y1} Z"))
        x += step
    return out


def draw():
    return [
        sun(690, 190, 50, rays=10),
        cloud(190, 180, 160),
        *barn(),
        *fence(600, 720),
        hills(700, amp=20, bumps=1),
        place(cow(), 220, 760, 1.2),
        place(pig(), 632, 790, 1.1),
        place(chick(), 432, 900, 1.15),
        grass_tuft(110, 995), grass_tuft(745, 995), grass_tuft(560, 995),
    ]
