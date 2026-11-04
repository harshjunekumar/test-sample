"""23. Cute house surrounded by flowers."""
from lib import *


def window(x, y, w=92, h=92):
    return [
        rect(x - 8, y + h - 2, w + 16, 22, r=6),  # flower box
        rect(x, y, w, h, r=10),
        line(f"M{x + w / 2} {y} L{x + w / 2} {y + h} M{x} {y + h / 2} L{x + w} {y + h / 2}", SW2),
        flower(x + 18, y + h - 4, 15, sw=SW2), flower(x + w - 18, y + h - 4, 15, sw=SW2),
    ]


def draw():
    items = [
        cloud(230, 185, 180), heart(735, 175, 0) if False else "",
        circle(590, 245, 18), circle(620, 205, 24), circle(665, 160, 32),  # chimney smoke
        hills(840, amp=40, bumps=2),
        rect(545, 285, 64, 140, r=6),  # chimney
        rect(530, 270, 94, 30, r=8),
        rect(210, 470, 430, 400, r=8),  # house body
        path("M165 490 L425 260 L685 490 Q690 505 672 505 L178 505 Q160 505 165 490 Z"),  # roof
        circle(425, 405, 44), line("M425 361 L425 449 M381 405 L469 405", SW2),  # round attic window
        heart(425, 405, 0) if False else "",
    ]
    items += window(245, 560) + window(513, 560)
    items += [
        path("M370 870 L370 735 Q425 670 480 735 L480 870 Z"),  # door
        line("M425 704 L425 870", SW2),
        circle(408, 800, 7, fill=BLACK, sw=0), circle(442, 800, 7, fill=BLACK, sw=0),
        path("M370 870 L480 870 Q520 940 560 1040 L290 1040 Q330 940 370 870 Z"),  # path
        line("M350 920 Q425 932 500 920 M330 975 Q425 990 525 975", SW2),
    ]
    # flowers along the front
    for x, h, r, n in [(110, 120, 32, 5), (180, 95, 28, 6), (250, 135, 30, 5),
                       (600, 135, 30, 6), (670, 100, 28, 5), (740, 125, 32, 6)]:
        items.append(stem_flower(x, 1000, h, r, n))
    items += [bush(140, 880, 120), bush(712, 880, 120)] if False else []
    return items
