__author__ = 'vivek'

import time
import math

startTime = time.clock()
matched_numbers = []
for count in xrange(2,1000000):
    number = count
    addition = 0
    while(number>0):
        digit = number%10
        number = number/10
        addition = addition + math.pow(digit,5)
    if addition == count:
        matched_numbers.append(count)
print(matched_numbers)

print sum(matched_numbers)




print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
