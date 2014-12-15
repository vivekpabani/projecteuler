__author__ = 'vivek'

import time
import math
startTime = time.clock()

def isPrime(number) :
    global known_primes
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

def equation(a,b,n):
    return ((n*n)+(a*n)+b)

ans_a = 0
ans_b = 0
ans_n = 0
max_prime = 0

for a in xrange(-999,1000):
    for b in xrange(2,1000):
        n = 0
        found_prime = 0

        while(isPrime(equation(a,b,n))):
            found_prime = found_prime + 1
            n = n+1
        if found_prime > max_prime:
            max_prime = found_prime
            ans_a = a
            ans_b = b
            ans_n = n
print(ans_a, ans_b, ans_n)
print(ans_a*ans_b)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
