#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

Euler discovered the remarkable quadratic formula:
n² + n + 41
It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39.
However, when n = 40, 402 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, and certainly when
n = 41, 41² + 41 + 41 is clearly divisible by 41.

The incredible formula  n² − 79n + 1601 was discovered, which produces 80 primes
for the consecutive values n = 0 to 79. The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:
n² + an + b, where |a| < 1000 and |b| < 1000 where |n| is the modulus/absolute value of n
e.g. |11| = 11 and |−4| = 4

Find the product of the coefficients, a and b, for the quadratic expression that produces the
maximum number of primes for consecutive values of n, starting with n = 0.

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
            if number % (start+2) == 0:
                return 0
            start += 6
        return 1


def equation(a, b, n):
    return (n*n)+(a*n)+b


def main():

    start_time = time.clock()
    
    ans_a = 0
    ans_b = 0
    ans_n = 0
    max_prime = 0

    for a in xrange(-999, 1000):
        for b in xrange(2, 1000):
            n = 0
            found_prime = 0

            while is_prime(equation(a, b, n)):
                found_prime += 1
                n += 1
            if found_prime > max_prime:
                max_prime = found_prime
                ans_a, ans_b, ans_n = a, b, n

    print(ans_a, ans_b, ans_n)
    print(ans_a*ans_b)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()

