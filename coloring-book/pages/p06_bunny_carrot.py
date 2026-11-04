"""6. Bunny holding a carrot."""
from lib import *


def carrot(s=1.0):
    return place([
        leaf(0, 0, 70, -150, sw=SW2), leaf(0, 0, 80, -180, sw=SW2), leaf(0, 0, 70, -210, sw=SW2),
        path("M0 -38 C60 -40 160 -15 232 0 C160 15 60 40 0 38 C-14 20 -14 -20 0 -38 Z"),
        line("M50 -26 L60 -10 M95 8 L106 22 M140 -14 L150 -4 M175 6 L184 13", SW2 * 0.8),
    ], s=s)


def bunny():
    return [
        # tall ears
        ellipse(-48, -235, 36, 100, rot=-10), ellipse(48, -235, 36, 100, rot=10),
        ellipse(-48, -228, 20, 70, rot=-10, sw=SW2), ellipse(48, -228, 20, 70, rot=10, sw=SW2),
        # body + feet
        ellipse(0, 135, 102, 115),
        ellipse(0, 160, 56, 70, sw=SW2),
        ellipse(-62, 245, 58, 28), ellipse(62, 245, 58, 28),
        # head
        ellipse(0, -60, 112, 96),
        eye(-40, -72, 18), eye(40, -72, 18),
        cheek(-72, -28, 15), cheek(72, -28, 15),
        path("M-13 -38 Q0 -46 13 -38 Q8 -26 0 -24 Q-8 -26 -13 -38 Z", fill=BLACK, sw=SW2 * 0.6),
        line("M0 -24 L0 -14 M-22 -12 Q-11 2 0 -14 Q11 2 22 -12", SW2),
        rect(-11, -8, 22, 18, r=4, sw=SW2 * 0.8), line("M0 -8 L0 10", SW2 * 0.6),
        line("M-92 -40 L-135 -50 M-92 -24 L-136 -22 M92 -40 L135 -50 M92 -24 L136 -22", SW2 * 0.7),
        # carrot held across the tummy
        place([carrot(0.85)], 90, 35, rot=135),
        # arms + paws hugging the carrot
        tube("M-88 40 Q-70 80 -40 95", 40), tube("M88 40 Q80 70 50 70", 40),
        circle(-36, 96, 25), circle(48, 68, 25),
    ]


def carrot_top(x, y):
    return "\n".join([leaf(x, y, 50, -60, sw=SW2), leaf(x, y, 55, -90, sw=SW2), leaf(x, y, 50, -120, sw=SW2),
                      ellipse(x, y + 6, 26, 14)])


def draw():
    return [
        sun(680, 210, 50, rays=10),
        cloud(190, 200, 160),
        hills(800, amp=40, bumps=2),
        place(bunny(), 400, 600, 1.3),
        carrot_top(150, 900), carrot_top(240, 950), carrot_top(700, 920), carrot_top(610, 970),
        grass_tuft(420, 990), grass_tuft(130, 990),
    ]
