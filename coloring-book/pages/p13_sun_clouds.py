"""13. Smiling sun and fluffy clouds."""
from lib import *


def cloud_face(cx, cy, w, closed=False):
    s = w / 160
    face = [closed_eye(-22, -14, 9) if closed else eye(-22, -14, 8),
            closed_eye(22, -14, 9) if closed else eye(22, -14, 8),
            smile(0, -2, 10), cheek(-40, 0, 8), cheek(40, 0, 8)]
    return "\n".join([cloud(cx, cy, w), place(face, cx, cy, s)])


def bird(x, y, s=1):
    return place([line("M-24 0 Q-12 -16 0 0 Q12 -16 24 0", SW2)], x, y, s)


def draw():
    items = [
        sun(425, 390, 150, rays=12, face=False),
        eye(375, 360, 20), eye(475, 360, 20),
        open_smile(425, 420, 50, 24),
        cheek(330, 425, 20), cheek(520, 425, 20),
        line("M350 315 Q375 300 400 315 M450 315 Q475 300 500 315", SW2),
        hills(940, amp=40, bumps=3),
        cloud_face(230, 680, 320),
        cloud_face(630, 735, 290, closed=True),
        cloud_face(420, 885, 360),
        bird(170, 190, 1.6), bird(250, 250, 1.3), bird(690, 175, 1.5),
        heart(150, 440, 36), heart(715, 470, 34, rot=12),
    ]
    return items
