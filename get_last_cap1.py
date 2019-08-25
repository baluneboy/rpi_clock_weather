#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from datetime import datetime
import pyexcel_ods
from dateutil.rrule import rrule, MONTHLY, DAILY
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from datetime_interval import Interval


now = datetime.now().date()
rd_month = relativedelta(months=1)
rd_4days = relativedelta(days=4)
next_month = datetime(now.year, now.month, 1).date() + rd_month
fifth = next_month + rd_4days
warn_int = Interval(now, fifth)
print(warn_int.start, warn_int.end)
print(now in warn_int)
raise SystemExit

# def date_list(start, end):
#     # start = datetime(start.year, start.month, 1)
#     # end = datetime(end.year, end.month, 1)
#     dates = [dt.date() for dt in rrule(DAILY, dtstart=start, until=end)]
#     return dates
#
# start = datetime(2015, 12, 28).date()
# stop = datetime(2016, 1, 7).date()
# print(date_list(start, stop))
# raise SystemExit


# read data file
data = pyexcel_ods.get_data('/home/pi/data/six_count.ods')

curr_date = datetime.today().date()
print("curr_date", curr_date)

# reverse rows and get rid of empties
rows = [x for x in data['cap1'][::-1] if x != []]

# get most recent values
due_date, bal, paid_date = rows[0]
print("due_date, bal, paid_date:", due_date, bal, paid_date)

# compare dates to decide what condition we are in
tfg_color, tbg_color = 'white', 'gray'
if curr_date > due_date:
    # beyond due date (is this bad?)
    tfg_color, tbg_color = 'yellow', 'red'
elif due_date > curr_date > paid_date:
    # middle ground
    tfg_color, tbg_color = 'white', 'gray'

dom = curr_date.day
print("dom =", dom)
# if no entry, then change colors like so:
# 15-21: tfg_color, tbg_color = 'yellow', 'black'
# 22-26: tfg_color, tbg_color = 'red', 'black'
# 27-EM: tfg_color, tbg_color = 'black', 'white'
# 01-03: tfg_color, tbg_color = 'black', 'yellow'
# 04-05: tfg_color, tbg_color = 'black', 'red'

print(tfg_color, tbg_color)
