#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :
It is possible to show that the square root of two can be expressed as an infinite continued fraction.

√ 2 = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?

"""

__author__ = 'vivek'

import time

startTime = time.clock()

number = 1/2


def term_calc(numerator, denominator):
    if numerator > 0:
        term_num = (2*denominator)+numerator
        term_denom = denominator
    else:
        term_num = 2
        term_denom = 1
    return term_num, term_denom


def ans_calc(numerator, denominator):
    ans_num = numerator + denominator
    ans_denom = denominator
    return ans_num, ans_denom


start_num = 0
start_denom = 1
count = 0
for i in xrange(1000):
    start_denom, start_num = term_calc(start_num,start_denom)
    answer_num, answer_denom = ans_calc(start_num,start_denom)

    if len(str(answer_num)) > len(str(answer_denom)):
        count += 1

print(count)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
