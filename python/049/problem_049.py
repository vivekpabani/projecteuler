import itertools

def primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3, int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)/(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]


def perm(num):

    digits = [int(x) for x in str(num)]
    n_digits = len(digits)
    n_power = n_digits - 1
    permutations = itertools.permutations(digits)
    l = [sum(v * (10**(n_power - i)) for i, v in enumerate(item)) for item in permutations]
    return sorted(list(set(l)))

def main():
    limit = 10000
    prime_list = primes(limit)
    pl = [x for x in prime_list if x > 1000]
    used = list()
    found = 0
    for item in pl:
        if item in used:
            continue
        temp = list()
        perm_l = perm(item)
        for i in perm_l:
            if i in pl:
                temp.append(i)
        used.extend(temp)
        if len(temp) >= 3:
            all_c = list(itertools.combinations(temp,3))
            for k in all_c:
                if k[1] - k[0] == k[2] - k[1]:
                    print(k)


if __name__ == "__main__":
    main()
