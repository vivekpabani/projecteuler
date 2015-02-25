#!/usr/bin/env python


"""
Problem Definition :


"""

__author__ = 'vivek'

import time
import string


def main():

    start_time = time.clock()

    triangle_numbers = [n*(n+1)/2 for n in xrange(1, 30)]

    alpha_dict = dict((ch, ord(ch)-64) for ch in string.ascii_uppercase)

    word_file = open("words.txt","r+")

    data = word_file.read().replace('"', '')

    word_file.close()

    words = data.split(",")

    count = 0
    for word in words:
        word_total = 0
        for letter in word:
            word_total += alpha_dict[letter]
        if word_total in triangle_numbers:
            count += 1

    print(count)

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))


if __name__ == '__main__':
    main()
