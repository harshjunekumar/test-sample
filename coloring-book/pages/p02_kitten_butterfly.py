"""2. Happy kitten chasing a butterfly."""
from lib import *


def kitten():
    return [
        # tail curling up behind
        tube("M60 200 C170 215 215 150 195 110 C182 85 198 65 220 72", 34),
        # body
        ellipse(0, 135, 98, 108),
        ellipse(0, 160, 52, 68, sw=SW2),
        # back legs
        ellipse(-80, 222, 52, 32), ellipse(80, 222, 52, 32),
        # front leg on ground
        path("M-62 228 L-60 140 Q-40 115 -20 140 L-18 228 Z"),
        ellipse(-40, 236, 36, 21),
        line("M-48 230 L-48 248 M-32 230 L-32 248", SW2 * 0.8),
        # raised front paw reaching for the butterfly
        tube("M60 60 C120 50 160 20 185 -40", 44),
        circle(190, -55, 31),
        line("M176 -80 L180 -66 M196 -84 L196 -68 M212 -74 L206 -62", SW2 * 0.8),
        # ears (behind head)
        path("M-108 -70 L-96 -190 L-20 -128 Z"), path("M108 -70 L96 -190 L20 -128 Z"),
        path("M-86 -100 L-82 -158 L-44 -128 Z", sw=SW2), path("M86 -100 L82 -158 L44 -128 Z", sw=SW2),
        # head
        ellipse(0, -55, 122, 100),
        line("M-16 -150 L-13 -126 M0 -154 L0 -128 M16 -150 L13 -126", SW2),  # forehead stripes
        eye(-45, -62, 20, look=(4, -2)), eye(45, -62, 20, look=(4, -2)),
        cheek(-78, -18, 15), cheek(78, -18, 15),
        path("M-12 -30 L12 -30 L0 -16 Z", fill=BLACK, sw=SW2 * 0.7),
        line("M0 -16 L0 -6 M-24 -6 Q-12 10 0 -6 Q12 10 24 -6", SW2),
        line("M-100 -40 L-150 -54 M-100 -22 L-152 -18 M100 -40 L150 -54 M100 -22 L152 -18", SW2 * 0.8),
    ]


def draw():
    return [
        cloud(210, 190, 170), cloud(430, 150, 120),
        hills(820, amp=45, bumps=2),
        place(kitten(), 330, 580, 1.3),
        butterfly(640, 300, 1.1, rot=18),
        line("M640 440 Q625 460 640 480 M675 430 Q662 452 676 470", SW2),  # flutter marks
        stem_flower(140, 960, 100, 34), stem_flower(720, 950, 120, 36, petals=6),
        grass_tuft(470, 985, 1.2), grass_tuft(620, 985), grass_tuft(260, 990),
    ]
