#!/usr/bin/env python


"""
Problem Definition :

Some positive integers n have the property that the sum [ n + reverse(n) ] consists entirely of odd (decimal) digits. For instance, 36 + 63 = 99 and 409 + 904 = 1313. We will call such numbers reversible; so 36, 63, 409, and 904 are reversible. Leading zeroes are not allowed in either n or reverse(n).

There are 120 reversible numbers below one-thousand.

How many reversible numbers are there below one-billion (10^9)?
"""

__author__ = 'vivek'

import time

startTime = time.clock()

answers = []


def reversible(number):
    even = 0

    while number > 0:
        number, digit = divmod(number,10)
        if digit %2 == 0 and number>0:
            even = 1
            break

    if even:
        return 0
    else:
        return 1


#number = 103
#print(reversed(str(number)))

for x in xrange(11,10000001):
    if x%10 !=0 and reversible(x + int(str(x)[::-1])):
        answers.append(x)

print(len(answers))

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
