#!/usr/bin/env python


"""
Problem Definition :

The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.

"""

__author__ = 'vivek'

import time
import math


def main():

    start_time = time.clock()
    maximum = 100000001
    limit = int(math.sqrt(maximum))+1

    matrix = [[0 for x in xrange(limit)] for x in xrange(limit)]
    answers = list()

    for i in xrange(1, limit):
        for j in xrange(i, limit):
            matrix[i][j] =  matrix[i][j-1] + (j*j)
            if str(matrix[i][j]) == str(matrix[i][j])[::-1] and matrix[i][j] < maximum and j != i:
                answers.append(matrix[i][j])

    print(sum(set(answers)))

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()


