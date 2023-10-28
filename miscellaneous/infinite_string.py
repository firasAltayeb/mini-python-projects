#
# Complete the 'repeatedString' function below.
#
# Find and print the number of letter a's in the first  letters of the infinite string.
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. STRING s
#  2. LONG_INTEGER n
#

def repeatedString(s, n):
    infinite_s = ''
    char_counter = 0
    num_of_a_in_s = 0

    while len(infinite_s) < n:
        s_to_add = ''
        if len(infinite_s + s) > n:
            overflow_n = len(infinite_s + s) - n
            s_to_add = s[:-overflow_n]
            infinite_s += s_to_add
            for character in s_to_add:
                if character == 'a':
                    char_counter += 1
        else:
            infinite_s += s
            if num_of_a_in_s == 0:
                for character in s:
                    if character == 'a':
                        num_of_a_in_s += 1
            char_counter += num_of_a_in_s

    return char_counter


if __name__ == '__main__':
    # s = input()
    s = 'aba'

    # n = int(input().strip())
    n = 10

    result = repeatedString(s, n)

    print(result)
