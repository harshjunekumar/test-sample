"""25. Happy school bus."""
from lib import *


def kid_head(cx, cy, girl=False):
    out = []
    if girl:
        out += [circle(cx - 32, cy - 12, 12, sw=SW2), circle(cx + 32, cy - 12, 12, sw=SW2)]
    out += [circle(cx, cy, 32, sw=SW2),
            path(f"M{cx - 32} {cy - 2} Q{cx - 31} {cy - 36} {cx} {cy - 36} Q{cx + 31} {cy - 36} {cx + 32} {cy - 2} "
                 f"Q{cx + 12} {cy - 22} {cx - 32} {cy - 2} Z", sw=SW2),
            eye(cx - 11, cy + 3, 5.5), eye(cx + 11, cy + 3, 5.5), smile(cx, cy + 14, 9, sw=SW2 * 0.7)]
    return out


def draw():
    items = [
        sun(660, 200, 58), cloud(230, 175, 180),
        cloud(470, 300, 130),
        hills(760, amp=25, bumps=1),
        rect(66, 840, 720, 190, r=0),  # road
        rect(120, 925, 90, 18, r=9), rect(300, 925, 90, 18, r=9), rect(480, 925, 90, 18, r=9), rect(660, 925, 90, 18, r=9),
        # bus body
        path("M135 430 L590 430 Q622 430 630 460 L652 588 L735 600 Q760 604 760 630 L760 800 "
             "Q760 820 740 820 L135 820 Q110 820 110 795 L110 455 Q110 430 135 430 Z"),
        rect(90, 760, 40, 34, r=10), rect(735, 760, 40, 34, r=10),  # bumpers
        rect(150, 410, 40, 22, r=8), rect(530, 410, 40, 22, r=8),  # roof lights
        line("M110 640 L760 640 M110 672 L760 672", SW2),  # side stripes
    ]
    for i, x in enumerate((140, 240, 340, 440)):
        items.append(rect(x, 478, 82, 100, r=14))
    items += kid_head(181, 545) + kid_head(281, 545, girl=True) + kid_head(381, 545) + kid_head(481, 545, girl=True)
    items += [
        rect(545, 478, 66, 300, r=10),  # door
        rect(556, 492, 44, 120, r=6, sw=SW2), rect(556, 640, 44, 120, r=6, sw=SW2),
        path("M622 478 L640 478 Q648 478 650 490 L664 590 L622 590 Z", sw=SW2),  # windshield
        circle(740, 660, 22),  # headlight
        # friendly face on the hood
        eye(690, 690, 13), smile(712, 735, 22, sw=SW2), cheek(670, 730, 12),
    ]
    for x in (250, 625):
        items += [circle(x, 820, 64), circle(x, 820, 28), circle(x, 820, 6, fill=BLACK, sw=0)]
    items += [grass_tuft(420, 815), grass_tuft(470, 790, 0.8)] if False else []
    return items
