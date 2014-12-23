__author__ = 'vivek'

####### IN PROGRESS ########

import time

startTime = time.clock()

one_d = [i for i in xrange(1,10)]
two_d = [i for i in xrange(10,100)]
three_d = [i for i in xrange(100,1000)]
four_d = [i for i in xrange(1000,10000)]
all_numbers = [one_d,two_d,three_d,four_d]

all_numbers = [one_d,two_d,three_d,four_d]
#print(all_numbers)
pandigital = []
answers = []

def checkPandigital(numbers):

    constr = ''.join(str(i) for i in numbers)
    if '0' not in constr and len(constr) == 9 and len(constr)==len(''.join(set(constr))):
        #print(numbers, constr)
        return 1
    else:
        return 0
"""
for number in four_d :
    answers = []
    answers.append(number*one_d[0])
    answers.append(number*one_d[1])
    if checkPandigital(answers):
        pandigital.append(''.join(str(i) for i in answers))

print(pandigital)
"""

ranges = {1:[[0,5],[0,6],[0,7],[0,8],[0,9]], 2:[[0,3],[0,4]], 3:[[0,3]], 4:[[0,2]]}

for range_i in ranges[1]:
    for number in range(range_i[0],range_i[1]):
        print(number),
    print('')

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
