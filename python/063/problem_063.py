#!/usr/bin/env python


"""
Problem Definition :

The 5-digit number, 16807=75, is also a fifth power. Similarly, the 9-digit number, 134217728=89, is a ninth power.

How many n-digit positive integers exist which are also an nth power?

"""

__author__ = 'vivek'

import time


def main():

    start_time = time.clock()

    count = 2
    total = 0
    power = 1
    new_start = 1

    while count > 1 and new_start:

        count = 0
        length = 0
        start = new_start
        new_start = 0

        while length <= power:

            answer = pow(start, power)
            length = len(str(answer))

            if length == power:
                total += 1

                if new_start == 0:
                    new_start = start

            start += 1
            count += 1

        power += 1

    print("total", total)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()

