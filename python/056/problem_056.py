#!/usr/bin/env python


"""
Problem Definition :

A googol (10100) is a massive number: one followed by one-hundred zeros; 100100 is almost unimaginably large: one
followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?
"""

__author__ = 'vivek'

import time


def main():

    start_time = time.clock()

    maximum = 0

    for a in xrange(95, 100):
        for b in xrange(95, 100):

            answer = pow(a, b)
            total = 0

            while answer > 0:

                answer, digit = divmod(answer, 10)
                total += digit

            maximum = max(maximum, total)

    print(maximum)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()
