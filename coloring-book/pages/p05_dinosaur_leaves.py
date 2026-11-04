"""5. Cute dinosaur eating leaves."""
from lib import *


def dino():
    return [
        # far legs
        rect(-85, 30, 56, 110, r=24), rect(105, 30, 56, 110, r=24),
        # tail
        path("M-130 -25 C-190 -35 -225 -70 -245 -120 C-268 -40 -225 45 -120 50 Z"),
        # long neck
        path("M40 -50 C95 -150 115 -240 175 -305 L245 -268 C185 -215 175 -110 160 10 Z"),
        # body
        ellipse(0, 0, 172, 105),
        line("M-120 55 Q0 105 120 55", SW2),  # belly line
        circle(-70, -50, 22, sw=SW2), circle(-10, -72, 18, sw=SW2), circle(-130, -10, 16, sw=SW2),
        circle(50, -55, 15, sw=SW2),
        # near legs
        rect(-132, 45, 64, 118, r=26), rect(55, 45, 64, 118, r=26),
        line("M-120 160 Q-114 148 -108 160 M-98 160 Q-92 148 -86 160 M67 160 Q73 148 79 160 M89 160 Q95 148 101 160",
             SW2 * 0.8),
        # head
        ellipse(228, -300, 66, 46, rot=-8),
        circle(150, -175, 12, sw=SW2), circle(175, -230, 10, sw=SW2),  # neck spots
        eye(228, -318, 15, look=(4, 0)),
        line("M210 -350 Q228 -360 246 -350", SW2),
        cheek(252, -288, 12),
        circle(282, -318, 3.5, fill=BLACK, sw=0),
        line("M240 -270 Q262 -262 288 -280", SW2),
        # leafy snack in the mouth
        leaf(276, -276, 70, 30, sw=SW2), leaf(276, -276, 60, 70, sw=SW2),
    ]


def draw():
    return [
        cloud(200, 190, 160),
        path("M590 850 L612 400 L690 400 L712 850 Z"), line("M630 600 Q645 620 638 650 M670 720 Q680 740 672 770", SW2),
        scallop(648, 320, 100, n=10),
        hills(830, amp=35, bumps=2),
        place(dino(), 350, 725, 1.0),
        leaf(740, 500, 45, 60), leaf(745, 620, 42, 110),  # falling leaves
        stem_flower(140, 985, 90, 32), stem_flower(720, 985, 80, 30, petals=6),
        grass_tuft(420, 985), grass_tuft(560, 975, 1.1),
    ]
