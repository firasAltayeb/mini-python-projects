#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimum_bribes(q):
    total_bribes = 0
    expected_first = 1
    expected_second = 2
    expected_third = 3

    for i in range(len(q)):
        if q[i] == expected_first:
            expected_first = expected_second
            expected_second = expected_third
            expected_third += 1
        elif q[i] == expected_second:
            total_bribes += 1
            expected_second = expected_third
            expected_third += 1
        elif q[i] == expected_third:
            total_bribes += 2
            expected_third += 1
        else:
            return print('Too chaotic')

    print(total_bribes)


if __name__ == '__main__':
    # t = int(input().strip())
    t = 2

    for t_itr in range(t):
        # 2, 1, 5, 3, 4 is 3
        # 2, 5, 1, 3, 4 is Too chaotic
        q = list(map(int, input().rstrip().split()))

        minimum_bribes(q)
