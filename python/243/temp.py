__author__ = 'vivek'

import time
import math

startTime = time.clock()

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

print(isPrime(199999))

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
