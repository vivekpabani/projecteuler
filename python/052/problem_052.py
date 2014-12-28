#!/usr/bin/env python


"""
Problem Definition :


It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.

"""

__author__ = 'vivek'

import time

startTime = time.clock()

for num in xrange(1,1000000):
    if ''.join(sorted(str(num*2))) == ''.join(sorted(str(num*3))) == ''.join(sorted(str(num*4)))  == ''.join(sorted(str(num*5))) == ''.join(sorted(str(num*6))) :
        print(num)
        print(num*2, num*3, num*4, num*5, num*6)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
