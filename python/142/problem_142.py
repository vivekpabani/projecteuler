#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time
import math
startTime = time.clock()

limit = 1000
answers = []
for x in xrange(1, limit):
    for y in xrange(x+1, limit):
        num1 = math.sqrt(x + y)
        num2 = math.sqrt(y - x)

        if num1 - int(num1) == 0 and num2 - int(num2) == 0:
            answers.append([x, y])

print(len   (answers))
#print(answers)
count = 0
length = len(answers)
for i in xrange(0, length):
    for j in xrange(i+1, length):
        #for k in xrange(j+1, length):
        common = set(answers[i]) & set(answers[j])
        if len(set(answers[i]+answers[j])) == 3 and [set(answers[i]) - common, set(answers[j]) - common] in answers :
            print(answers[i], answers[j])
            count += 1
print(count)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
