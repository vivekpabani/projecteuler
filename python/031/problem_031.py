#!/usr/bin/env python
# coding=utf-8


"""
Problem Definition :

In England the currency is made up of pound, £, and pence, p, and there are eight coins in general circulation:

1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
It is possible to make £2 in the following way:

1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
How many different ways can £2 be made using any number of coins?

"""

__author__ = 'vivek'

import time

startTime = time.clock()

denominations = [1, 2, 5, 10, 20, 50, 100, 200]


def combination(amount, denom):

    if amount < 0:
        return 0

    if denom == 0:
        return 1

    return combination(amount,denom-1) + combination(amount-denominations[denom],denom)

print combination(200,7)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
