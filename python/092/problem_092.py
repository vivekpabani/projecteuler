__author__ = 'vivek'

import time

startTime = time.clock()

sum_square_o = [1]
sum_square_e = [89]
number_status = [0]*10000001

def sum_square_base(number):
    global sum_square_o
    global sum_square_e
    addition = number
    square_sum_numbers = []

    while 1:
        if addition in sum_square_o:
            for item in square_sum_numbers:
                sum_square_o.append(item)
                number_status[item] = 0
            return 0
            break
        elif addition in sum_square_e:
            for item in square_sum_numbers:
                sum_square_e.append(item)
                number_status[item] = 1
            return 1
            break
        else:
            square_sum_numbers.append(addition)
            #print(square_sum_numbers)
            digits = []
            while addition > 0:
                digits.append(addition%10)
                addition = addition/10

            for digit in digits:
                addition = addition + (digit*digit)

            if addition == 1:
                for item in square_sum_numbers:
                    sum_square_o.append(item)
                    number_status[item] = 0
                return 0
                break
            elif addition == 89:
                for item in square_sum_numbers:
                    sum_square_e.append(item)
                    number_status[item] = 1
                return 1
                break
            #print("lists:", sum_square_o, sum_square_e)

def sum_square(number):
    global sum_square_o
    global sum_square_e
    addition = number

    digits = []
    while addition > 0:
        digits.append(addition%10)
        addition = addition/10

    for digit in digits:
        addition = addition + (digit*digit)

    if addition in sum_square_o:
        number_status[number] = 0
        return 1
    elif addition in sum_square_e:
        number_status[number] = 1
        return 1
    else:
        return 0

for x in xrange(1,568):
    sum_square_base(x)

for x in xrange(568,10000000):
    if(not sum_square(x)):
        print(x, ': 0')

print(number_status.count(1)+1)
#print("lists:", sum_square_o, sum_square_e)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))