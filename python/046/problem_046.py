#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

It was proposed by Christian Goldbach that every odd composite number can be written as the sum of a prime and twice a square.

9 = 7 + 2×1^2
15 = 7 + 2×2^2
21 = 3 + 2×3^2
25 = 7 + 2×3^2
27 = 19 + 2×2^2
33 = 31 + 2×1^2

It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?

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

    prime_numbers = []

    square_sums = [2*i*i for i in xrange(1, 100)]

    for x in xrange(1, 10000):
        if is_prime(x):
            prime_numbers.append(x)

    num = 9

    while 1:
        if num not in prime_numbers:
            found = 0
            prime_count = 0
            prime_number = prime_numbers[prime_count]

            while prime_number < num:
                square_count = 0
                addition = prime_number + square_sums[square_count]

                while addition <= num:
                    if addition == num:
                        found = 1
                        break
                    square_count += 1
                    addition = prime_number + square_sums[square_count]

                if found == 1:
                    break
                prime_count += 1
                prime_number = prime_numbers[prime_count]

        if found == 0:
            print(num)
            break
        num += 2

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()
