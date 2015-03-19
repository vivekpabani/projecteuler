#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
It turns out that F541, which contains 113 digits, is the first Fibonacci number for which the last nine digits are 1-9
pandigital (contain all the digits 1 to 9, but not necessarily in order). And F2749, which contains 575 digits, is the
first Fibonacci number for which the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital,
find k.
"""

__author__ = 'vivek'

import time


def check_pandigital(number_s):

    if '0' not in number_s and len(''.join(set(number_s))) == 9:
        return 1
    else:
        return 0


def main():

    start_time = time.clock()

    num1, num2, count = 1, 1, 2

    while len(str(num2)) < 10:
        num1, num2 = num2, num1 + num2
        count += 1

    stat_count = count
    start_num1, start_num2 = num1, num2

    right_count, left_count = 0, 0
    right_numbers = list()
    left_numbers = list()

    while right_count < 200:
        num1, num2 = num2, num1 + num2
        count += 1
        if len(str(num2)) > 15:
            num1 %= pow(10, 12)
            num2 %= pow(10, 12)

        if check_pandigital(str(num2)[-9:]):

            right_numbers.append(count)
            right_count += 1

    num1, num2 = start_num1, start_num2
    count = stat_count

    while left_count < 200:
        num1, num2 = num2, num1 + num2
        count += 1
        if len(str(num2)) > 18:
            num1 /= pow(10, 5)
            num2 /= pow(10, 5)

        if check_pandigital(str(num2)[:9]):

            left_numbers.append(count)
            left_count += 1

    print(set(left_numbers) & set(right_numbers))

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()
