

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in xrange(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in xrange(3,n,2) if sieve[i]]


def main():
    limit = 200000
    prime_l = primes(p_count)
    found = 0 
    current = 10
    streak = 0
    answer_l = list()

    while not found and current < limit:
        i = 0
        repeat = 0 
        count = 0
        temp = current
        # try till count of distinct prime factors is below 5
        # and number is > 1
        while count < 5 and temp != 1:
            if temp%prime_l[i] == 0:
                temp = temp/prime_l[i]
                # if same as last factor, then ignore from count.
                if not repeat:
                    count += 1
                    repeat = 1
            else:
                repeat = 0
                i += 1
        if count == 4 and temp == 1:
            if answer_l and current - answer_l[-1] == 1:
                streak += 1
            else:
                streak = 1
            answer_l.append(current)
        if streak == 4:
            print(answer_l[-4], answer_l[-3], answer_l[-2], answer_l[-1])
            found = 1 
        current += 1

if __name__ == "__main__":
    main()
