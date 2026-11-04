"""28. Cute owl sitting on a branch."""
from lib import *


def owl():
    """Big owl, feet at (0,0)."""
    out = [
        # ear tufts
        path("M-140 -390 L-150 -480 L-70 -420 Z"), path("M140 -390 L150 -480 L70 -420 Z"),
        ellipse(0, -230, 170, 215),  # body
        # wings
        path("M-160 -270 Q-230 -170 -170 -50 Q-120 -90 -125 -200 Z"),
        path("M160 -270 Q230 -170 170 -50 Q120 -90 125 -200 Z"),
        ellipse(0, -130, 100, 110, sw=SW2),  # belly
    ]
    for y, xs in ((-175, (-45, 0, 45)), (-125, (-65, -22, 22, 65)), (-75, (-45, 0, 45))):
        for x in xs:
            out.append(line(f"M{x - 14} {y} Q{x} {y + 16} {x + 14} {y}", SW2 * 0.9))
    out += [
        # face disc + eyes
        path("M0 -390 Q-60 -420 -110 -380 Q-160 -330 -125 -265 Q-90 -220 0 -245 "
             "Q90 -220 125 -265 Q160 -330 110 -380 Q60 -420 0 -390 Z", sw=SW2),
        circle(-62, -322, 52), circle(62, -322, 52),
        eye(-58, -318, 26), eye(58, -318, 26),
        path("M-20 -278 L20 -278 L0 -240 Z"),  # beak
        cheek(-100, -262, 14), cheek(100, -262, 14),
        # feet
        path("M-70 -15 Q-75 12 -50 12 Q-40 20 -30 12 Q-10 14 -15 -15 Z", sw=SW2),
        path("M70 -15 Q75 12 50 12 Q40 20 30 12 Q10 14 15 -15 Z", sw=SW2),
    ]
    return out


def draw():
    leaf_d = "M0 0 Q30 -30 60 0 Q30 30 0 0 Z"
    scene = [
        path("M60 760 Q300 730 560 765 Q640 775 700 745 L712 772 Q650 805 560 800 Q300 790 60 815 Z"),
        path("M560 780 Q620 820 680 830 L676 852 Q610 845 545 800 Z"),
        place([path(leaf_d, sw=SW2)], 690, 760, 1.2, rot=-20),
        place([path(leaf_d, sw=SW2)], 680, 840, 1.2, rot=15),
        place([path(leaf_d, sw=SW2)], 130, 795, 1.3, rot=120),
        place([path(leaf_d, sw=SW2)], 230, 790, 1.3, rot=70),
    ]
    return [
        place([path("M175 150 A80 80 0 1 0 245 290 A62 62 0 1 1 175 150 Z")], 10, -10, 0.95),
        star(705, 160, 34), star(715, 360, 24, rot=12), star(330, 150, 20), star(125, 470, 24),
        g(scene, "translate(0 130)"),
        place(owl(), 425, 908, 1.27),
    ]
