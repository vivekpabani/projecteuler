#!/usr/bin/env python

import math

# Problem Definition :

def find_sum_factors(i) :
    number = 2
    sum = 1
    
    while number < int(math.sqrt(i)) :
        if i % number == 0 :
            sum = sum + number + (i/number)
        number = number + 1
    if math.sqrt(i) == number :
            sum = sum + number
    return sum

sum_div = [0]*10001
amicable = []
answer = 0

for i in xrange(1,10001):
    sum_div[i] = find_sum_factors(i)

for x in xrange(1,10001):
    if sum_div[x]<10001:
        if sum_div[x] != 1 and  sum_div[x] != x and x == sum_div[sum_div[x]] :
            amicable.append(x)

print sum(amicable)