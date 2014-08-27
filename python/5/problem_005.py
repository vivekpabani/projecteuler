def find_lcm(num1, num2) :
    a = max(num1,num2)
    b = min(num1,num2)
    lcm = 1
    num = 1
    while num <= b :
        if ((a*num)%b) == 0 :
            return a*num 
        num = num+1

lcm = 1

for x in xrange(1,21) :
    lcm = find_lcm(lcm,x)

print lcm