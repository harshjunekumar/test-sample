"""9. Happy unicorn with a rainbow."""
from lib import *


def unicorn():
    return [
        # flowing tail
        path("M-110 -25 C-175 -45 -210 20 -185 80 C-170 115 -200 150 -232 140 "
             "C-200 185 -125 160 -128 95 C-130 50 -118 20 -100 15 Z"),
        line("M-160 30 C-175 70 -160 100 -175 125 M-140 20 C-150 60 -140 90 -150 120", SW2 * 0.8),
        # far legs
        rect(-72, 35, 40, 120, r=18), rect(62, 35, 40, 120, r=18),
        # neck
        path("M45 -40 L92 -160 L172 -128 L115 15 Z"),
        # body
        ellipse(0, 0, 122, 76),
        star(-55, -10, 22, sw=SW2), heart2(-10, 25, 16, sw=SW2),  # cute marks on the hip
        # near legs + hooves
        rect(-108, 40, 46, 130, r=20), rect(32, 40, 46, 130, r=20),
        line("M-108 145 L-62 145 M32 145 L78 145", SW2),
        # wavy mane down the neck
        path("M120 -238 C70 -255 40 -225 52 -195 C20 -188 10 -150 32 -132 C2 -120 4 -82 30 -72 "
             "C18 -42 42 -20 64 -32 L104 -150 Z"),
        line("M95 -225 C70 -210 70 -190 82 -180 M70 -160 C50 -140 52 -120 64 -110", SW2 * 0.8),
        # ear, horn, head + snout
        path("M100 -215 L92 -268 L135 -232 Z"),
        path("M128 -222 L176 -338 L168 -218 Z"),
        line("M147 -258 L170 -263 M156 -284 L171 -287", SW2 * 0.8),
        circle(135, -172, 72),
        ellipse(192, -140, 46, 36, rot=15),
        circle(214, -142, 4.5, fill=BLACK, sw=0),
        line("M188 -114 Q205 -104 222 -118", SW2),
        # face
        eye(140, -175, 17, look=(3, 0)),
        cheek(118, -138, 13),
    ]


def rainbow(cx, cy, radii):
    out = []
    for r in radii:
        out.append(path(f"M{cx - r} {cy} A{r} {r} 0 0 1 {cx + r} {cy} Z"))
    return out


def draw():
    return [
        *rainbow_bands(425, 790, [370, 326, 282, 238, 194, 150]),
        cloud(150, 782, 230), cloud(700, 782, 230),
        hills(800, amp=30, bumps=2),
        place(unicorn(), 375, 640, 1.12),
        star(150, 200, 26), star(700, 190, 24), star(560, 130, 18), star(270, 130, 18),
        stem_flower(130, 975, 90, 30), stem_flower(730, 980, 90, 32, petals=6),
        grass_tuft(560, 985), grass_tuft(300, 990),
    ]
