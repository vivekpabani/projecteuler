#!/usr/bin/env python


"""
Problem Definition :

The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.

There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

How many circular primes are there below one million?

"""

__author__ = 'vivek'

import time
import math

startTime = time.clock()

prime_numbers = []
prime_rotations = []


def isPrime(number) :
    if number < 0:
        return 0
    elif number == 2 or number == 3 :
        return 1
    elif number % 2 == 0 or number % 3 ==0 or number == 1 :
        return 0
    else :
        start = 5
        while (start <= int(math.sqrt(number))) :
            if(number % start == 0) :
                return 0
                break
            if(number % (start+2) == 0) :
                return 0
                break
            start = start + 6
        return 1


def rotation(number):
    rotations = []
    rotations.append(number)
    length = len(str(number)) - 1

    if length == 0:
        return rotations
    else:
        for count in range(length):
            digit = number%10
            number = number/10
            number = digit*pow(10,length) + number
            rotations.append(number)
        return rotations


def isPrimeRot(numbers):
    allPrime = 1
    for number in numbers:
        if not isPrime(int(number)):
            allPrime = 0
            break
    return allPrime

for x in xrange(1,1000000):
    if isPrime(x):
        prime_numbers.append(x)

for number in prime_numbers:
    if isPrimeRot(rotation(number)):
        prime_rotations.append(number)

print(len(prime_rotations))

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))