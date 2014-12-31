#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

Consider the consecutive primes p1 = 19 and p2 = 23. It can be verified that 1219 is the smallest number such that the last digits are formed by p1 whilst also being divisible by p2.

In fact, with the exception of p1 = 3 and p2 = 5, for every pair of consecutive primes, p2 > p1, there exist values of n for which the last digits are formed by p1 and n is divisible by p2. Let S be the smallest of these values of n.

Find ∑ S for every pair of consecutive primes with 5 ≤ p1 ≤ 1000000.

"""

__author__ = 'vivek'

import time
import math

startTime = time.clock()

prime_numbers = []


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

#prime_numbers = [x for x in xrange(5,1000000,2) if isPrime(x)]

for x in xrange(5,1000,2):
    if isPrime(x):
        prime_numbers.append(x)

limit = len(prime_numbers)
answers = []

for i in xrange(0,limit-1):
    num1 = prime_numbers[i]
    num2 = prime_numbers[i+1]
    #for j in xrange(i+1, limit):

    #print("num1", num1)
    found = 0
    start = 0
    steps = [1,3,5,7,9]
    while not found:
        for j in xrange(0,5):
            num = start + steps[j]
            print(num)
            number = str(num2*num)
            if number.endswith(str(num1)):
                answers.append(int(number))
                found = 1
                break
        print("start",start)

        #start += 10

print answers
print(sum(answers))
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
