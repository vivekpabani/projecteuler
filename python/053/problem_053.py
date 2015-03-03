#!/usr/bin/env python
# coding=utf-8

"""
Problem Definition :

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =
n!
r!(n−r)!
,where r ≤ n, n! = n×(n−1)×...×3×2×1, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1 ≤ n ≤ 100, are greater than one-million?

"""

__author__ = 'vivek'

import time
from operator import mul
from fractions import Fraction


def nck(n, k):

    return int(reduce(mul, (Fraction(n-i, i+1) for i in xrange(k)), 1))


def main():

    start_time = time.clock()

    count = 0

    for num1 in xrange(1, 101):
        for num2 in xrange(1, num1+1):
            if nck(num1, num2) > 1000000:
                count += 1

    print(count)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()
