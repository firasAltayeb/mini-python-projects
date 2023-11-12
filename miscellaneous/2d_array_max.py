#
# Complete the 'hourglassSum' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def hourglass_sum(arr):
    hourglass_array = []
    for i in range(len(arr) - 2):
        for j in range(len(arr[i]) - 2):
            hourglass_array.append(arr[i][j] + arr[i][j + 1] + arr[i][j + 2]
                                   + arr[i + 1][j + 1]
                                   + arr[i + 2][j] + arr[i + 2][j + 1] + arr[i + 2][j + 2])
    return max(hourglass_array)


if __name__ == '__main__':
    arr = [
        [-9, -9, -9, 1, 1, 1],
        [0, -9, 0, 4, 3, 2],
        [-9, -9, -9, 1, 2, 3],
        [0, 0, 8, 6, 6, 0],
        [0, 0, 0, -2, 0, 0],
        [0, 0, 1, 2, 4, 0]
    ]

    result = hourglass_sum(arr)

    print(f'max_value is {result}')
