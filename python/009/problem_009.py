#!/usr/bin/env python


"""
Problem Definition :

A Pythagorean triplet is a set of three natural numbers, a < b < c, for which, a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

import math
import sys


def main():

    for a in xrange(1, 1001):
        for b in xrange (a, 1001):
            c = a**2 + b**2
            d = math.sqrt(c)

            if d.is_integer() and a+b+d == 1000:
                print a, b, int(d)
                sys.exit(0)


if __name__ == '__main__':
    main()

        