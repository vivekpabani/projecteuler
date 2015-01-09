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

startTime = time.clock()


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


prime_numbers = [x for x in xrange(1,8000) if is_prime(x)]


p2 = []
p3 = []
p4 = []

answers = []

for number in prime_numbers:
    num = number**2
    if num < 50000000:
        p2.append(num)
    else:
        break

for number in prime_numbers:
    num = number**3
    if num < 50000000:
        p3.append(num)
    else:
        break

for number in prime_numbers:
    num = number**4
    if num < 50000000:
        p4.append(num)
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

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
