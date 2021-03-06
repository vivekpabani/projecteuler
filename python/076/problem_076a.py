#!/usr/bin/env python


"""
Problem Definition :

Let p(n) represent the number of different ways in which n coins can be separated into piles. For example, five coins can separated into piles in exactly seven different ways, so p(5)=7.
Find the least value of n for which p(n) is divisible by one million.

"""

__author__ = 'vivek'

import time

startTime = time.clock()


penta = []
partition_numbers = []
partition_numbers.append(1)


def pentagonal(num):
    return num*(3*num - 1)/2


def alternate(num):
    if num > 0:
        return -1*num
    else:
        return (-1*num)+1


def partition(num):
    global partition_numbers
    add = 0
    i = 0
    start = 0
    symbol = 1

    while penta[i] <= num:

        add += symbol*partition_numbers[num - penta[i]]

        start +=1

        if start%2 == 0:
            symbol *= (-1)
            start = 0

        i += 1

    return add


alt_num = 1
found = 0
number = 1

for i in xrange(100):
    penta.append(pentagonal(alt_num))
    alt_num = alternate(alt_num)


while number<101:
    partition_number = partition(number)
    partition_numbers.append(partition_number)
    number +=1


print(partition_numbers[100]-1)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
