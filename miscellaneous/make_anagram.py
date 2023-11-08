#
# Complete the 'makeAnagram' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING a
#  2. STRING b
#

def make_anagram(a, b):
    dict_chars = dict()

    for char in a:
        if char in dict_chars:
            dict_chars[char] += 1
        else:
            dict_chars[char] = 1
    for char in b:
        if char in dict_chars:
            dict_chars[char] -= 1
        else:
            dict_chars[char] = -1

    deletion_counter = 0

    for char in dict_chars.keys():
        # print(dict_chars[char])
        # print(abs(dict_chars[char]))
        deletion_counter += abs(dict_chars[char])

    return deletion_counter


if __name__ == '__main__':
    # a = input()
    a = 'fcrxzwscanmligyxyvym'

    # b = input()
    b = 'jxwtrhvujlmrpdoqbisbwhmgpmeoke'

    result = make_anagram(a, b)

    # Expected Output 4
    print(str(result) + '\n')
