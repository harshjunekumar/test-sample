"""4. Friendly lion sitting in the jungle."""
from lib import *


def lion():
    return [
        # tail with tuft
        tube("M80 200 C170 220 200 160 190 110", 26),
        path("M190 115 C160 90 175 50 195 40 C215 55 225 95 190 115 Z"),
        # body
        ellipse(0, 150, 100, 112),
        ellipse(0, 175, 52, 70, sw=SW2),
        ellipse(-82, 238, 54, 32), ellipse(82, 238, 54, 32),
        path("M-62 245 L-60 160 Q-40 135 -20 160 L-18 245 Z"),
        path("M62 245 L60 160 Q40 135 20 160 L18 245 Z"),
        ellipse(-40, 252, 36, 21), ellipse(40, 252, 36, 21),
        line("M-48 246 L-48 264 M-32 246 L-32 264 M32 246 L32 264 M48 246 L48 264", SW2 * 0.8),
        # mane
        scallop(0, -60, 158, n=14),
        # ears
        circle(-72, -135, 30), circle(72, -135, 30),
        circle(-72, -135, 15, sw=SW2), circle(72, -135, 15, sw=SW2),
        # face
        circle(0, -60, 100),
        eye(-38, -82, 18), eye(38, -82, 18),
        line("M-58 -118 Q-40 -128 -22 -118 M22 -118 Q40 -128 58 -118", SW2),
        cheek(-66, -38, 14), cheek(66, -38, 14),
        ellipse(-22, -22, 28, 22), ellipse(22, -22, 28, 22),
        path("M-18 -48 L18 -48 L0 -28 Z", fill=BLACK, sw=SW2 * 0.7),
        line("M0 -28 L0 -18", SW2 * 0.8),
        path("M-14 2 Q0 -6 14 2 Q10 18 0 18 Q-10 18 -14 2 Z", sw=SW2 * 0.8),
        circle(-30, -20, 3, fill=BLACK, sw=0), circle(-18, -12, 3, fill=BLACK, sw=0),
        circle(30, -20, 3, fill=BLACK, sw=0), circle(18, -12, 3, fill=BLACK, sw=0),
    ]


def draw():
    return [
        # vines hanging from the top
        tube("M110 70 Q130 200 105 330", 14), leaf(116, 160, 60, 20), leaf(112, 260, 60, 160),
        tube("M740 70 Q720 180 745 270", 14), leaf(732, 150, 60, 160), leaf(740, 230, 55, 20),
        tube("M430 70 Q445 110 425 150", 12), leaf(430, 130, 50, 30),
        hills(800, amp=40, bumps=2),
        # jungle leaves on both sides
        big_leaf(80, 820, 200, -55), big_leaf(80, 900, 220, -25), big_leaf(110, 980, 170, -5),
        big_leaf(770, 820, 200, -125), big_leaf(770, 900, 220, -155), big_leaf(740, 980, 170, -175),
        place(lion(), 425, 560, 1.28),
        grass_tuft(300, 980), grass_tuft(560, 985, 1.1),
    ]
