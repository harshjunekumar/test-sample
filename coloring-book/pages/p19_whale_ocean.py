"""19. Friendly whale swimming in the ocean."""
import math
from lib import *


def whale():
    return [
        # water spout
        path("M-95 -150 C-100 -190 -105 -215 -110 -235 L-80 -235 C-85 -215 -88 -190 -85 -150 Z", sw=SW2),
        path("M-95 -235 C-130 -280 -190 -280 -205 -240 C-170 -258 -140 -250 -110 -230 Z", sw=SW2),
        path("M-80 -235 C-45 -280 15 -280 30 -240 C-5 -258 -35 -250 -65 -230 Z", sw=SW2),
        water_drop(-215, -205, 18, rot=-20), water_drop(40, -205, 18, rot=20), water_drop(-95, -290, 18),
        # tail
        path("M230 -10 C270 -30 285 -60 295 -95 L330 -85 C320 -30 290 30 240 50 Z"),
        path("M310 -85 C270 -125 255 -175 275 -205 C305 -175 318 -140 315 -105 "
             "C335 -150 365 -175 400 -170 C390 -125 355 -95 310 -85 Z"),
        # body
        path("M-275 30 C-285 -100 -150 -175 0 -165 C130 -155 215 -85 255 -20 L255 40 "
             "C205 120 50 132 -80 128 C-205 124 -270 92 -275 30 Z"),
        # belly
        path("M-262 60 C-200 70 -60 82 70 76 C140 72 200 55 238 45 C200 110 50 128 -80 126 "
             "C-180 122 -245 98 -262 60 Z", sw=SW2),
        line("M-170 72 L-160 115 M-100 78 L-95 124 M-30 80 L-28 126 M40 78 L35 122 M110 72 L100 110", SW2 * 0.8),
        # flipper
        path("M-75 25 C-45 75 5 105 45 95 C25 65 -15 35 -45 17 Z"),
        # face
        eye(-170, -35, 18),
        line("M-195 -70 Q-175 -82 -152 -72", SW2),
        smile(-240, 25, 30, 14),
        cheek(-130, 5, 18),
        # spots on back
        circle(40, -110, 14, sw=SW2), circle(80, -90, 10, sw=SW2), circle(10, -80, 9, sw=SW2),
    ]


def draw():
    items = [
        line(" ".join(f"M{690 + 70 * math.cos(a):.1f} {185 + 70 * math.sin(a):.1f} "
                      f"L{690 + 100 * math.cos(a):.1f} {185 + 100 * math.sin(a):.1f}"
                      for a in [i * math.pi / 5 for i in range(10)]), SW),
        circle(690, 185, 55), eye(672, 178, 8), eye(708, 178, 8), smile(690, 198, 12),
        cloud(200, 170, 170),
        place(whale(), 375, 515, 0.98),
        # ocean surface (waves) covers whale's bottom
        path("M60 640 Q100 605 140 640 Q180 605 220 640 Q260 605 300 640 Q340 605 380 640 Q420 605 460 640 "
             "Q500 605 540 640 Q580 605 620 640 Q660 605 700 640 Q740 605 780 640 Q820 605 860 640 L860 1100 L60 1100 Z"),
        line("M120 700 Q150 685 180 700 M520 720 Q550 705 580 720", SW2),
        hills(960, amp=30, bumps=2),
        fish_char(250, 800, 1.0, flip=True), fish_char(600, 860, 0.85),
        bubble_ring(380, 760, 18), bubble_ring(410, 715, 11), bubble_ring(700, 760, 14),
        star(150, 950, 28), path("M520 990 C520 950 570 935 590 960 L555 990 Z", sw=SW2),
        place([path("M0 0 C-20 -50 15 -90 -5 -140 C25 -100 10 -50 25 0 Z")], 720, 985),
        place([path("M0 0 C-20 -50 15 -90 -5 -120 C25 -90 10 -50 25 0 Z")], 750, 990),
    ]
    return items
