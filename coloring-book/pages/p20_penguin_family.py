"""20. Cute family of penguins."""
from lib import *


def penguin(kind="adult"):
    items = [
        # flippers
        ellipse(-92, 15, 24, 66, rot=22), ellipse(92, 15, 24, 66, rot=-22),
        # body
        ellipse(0, 0, 100, 135),
        # white belly + face mask
        path("M-38 -100 C-75 -105 -88 -50 -70 -5 C-60 40 -70 90 -40 115 C-15 132 15 132 40 115 "
             "C70 90 60 40 70 -5 C88 -50 75 -105 38 -100 C20 -98 8 -80 0 -70 C-8 -80 -20 -98 -38 -100 Z",
             sw=SW2),
        # feet
        path("M-70 130 Q-60 108 -30 118 Q-10 125 -8 140 Q-40 150 -70 130 Z"),
        path("M70 130 Q60 108 30 118 Q10 125 8 140 Q40 150 70 130 Z"),
        # face
        eye(-30, -58, 13), eye(30, -58, 13),
        path("M-20 -36 Q0 -48 20 -36 Q0 -6 -20 -36 Z", sw=SW2),
        cheek(-55, -30, 11), cheek(55, -30, 11),
    ]
    if kind == "dad":
        items += [path("M0 22 L-34 4 L-34 40 Z", sw=SW2), path("M0 22 L34 4 L34 40 Z", sw=SW2), circle(0, 22, 9, sw=SW2)]
    if kind == "mom":
        items += [place([path("M0 0 C-30 -30 -55 -5 -40 15 C-30 25 -10 15 0 0 Z", sw=SW2),
                         path("M0 0 C30 -30 55 -5 40 15 C30 25 10 15 0 0 Z", sw=SW2),
                         circle(0, 0, 10, sw=SW2)], 45, -118, rot=20),
                  heart(0, 30, 26, sw=SW2)]
    if kind == "baby":
        items += [line("M-10 -134 Q-5 -158 6 -150 M2 -134 Q12 -156 20 -144", SW2)]
    return items


def draw():
    items = [
        # snowy mountains / iceberg + igloo in back
        path("M70 560 L200 380 L260 450 L340 330 L480 560 Z"),
        line("M170 420 L200 440 L225 420 M310 370 L340 390 L365 370", SW2),
        path("M520 560 L520 500 A110 110 0 0 1 740 500 L740 560 Z"),
        path("M595 560 L595 520 A35 35 0 0 1 665 520 L665 560 Z"),
        line("M530 470 L730 470 M520 520 L595 520 M665 520 L740 520 M560 420 L700 420", SW2),
        line("M580 420 L580 470 M630 380 L630 420 M680 420 L680 470 M555 470 L555 520 M705 470 L705 520", SW2),
        hills(560, amp=0, bumps=1),
        line("M60 610 Q300 590 520 620 Q700 640 800 615", SW2),
        place(penguin("dad"), 210, 720, 1.2),
        place(penguin("mom"), 575, 730, 1.1),
        place(penguin("baby"), 390, 860, 0.62),
        place(penguin("baby"), 705, 895, 0.55),
    ]
    for x, y, r in [(120, 170, 22), (300, 230, 18), (470, 150, 24), (640, 230, 18), (740, 140, 20), (200, 300, 14)]:
        items.append(star(x, y, r, points=6, inner=0.45, sw=SW2))
    return items
