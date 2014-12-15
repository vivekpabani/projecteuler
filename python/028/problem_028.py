__author__ = 'vivek'

import time

startTime = time.clock()

answer = 1
number = 1
difference = 2
spiral_size = 1001
loop_size = (spiral_size+1)/2

for loop in xrange(loop_size-1):
    for count in xrange(4):
        number = number + difference
        answer = answer + number
    difference = difference + 2

print(answer)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
