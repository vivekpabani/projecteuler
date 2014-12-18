#!/usr/bin/env python


"""
Problem Definition :

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

21 22 23 24 25
20  7  8  9 10
19  6  1  2 11
18  5  4  3 12
17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""

__author__ = 'vivek'

import time

startTime = time.clock()

answer = 1
number = 1
difference = 2
spiral_size = 1001
loop_size = (spiral_size+1)/2

for loop in xrange(loop_size-1):
    for count in xrange(4):
        number = number + difference
        answer = answer + number
    difference = difference + 2

print(answer)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
