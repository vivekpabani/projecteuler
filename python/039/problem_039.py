#!/usr/bin/env python


"""
Problem Definition :

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p <= 1000, is the number of solutions maximised?
"""

__author__ = 'vivek'

import time

startTime = time.clock()

square_l = []
square_d = {}
answers = [0]*1001
limit = 1000
maximum = limit/2
for number in xrange(1,500):
    square = number**2
    square_l.append(square)
    square_d[square] = number



for number1 in xrange(3,maximum):
    for number2 in xrange(1,maximum-number1):
        if number2>number1:
            break
        add = number1**2 + number2**2
        if add in square_l :
            answer = number1+number2+square_d[add]
            if answer < 1001:
                answers[answer] += 1

print(answers.index(max(answers)))


print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
