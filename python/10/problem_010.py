#!/usr/bin/env python

import math

# Problem Definition :


def isPrime(number) :
    if number == 2 or number == 3 :
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

answer, num = 2,3

while num < 2000001 :
    if isPrime(num) :
        answer = answer + num
    num = num + 2

print answer
