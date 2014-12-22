#!/usr/bin/env python


"""
Problem Definition :

A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.

"""

__author__ = 'vivek'

import time
from decimal import *
import operator

startTime = time.clock()

getcontext().prec = 2000
length = 0
answers = {}

for number in xrange(1,1001):
    answer = str(Decimal(1)/Decimal(number))[2:]
    str_length = len(answer)

    if str_length > 10:
        found = 0

        for i in xrange(0,10):
            dist = 1
            while i+ 2*dist <= str_length:
                if answer[i:i+dist] == answer[i+dist:i+2*dist] and int(answer[i:i+dist]) > 0:
                    answers[number] = dist
                    found = 1
                    break
                dist += 1

            if found:
                break

print max(answers.iteritems(), key=operator.itemgetter(1))[0]

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
