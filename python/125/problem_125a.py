#!/usr/bin/env python


"""
Problem Definition :

The palindromic number 595 is interesting because it can be written as the sum of consecutive squares: 62 + 72 + 82 + 92 + 102 + 112 + 122.

There are exactly eleven palindromes below one-thousand that can be written as consecutive square sums, and the sum of these palindromes is 4164. Note that 1 = 02 + 12 has not been included as this problem is concerned with the squares of positive integers.

Find the sum of all the numbers less than 108 that are both palindromic and can be written as the sum of consecutive squares.

"""

__author__ = 'vivek'

import time


def main():
    start_time = time.clock()

    answers = set()
    answer = 0

    for i in xrange(1, 10001):
        total = i*i
        for j in xrange(i+1, 10000):
            total += j*j
            if total > 100000000:
                break
            answers.add(total)

    for number in answers:
        s = str(number)

        if s == s[::-1]:
            answer += number

    print(answer)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()

