__author__ = 'vivek'

import time
import math

startTime = time.clock()

prime_numbers = []
trunckable_primes = []

special_char = ['2','3','5','7']


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


def isPrimeTrunck(number) :

    if number < 0:
        return 0
    elif number == 2 or number == 3 :
        return 1
    elif number % 2 == 0 or number % 3 ==0 or number == 1 :
        return 0
    elif str(number)[-1:] not in special_char or str(number)[:1] not in special_char:
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


def isRightTrunckable(number):
    trunckable = 1
    number = str(number)[:-1]
    while number:

        if not isPrime(int(number)):
            trunckable = 0
            break
        number = str(number)[:-1]
    return trunckable


def isLeftTrunckable(number):
    trunckable = 1
    number = str(number)[1:]
    while number:

        if not isPrime(int(number)):
            trunckable = 0
            break
        number = str(number)[1:]
    return trunckable

for x in xrange(1,1000000):
    if isPrimeTrunck(x):
        prime_numbers.append(x)
print("Prime Numbers Found")

prime_numbers.remove(2)
prime_numbers.remove(3)
prime_numbers.remove(5)
prime_numbers.remove(7)

for number in prime_numbers:
    if isRightTrunckable(number) and isLeftTrunckable(number):
        trunckable_primes.append(number)

add = 0
for item in trunckable_primes:
    add = add+item
print(add)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
