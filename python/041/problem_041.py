#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time
import math
from itertools import permutations
perms = [''.join(p) for p in permutations('1234567')]
startTime = time.clock()

prime_numbers = []


def isPrime(number) :

    if number < 0:
        return 0
    elif number == 2 or number == 3 :
        return 1
    elif number % 2 == 0 or number % 3 ==0 or number == 1 :
        return 0
    else :
        start = 5
        while start <= int(math.sqrt(number)) :

            if number % start == 0 :
                return 0
                break
            if number % (start+2) == 0 :
                return 0
                break
            start = start + 6
        return 1

for number in perms:
    if isPrime(int(number)):
        prime_numbers.append(int(number))

print(max(prime_numbers))

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
