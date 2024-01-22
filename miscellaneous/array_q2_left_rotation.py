#
# Complete the 'rotLeft' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER d
#

def rot_left(a, d):
    d = d % len(a)  # effective number of rotations
    new_array = a[d:] + a[:d]
    # new_array = a
    # for i in range(d):
    #     new_array.append(new_array[0])
    #     new_array = new_array[1::]
    return new_array


if __name__ == '__main__':
    # first_multiple_input = input().rstrip().split()
    # d = int(first_multiple_input[1])
    d = 6

    # a = list(map(int, input().rstrip().split()))
    a = [1, 2, 3, 4, 5]

    result = rot_left(a, d)

    print(f'result is {result}')
