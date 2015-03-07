#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

Starting with 1 and spiralling anticlockwise in the following way, a square spiral with side length 7 is formed.

37 36 35 34 33 32 31
38 17 16 15 14 13 30
39 18  5  4  3 12 29
40 19  6  1  2 11 28
41 20  7  8  9 10 27
42 21 22 23 24 25 26
43 44 45 46 47 48 49

It is interesting to note that the odd squares lie along the bottom right diagonal, but what is more interesting is that 8 out of the 13 numbers lying along both diagonals are prime; that is, a ratio of 8/13 ≈ 62%.

If one complete new layer is wrapped around the spiral above, a square spiral with side length 9 will be formed. If this process is continued, what is the side length of the square spiral for which the ratio of primes along both diagonals first falls below 10%?
"""

__author__ = 'vivek'

import time
import math


def is_prime(number):
    if number < 0:
        return 0
    elif number == 2 or number == 3:
        return 1
    elif number % 2 == 0 or number % 3 == 0 or number == 1:
        return 0
    else:
        start = 5
        while start <= int(math.sqrt(number)):
            if number % start == 0:
                return 0
                break
            if number % (start+2) == 0:
                return 0
                break
            start += 6
        return 1


def main():

    start_time = time.clock()
    num = 1
    step = 2
    dia = 1
    prime_count = 0

    while True:
        for i in xrange(4):
            num += step
            if is_prime(num):
                prime_count += 1
        dia += 4
        if prime_count*1.0/dia < 0.1:
            break
        step += 2

    print(num, dia,prime_count)
    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == "__main__":
    main()



