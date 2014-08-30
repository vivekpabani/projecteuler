#!/usr/bin/env python

#Description :
#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
#Find the largest palindrome made from the product of two 3-digit numbers.

num = 998001
flag = 1

while num > 10000 and flag :
    x = 999
    if str(num) == str(num)[::-1] :
        while x > 99 and flag :
            if num%x == 0 and len(str(num/x)) == 3 :
                print "Num1 : ", x
                print "Num2 : ", num/x
                print "Palindrome : ", num 
                flag = 0
            x = x-1
    num = num-1
                                  