#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

import math


def find_sum_factors(num):
    number = 2
    addition = 1
    
    while number < int(math.sqrt(num)):
        if num % number == 0:
            addition += number + (num/number)
        number += 1
    if math.sqrt(num) == number:
            addition += number
    return addition


def main():
    sum_div = [0]*10001
    amicable = list()

    for i in xrange(1, 10001):
        sum_div[i] = find_sum_factors(i)

    for x in xrange(1, 10001):
        if sum_div[x] < 10001:
            if sum_div[x] != 1 and sum_div[x] != x and x == sum_div[sum_div[x]]:
                amicable.append(x)

    print sum(amicable)

if __name__ == '__main__':
    main()