# Given an array of integers arr and two integers k and threshold, return the
# number of sub-arrays of size k and average greater than or equal to threshold.
from typing import List


def num_of_subarrays(arr: List[int], k: int, threshold: int) -> int:
    res = 0
    cur_sum = sum(arr[:k - 1])

    for L in range(len(arr) - k + 1):
        cur_sum += arr[L + k - 1]
        if (cur_sum / k) >= threshold:
            res += 1
        cur_sum -= arr[L]
    return res


print(num_of_subarrays([2, 2, 2, 2, 5, 5, 5, 8], 3, 4))
