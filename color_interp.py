#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk
import operator

RED, YELLOW, GREEN = (255, 0, 0), (255, 255, 0), (0, 255, 0)
CYAN, BLUE, MAGENTA = (0, 255, 255), (0, 0, 255), (255, 0, 255)
ORANGE = (255, 165, 0)


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb

# rgb = (255, 255, 0)
# print("rgb =", rgb)
# hex = _from_rgb(rgb)
# print("hex = ", hex)
# raise SystemExit

def show_color():
    COLOR += 1
    print(COLOR)
    root.configure(bg=_from_rgb((0, 10, 255)))
    root.after(1000, show_color)


class DaysToGoIter(object):

    def __init__(self, start=0, steps=20, start_color=YELLOW, stop_color=RED):
        self.start = start
        self.steps = steps
        self.start_color = start_color
        self.stop_color = stop_color
        self._min, self._max = 0, 255
        self.incr = (self._max - self._min) / steps
        self.num = start

    def __iter__(self):
        return self

    def colfunc(self, val, minval, maxval, startcolor, stopcolor):
        """ Convert value in the range minval...maxval to a color in the range
            startcolor to stopcolor. The colors passed and the one returned are
            composed of a sequence of N component values (e.g. RGB).
            -- KH -- added rounding
        """
        f = float(val - minval) / (maxval - minval)
        return tuple(round(f * (b - a) + a) for (a, b) in zip(startcolor, stopcolor))

    def __next__(self):
        num = self.num
        if num >= self.steps - 10:
            val = self._max
        else:
            val = round(self._min + round(self.num * self.incr, 1))
        rgb = self.colfunc(val, self._min, self._max, self.start_color, self.stop_color)
        self.num += 1
        return num, rgb


DAYS2GOCOLOR = {
    20: (255, 255, 0),
    19: (255, 242, 0),
    18: (255, 229, 0),
    17: (255, 217, 0),
    16: (255, 204, 0),
    15: (255, 191, 0),
    14: (255, 179, 0),
    13: (255, 166, 0),
    12: (255, 153, 0),
    11: (255, 140, 0),
    10: (255, 0, 0),
     9: (255, 0, 0),
     8: (255, 0, 0),
     7: (255, 0, 0),
     6: (255, 0, 0),
     5: (255, 0, 0),
     4: (255, 0, 0),
     3: (255, 0, 0),
     2: (255, 0, 0),
     1: (255, 0, 0),
     0: (255, 0, 0),
}


def get_days2go_rgb(d2go):
    """return RGB based on days to go input (int)"""
    max_key = max(DAYS2GOCOLOR.items(), key=operator.itemgetter(1))[0]
    if d2go > max_key:
        rgb = (255, 255, 255)  # white
    elif d2go < 0:
        rgb = (255, 0, 255)  # magenta
    else:
        rgb = DAYS2GOCOLOR[d2go]
    return rgb



if __name__ == '__main__':
    count = 0
    count_days = 20
    ci = DaysToGoIter()
    print(' 2go       R    G    B')
    while count <= count_days:
        count += 1
        num, rgb = next(ci)
        print(' {:3d} -> ({:3d}, {:3d}, {:3d})'.format(20-num, *rgb))

    # root = tk.Tk()
    # root.after(1000, show_color)
    # root.configure(bg=_from_rgb((0, 10, 255)))
    # root.mainloop()
