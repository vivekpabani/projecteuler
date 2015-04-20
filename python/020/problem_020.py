#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time
import math


def main():
    
    start_time = time.clock()

    number = math.factorial(100)
    add = 0

    while number > 0:
        digit = number % 10
        number /= 10
        add += digit

    print(add)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()

