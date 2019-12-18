#!/bin/python

import math
import os
import random
import re
import sys
from collections import namedtuple

TIME_DEFINITION = {0: " o' clock",
                   15: "quarter past ",
                   30: "half past ",
                   45: "quarter to ",
                   98: " minutes past ",
                   99: " minutes to "}

ONES = {0: 'zero', 
        1: 'one', 
        2: 'two', 
        3: 'three', 
        4: 'four', 
        5: 'five', 
        6: 'six',
        7: 'seven', 
        8: 'eight', 
        9: 'nine',
        10: 'ten',
        11: 'eleven', 
        12: 'twelve',
        13: 'thirteen',
        14: 'fourteen', 
        15: 'fifteen', 
        16: 'sixteen',
        17: 'seventeen',
        18: 'eighteen',
        19: 'nineteen'}

TENS = {10: 'ten',
        20: 'twenty', 
        30: 'thirty', 
        40: 'forty', 
        50: 'fifty'}


# Complete the timeInWords function below.
def time_in_words(h, m):
    """
    :param h: hours
    :param m: minutes
    :return: input time in words
    """
    time_in_words = ""
    if m == 0:
        time_in_words = get_num_in_text(h)
        time_in_words += TIME_DEFINITION[m]
    elif m == 15 or m == 30 or m == 45:
        time_in_words += TIME_DEFINITION[m]
        time_in_words += get_num_in_text(h)
    else:
        if m< 30:
            fixed_time = 98
            tmp_h = h
            tmp_m = m
        else:
            fixed_time = 99
            tmp_m = 60 - m
            tmp_h = h + 1
        time_in_words += get_num_in_text(tmp_m)
        time_in_words += TIME_DEFINITION[fixed_time]
        time_in_words += get_num_in_text(tmp_h)
    return time_in_words


def get_num_in_text(num):
    num = int(num)
    num_in_text = ""
    if num < 20:
        num_in_text = ONES[num]
    elif num % 10 == 0:
        num_in_text = TENS[num]
    else:
        num = str(num)       
        num_in_text = TENS[int(num[0])*10] + " " + ONES[int(num[1])]
    return num_in_text


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    h = int(input())
    m = int(input())
    result = time_in_words(h, m)
    fptr.write(result + '\n')
    fptr.close()
