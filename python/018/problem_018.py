#!/usr/bin/env python


"""
Problem Definition :

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.That is, 3 + 7 + 4 + 9 = 23.
Find the maximum total from top to bottom of the triangle below:

"""


value_matrix = [[75],
                [95,64],
                [17,47,82],
                [18,35,87,10],
                [20,4,82,47,65],
                [19,1,23,75,3,34],
                [88,2,77,73,7,63,67],
                [99,65,4,28,6,16,70,92],
                [41,41,26,56,83,40,80,70,33],
                [41,48,72,33,47,32,37,16,94,29],
                [53,71,44,65,25,43,91,52,97,51,14],
                [70,11,33,28,77,73,17,78,39,68,17,57],
                [91,71,52,38,17,14,91,43,58,50,27,29,48],
                [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
                [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]]

length = len(value_matrix)
answer_matrix = []

for i in xrange(0,length) :
    temp_list = []
    for j in xrange(0,i+1) :
        temp_list.append(0)
    answer_matrix.append(temp_list)        

answer_matrix[0][0] = 75

for i in xrange(1,length) :
    for j in xrange(0,i+1) :

        if j == 0 :
            answer_matrix[i][j] = value_matrix[i][j] + answer_matrix[i-1][j]
        elif i == j :
            answer_matrix[i][j] = value_matrix[i][j] + answer_matrix[i-1][j-1]
        else :
            answer_matrix[i][j] = value_matrix[i][j] + max(answer_matrix[i-1][j],answer_matrix[i-1][j-1])

print max(answer_matrix[length-1])
