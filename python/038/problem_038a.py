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


for num1 in xrange(1,10):
    for num2 in xrange(num1,10):
        for number in three_d+four_d:
            products = []
            products.append(str(number*num1))
            products.append(str(number*num2))
            if checkPandigital(products):
                pandigital.append(int(''.join(str(i) for i in products)))

for num1 in xrange(1,10):
    for num2 in xrange(num1,10):
        for num3 in xrange(num2,10):
            for number in two_d+three_d:
                products = []
                products.append(str(number*num1))
                products.append(str(number*num2))
                products.append(str(number*num3))
                if checkPandigital(products):
                    pandigital.append(int(''.join(str(i) for i in products)))

for num1 in xrange(1,10):
    for num2 in xrange(num1,10):
        for num3 in xrange(num2,10):
            for num4 in xrange(num3,10):
                for number in two_d:
                    products = []
                    products.append(str(number*num1))
                    products.append(str(number*num2))
                    products.append(str(number*num3))
                    products.append(str(number*num4))
                    if checkPandigital(products):
                        pandigital.append(int(''.join(str(i) for i in products)))

for num1 in xrange(1,10):
    for num2 in xrange(num1,10):
        for num3 in xrange(num2,10):
            for num4 in xrange(num3,10):
                for num5 in xrange(num4,10):
                    for number in one_d:
                        products = []
                        products.append(str(number*num1))
                        products.append(str(number*num2))
                        products.append(str(number*num3))
                        products.append(str(number*num4))
                        products.append(str(number*num5))
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
                            for num8 in one_d:
                                num = str(num1)+str(num2)+str(num3)+str(num4)+str(num5)+str(num6)+str(num7)+str(num8)
                                if len(num) == len(''.join(set(num))):
                                    for number in one_d:
                                        products = []
                                        products.append(str(number*num1))
                                        products.append(str(number*num2))
                                        products.append(str(number*num3))
                                        products.append(str(number*num4))
                                        products.append(str(number*num5))
                                        products.append(str(number*num6))
                                        products.append(str(number*num7))
                                        products.append(str(number*num8))

                                        products.sort(reverse=True)
                                        if checkPandigital(products):
                                            pandigital.append(int(''.join(str(i) for i in products)))
"""

pandigital.sort(reverse=True)
print(pandigital)
print(len(pandigital))
print(max(pandigital))


print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
