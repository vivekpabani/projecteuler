__author__ = 'vivek'

import time

startTime = time.clock()

one_d = [str(i) for i in xrange(1,10)]
#print(one_d)
two_d = [str(i) for i in xrange(10,100)]
three_d = [str(i)  for i in xrange(100,1000)]
four_d = [str(i)  for i in xrange(1000,10000)]

pandigital = []


def checkPandigital(num1,num2,num3):

    constr = str(num1)+str(num2)+str(num3)
    if '0' not in constr and len(constr) == 9 and len(constr)==len(''.join(set(constr))):
        #print(num1,num2,num3)
        return 1
    else:
        return 0


for num1 in two_d:
    for num2 in three_d:
        if '0' not in num1 and '0' not in num2 and len(num2)==len(''.join(set(num2))) and len(num1)==len(''.join(set(num1))) and len(num1+num2)==len(''.join(set(num1+num2))):
            product = int(num1)*int(num2)
            if checkPandigital(num1,num2,product):
                pandigital.append(product)

for num1 in one_d:
    for num2 in four_d:
        if '0' not in num2 and len(num2)==len(''.join(set(num2))) and len(num1+num2)==len(''.join(set(num1+num2))):
            product = int(num1)*int(num2)
            if checkPandigital(num1,num2,product):
                pandigital.append(product)


pandigital = list(set(pandigital))

addition = 0
for number in pandigital:
    addition = addition + number


#print(pandigital)
print(addition)
"""
for num1 in one_d:
    for num2 in four_d:
        if len(num2)==len(''.join(set(num2))):
            print(num2)


for num2 in two_d:
    if len(num2)==len(''.join(set(num2))):
        print(num2)
"""
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
