#!/usr/bin/env python


"""
Problem Definition :

The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

"""

__author__ = 'vivek'

import time


def main():
    start_time = time.clock()

    palindromes = []

    for number in xrange(1, 1000000):
        if str(number) == str(number)[::-1] and str(bin(number))[2:] == str(bin(number))[:1:-1]:
            palindromes.append(number)

    add = 0

    for number in palindromes:
        add += number

    print(add)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()
