__author__ = 'vivek'


import time


def check_pandigital(number_s):

    if '0' not in number_s and len(number_s) == 9 and len(number_s) == len(''.join(set(number_s))):
        return 1
    else:
        return 0


def main():
    start_time = time.clock()

    one_d = [i for i in xrange(1, 10)]
    two_d = [i for i in xrange(10, 100)]
    three_d = [i for i in xrange(100, 1000)]
    four_d = [i for i in xrange(1000, 10000)]

    all_numbers = {1: one_d, 2: two_d, 3: three_d, 4: four_d}
    ranges = {1: [[0, 5], [0, 6], [0, 7], [0, 8], [0, 9]], 2: [[0, 3], [0, 4]], 3: [[0, 3]], 4: [[0, 2]]}

    pandigital = []

    for i in xrange(1, 5):
        for number in all_numbers[i]:
            for range_value in ranges[i]:
                answer_l = []
                for multiplier in xrange(range_value[0], range_value[1]):
                    answer_l.append(str(number*one_d[multiplier]))
                answer_str = ''.join(j for j in answer_l)
                if check_pandigital(answer_str):
                    pandigital.append(answer_str)

    print(max(pandigital))

    print "Run time...{} secs \n".format(round(time.clock() - start_time, 4))

if __name__ == '__main__':
    main()