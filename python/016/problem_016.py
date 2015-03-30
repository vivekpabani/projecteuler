#!/usr/bin/env python


"""
Problem Definition :

2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2^1000?

"""

__author__ = 'vivek'

import time


def main():
    start_time = time.clock()

    number = pow(2, 1000)
    add = 0

    while number > 0 :
        digit = number % 10
        number /= 10
        add += digit

    print(add)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()
