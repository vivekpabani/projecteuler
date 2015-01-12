#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time

startTime = time.clock()

l1 = [1,2]
l2 = [2,3]

print(set(l1)-set(l2))

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
