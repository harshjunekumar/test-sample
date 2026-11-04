"""30. Magical castle with friendly characters."""
from lib import *
from pages.f3_helpers import bunny


def tower(x, top, w, base, roof_h):
    out = [rect(x - w / 2, top, w, base - top, r=0)]
    # cone roof + flag
    out += [line(f"M{x} {top - roof_h} L{x} {top - roof_h - 60}", SW2),
            path(f"M{x} {top - roof_h - 60} L{x + 48} {top - roof_h - 44} L{x} {top - roof_h - 28} Z", sw=SW2),
            path(f"M{x - w / 2 - 18} {top + 4} L{x} {top - roof_h} L{x + w / 2 + 18} {top + 4} Q{x} {top + 22} {x - w / 2 - 18} {top + 4} Z")]
    return out


def arch_window(x, y, w=40, h=64):
    return path(f"M{x - w / 2} {y + h} L{x - w / 2} {y + w / 2} Q{x - w / 2} {y} {x} {y} Q{x + w / 2} {y} {x + w / 2} {y + w / 2} "
                f"L{x + w / 2} {y + h} Z")


def dragon():
    """Small friendly dragon sitting, base at (0,0), facing left."""
    return [
        path("M40 -45 Q100 -45 98 -105 L96 -130 L122 -112 L112 -100 Q118 -20 40 -12 Z"),  # tail
        path("M10 -150 Q70 -230 110 -190 Q90 -180 95 -160 Q70 -170 70 -140 Z"),  # wing
        ellipse(0, -75, 70, 78),
        ellipse(-8, -60, 40, 55, sw=SW2),
        line("M-38 -80 L22 -80 M-44 -55 L28 -55 M-40 -30 L24 -30", SW2 * 0.8),
        ellipse(-40, -8, 32, 16), ellipse(40, -8, 32, 16),
        path("M-28 -230 L-20 -262 L-6 -232 Z", sw=SW2), path("M20 -232 L30 -262 L38 -228 Z", sw=SW2),  # horns
        ellipse(0, -185, 68, 56),
        ellipse(-40, -170, 34, 24),  # snout
        circle(-55, -175, 4, fill=BLACK, sw=0), circle(-36, -178, 4, fill=BLACK, sw=0),
        eye(-8, -205, 12), eye(30, -205, 12),
        smile(-30, -160, 16, sw=SW2), cheek(40, -180, 10),
    ]


def draw():
    items = [
        # rainbow behind castle
        path("M145 600 A280 280 0 0 1 705 600 L655 600 A230 230 0 0 0 195 600 Z"),
        path("M195 600 A230 230 0 0 1 655 600 L605 600 A180 180 0 0 0 245 600 Z"),
        star(130, 180, 30), star(720, 170, 32, rot=12), star(425, 115, 20),
        hills(880, amp=25, bumps=2),
    ]
    items += tower(175, 470, 100, 900, 150) + tower(675, 470, 100, 900, 150)
    # main wall with battlements
    items.append(path("M230 900 L230 560 L262 560 L262 530 L302 530 L302 560 L342 560 L342 530 L382 530 L382 560 "
                      "L468 560 L468 530 L508 530 L508 560 L548 560 L548 530 L588 530 L588 560 L620 560 L620 900 Z"))
    items += tower(425, 380, 140, 620, 170)
    items += [
        arch_window(425, 440, 50, 80), arch_window(175, 540, 42, 70), arch_window(675, 540, 42, 70),
        arch_window(300, 640, 42, 70), arch_window(550, 640, 42, 70),
        path("M360 900 L360 760 Q360 690 425 690 Q490 690 490 760 L490 900 Z"),  # door
        line("M425 690 L425 900 M380 760 L380 900 M470 760 L470 900", SW2) if False else line("M425 692 L425 900", SW2),
        circle(408, 810, 7, fill=BLACK, sw=0), circle(442, 810, 7, fill=BLACK, sw=0),
        heart(425, 655, 22),
        path("M330 900 L520 900 Q560 950 590 1040 L260 1040 Q290 950 330 900 Z"),  # path
    ]
    items += [place(bunny(), 160, 1000, 0.95), place(dragon(), 655, 1000, 0.95)]
    return items
