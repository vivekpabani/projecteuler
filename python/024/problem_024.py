#!/usr/bin/env python


""" Problem Definition :
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

    012   021   102   120   201   210

    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?.
"""

__author__ = 'vivek'

import math
import time


def main():
    start_time = time.clock()

    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    target = 1000000
    result = 0
    result_digits = list()


    while result != target:
        length = len(digits)
        fact_len = length - 1

        for count in xrange(length):
            if result + math.factorial(fact_len) > target:
                break
            elif result + math.factorial(fact_len) == target:
                if fact_len == 1:
                    result += math.factorial(fact_len)
                    break
                else:
                    break
            else:
                result += math.factorial(fact_len)
        result_digits.append(digits[count])

        del digits[count]

    result_string = ''.join([str(item) for item in (result_digits + digits)])

    print(result_string)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()
