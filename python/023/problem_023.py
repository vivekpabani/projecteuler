#!/usr/bin/env python


"""
Problem Definition :

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.
A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.
As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two
abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.
Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.'''

"""

import math


def find_sum_factors(i):
    number = 2
    ans = 1
    while number <= int(math.sqrt(i)):
        if i % number == 0:
            ans += (number + (i/number))
        number += 1
    if math.sqrt(i) == number - 1:
        ans -= number
    return ans


def main():
    abundant_numbers = list()
    sum_abundant_ref = [0]*60000
    sum_abundant = list()

    for i in xrange(1, 30000):
        if i < find_sum_factors(i):
            abundant_numbers.append(i)

    length_abundant = len(abundant_numbers)

    for i in xrange(0, length_abundant):
        for j in xrange(i, length_abundant):
            temp_sum = abundant_numbers[i]+abundant_numbers[j]
            sum_abundant_ref[temp_sum] = 1

    for i in xrange(0, 28124):
        if sum_abundant_ref[i] == 1:
            sum_abundant.append(i)

    all_sum = sum(range(1, 28124))

    print all_sum-sum(sum_abundant)

if __name__ == '__main__':
    main()
