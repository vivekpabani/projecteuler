#!/usr/bin/env python

import math

# Problem Definition :
'''A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:
    
    012   021   102   120   201   210
    
    What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?.'''


numbers =  range(0,3)
final = 0
answer = []
final_number = ''


while (final != 4) :
    i = 0
    length_numbers = len(numbers)
    print 'i before', i
    print "length ", length_numbers
    while(final < 4 and i < length_numbers):
        final = final + math.factorial(length_numbers-1)
        i = i+1
        print 'i after', i
        print 'answer before ', final
    
    
    if final != 4 :
        if final > 4 :
            final = final - math.factorial(length_numbers-1)
        else :    
            pass
        
        print 'answer before ', final
        print 'i later', i
        answer.append(numbers[i])
        print answer
        numbers.remove(numbers[i])
for item in numbers:
    answer.append(item)
for item in answer:
    final_number = final_number + str(item)
print final_number

    #for i in xrange(0,10):
#print i, math.factorial(i)

'''for i in xrange(0.len(answer)):
    print i, i*math.factorial('''