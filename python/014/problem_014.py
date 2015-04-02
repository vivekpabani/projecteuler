#!/usr/bin/env python


"""
Problem Definition :

The following iterative sequence is defined for the set of positive integers:

n = n/2 (n is even)
n = 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 - 40 - 20 - 10 - 5 - 16 - 8 - 4 - 2 - 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.'''

"""


numbers = [0]*10000000
numbers[1] = 1
final = 0
length = len(numbers)

for i in xrange(1,1000001) :

    if numbers[i] == 0 :                    #Only check for unseen numbers (list value  = 0)
        final = i
        dict = {}

        while (final > 1) :
            if final<length :               #To check if the value of final is less than the length of list - numbers - to avoid array index out of range error. If so, treat is as a never seen number in the else logic.
                if numbers[final] == 0 :    #To confirm that the current final value was never seen before during any calculation ( 0 is by default value assigned to every list membeSrs)
                    dict[final] = 1         #Add the new number to the temp dictionary and assign value = 1 ( i.e. default length = 1 for any single number seen during calculation)

                    if final % 2 == 0 :
                        final = final/2
                    else :
                        final = 3*final + 1

                    if final < length :     #To check if the new value of final is less than the length of list - numbers - to avoid array index out of range error.

                        if numbers[final] == 0 :        #Never seen logic : if the final value is new, increase values of each current member of dictionary by 1. and this number will be added to the dictionary in the next iteration of while loop.
                            for key in dict :
                                dict[key] = int(dict[key]) + 1
                        else :                          #Old value logic : if the final value is available in the list, add its corresponding value to each current member of dictionary.
                            for key in dict :
                                dict[key] = int(dict[key]) + int(numbers[final])
                    else :
                        for key in dict :
                            dict[key] = int(dict[key]) + 1

                else :
                    final = 1
            else :
                dict[final] = 1
                if final % 2 == 0 :
                    final = final/2
                else :
                    final = 3*final + 1

                for key in dict :                   #Never seen logic.
                    dict[key] = int(dict[key]) + 1

        for key in dict :
            if key < length :
                numbers[key] = dict[key]

print numbers.index(max(numbers))