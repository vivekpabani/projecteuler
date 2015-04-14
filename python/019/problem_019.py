#!/usr/bin/env python

"""
Problem Definition :

You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?'''

 This program finds the number of days when given particular day of a week falls on 1st date of month for the range of given years.
 first argument - start_year, second argument - end_year , third argument - day (Monday - 1, Sunday - 7)

"""

import sys


def find_leap(year_input):
    """function to find if given year is leap year or not."""
    if year_input % 400 == 0:
        return 1
    elif year_input % 100 == 0:
        return 0
    elif year_input % 4 == 0:
        return 1
    else:
        return 0


def count_days(year_input):
    """function to find the days between year 1900 and given year"""
    total_days = 0
    for years in range(1900, year_input):
        if find_leap(years):
            total_days += 366
        else:
            total_days += 365
    return total_days


def main():

    normal_year = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days of months for a non leap year
    leap_year = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]  # days of months for a leap year
    days, day_first = 0, 0
    start_year = int(sys.argv[1])
    end_year = int(sys.argv[2])
    day = int(sys.argv[3])
    flag = 1

    if start_year < 1900 or end_year < 1900 or start_year > 9999 or end_year > 9999 or day < 1 or day > 7:
        print "Please provide valid values."
        flag = 0

    if flag:
        days = count_days(start_year)

        for year in range(start_year, end_year + 1):
            if find_leap(year):
                count_year = leap_year
            else:
                count_year = normal_year

            for months in xrange(12):
                if days % 7 == (day - 1):
                    day_first += 1
                days += count_year[months]

        print day_first

if __name__ == '__main__':
    main()
