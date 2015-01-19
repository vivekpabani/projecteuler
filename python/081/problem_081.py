#!/usr/bin/env python


"""
Problem Definition :
    
In the 5 by 5 matrix below, the minimal path sum from the top left to the bottom right, by only moving to the right and down, is indicated in bold red and is equal to 2427.
    
Find the minimal path sum, in matrix.txt (right click and "Save Link/Target As..."), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.
    
"""
__author__ = 'vivek'

import time

startTime = time.clock()

value_matrix = []
for line in open('matrix.txt'):

    separator = ','
    temp_list = []

    line = line.split(separator)

    for value in line:
        temp_list.append(int(value))
    value_matrix.append(temp_list)


length = len(value_matrix)

answer_matrix = [[0]*length for i in range(length)]

for i in xrange(0, length):
    for j in xrange(0, length):
        if i == 0 and j == 0:
            answer_matrix[i][j] = value_matrix[i][j]
        elif i == 0 and j > 0:
            answer_matrix[i][j] = value_matrix[0][j] + answer_matrix[0][j-1]
        elif i > 0 and j == 0:
            answer_matrix[i][j] = value_matrix[i][0] + answer_matrix[i-1][0]
        else:
            if answer_matrix[i-1][j]<answer_matrix[i][j-1]:
                answer_matrix[i][j] = value_matrix[i][j] + answer_matrix[i-1][j]
            else:
                answer_matrix[i][j] = value_matrix[i][j] + answer_matrix[i][j-1]

print answer_matrix[length-1][length-1]

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
