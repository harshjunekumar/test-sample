"""29. Children playing in a park."""
from lib import *
from pages.f3_helpers import child, arm_end


def kite(x, y):
    return [
        line(f"M{x} {y + 95} Q{x + 50} {y + 130} {x + 70} {y + 175} Q{x + 85} {y + 215} {x + 130} {y + 225}", SW2),
        place([path("M0 0 L-24 -18 L-24 18 Z", sw=SW2), path("M0 0 L24 -18 L24 18 Z", sw=SW2)], x + 66, y + 165, 1.2, rot=30),
        place([path("M0 0 L-24 -18 L-24 18 Z", sw=SW2), path("M0 0 L24 -18 L24 18 Z", sw=SW2)], x + 130, y + 225, 1.2, rot=-10),
        poly([(x, y - 95), (x + 70, y), (x, y + 95), (x - 70, y)]),
        line(f"M{x} {y - 95} L{x} {y + 95} M{x - 70} {y} L{x + 70} {y}", SW2),
    ]


def draw():
    s = 1.4
    gx, bx, ground = 275, 595, 965
    hx, hy = arm_end(42, -192, -150)  # girl's raised right hand (local)
    hand = (gx + hx * s, ground + hy * s)
    kx, ky = 560, 205
    items = [
        sun(160, 190, 50), cloud(700, 300, 130), cloud(330, 330, 110),
        tree(700, 820, 380, 0) if False else "",
        hills(800, amp=45, bumps=2),
        line(f"M{hand[0]} {hand[1]} Q{(hand[0] + kx) / 2 + 40} {(hand[1] + ky) / 2 + 40} {kx} {ky + 95}", SW2 * 0.8),
    ]
    items += kite(kx, ky)
    items += [
        place(child(girl=True, arms=(35, -150), hair_style=0), gx, ground, s),
        place(child(girl=False, arms=(150, -35)), bx, ground, s),
        # ball
        circle(445, 955, 44), line("M401 955 Q445 930 489 955", SW2), line("M434 912 Q465 955 434 998", SW2),
        grass_tuft(745, 1000), grass_tuft(110, 870),
        stem_flower(120, 1010, 75, 32, 6),
    ]
    return items
