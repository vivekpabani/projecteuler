__author__ = 'vivek'

import time
import math

startTime = time.clock()

power_answers = []

for a in xrange(2,101):
    for b in xrange(2,101):
        power_answers.append(math.pow(a,b))
power_answers = list(set(power_answers))
print(len(power_answers))
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
