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
#partition_numbers.append(1)

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
    #print("Number", num)
    while True:
        #try:
        if penta[i] <= num:
            add = add + symbol*partition_numbers[num - penta[i]]
            #print(partition_numbers)
            #print(add, symbol, num, i, penta[i], partition_numbers[num - penta[i]])
            #print("Symbol",symbol)
        #except:
        else:
            break

        start +=1

        if start%2 == 0:
            symbol = symbol*(-1)
            start = 0

        i +=1

    return add


alt_num = 1
found = 0
number = 1

for i in xrange(60000):
    penta.append(pentagonal(alt_num))
    alt_num = alternate(alt_num)


while not found:
    #print(alt_num)
    #penta.append(pentagonal(alt_num))
    #alt_num = alternate(alt_num)
    partition_number = partition(number)
    partition_numbers.append(partition_number)
    #if len(partition_numbers) > 2000:
    if partition_number%1000000 == 0 or len(partition_numbers) > 60000:
        found = 1
        print(number)
        print(partition_number)
    number +=1

#print(penta)
print(partition_number)
print(len(partition_numbers))
#print(partition_numbers)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
