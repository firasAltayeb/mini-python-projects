#
# Complete the 'jumpingOnClouds' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY c as parameter.
#

def jumping_on_clouds(c_array):
    if len(c_array) == 1: return 0
    if len(c_array) == 2: return 0 if c_array[1] == 1 else 1
    if c_array[2] == 1:
        return 1 + jumping_on_clouds(c_array[1:])
    if c_array[2] == 0:
        return 1 + jumping_on_clouds(c_array[2:])

    # current_idx = 0
    # for i in range(len(c_array)):
    #     if current_idx == len(c_array) - 1:
    #         return i
    #     if current_idx + 2 < len(c_array) and c_array[current_idx + 2] == 0:
    #         current_idx += 2
    #     elif current_idx + 1 < len(c_array) and c_array[current_idx + 1] == 0:
    #         current_idx += 1
    #     else:
    #         return 0


if __name__ == '__main__':
    # c = list(map(int, input().rstrip().split()))
    c = [0, 0, 1, 0, 0, 1, 0]

    result = jumping_on_clouds(c)

    print(result)
