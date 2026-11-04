"""16. Baby panda eating bamboo."""
from lib import *


def bamboo(x, y, h, rot=0, nodes=4, w=40):
    items = [rect(-w / 2, -h / 2, w, h, w / 2)]
    for i in range(1, nodes):
        yy = -h / 2 + h * i / nodes
        items.append(line(f"M{-w / 2} {yy} Q0 {yy + 8} {w / 2} {yy}", SW2))
    return place(items, x, y, rot=rot)


def panda():
    return [
        # body
        ellipse(0, 120, 150, 140),
        ellipse(0, 140, 88, 95, sw=SW2),
        # feet
        ellipse(-115, 235, 68, 46), ellipse(115, 235, 68, 46),
        ellipse(-115, 242, 28, 22, sw=SW2), ellipse(115, 242, 28, 22, sw=SW2),
        circle(-148, 220, 8, sw=SW2), circle(-130, 205, 8, sw=SW2), circle(-108, 202, 8, sw=SW2),
        circle(148, 220, 8, sw=SW2), circle(130, 205, 8, sw=SW2), circle(108, 202, 8, sw=SW2),
        # ears + head
        circle(-108, -222, 46), circle(108, -222, 46),
        circle(-108, -222, 24, sw=SW2), circle(108, -222, 24, sw=SW2),
        ellipse(0, -120, 150, 125),
        ellipse(-58, -122, 36, 46, rot=35), ellipse(58, -122, 36, 46, rot=-35),
        eye(-52, -126, 15), eye(52, -126, 15),
        ellipse(0, -62, 48, 34, sw=SW2),
        nose(0, -78, 15),
        line("M0 -70 L0 -58", SW2),
        smile(-14, -56, 14, 6, sw=SW2), smile(14, -56, 14, 6, sw=SW2),
        cheek(-100, -68, 14), cheek(100, -68, 14),
        # bamboo held in paws
        bamboo(25, 40, 430, rot=28, nodes=5),
        leaf(130, -150, 70, -60, sw=SW2), leaf(132, -150, 60, -5, sw=SW2),
        # arms + paws over bamboo
        ellipse(-95, 50, 46, 85, rot=-35), ellipse(105, 30, 46, 85, rot=40),
        ellipse(-40, 95, 42, 34), ellipse(50, -5, 42, 34),
        # leaf being munched
        leaf(10, -48, 60, 150, sw=SW2),
    ]


def draw():
    items = [
        bamboo(120, 520, 820, nodes=6), leaf(140, 330, 70, -30), leaf(100, 500, 70, 200),
        bamboo(730, 540, 780, nodes=6, w=36), leaf(712, 300, 70, 210), leaf(748, 560, 70, -20),
        hills(880, amp=30, bumps=2),
        place(panda(), 420, 600, 1.15),
        grass_tuft(140, 980), grass_tuft(700, 985, 1.2),
    ]
    return items
