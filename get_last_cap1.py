#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# from datetime import datetime
import time
import pyexcel_ods
import syslog
from dateutil.rrule import rrule, MONTHLY, DAILY
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta
from datetime_interval import Interval
from color_interp import get_days2go_rgb, _from_rgb


def paid_already(target_due_date):
    """return True if info in local copy of six_count.ods shows paid, else False"""

    is_paid = False
    curr_date = datetime.today().date()

    # read data file
    data = pyexcel_ods.get_data('/home/pi/data/six_count.ods')

    # reverse rows and get rid of empties
    rows = [x for x in data['cap1'][::-1] if x != []]

    # get most recent values
    due_date, bal, paid_date = rows[0]

    # num days paid before due
    num_days_before_due = (target_due_date - paid_date).days
    # print("due_date, bal, paid_date:", due_date, bal, paid_date)

    # see if paid_date is less than 2 weeks before target_due_date
    if num_days_before_due <= 14:
        is_paid = True

    return is_paid


def get_due_date(now):
    rd_month = relativedelta(months=1)
    rd_4days = relativedelta(days=4)
    target_month = datetime(now.year, now.month, 1).date()
    if now.day > 5:
        target_month += rd_month
    due_date = target_month + rd_4days
    return due_date


def get_days2go(now):
    due_date = get_due_date(now)
    warn_date = due_date - relativedelta(days=20)
    days_2go = (due_date - now).days
    return days_2go


def get_font_color():
    now_date = datetime.now().date()
    days2go = get_days2go(now_date)
    targ_due_date = get_due_date(now_date)
    is_paid = paid_already(targ_due_date)

    # print('is_paid is', is_paid)
    # print('days_2go =', days2go)
    syslog.syslog('@%s, is_paid = %s, days2go = %d' % (time.strftime('%I:%M'), str(is_paid), days2go))

    # warn_int = Interval(warn_date, due_date)
    # print("warn interval:", warn_int.start, warn_int.end)
    # print("now is in warn interval:", now in warn_int)

    if is_paid:
        rgb = (255, 255, 255)
    else:
        rgb = get_days2go_rgb(days2go)
    # print('rgb =', get_days2go_rgb(days2go))

    hex_code = _from_rgb(rgb)
    syslog.syslog('font color hex_code = %s' % hex_code)

    return hex_code


# rgb_font = get_font_color()
# print('rgb_font =', rgb_font)
