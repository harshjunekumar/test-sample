"""15. Happy train traveling through mountains."""
from lib import *


def mountain(x0, x1, peak_x, peak_y, base_y=820):
    w = x1 - x0
    snow_y = peak_y + (base_y - peak_y) * 0.28
    lx = peak_x - (peak_x - x0) * 0.28
    rx = peak_x + (x1 - peak_x) * 0.28
    return "\n".join([
        path(f"M{x0} {base_y} L{peak_x - 25} {peak_y + 18} Q{peak_x} {peak_y - 12} {peak_x + 25} {peak_y + 18} L{x1} {base_y} Z"),
        line(f"M{lx} {snow_y} Q{lx + (peak_x - lx) * 0.5} {snow_y + 30} {peak_x - 8} {snow_y - 8} "
             f"Q{peak_x + (rx - peak_x) * 0.5} {snow_y + 30} {rx} {snow_y}", SW2),
    ])


def wheel(cx, cy, r):
    return "\n".join([circle(cx, cy, r), circle(cx, cy, r * 0.32, sw=SW2)])


def car(x, w=150, shape="round"):
    items = [rect(x, 610, w, 130, 14), rect(x - 10, 585, w + 20, 32, 12)]
    if shape == "round":
        items += [circle(x + w * 0.3, 670, 26, sw=SW2), circle(x + w * 0.7, 670, 26, sw=SW2)]
    else:
        items += [rect(x + 20, 640, w - 40, 55, 12, sw=SW2), heart(x + w / 2, 668, 18, sw=SW2)]
    items += [wheel(x + 35, 770, 30), wheel(x + w - 35, 770, 30)]
    return "\n".join(items)


def draw():
    items = [
        cloud(170, 200, 170), cloud(600, 150, 140),
        mountain(40, 470, 250, 330, 870), mountain(320, 830, 600, 270, 870),
        mountain(560, 840, 760, 500, 870),
        hills(870, amp=0, bumps=1),
    ]
    train = [line("M60 805 L790 805", SW)]
    for x in range(90, 790, 60):
        train.append(rect(x, 812, 34, 20, 4, sw=SW2))
    # smoke puffs
    train += [cloud(628, 498, 80), cloud(565, 425, 105), cloud(470, 345, 140)]
    train += [car(95, 150, "heart"), rect(245, 715, 30, 16, 6, sw=SW2), car(275, 150, "round"),
              rect(425, 715, 30, 16, 6, sw=SW2)]
    # engine
    train += [
        rect(455, 545, 125, 195, 10),
        rect(440, 520, 155, 35, 12),
        rect(478, 575, 80, 70, 12, sw=SW2),
        rect(575, 605, 130, 135, 20),
        path("M600 605 L592 545 L652 545 L644 605 Z"),
        rect(580, 522, 84, 28, 10),
        path("M660 606 A22 22 0 0 1 704 606 Z"),
        rect(450, 732, 290, 28, 8),
        path("M720 760 L760 795 L705 795 Z"),
        circle(700, 672, 62),
        eye(678, 660, 11), eye(722, 660, 11), smile(700, 688, 16), cheek(668, 694, 10), cheek(732, 694, 10),
        wheel(515, 765, 40), wheel(625, 775, 30),
        rect(510, 760, 120, 12, 6, sw=SW2),
    ]
    items.append(place(train, 0, 95))
    items += [grass_tuft(120, 990), grass_tuft(330, 985, 1.2), grass_tuft(560, 992), grass_tuft(730, 985, 1.1),
              stem_flower(230, 1005, 40, 26), stem_flower(450, 1005, 38, 24, petals=6), stem_flower(650, 1005, 42, 26)]
    return items
