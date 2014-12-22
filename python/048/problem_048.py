#!/usr/bin/env python


"""
Problem Definition :

The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

__author__ = 'vivek'

import time

startTime = time.clock()

total = 0

for number in xrange(1,1001):
    total += pow(number,number)
#print(total)
#number = '123456789'
print(str(total)[-10:])

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
