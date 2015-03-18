#!/usr/bin/env python


"""
Problem Definition :

Comparing two numbers written in index form like 211 and 37 is not difficult, as any calculator would confirm that 211 = 2048 < 37 = 2187.

However, confirming that 632382518061 > 519432525806 would be much more difficult, as both numbers contain over three million digits.

Using base_exp.txt (right click and 'Save Link/Target As...'), a 22K text file containing one thousand lines with a base/exponent pair on each line, determine which line number has the greatest numerical value.

NOTE: The first two lines in the file represent the numbers in the example given above.

"""

__author__ = 'vivek'

import time
import math


def main():
    start_time = time.clock()

    with open("base_exp.txt") as f:
        numbers = [line.split(',') for line in f.readlines()]

    count = 1
    maximum = 0
    answer = 0

    for number in numbers:
        value = int(number[1]) * math.log10(int(number[0]))
        if value > maximum:
            maximum = value
            answer = count
        count += 1

    print answer

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()

