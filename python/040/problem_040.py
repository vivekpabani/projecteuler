#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time

startTime = time.clock()


#number_str = ''.join(str(x) for x in xrange(0,20))
#print(number_str)
limit = 1000000
length = 1
power = 0
while length < limit :
    power += 1
    length = length + pow(10,power)*power - pow(10,power-1)*(power)

print(length)
print(power)

number_str = ''.join(str(x) for x in xrange(0,pow(10,power)))
print len(number_str)

answer = 1

for i in xrange(0,7) :
    answer = answer * int(number_str[pow(10,i)])

print(answer)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
