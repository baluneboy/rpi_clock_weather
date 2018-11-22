#!/usr/bin/env python3

import time
from tkinter import *
from tkinter import ttk
from tkinter import font
from my_weather import get_weather


def quit(*args):
	root.destroy()


def show_time():

	time_str.set(time.strftime("%I:%M"))

	xmin, xmax = 0.47, 0.53
	A, B = (xmax - xmin) / 60.0, xmin
	min_float = float(time.strftime("%M"))
	xre = min_float * A + B

	ymin, ymax = 0.17, 0.80
	C, D = (ymax - ymin) / 60.0, ymin
	sec_float = float(time.strftime("%S"))
	yre = sec_float * C + D
	
	xmin2, xmax2 = 0.33, 0.66
	E, F = (xmax2 - xmin2) / 60.0, xmin2
	xre2 = min_float * E + F

	if (min_float % 10) == 0 and sec_float == 0:
		weat_str.set(get_weather())
		#print('time is %s, so get weather now' % time.strftime("%I:%M:%S"))
	if sec_float <= 30:
		weat_yre = 0.82
	else:
		weat_yre = 0.18
	weat_label.place(relx=xre2, rely=weat_yre, anchor=CENTER)

	#print('%.3f, %.3f' % (xre, yre))
	time_label.place(relx=xre, rely=yre, anchor=CENTER)
	root.after(1000, show_time)


root = Tk()
root.attributes("-fullscreen", True)
root.configure(background='black')
root.bind("<Escape>", quit)
root.bind("x", quit)
root.config(cursor="none")
root.after(1000, show_time)

fnt = font.Font(family='Helvetica', size=350, weight='bold')
fnt2 = font.Font(family='Helvetica', size=120, weight='bold')
time_str, weat_str = StringVar(), StringVar()
time_str.set(time.strftime("%I:%M:%S"))
weat_str.set('weather\nconditions')
time_label = ttk.Label(root, textvariable=time_str, font=fnt, foreground="white", background="black")
time_label.place(relx=0.5, rely=0.3, anchor=CENTER)
weat_label = ttk.Label(root, textvariable=weat_str, font=fnt2, foreground="white", background="black")
weat_label.place(relx=0.5, rely=0.7, anchor=CENTER)

root.mainloop()