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
import math

startTime = time.clock()

getcontext().prec = 200
length = 0
answers = {}

for number in xrange(1,100):
    answer = str(Decimal(1)/Decimal(number))[2:]
    print(number,answer)
    str_length = len(answer)

    if str_length > 10:
        found = 0

        for i in xrange(1,11):
            dist = 1
            while i+ 2*dist <= str_length:
                if answer[i:i+dist] == answer[i+dist:i+2*dist]:
                    answers[number] = dist
                    found = 1
                    break
                dist += 1

            if found:
                break
print(answers)

maxlength = 0
for key in answers:
    maxlength = max(maxlength,answers[key])

print(maxlength)

print(Decimal(1)/Decimal(61))

    #print(answer)
#print(length)

"""
x = 1.0/3
print(x)
print(x/9)

print(3.0/9)
#   print(10*x)

print(10*x - x)

print(divmod(1,6))

#print round(1/3, 20)
"""

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
