#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time
import math

startTime = time.clock()

with open("base_exp.txt") as f:
    numbers = [line.split(',') for line in f.readlines()]

count = 1
maximum = 0
answer = 0

for number in numbers:
    value = int(number[1])* math.log10(int(number[0]))
    if value > maximum:
        maximum = value
        answer = count
    count += 1
print answer
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
