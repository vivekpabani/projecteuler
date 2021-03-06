#!/usr/bin/env python


"""
Problem Definition :

The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...
Let us list the factors of the first seven triangle numbers:
    
1: 1
3: 1,3
6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28

We can see that 28 is the first triangle number to have over five divisors.
What is the value of the first triangle number to have over five hundred divisors?'''

"""

import math


def find_triangle(i):
    return i*(i+1)/2


def find_count(i):
    number = 1
    count = 0
    while number < int(math.sqrt(i)):
        if i % number == 0:
            count += 2
        number += 1
    if math.sqrt(i) == number:
        count += 1
    return count
    

def main():

    final_count, triangle = 0, 0
    num = 0

    while final_count < 500:
        num += 1
        triangle = find_triangle(num)
        final_count = find_count(triangle)

    print triangle

if __name__ == '__main__':
    main()
