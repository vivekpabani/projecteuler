#!/usr/bin/env python
#  coding=utf-8


"""
Problem Definition :

Find the unique positive integer whose square has the form 1_2_3_4_5_6_7_8_9_0,
where each “_” is a single digit.

"""

__author__ = 'vivek'

import time

startTime = time.clock()


def check_property(num):
    return str(num)[::2] == "1234567890"

lower_limit = 1010101000
upper_limit = 1389026600
current = upper_limit


while current > lower_limit:

    number = current - 30

    if check_property(str(number ** 2)) :
        print(number)
        break

    number = current - 70

    if check_property(str(number ** 2)) :
        print(number)
        break

    current -= 100


print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
