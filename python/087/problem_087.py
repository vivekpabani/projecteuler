#!/usr/bin/env python


"""
Problem Definition :

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 2^2 + 2^3 + 2^4
33 = 3^2 + 2^3 + 2^4
49 = 5^2 + 2^3 + 2^4
47 = 2^2 + 3^3 + 2^4

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?

"""

__author__ = 'vivek'

import time
import math


def is_prime(num):
    if num < 0:
        return 0
    elif num == 2 or num == 3:
        return 1
    elif num % 2 == 0 or num % 3 == 0 or num == 1:
        return 0
    else:
        start = 5
        while start <= int(math.sqrt(num)):
            if num % start == 0:
                return 0
                break
            if num % (start+2) == 0:
                return 0
                break
            start += 6
        return 1


def main():
    start_time = time.clock()

    prime_numbers = [x for x in xrange(1, 8000) if is_prime(x)]

    p2 = list()
    p3 = list()
    p4 = list()

    answers = list()

    for number in prime_numbers:
        num1 = number**2
        if num1 < 50000000:
            p2.append(num1)
        else:
            break

    for number in prime_numbers:
        num2 = number**3
        if num2 < 50000000:
            p3.append(num2)
        else:
            break

    for number in prime_numbers:
        num3 = number**4
        if num3 < 50000000:
            p4.append(num3)
        else:
            break

    for num1 in p2:
        for num2 in p3:
            for num3 in p4:
                answer = num1 + num2 + num3
                if answer < 50000000:
                    answers.append(answer)
    answers = list(set(answers))

    print(len(answers))

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()

