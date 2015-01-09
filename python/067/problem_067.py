#!/usr/bin/env python


"""
Problem Definition :

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:

"""

import time



value_matrix = []

for line in open('tri.txt') :

    separator = ','
    temp_list = []
    
    line = line.split(separator)

    for value in line : 
        temp_list.append(value)
    value_matrix.append(temp_list)
        

length = len(value_matrix)
answer_matrix = []

for i in xrange(0,length) :

    temp_list = []

    for j in xrange(0,i+1) :
        temp_list.append(0)

    answer_matrix.append(temp_list)        


answer_matrix[0][0] = 59

startTime = time.clock()

for i in xrange(1,length) :
    for j in xrange(0,i+1) :

        if j == 0 :
            answer_matrix[i][j] = int(value_matrix[i][j]) + int(answer_matrix[i-1][j])
        elif i == j :
            answer_matrix[i][j] = int(value_matrix[i][j]) + int(answer_matrix[i-1][j-1])
        else :
            answer_matrix[i][j] = int(value_matrix[i][j]) + max(int(answer_matrix[i-1][j]),int(answer_matrix[i-1][j-1]))

print max(answer_matrix[length-1])

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))