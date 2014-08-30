# This program finds the number of days when given particular day of a week falls on 1st date of month for the range of given years.
# first argument - start_year, second argument - end_year , third argument - day (Monday - 1, Sunday - 7)
import sys

normal_year = [31,28,31,30,31,30,31,31,30,31,30,31] # days of months for a non leap year
leap_year =   [31,29,31,30,31,30,31,31,30,31,30,31] # days of months for a leap year
count_year=   [] 

days, day_first = 0,0

# function to find if given year is leap year or not.

def find_leap(year_input) :
    if year_input%400 == 0 :
        return 1
    elif year_input%100 == 0 :
        return 0
    elif year_input%4 == 0 :
        return 1
    else :
        return 0
# function to find the days between year 1900 and given year

def count_days(year_input) :
    total_days = 0
    for years in range(1900,year_input) :
        if find_leap(years) :
            total_days = total_days + 366
        else :
            total_days = total_days + 365
    return total_days

ystart = int(sys.argv[1])
yend = int(sys.argv[2])
day = int(sys.argv[3])
flag = 1


if ystart < 1900 or yend < 1900 or ystart > 9999 or yend > 9999 or day < 1 or day > 7 :
    print "Please provide valid values."
    flag = 0;

if flag :
    days = count_days(ystart)
    
    for year in range(ystart,yend+1):
        if find_leap(year) :
            count_year = leap_year
        else :
            count_year = normal_year
    
        for months in range(0,12) :
            if days%7 == (day-1):
                day_first = day_first + 1
            days = days + count_year[months]
        
    print day_first