"""18. Little astronaut on the moon."""
from lib import *


def astronaut():
    return [
        # backpack
        rect(-118, -40, 236, 190, 30),
        # legs + boots
        rect(-72, 150, 58, 110, 22), rect(14, 150, 58, 110, 22),
        path("M-90 250 Q-92 210 -60 210 L-10 210 L-6 275 L-92 275 Z"),
        path("M90 250 Q92 210 60 210 L10 210 L6 275 L92 275 Z"),
        # body
        rect(-95, -20, 190, 200, 60),
        line("M-92 140 L92 140", SW2),
        rect(-50, 20, 100, 70, 14, sw=SW2),
        star(-12, 55, 24, sw=SW2), circle(28, 40, 8, sw=SW2), circle(28, 70, 8, sw=SW2),
        # left arm waving
        path("M-80 10 C-130 -20 -150 -70 -160 -120 L-122 -132 C-112 -90 -95 -60 -60 -40 Z"),
        circle(-142, -150, 30),
        # right arm holding flag pole
        path("M80 10 C120 30 140 60 150 90 L115 105 C108 82 95 60 62 46 Z"),
        circle(135, 110, 28),
        # helmet
        circle(0, -150, 130),
        ellipse(0, -140, 95, 82),
        line("M-62 -190 Q-45 -210 -20 -212", SW2),
        rect(-8, -310, 16, 40, 8), circle(0, -318, 16),
        # face inside visor
        eye(-32, -145, 14), eye(32, -145, 14),
        open_smile(0, -110, 22, 14),
        cheek(-62, -115, 13), cheek(62, -115, 13),
    ]


def draw():
    items = [
        # earth
        circle(650, 220, 80),
        blob_shape(625, 195, 32, 24, seed=2), blob_shape(680, 255, 26, 18, seed=4), blob_shape(600, 260, 14, 12, seed=6),
        hills(820, amp=40, bumps=2),
        ellipse(160, 920, 70, 22), ellipse(160, 914, 56, 14, sw=SW2),
        ellipse(620, 960, 90, 26), ellipse(620, 953, 72, 17, sw=SW2),
        ellipse(410, 990, 40, 12),
        # flag
        line("M610 520 L610 860", SW),
        path("M610 520 L760 545 Q730 580 760 615 L610 600 Z"),
        star(670, 565, 22, sw=SW2),
        place(astronaut(), 390, 560, 1.12),
    ]
    for x, y, r in [(150, 170, 22), (330, 140, 16), (480, 220, 12), (140, 420, 14), (230, 300, 10),
                    (740, 390, 18), (520, 120, 14), (760, 140, 12)]:
        items.append(star(x, y, r, sw=SW2))
    return items
