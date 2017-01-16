#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

"""

import math


def find_sum_factors(num):
    number = 2
    addition = 1
    
    while number < int(math.sqrt(num)):
        if num % number == 0:
            addition += number + int((num/number))
        number += 1

    if math.sqrt(num) == number:
            addition += number

    return int(addition)


def main():
    limit = 10001
    sum_factors_dict = [0 for i in range(limit)]
    amicable = list() 

    for i in range(1, limit):
        sum_factors_dict[i] = find_sum_factors(i)

    for x in range(2, limit):
        if -1 < sum_factors_dict[x] < limit and sum_factors_dict[x] != x and x == sum_factors_dict[sum_factors_dict[x]]:
            amicable.append(x)
            amicable.append(sum_factors_dict[x])
            sum_factors_dict[sum_factors_dict[x]] = -1  
    print(sum(amicable))

if __name__ == '__main__':
    main()
