__author__ = 'vivek'

import time
import itertools

startTime = time.clock()

print int(''.join(map(str,list(itertools.permutations(range(10)))[999999])))

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))