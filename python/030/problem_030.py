#!/usr/bin/env python


"""
Problem Definition :

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 1^4 + 6^4 + 3^4 + 4^4
8208 = 8^4 + 2^4 + 0^4 + 8^4
9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.

"""

__author__ = 'vivek'

import time
import math


def main():

    start_time = time.clock()
    matched_numbers = []

    for count in xrange(2, 1000000):
        number = count
        addition = 0
        while number > 0:
            digit = number % 10
            number /= 10
            addition += math.pow(digit, 5)
        if addition == count:
            matched_numbers.append(count)

    print sum(matched_numbers)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()
