#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time

startTime = time.clock()

special_cards = ['T','J','Q','K','A']
special_cards_translate = {'T':'10','J':'11', 'Q':'12', 'K':'13', 'A':'14'}


def divide_cards(data) :
    cards = data.split(' ')
    p1 = {}
    p2 = {}

    for i in xrange(0,5):
        p1[cards[i][:-1]] = cards[i][-1:]
    #print(p1)


with open("poker.txt") as f:
    data = f.read()
for ch in special_cards:
    data = data.replace(ch,special_cards_translate[ch])

numbers = data.split('\n')

for number in numbers:
    #print(number)
    if(number):
        divide_cards(number)
#print(numbers)
print "Run time...{} secs \n".format(round(time.clock() - startTime, 5))
