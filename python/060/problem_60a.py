#!/usr/bin/env python


"""
Problem Definition :

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

"""

__author__ = 'vivek'

import time
import math

startTime = time.clock()

p2 = []
#p3 = []
p4 = []
p5 = []

def is_prime(number):
    if number < 0:
        return 0
    elif number == 2 or number == 3:
        return 1
    elif number % 2 == 0 or number % 3 == 0 or number == 1:
        return 0
    else:
        start = 5
        while start <= int(math.sqrt(number)):
            if number % start == 0:
                return 0
                break
            if number % (start+2) == 0:
                return 0
                break
            start += 6
        return 1


prime_numbers = [x for x in xrange(1,1300) if is_prime(x)]
length = len(prime_numbers)
for i in xrange(0,length):
    num1 = prime_numbers[i]
    for j in xrange(i+1,length):
        num2 = prime_numbers[j]
        if is_prime(int(str(num1)+str(num2))) and is_prime(int(str(num2)+str(num1))):

            p2.append((num1,num2))

#print(len(p21))

#p2 = list(sorted(s) for s in p21)
#p22 = []
#for item in p21:
#    if item not in p22:
#        p22.append(item)

length = len(p2)
print(length)
for i in xrange(0,length):
    pair21 = p2[i]
    for j in xrange(i+1,length):
        pair22 = p2[j]
        flag = 0
        for num1 in pair21:
            for num2 in pair22:

                if is_prime(int(str(num1)+str(num2))) and is_prime(int(str(num2)+str(num1))):
                    flag += 1
        if flag == 4:
            p4.append((pair21[0],pair21[1],pair22[0],pair22[1]))
"""
for item in p4:
    item = sorted(item)
print(p4)
"""
#answers = list(tuple(list(sorted(s))) for s in p4)

p4 = list(sorted(s) for s in p4)
answers = []
for item in p4:
    if item not in answers:
        answers.append(item)


print(answers)

"""
for num1 in prime_numbers:
    for pair3 in p3:
        flag = 0
        for num2 in pair3:
            if is_prime(int(str(num1)+str(num2))) and is_prime(int(str(num2)+str(num1))):
                if num1!= num2:
                    flag += 1
        if flag == 3:
            p4.append((num1,pair3[0],pair3[1],pair3[2]))

for num1 in prime_numbers:
    for pair4 in p4:
        flag = 0
        for num2 in pair4:
            if is_prime(int(str(num1)+str(num2))) and is_prime(int(str(num2)+str(num1))):
                if num1!= num2:
                    flag += 1
        if flag == 4:
            p5.append((num1,pair4[0],pair4[1],pair4[2],pair4[3]))
"""

#print(p4)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
