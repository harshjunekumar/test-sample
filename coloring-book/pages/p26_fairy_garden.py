"""26. Little fairy in an enchanted garden."""
from lib import *
from pages.f3_helpers import child, arm_end


def mushroom(x, ground, s=1.0):
    return place([
        path("M-30 0 Q-36 -60 -26 -95 L26 -95 Q36 -60 30 0 Z"),
        path("M-95 -90 Q-100 -200 0 -205 Q100 -200 95 -90 Q0 -70 -95 -90 Z"),
        circle(-45, -135, 16, sw=SW2), circle(10, -168, 19, sw=SW2), circle(55, -120, 14, sw=SW2),
        rect(-10, -55, 20, 30, r=10, sw=SW2),  # tiny door
    ], x, ground, s)


def draw():
    s = 1.6
    cx, ground = 425, 940
    # wand hand: right arm raised (angle -140 => up and right)
    hx, hy = arm_end(42, -192, -140)
    wand_tip = (cx + (hx + 60) * s, ground + (hy - 70) * s)
    fairy = [
        # wings (behind everything)
        ellipse(-95, -250, 95, 55, rot=-30), ellipse(95, -250, 95, 55, rot=30),
        ellipse(-80, -165, 62, 38, rot=25), ellipse(80, -165, 62, 38, rot=-25),
    ]
    fairy += child(girl=True, arms=(38, -140), hair_style=1)
    fairy += [
        star(0, -150, 18, sw=SW2),  # star on dress
        path("M-34 -340 L-24 -378 L0 -356 L24 -378 L34 -340 Z", sw=SW2),  # crown
        line(f"M{hx} {hy} L{hx + 60} {hy - 70}", SW),  # wand stick
        star(hx + 60, hy - 70, 34),
    ]
    items = [
        circle(120, 160, 4, fill=BLACK, sw=0),
        star(150, 220, 34), star(700, 180, 36, rot=15), star(470, 160, 26), star(130, 420, 26, rot=-10),
        hills(860, amp=30, bumps=2),
        mushroom(150, 900, 0.95), mushroom(712, 905, 0.8),
        place(fairy, cx, ground, s),
        line(f"M{wand_tip[0] + 30} {wand_tip[1] + 50} Q{wand_tip[0] + 60} {wand_tip[1] + 90} "
             f"{wand_tip[0] + 45} {wand_tip[1] + 130}", SW2) if False else "",
        stem_flower(110, 1000, 80, 34), stem_flower(250, 1005, 55, 30, 6),
        stem_flower(605, 1005, 55, 30, 6), stem_flower(740, 1000, 80, 34),
    ]
    items.pop(0)
    return items
