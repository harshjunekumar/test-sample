"""1. Cute puppy playing with a ball."""
from lib import *


def puppy():
    return [
        # tail (wagging)
        path("M80 150 C150 120 150 40 190 30 C205 28 210 45 198 55 C170 80 175 150 95 185 Z"),
        # body
        ellipse(0, 130, 112, 118),
        ellipse(0, 160, 58, 78, sw=SW2),
        # back legs
        ellipse(-92, 225, 58, 36), ellipse(92, 225, 58, 36),
        # front legs + paws
        path("M-66 225 L-64 140 Q-42 112 -20 140 L-18 225 Z"),
        path("M66 225 L64 140 Q42 112 20 140 L18 225 Z"),
        ellipse(-42, 235, 38, 22), ellipse(42, 235, 38, 22),
        line("M-50 228 L-50 248 M-34 228 L-34 248 M34 228 L34 248 M50 228 L50 248", SW2 * 0.8),
        # collar + tag
        path("M-82 12 Q0 55 82 12 L86 38 Q0 85 -86 38 Z"),
        circle(0, 82, 18),
        heart(0, 82, 14, sw=SW2 * 0.8),
        # head
        ellipse(0, -65, 128, 110),
        ellipse(52, -88, 40, 36, sw=SW2),  # eye patch
        # floppy ears
        path("M-95 -140 C-170 -140 -190 -40 -160 20 C-140 50 -100 30 -100 -20 C-100 -60 -80 -100 -95 -140 Z"),
        path("M95 -140 C170 -140 190 -40 160 20 C140 50 100 30 100 -20 C100 -60 80 -100 95 -140 Z"),
        # muzzle
        ellipse(0, -18, 62, 44),
        nose(0, -44, 20),
        line("M0 -32 L0 -12", SW2),
        path("M-28 -18 Q-14 -2 0 -12 Q14 -2 28 -18 Q30 10 0 22 Q-30 10 -28 -18 Z", sw=SW2),
        path("M-14 4 Q0 -6 14 4 Q14 30 0 32 Q-14 30 -14 4 Z", sw=SW2 * 0.8),  # tongue
        line("M0 6 L0 22", SW2 * 0.6),
        eye(-48, -88, 17), eye(52, -88, 17),
        cheek(-82, -40, 14), cheek(82, -40, 14),
        line("M-70 -128 Q-50 -142 -30 -132 M30 -132 Q50 -142 70 -128", SW2),  # eyebrows
    ]


def ball(cx, cy, r):
    return [
        circle(cx, cy, r),
        line(f"M{cx - r} {cy} Q{cx} {cy - r * 0.55} {cx + r} {cy}", SW2),
        line(f"M{cx - r * 0.25} {cy - r * 0.97} Q{cx + r * 0.45} {cy} {cx - r * 0.25} {cy + r * 0.97}", SW2),
        star(cx + r * 0.45, cy + r * 0.42, r * 0.22, sw=SW2),
    ]


def draw():
    items = [
        cloud(220, 210, 190), cloud(610, 170, 150),
        hills(800, amp=50, bumps=2),
    ]
    items += [place(puppy(), 330, 545, 1.3)]
    items += ball(615, 850, 78)
    items += [grass_tuft(470, 975, 1.2), grass_tuft(620, 975), grass_tuft(230, 985)]
    items += [stem_flower(135, 930, 110, 34), stem_flower(745, 975, 70, 30, petals=6)]
    return items
