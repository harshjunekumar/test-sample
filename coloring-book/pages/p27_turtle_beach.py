"""27. Baby turtle at the beach."""
from lib import *


def turtle():
    """Side-view baby turtle facing right, belly at y=0."""
    hexa = [(-45, -150), (45, -150), (78, -95), (45, -40), (-45, -40), (-78, -95)]
    return [
        path("M-150 -10 Q-205 -20 -215 -45 Q-180 -45 -150 -40 Z"),  # tail
        ellipse(-105, 18, 48, 26, rot=-15), ellipse(95, 20, 50, 26, rot=15),  # flippers
        path("M140 -50 Q185 -70 200 -110 L260 -95 Q240 -20 150 0 Z"),  # neck
        circle(245, -130, 68),  # head
        eye(262, -148, 15), open_smile(268, -110, 22, 12, tongue=False), cheek(225, -105, 12),
        path("M-175 -5 Q-170 -205 0 -210 Q170 -205 175 -5 Z"),  # shell dome
        path("M-195 0 Q-195 -24 -170 -24 L170 -24 Q195 -24 195 0 Q195 22 170 22 L-170 22 Q-195 22 -195 0 Z"),  # rim
        poly(hexa, sw=SW2),
        line("M-45 -150 L-70 -200 M45 -150 L70 -200 M78 -95 L158 -95 M-78 -95 L-158 -95 "
             "M45 -40 L70 -24 M-45 -40 L-70 -24", SW2),
        line("M-120 -24 L-120 22 M-60 -24 L-60 22 M0 -24 L0 22 M60 -24 L60 22 M120 -24 L120 22", SW2 * 0.8),
    ]


def starfish(x, y, r=40, rot=0):
    return [star(x, y, r, inner=0.45, rot=rot), circle(x, y, r * 0.12, sw=SW2)]


def shell(x, y, s=1.0):
    return place([
        path("M-45 0 Q-50 -60 0 -62 Q50 -60 45 0 Q0 12 -45 0 Z"),
        line("M0 -60 L0 4 M-25 -54 L-15 4 M25 -54 L15 4", SW2),
        path("M-14 4 L14 4 L10 18 L-10 18 Z", sw=SW2),
    ], x, y, s)


def draw():
    items = [
        sun(680, 200, 55), cloud(240, 175, 170),
        # sailboat on the horizon
        path("M470 300 L470 190 L540 290 Z"), path("M462 300 L462 210 L415 290 Z"),
        path("M405 305 L555 305 Q545 340 515 340 L440 340 Q412 340 405 305 Z"),
        line("M66 340 L790 340", SW),  # horizon
        line("M110 395 Q140 375 170 395 Q200 415 230 395 M520 410 Q550 390 580 410 Q610 430 640 410 "
             "M300 460 Q330 440 360 460 Q390 480 420 460", SW2),
        # sand with wavy shoreline
        path("M66 560 Q160 520 250 555 Q340 590 430 550 Q520 510 610 550 Q700 590 790 545 L790 1100 L66 1100 Z"),
        place(turtle(), 360, 870, 1.25),
    ]
    items += starfish(150, 960, 46, 10) + starfish(150, 640, 34, -12)
    items += [shell(660, 985, 1.0)]
    return items
