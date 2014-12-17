__author__ = 'vivek'

import time

startTime = time.clock()
palindromes = []

for number in xrange(1,1000000):
    if str(number)==str(number)[::-1] and str(bin(number))[2:]== str(bin(number))[:1:-1]:
        palindromes.append(number)

#print(str(bin(585)))
#print str(bin(585))[2:]
#print str(bin(585))[:1:-1]

print(len(palindromes))
add = 0
for number in palindromes:
    #print(str(number),str(number)[::-1], str(bin(number))[2:], str(bin(number))[:1:-1])
    add = add + number
print(add)

print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
