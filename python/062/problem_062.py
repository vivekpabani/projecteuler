#!/usr/bin/env python


"""
Problem Definition :

The cube, 41063625 (3453), can be permuted to produce two other cubes: 56623104 (3843) and 66430125 (4053). In fact, 41063625 is the smallest cube which has exactly three permutations of its digits which are also cube.

Find the smallest cube for which exactly five permutations of its digits are cube.

"""

__author__ = 'vivek'

import time
from collections import Counter

startTime = time.clock()

cubes = [''.join(sorted(str(i**3))) for i in xrange(0,10000)]

perm_count = Counter(cubes)
answer = 10000

for key in perm_count:
    if perm_count[key] == 5:
        answer = min(answer,cubes.index(key))

print(answer**3)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
