#!/bin/python
from __future__ import print_function
import os


# Complete the timeConversion function below.
def tine_conversion(s):
    #
    # Write your code here.
    #
    hour_am_pm, minutes_am_pm, seconds_am_pm, am_pm = split_string_time(s)
    military_hour = get_military_hour(hour_am_pm, am_pm)
    military_time = get_military_time(military_hour, minutes_am_pm, seconds_am_pm)
    return military_time


def split_string_time(s):
    return s[:2], s[3:5], s[6:8], s[8:10]


def get_military_hour(am_pm_hour, am_pm):
    am_pm_hour = int(am_pm_hour)
    military_hour = None
    if am_pm == "AM":
        if am_pm_hour == 12:
            military_hour = "00"
        else:
            military_hour = str(am_pm_hour)
    else:
        if am_pm_hour == 12:
            military_hour = "12"
        else:
            military_hour = str(am_pm_hour + 12)
    military_hour = validate_hour_length(military_hour)
    return military_hour


def validate_hour_length(military_hour):
    if len(military_hour) == 1:
        military_hour = "0" + military_hour
    return military_hour


def get_military_time(military_hour, minutes_am_pm, seconds_am_pm):
    return military_hour + ":" + minutes_am_pm + ":" + seconds_am_pm


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')
    s = input()
    result = tine_conversion(s)
    f.write(result + '\n')
    f.close()
