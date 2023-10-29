#
# Complete the 'repeatedString' function below.
#
# Find and print the number of letter a's in the first  letters of the infinite string.
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeated_string(s, n):
    multiplier = n // len(s)
    remainder_s = s[:n % len(s)]

    print(multiplier)
    print(remainder_s)

    return s.count("a") * multiplier + remainder_s.count("a")

    # char_counter = 0
    # infinite_s = s * n
    #
    # if len(infinite_s) > n:
    #     overflow_n = len(infinite_s) - n
    #     infinite_s = infinite_s[:-overflow_n]
    #
    # for character in infinite_s:
    #     if character == 'a':
    #         char_counter += 1
    #
    # print(infinite_s)
    #
    # return char_counter


if __name__ == '__main__':
    # s = input()
    s = 'aba'

    # n = int(input().strip())
    n = 10

    result = repeated_string(s, n)

    print(result)
