__author__ = 'vivek'

import time

startTime = time.clock()

sum_square_o = [1]
sum_square_e = [89]


def sum_square(number):
    global sum_square_o
    global sum_square_e
    addition = number
    square_sum_numbers = []

    while 1:
        if addition in sum_square_o:
            for item in square_sum_numbers:
                sum_square_o.append(item)
            return 0
            break
        elif addition in sum_square_e:
            for item in square_sum_numbers:
                sum_square_e.append(item)
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
                return 0
                break
            elif addition == 89:
                for item in square_sum_numbers:
                    sum_square_e.append(item)
                return 1
                break
            #print("lists:", sum_square_o, sum_square_e)

#for x in xrange(1,10000000):
#print x, ' : ', sum_square(x)
print sum_square(9999999)

#print("lists:", sum_square_o, sum_square_e)

sum_square_e.sort()

index_found = 0
find_number = 9999999
while not index_found:
    if find_number in sum_square_e:
        print(sum_square_e)
        print(find_number)
        print(sum_square_e.index(find_number))
        index_found = 1
    find_number+=1
#print(sum_one)

#print(sum_enine)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
