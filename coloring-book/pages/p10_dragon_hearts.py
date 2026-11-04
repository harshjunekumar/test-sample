"""10. Friendly dragon breathing tiny hearts."""
from lib import *


def wing():
    return path("M-60 30 L-185 -70 C-178 -25 -190 10 -162 22 C-162 55 -140 66 -112 60 "
                "C-106 88 -84 94 -64 82 Z")


def dragon():
    return [
        # tail with heart tip
        tube("M70 200 C170 230 220 180 215 120", 32),
        heart2(222, 92, 40, rot=10),
        # wings behind
        wing(), place([wing()], flip=True),
        line("M-70 45 L-162 22 M-72 64 L-112 60 M70 45 L162 22 M72 64 L112 60", SW2 * 0.8),
        # body + belly plates
        ellipse(0, 130, 105, 115),
        ellipse(0, 150, 60, 82, sw=SW2),
        line("M-55 115 Q0 125 55 115 M-58 150 Q0 160 58 150 M-52 185 Q0 195 52 185", SW2 * 0.8),
        # back feet + little arms
        ellipse(-75, 230, 55, 30), ellipse(75, 230, 55, 30),
        line("M-100 222 L-100 238 M-80 220 L-80 240 M80 220 L80 240 M100 222 L100 238", SW2 * 0.8),
        ellipse(-88, 95, 24, 42, rot=30), ellipse(88, 95, 24, 42, rot=-30),
        # spikes, horns
        path("M-40 -150 L-20 -195 L0 -150 Z"), path("M0 -152 L20 -200 L40 -150 Z"),
        path("M-80 -125 L-90 -205 L-40 -145 Z"), path("M80 -125 L90 -205 L40 -145 Z"),
        # ears
        # head
        ellipse(0, -65, 118, 95),
        eye(-44, -85, 18), eye(44, -85, 18),
        cheek(-80, -45, 14), cheek(80, -45, 14),
        ellipse(0, -25, 62, 38),
        ellipse(-18, -38, 6, 8, fill=BLACK, sw=0), ellipse(18, -38, 6, 8, fill=BLACK, sw=0),
        ellipse(0, -8, 14, 11, sw=SW2),  # little "o" mouth blowing hearts
    ]


def draw():
    items = [
        cloud(170, 190, 160),
        cloud(650, 150, 130),
        hills(820, amp=35, bumps=2),
        place(dragon(), 360, 600, 1.25),
    ]
    # trail of hearts floating up from the mouth (mouth at about 360, 590)
    for x, y, s, r in [(540, 430, 22, 10), (610, 400, 30, -10), (700, 360, 38, 12), (620, 300, 32, -8),
                       (720, 260, 28, 15), (560, 250, 22, -12), (650, 210, 20, 8)]:
        items.append(heart2(x, y, s, rot=r))
    items += [stem_flower(140, 980, 90, 30), stem_flower(720, 985, 80, 30, petals=6),
              grass_tuft(560, 990), grass_tuft(300, 990)]
    return items
