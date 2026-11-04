"""3. Baby elephant spraying water."""
from lib import *


def elephant():
    return [
        # back legs + tail
        rect(-110, 150, 60, 110, r=24), rect(50, 150, 60, 110, r=24),
        # body
        ellipse(0, 120, 128, 100),
        # front legs
        rect(-62, 170, 56, 105, r=24), rect(6, 170, 56, 105, r=24),
        line("M-50 262 Q-46 252 -42 262 M-26 262 Q-22 252 -18 262 M18 262 Q22 252 26 262 M42 262 Q46 252 50 262", SW2 * 0.8),
        # big ears
        ellipse(-128, -25, 88, 104, rot=-15), ellipse(128, -25, 88, 104, rot=15),
        ellipse(-128, -20, 58, 72, rot=-15, sw=SW2), ellipse(128, -20, 58, 72, rot=15, sw=SW2),
        # trunk raised up (drawn before head so head covers its root)
        tube("M0 20 C0 110 90 120 130 40 C155 -10 160 -80 175 -150", 46),
        ellipse(178, -160, 26, 14, rot=-15),
        ellipse(178, -160, 10, 5, rot=-15, fill=BLACK, sw=0),
        line("M120 70 L145 82 M140 30 L166 38 M150 -15 L178 -10", SW2 * 0.8),  # trunk wrinkles
        # head
        ellipse(0, -30, 112, 100),
        # hair tuft
        line("M-10 -128 Q-14 -150 -2 -160 M6 -128 Q8 -152 22 -158", SW2),
        eye(-42, -48, 19), eye(42, -48, 19),
        cheek(-70, 5, 15), cheek(70, 5, 15),
        smile(-38, 42, 18, 6),
    ]


def draw():
    items = [
        sun(160, 220, 55, rays=10),
        cloud(330, 170, 140),
        hills(780, amp=30, bumps=1),
        ellipse(420, 930, 300, 55),  # puddle / pond
        line("M170 935 Q200 922 230 935 M620 945 Q650 932 680 945", SW2),
        place(elephant(), 370, 650, 1.25),
    ]
    # water spray arcing up out of the trunk and raining down
    # fountain of water from the trunk tip (tip is at about 592, 450)
    items.append(line("M585 430 Q560 330 480 300 M595 425 Q600 320 600 250 M605 430 Q650 330 720 310", SW2))
    for x, y, s, r in [(470, 330, 22, -30), (440, 395, 18, -10), (600, 220, 24, 0), (560, 270, 16, -15),
                       (735, 340, 22, 30), (760, 410, 18, 10), (650, 270, 16, 15), (505, 250, 15, -25),
                       (700, 255, 15, 25)]:
        items.append(drop(x, y, s, r))
    items += [grass_tuft(130, 860), grass_tuft(730, 860, 1.1), grass_tuft(700, 990), grass_tuft(140, 990)]
    return items
