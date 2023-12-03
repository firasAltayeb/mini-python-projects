#
# Given two strings s and t, return true if t is an anagram of s, and false otherwise.
#
# An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase,
# typically using all the original letters exactly once.
#

def is_anagram(s, t):
    if len(s) != len(t):
        return False

    count_s, count_t = {}, {}

    for e in s:
        count_s[e] = 1 + count_s.get(e, 0)
        count_t[e] = 1 + count_t.get(e, 0)

    return count_s == count_t


def is_anagram_two(s, t):
    if len(s) != len(t):
        return False

    store = [0] * 26

    for i in range(len(s)):
        store[ord(s[i]) - ord('a')] += 1
        store[ord(t[i]) - ord('a')] -= 1

    for n in store:
        if n != 0:
            return False

    return True


if __name__ == '__main__':
    # a = input()
    a = 'anagram'

    # b = input()
    b = 'nagaram'

    result = is_anagram(a, b)

    print(str(result) + '\n')
