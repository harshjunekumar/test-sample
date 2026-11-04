"""17. Cute giraffe eating leaves."""
from lib import *


def leg(x, top, bottom, w=46):
    """Slightly tapered leg with a rounded hoof and a knee line."""
    return [
        path(f"M{x - w / 2} {top} L{x - w / 2 + 4} {bottom - 30} L{x + w / 2 - 4} {bottom - 30} L{x + w / 2} {top} Z"),
        rect(x - w / 2 - 2, bottom - 34, w + 4, 36, r=12),
        line(f"M{x - 12} {top + (bottom - top) * 0.5} Q{x} {top + (bottom - top) * 0.5 + 8} {x + 12} {top + (bottom - top) * 0.5}", SW2),
    ]


def tree():
    return [
        path("M610 900 C630 780 630 560 625 420 L715 420 C710 560 715 780 745 900 Z"),
        line("M655 560 Q664 600 656 640 M690 720 Q682 760 694 800", SW2),
        puff_cluster([(560, 330, 85), (660, 290, 105), (720, 380, 60), (610, 190, 80), (705, 200, 65),
                      (650, 410, 65)]),
        leaf(610, 300, 44, 200), leaf(700, 190, 40, 20), leaf(720, 360, 40, 60), leaf(600, 175, 40, -60),
    ]


def giraffe():
    neck_pts = [(372 + (488 - 372) * t, 600 + (300 - 600) * t) for t in [i / 7 for i in range(8)]]
    mane = [circle(x - 14, y - 2, 17, sw=SW2) for x, y in neck_pts[1:]]
    return [
        # tail
        line("M165 610 Q130 660 140 720", SW),
        drop(140, 735, 18, rot=180, sw=SW2),
        # far legs
        *leg(235, 650, 905, 42), *leg(395, 650, 905, 42),
        *leg(195, 640, 930), *leg(360, 640, 930),
        # mane + neck (behind body)
        *mane,
        path("M360 640 C390 520 440 400 470 280 L560 300 C520 400 455 520 430 655 Z"),
        # body
        ellipse(300, 620, 160, 95),
        blob_shape(240, 600, 42, 30, seed=3), blob_shape(345, 590, 38, 28, seed=5),
        blob_shape(300, 668, 30, 20, seed=7), blob_shape(190, 655, 22, 18, seed=9),
        blob_shape(420, 620, 22, 26, seed=11),
        blob_shape(455, 480, 22, 30, seed=2), blob_shape(497, 375, 18, 24, seed=4),
        # ossicones + ears
        line("M495 205 L488 150 M560 205 L570 150", SW),
        circle(487, 140, 16), circle(571, 140, 16),
        ellipse(430, 215, 42, 18, rot=-20), ellipse(630, 215, 42, 18, rot=20),
        line("M405 222 L450 208 M655 222 L612 208", SW2 * 0.8),
        # head
        ellipse(530, 250, 85, 72),
        ellipse(548, 312, 70, 46),
        eye(500, 240, 17), eye(565, 240, 17),
        cheek(465, 285, 14), cheek(610, 280, 13),
        circle(530, 302, 6, fill=BLACK, sw=0), circle(568, 302, 6, fill=BLACK, sw=0),
        line("M518 330 Q550 350 582 330", SW2),
        # leafy twig in mouth
        line("M585 335 L660 360", SW),
        leaf(612, 344, 52, -35, sw=SW), leaf(630, 350, 52, 30, sw=SW),
    ]


def draw():
    return [
        cloud(200, 190, 180), cloud(250, 370, 110),
        *tree(),
        hills(890, amp=40, bumps=2),
        *giraffe(),
        leaf(740, 600, 38, 100), leaf(560, 720, 34, 60),
        stem_flower(560, 985, 80, 30), stem_flower(720, 975, 70, 28, petals=6),
        grass_tuft(110, 975), grass_tuft(300, 985, 1.2), grass_tuft(460, 965),
    ]
