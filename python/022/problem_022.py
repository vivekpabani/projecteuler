#!/usr/bin/env python
# coding=utf-8

"""
problem definition:

Using names.txt, a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?

"""

__author__ = 'vivek'

import string


def main():
    # dictionary with character values of uppercase alphabets.
    alpha_dict = dict((ch, ord(ch)-64) for ch in string.ascii_uppercase)

    with open("names.txt") as f:
        words = f.read()

    # replace the quotes and store into a list with coma separator and sort list.
    words = string.replace(words, '"', '')
    word_list = words.split(',')
    word_list.sort()

    # find value of each word, and add to the final total with count multiplication.
    file_total = 0
    count = 0
    for word in word_list:
        count += 1
        word_total = 0
        for letter in word:
            word_total += alpha_dict[letter]
        file_total += (count*word_total)

    print "File Total = ", file_total

if __name__ == '__main__':
    main()

