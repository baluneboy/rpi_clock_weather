#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import tkinter as tk

RED, YELLOW, GREEN = (255, 0, 0), (255, 255, 0), (0, 255, 0)
CYAN, BLUE, MAGENTA = (0, 255, 255), (0, 0, 255), (255, 0, 255)
ORANGE = (255, 165, 0)


def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb


def show_color():
    COLOR += 1
    print(COLOR)
    root.configure(bg=_from_rgb((0, 10, 255)))
    root.after(1000, show_color)


class DaysToAgoColorIter(object):

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
        if num >= self.steps - 7:
            val = self._max
        else:
            val = round(self._min + round(self.num * self.incr, 1))
        rgb = self.colfunc(val, self._min, self._max, self.start_color, self.stop_color)
        self.num += 1
        return num, rgb


if __name__ == '__main__':
    count = 0
    count_days = 20
    ci = DaysToAgoColorIter()
    print(' 2go       R    G    B')
    while count <= count_days:
        count += 1
        num, rgb = next(ci)
        print(' {:3d} -> ({:3d}, {:3d}, {:3d})'.format(20-num, *rgb))

    # root = tk.Tk()
    # root.after(1000, show_color)
    # root.configure(bg=_from_rgb((0, 10, 255)))
    # root.mainloop()
