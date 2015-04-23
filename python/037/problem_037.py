#!/usr/bin/env python


"""
Problem Definition :

The number 3797 has an interesting property. Being prime itself, it is possible to continuously remove digits from left to right, and remain prime at each stage: 3797, 797, 97, and 7. Similarly we can work from right to left: 3797, 379, 37, and 3.

Find the sum of the only eleven primes that are both truncatable from left to right and right to left.

NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

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


def is_prime_trunck(number):
    
    special_char = ['2','3','5','7']
    
    if number < 0:
        return 0
    elif number == 2 or number == 3:
        return 1
    elif number % 2 == 0 or number % 3 == 0 or number == 1:
        return 0
    elif str(number)[-1:] not in special_char or str(number)[:1] not in special_char:
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


def is_right_trunckable(number):
    trunckable = 1
    number = str(number)[:-1]
    while number:
        if not is_prime(int(number)):
            trunckable = 0
            break
        number = str(number)[:-1]
    return trunckable


def is_left_trunckable(number):
    trunckable = 1
    number = str(number)[1:]
    while number:

        if not is_prime(int(number)):
            trunckable = 0
            break
        number = str(number)[1:]
    return trunckable


def main():

    start_time = time.clock()

    prime_numbers = list()
    trunckable_primes = list()

    for x in xrange(1, 1000000):
        if is_prime_trunck(x):
            prime_numbers.append(x)

    prime_numbers.remove(2)
    prime_numbers.remove(3)
    prime_numbers.remove(5)
    prime_numbers.remove(7)

    for num in prime_numbers:
        if is_right_trunckable(num) and is_left_trunckable(num):
            trunckable_primes.append(num)

    add = 0

    for item in trunckable_primes:
        add += item

    print(add)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()
