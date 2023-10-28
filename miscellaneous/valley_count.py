#
# Complete the 'countingValleys' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER steps
#  2. STRING path
#

def counting_valleys(steps, path):
    # descending = False
    valley_count = 0
    sea_level = 0

    for step in path:
        if step == 'U':
            sea_level += 1
            if sea_level == 0:
                valley_count += 1
        else:
            sea_level -= 1
    return valley_count


if __name__ == '__main__':
    # steps = int(input().strip())
    steps = 8

    # path = input()
    path = 'UDDDUDUU'

    result = counting_valleys(steps, path)

    # Expected Output 1
    print(result)
