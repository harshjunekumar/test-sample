"""7. Little monkey swinging on a tree."""
from lib import *


def monkey():
    return [
        # curly tail
        tube("M45 230 C150 250 200 150 160 80 C140 45 170 15 200 30", 22),
        # legs dangling
        tube("M-35 250 C-55 310 -30 350 -65 385", 34), tube("M35 250 C65 305 55 345 90 375", 34),
        ellipse(-75, 395, 32, 20, rot=-20), ellipse(100, 383, 32, 20, rot=20),
        # body
        ellipse(0, 185, 76, 98),
        ellipse(0, 205, 46, 64, sw=SW2),
        # arm reaching up to the branch + waving arm
        tube("M55 110 C100 40 125 -60 135 -170", 34),
        tube("M-55 120 C-110 110 -150 80 -170 30", 34),
        circle(-176, 20, 24),
        # ears
        circle(-105, 0, 36), circle(105, 0, 36),
        circle(-105, 0, 19, sw=SW2), circle(105, 0, 19, sw=SW2),
        # head + face mask
        circle(0, 0, 100),
        line("M-8 -100 Q-14 -125 2 -132 M8 -100 Q12 -122 28 -124", SW2),
        path("M0 -32 C-22 -62 -86 -55 -80 0 C-88 42 -58 86 0 86 C58 86 88 42 80 0 C86 -55 22 -62 0 -32 Z", sw=SW2),
        eye(-34, -8, 16), eye(34, -8, 16),
        circle(-9, 28, 4, fill=BLACK, sw=0), circle(9, 28, 4, fill=BLACK, sw=0),
        open_smile(0, 48, 30, 14),
        cheek(-56, 34, 12), cheek(56, 34, 12),
    ]


def banana(x, y, rot=0):
    return place([path("M0 0 C30 40 90 45 120 10 C122 2 116 -2 110 2 C85 25 40 22 10 -8 Z"),
                  rect(-10, -16, 16, 14, r=4, rot=40, sw=SW2)], x, y, rot=rot)


def draw():
    return [
        # tree trunk on the left + long branch
        tube("M180 240 C360 205 560 250 800 205", 46),
        path("M70 1100 L70 70 L200 70 C190 300 175 500 200 1100 Z"),
        line("M110 400 Q125 430 115 470 M150 650 Q165 690 155 720 M120 850 Q130 880 122 910", SW2),
        tube("M330 230 C360 180 400 165 440 160", 18),
        big_leaf(440, 160, 110, -15), big_leaf(330, 225, 100, -100),
        big_leaf(620, 225, 120, -70), big_leaf(760, 215, 100, -110), big_leaf(250, 240, 90, 120),
        place(monkey(), 395, 470, 1.15),
        # hand gripping the branch (drawn over it)
        circle(550, 237, 25), line("M535 222 Q550 212 565 222 M532 236 Q550 226 568 236", SW2 * 0.8),
        bush(690, 1000, 150),
        hills(975, amp=20, bumps=2),
        grass_tuft(300, 1000), grass_tuft(480, 1000), grass_tuft(560, 995),
    ]
