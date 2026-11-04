"""21. Butterfly garden."""
from lib import *


def daisy(x, ground_y, h, r):
    return "\n".join([
        line(f"M{x} {ground_y} Q{x + 10} {ground_y - h / 2} {x} {ground_y - h}", SW),
        leaf(x + 3, ground_y - h * 0.35, r * 1.4, -30, sw=SW2),
        leaf(x - 3, ground_y - h * 0.55, r * 1.2, 210, sw=SW2),
        flower(x, ground_y - h, r, petals=8),
    ])


def sunflower(x, ground_y, h, r):
    items = [line(f"M{x} {ground_y} L{x} {ground_y - h}", SW),
             leaf(x, ground_y - h * 0.4, r * 1.3, -25, sw=SW2), leaf(x, ground_y - h * 0.6, r * 1.2, 205, sw=SW2)]
    import math
    for i in range(12):
        a = math.radians(i * 30)
        items.append(ellipse(x + r * 1.05 * math.cos(a), ground_y - h + r * 1.05 * math.sin(a), r * 0.55, r * 0.25,
                             rot=i * 30))
    items += [circle(x, ground_y - h, r * 0.72), eye(x - r * 0.25, ground_y - h - r * 0.1, r * 0.1),
              eye(x + r * 0.25, ground_y - h - r * 0.1, r * 0.1), smile(x, ground_y - h + r * 0.15, r * 0.22)]
    return "\n".join(items)


def draw():
    items = [
        cloud(640, 160, 160),
        hills(900, amp=30, bumps=2),
        sunflower(150, 1010, 330, 62),
        tulip(300, 1010, 170, 40),
        daisy(440, 1010, 240, 50),
        tulip(590, 1010, 200, 38),
        sunflower(710, 1010, 270, 52),
        bfly(440, 380, 1.4, rot=-8),
        bfly(155, 215, 0.62, rot=-20),
        bfly(690, 575, 0.6, rot=18),
    ]
    return items
