__author__ = 'vivek'

import time
from fractions import gcd

#--- In Progress. ---#

startTime = time.clock()

for denominator in xrange(20000,50000):
    resilient = 0
    for numerator in xrange(1,denominator):
        if gcd(numerator,denominator)==1:
            resilient += 1
    if float(resilient)/float(denominator-1) < 15499.0/94744:
        print("found")
        break
print(numerator, denominator, resilient)


print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
