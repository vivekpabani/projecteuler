#!/usr/bin/env python


"""
Problem Definition :

Starting in the top left corner of a 2*2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20*20 grid?

"""

box = [[0]*21]*21

for i in xrange (0,21) :
    for j in xrange (0,21) :
        if i == 0 or j == 0 :
            box[i][j] = 1
        else :
            box[i][j] = box[i-1][j] + box[i][j-1]

print box[20][20]