#!/usr/bin/env python


"""
Problem Definition :

We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once.
For example, 2143 is a 4-digit pandigital and is also prime.

What is the largest n-digit pandigital prime that exists?
"""

__author__ = 'vivek'

import time
import math
from itertools import permutations


def is_prime(number) :

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
    perms = [''.join(p) for p in permutations('1234567')]

    prime_numbers = []
    for num in perms:
        if is_prime(int(num)):
            prime_numbers.append(int(num))

    print(max(prime_numbers))

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()

