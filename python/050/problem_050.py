#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time
import math


def is_prime(number):
    if number < 0:
        return 0
    elif number == 2 or number == 3:
        return 1
    elif number % 2 == 0 or number % 3 == 0 or number == 1:
        return 0
    else:
        start = 5
        while start <= int(math.sqrt(number)):
            if number % start == 0:
                return 0
                break
            if number % (start+2) == 0:
                return 0
                break
            start += 6
        return 1


def main():

    start_time = time.clock()

    prime_numbers = []

    for x in xrange(1, 3944):
        if is_prime(x):
            prime_numbers.append(x)

    length = len(prime_numbers)

    matrix = [[0 for x in range(length)] for x in range(length)]

    for j in xrange(0, length):
        try:
            matrix[0][j] = matrix[0][j-1] + prime_numbers[j]
        except:
            matrix[0][j] = prime_numbers[j]

    for i in xrange(1, length):
        for j in xrange(i, length):
            matrix[i][j] = matrix[i-1][j] - matrix[i-1][i-1]

    found = 0

    for num1 in xrange(0, length):
        for num2 in xrange(0, num1):
            if is_prime(matrix[num2][length-num1+num2]):
                print(num2, length-num1+num2)
                print(matrix[num2][length-num1+num2])
                found = 1
                break
        if found:
            break

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()

