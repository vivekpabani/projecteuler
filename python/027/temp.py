__author__ = 'vivek'

import time

startTime = time.clock()

for x in xrange(0,10):
    print(x)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
