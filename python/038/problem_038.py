__author__ = 'vivek'

####### IN PROGRESS ########

import time

startTime = time.clock()

one_d = [i for i in xrange(1,10)]
#print(one_d)
two_d = [i for i in xrange(10,100)]
three_d = [i for i in xrange(100,1000)]
four_d = [i for i in xrange(1000,10000)]

pandigital = []


def checkPandigital(numbers):

    constr = ''.join(str(i) for i in numbers)
    if '0' not in constr and len(constr) == 9 and len(constr)==len(''.join(set(constr))):
        print(numbers, constr)
        return 1
    else:
        return 0


for num1 in one_d:
    for num2 in one_d:
        if num1 != num2:
            for number in three_d+four_d:
                products = []
                products.append((number*num1))
                products.append((number*num2))
                #products.sort(reverse=True)
                if checkPandigital(products):
                    pandigital.append(int(''.join(str(i) for i in products)))

for num1 in one_d:
    for num2 in one_d:
            for num3 in one_d:
                num = str(num1)+str(num2)+str(num3)
                if len(num) == len(''.join(set(num))):

                    for number in two_d+three_d:
                        products = []
                        products.append((number*num1))
                        products.append((number*num2))
                        products.append((number*num3))
                        #products.sort(reverse=True)
                        if checkPandigital(products):
                            pandigital.append(int(''.join(str(i) for i in products)))

for num1 in one_d:
    for num2 in one_d:
            for num3 in one_d:
                for num4 in one_d:
                    num = str(num1)+str(num2)+str(num3)+str(num4)
                    if len(num) == len(''.join(set(num))):

                        for number in two_d:
                            products = []
                            products.append((number*num1))
                            products.append((number*num2))
                            products.append((number*num3))
                            products.append((number*num4))
                            #products.sort(reverse=True)
                            if checkPandigital(products):
                                pandigital.append(int(''.join(str(i) for i in products)))

for num1 in one_d:
    for num2 in one_d:
            for num3 in one_d:
                for num4 in one_d:
                    for num5 in one_d:
                        num = str(num1)+str(num2)+str(num3)+str(num4)+str(num5)
                        if len(num) == len(''.join(set(num))):

                            for number in one_d:
                                products = []
                                products.append((number*num1))
                                products.append((number*num2))
                                products.append((number*num3))
                                products.append((number*num4))
                                products.append((number*num5))
                                #products.sort(reverse=True)
                                if checkPandigital(products):
                                    pandigital.append(int(''.join(str(i) for i in products)))

"""

for num1 in one_d:
    for num2 in one_d:
        for num3 in one_d:
            for num4 in one_d:
                for num5 in one_d:
                    for num6 in one_d:
                        for num7 in one_d:
                            num = str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)+str(num7)
                            if len(num) == len(''.join(set(num))):
                                for number in one_d:
                                    products = []
                                    products.append((number*num1))
                                    products.append((number*num2))
                                    products.append((number*num3))
                                    products.append((number*num4))
                                    products.append((number*num5))
                                    products.append((number*num6))
                                    products.append((number*num7))
                                    products.sort(reverse=True)
                                    if checkPandigital(products):
                                        pandigital.append(int(''.join(str(i) for i in products)))

"""
print(pandigital)
print(len(pandigital))
print(max(pandigital))


print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
