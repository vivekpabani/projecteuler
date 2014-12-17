__author__ = 'vivek'

import time
from fractions import gcd
import math

#--- In Progress. ---#

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

def eulerTotient(number, factors):
    totient = number
    for factor in factors:
        totient = int(totient*(1-(1.0/factor)))
    #if len(str(totient))==3 and str(totient)[0]== '1':
    #print(number,totient)
    return int(totient)


for x in xrange(1,10000000):
    if isPrime(x):
        prime_numbers.append(x)

for denominator in xrange(2,10000000):
    factors = []
    #resilient = 0
    for prime_number in prime_numbers:
        if prime_number < denominator:
            if denominator%prime_number == 0:
                factors.append(prime_number)
        else:
            break
    resilient = eulerTotient(denominator,factors)
    if float(resilient)/float(denominator-1) < 15499.0/94744:
        print("found")
        break
print(denominator, resilient)


print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
