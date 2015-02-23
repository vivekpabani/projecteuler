#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :
An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

"""

__author__ = 'vivek'

import time


def main():
    start_time = time.clock()

    limit = 1000000
    length = 1
    power = 0

    while length < limit :
        power += 1
        length = length + pow(10, power)*power - pow(10, power-1)*power

    number_str = ''.join(str(x) for x in xrange(0, pow(10, power)))

    answer = 1

    for i in xrange(0, 7):
        answer *= int(number_str[pow(10, i)])

    print(answer)
    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()

