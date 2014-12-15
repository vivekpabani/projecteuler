__author__ = 'vivek'

import time

startTime = time.clock()

value_matrix = []
for line in open('matrix.txt') :

    separator = ','
    temp_list = []

    line = line.split(separator)

    for value in line :
        temp_list.append(int(value))
    value_matrix.append(temp_list)


length = len(value_matrix)

answer_matrix = [[0]*length for i in range(length)]

for i in xrange(0,length):
    for j in xrange(0,length):
        #print(answer_matrix)
        if i==0 and j==0:
            answer_matrix[i][j] = value_matrix[i][j]
        elif i==0 and j>0:
            answer_matrix[i][j] = value_matrix[0][j] + answer_matrix[0][j-1]
        elif i>0 and j==0:
            answer_matrix[i][j] = value_matrix[i][0] + answer_matrix[i-1][0]
        else:
            if answer_matrix[i-1][j]<answer_matrix[i][j-1]:
                answer_matrix[i][j] = value_matrix[i][j] + answer_matrix[i-1][j]
            else:
                answer_matrix[i][j] = value_matrix[i][j] + answer_matrix[i][j-1]

print answer_matrix[length-1][length-1]

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
