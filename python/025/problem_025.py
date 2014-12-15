#!/usr/bin/env python
__author__ = 'vivek'

import time

""" Problem Definition :
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?"""

startTime = time.clock()

def fib(a,b,n):
    a,b = b, a+b;
    n = n+1
    return a,b,n

num1 = 1
num2 = 1
count = 1

while(len(str(num1))!=1000):
    num1,num2,count = fib(num1,num2,count)

print(count)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 4))
