"""12. Cartoon rocket exploring space."""
from lib import *


def rocket():
    return [
        # flame
        path("M-62 190 Q-80 265 -38 252 Q-30 330 0 305 Q30 330 38 252 Q80 265 62 190 Z"),
        path("M-30 195 Q-36 240 -12 236 Q0 270 12 236 Q36 240 30 195 Z", sw=SW2),
        # nozzle
        path("M-62 140 L-74 200 L74 200 L62 140 Z"),
        # side fins
        path("M-100 20 C-175 60 -190 150 -178 215 C-150 190 -120 175 -100 165 Z"),
        path("M100 20 C175 60 190 150 178 215 C150 190 120 175 100 165 Z"),
        # body
        path("M0 -285 C95 -215 120 -90 108 160 L-108 160 C-120 -90 -95 -215 0 -285 Z"),
        line("M-70 -175 Q0 -150 70 -175", SW),
        line("M-112 110 Q0 132 112 110", SW),
        # middle fin
        path("M-16 128 Q0 118 16 128 L16 205 Q0 222 -16 205 Z"),
        # window
        circle(0, -88, 52), circle(0, -88, 36, sw=SW2),
        line("M-18 -100 Q-12 -114 2 -116", SW2 * 0.8),
        # face
        eye(-38, 15, 15), eye(38, 15, 15),
        smile(0, 45, 20), cheek(-66, 42, 13), cheek(66, 42, 13),
    ]


def draw():
    items = [
        # moon crescent
        place([path("M640 140 C580 160 570 260 640 290 C590 300 535 250 540 200 C545 150 600 125 640 140 Z")], 120, 30),
        circle(205, 230, 46), circle(190, 220, 10, sw=SW2), circle(222, 248, 7, sw=SW2),
        ringed_planet(620, 860, 72, rot=-15),
        circle(150, 920, 36), circle(165, 930, 8, sw=SW2),
    ]
    for x, y, r in [(130, 120 + 30, 20), (390, 140, 16), (700, 420, 24), (120, 520, 18), (740, 700, 16),
                    (390, 960, 18), (330, 330, 12), (290, 870, 14), (140, 380, 10), (470, 960, 12)]:
        items.append(star(x, y, r, sw=SW2))
    items.append(place(rocket(), 400, 530, 1.22, rot=25))
    return items
