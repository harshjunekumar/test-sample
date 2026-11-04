"""5. Cute dinosaur eating leaves."""
import math
from lib import *


def leafy_tree():
    return [
        path("M610 870 C625 760 615 560 600 420 L700 420 C690 560 690 760 720 870 Z"),
        line("M640 520 Q648 560 640 600 M670 700 Q662 740 672 780", SW2),
        puff_cluster([(560, 330, 95), (650, 290, 110), (720, 360, 70), (600, 200, 80), (700, 210, 70),
                      (640, 410, 70)]),
        leaf(560, 250, 44, -30), leaf(690, 180, 40, 20), leaf(720, 330, 40, 60), leaf(640, 300, 44, 160),
    ]


def dino():
    cx, cy, rx, ry = 320, 700, 185, 120
    plates = []
    for deg in range(205, 330, 22):
        a = math.radians(deg)
        bx, by = cx + rx * math.cos(a), cy + ry * math.sin(a)
        nx, ny = math.cos(a) * ry, math.sin(a) * rx
        n = math.hypot(nx, ny); nx, ny = nx / n, ny / n
        tx, ty = -ny, nx
        plates.append(poly([(bx - tx * 26, by - ty * 26), (bx + nx * 42, by + ny * 42), (bx + tx * 26, by + ty * 26)]))
    near_leg = lambda x: [rect(x, 745, 78, 125, r=30), line(f"M{x + 18} 868 L{x + 18} 852 M{x + 39} 868 L{x + 39} 852 M{x + 60} 868 L{x + 60} 852", SW2)]
    far_leg = lambda x: [rect(x, 735, 70, 120, r=28)]
    return [
        path("M170 650 C110 700 100 780 82 830 C150 815 210 790 250 770 Z"),     # tail
        *far_leg(225), *far_leg(420),
        *plates,
        path("M380 620 C410 520 430 450 470 400 L575 410 C540 470 510 560 480 670 Z"),  # neck
        ellipse(cx, cy, rx, ry),
        circle(260, 660, 22, sw=SW2), circle(330, 625, 17, sw=SW2), circle(395, 670, 24, sw=SW2),
        circle(220, 720, 15, sw=SW2),
        *near_leg(180), *near_leg(375),
        # head (3/4 view, looking at the tree)
        ellipse(525, 360, 98, 78),
        ellipse(590, 395, 60, 42),
        circle(470, 295, 20, sw=SW2), circle(510, 280, 15, sw=SW2),                  # head bumps
        eye(500, 345, 17), eye(565, 340, 17),
        cheek(458, 392, 15),
        circle(600, 382, 5, fill=BLACK, sw=0), circle(628, 380, 5, fill=BLACK, sw=0),
        line("M560 412 Q595 435 630 408", SW2),
        # munching a leafy twig
        line("M625 412 L700 450", SW),
        leaf(655, 428, 54, -25, sw=SW), leaf(670, 436, 54, 40, sw=SW),
    ]


def draw():
    return [
        cloud(210, 190, 190), cloud(400, 140, 120),
        *leafy_tree(),
        hills(860, amp=40, bumps=2),
        *dino(),
        leaf(745, 560, 40, 110), leaf(705, 640, 36, 70),
        stem_flower(130, 975, 90, 32), stem_flower(560, 985, 70, 28, petals=6),
        grass_tuft(330, 980, 1.2), grass_tuft(730, 960), grass_tuft(470, 935),
    ]
