#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time

startTime = time.clock()


def check_pandigital(number_s):

    if '0' not in number_s and len(''.join(set(number_s))) == 9:
        return 1
    else:
        return 0

num1 = 1
num2 = 1
count = 2
#limit = 10000

while len(str(num2)) < 10:
    num1, num2 = num2, num1 + num2
    #print num2, len(str(num2))
    count += 1

stat_count = count
start_num1 = num1
start_num2 = num2

right_count = 0
left_count = 0
right_numbers = []
left_numbers = []

while right_count < 200:
    num1, num2 = num2, num1 + num2
    count += 1
    if len(str(num2)) > 15:
        num1 %= pow(10,12)
        num2 %= pow(10,12)

    if check_pandigital(str(num2)[-9:]):

        right_numbers.append(count)
        right_count += 1


num1 = start_num1
num2 = start_num2
count = stat_count

while left_count < 200:
    num1, num2 = num2, num1 + num2
    count += 1
    if len(str(num2)) > 18:
        num1 /= pow(10,5)
        num2 /= pow(10,5)

    if check_pandigital(str(num2)[:9]):

        left_numbers.append(count)
        left_count += 1

print(set(left_numbers) & set(right_numbers))

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))


