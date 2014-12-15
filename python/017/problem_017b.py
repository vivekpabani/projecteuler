#!/usr/bin/env python


#description
#If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.
#If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?
#NOTE: Do not count spaces or hyphens. For example, 342 (three hundred and forty-two) contains 23 letters and 115 (one hundred and fifteen) contains 20 letters. The use of "and" when writing out numbers is in compliance with British usage.

ones = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine']
double = ['Ten','Eleven','Twelve','Thirteen','Fourteen','Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
tens = ['','','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
hundreds = ['','','','Hundred','Thousand']

#number = 235
#print number[1]
words = 0
        
for num in xrange(1,1001) :
    str_num = str(num)
    
    if len(str_num) == 1 :
        word = ones[num]
    elif len(str_num) == 2 :
        if(str_num[0] == '1'):
            word = double[int(str_num[1])]
        else :
            word = tens[int(str_num[0])]+ones[int(str_num[1])]
    elif len(str_num) == 3 :
        if(str_num[1] == '1'):
            word = ones[int(str_num[0])]+hundreds[3]+'And'+double[int(str_num[2])]
        else :
            word = ones[int(str_num[0])]+hundreds[3]+'And'+tens[int(str_num[1])]+ones[int(str_num[2])]
    else :
        word = 'OneThousand'
    print word
    words = words + len(word)
print words