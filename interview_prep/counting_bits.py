# Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
# ans[i] is the number of 1's in the binary representation of i.

from typing import List


# O(n)
def count_bits(self, n: int) -> List[int]:
    dp = [0] * (n + 1)
    offset = 1

    for i in range(1, n + 1):
        if offset * 2 == i:
            offset = i
        dp[i] = 1 + dp[i - offset]
    return dp


# O(n log n)
def count_bits_slow(self, n: int) -> List[int]:
    ans = []

    def count_ones(m):
        count = 0
        while m > 0:
            if m & 1 == 1:
                count += 1
            m = m >> 1
        return count

    for i in range(n + 1):
        ans.append(count_ones(i))

    return ans
