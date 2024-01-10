#
# Complete the 'isValid' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#
from collections import Counter


def is_valid_old(s):
    freq = [s.count(letter) for letter in set(s)]
    if max(freq) - min(freq) == 0:
        return 'YES'
    elif freq.count(max(freq)) == 1 and max(freq) - min(freq) == 1:
        return 'YES'
    elif freq.count(min(freq)) == 1:
        freq.remove(min(freq))
        if max(freq) - min(freq) == 0:
            return 'YES'
        else:
            return 'NO'
    else:
        return 'NO'


def is_valid(s):
    c = Counter(s)
    print(c)
    freq = Counter(c.values())
    print(freq)
    if len(freq) == 1:
        return "YES"
    elif len(freq) == 2:
        key_max = max(freq.keys())
        key_min = min(freq.keys())
        if key_max - key_min == 1 and freq[key_max] == 1:
            return "YES"
        elif key_min == 1 and freq[key_min] == 1:
            return "YES"
    return "NO"


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    # s = input()
    # s = 'AAABBBCC'
    s = 'abcdefghhgfedecba'

    result = is_valid(s)

    # Expected Output YES
    print(result)
