#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time
import math

startTime = time.clock()

number = math.factorial(100)
add = 0

while number > 0 :
    digit = number % 10
    number = number/10
    add = add + digit

print(add)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
