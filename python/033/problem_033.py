#!/usr/bin/env python


"""
Problem Definition :

The fraction 49/98 is a curious fraction, as an inexperienced mathematician in attempting to simplify it may incorrectly believe that 49/98 = 4/8, which is correct, is obtained by cancelling the 9s.

We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

There are exactly four non-trivial examples of this type of fraction, less than one in value, and containing two digits in the numerator and denominator.

If the product of these four fractions is given in its lowest common terms, find the value of the denominator.

"""

__author__ = 'vivek'

import time
from decimal import *

startTime = time.clock()

getcontext().prec = 5

def check_numbers(num1, num2) :
    cancelled = -1
    remaining_d = -1
    remaining_n = -1
    if str(num1)[0] == str(num2)[0]:
        cancelled = num1 / 10
        remaining_n = num1 % 10
        remaining_d = num2 % 10
    elif str(num1)[0] == str(num2)[1]:
        cancelled = num1 / 10
        remaining_n = num1 % 10
        remaining_d = num2 / 10
    elif str(num1)[1] == str(num2)[0]:
        cancelled = num1 % 10
        remaining_n = num1 / 10
        remaining_d = num2 % 10
    elif str(num1)[1] == str(num2)[1]:
        cancelled = num1 % 10
        remaining_n = num1 / 10
        remaining_d = num2 / 10

    return cancelled, remaining_n, remaining_d
answer_numerator = 1
answer_denominator = 1

for num1 in xrange(10,100):
    for num2 in xrange(num1, 100):
        if num1 != num2:
            comman, numerator, denominator = check_numbers(num1,num2)
            if comman > 0 and denominator > 0:
                if Decimal(numerator)/Decimal(denominator) == Decimal(num1)/Decimal(num2):
                    answer_numerator = answer_numerator * numerator
                    answer_denominator = answer_denominator * denominator


for i in [2,3,5,7,11,13]:
    while answer_denominator%i == 0 and answer_numerator%i == 0:
        answer_denominator = answer_denominator / i
        answer_numerator = answer_numerator / i
print(answer_denominator)



print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
