# Given an array of positive integers nums and a positive integer target, return the minimal length of a
# subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

from typing import List


def min_sub_array_len(target: int, nums: List[int]) -> int:
    l, total = 0, 0
    length = len(nums) + 1

    for r in range(len(nums)):
        total += nums[r]

        while total >= target:
            length = min(length, r - l + 1)
            total -= nums[l]
            l += 1

    return length if length < len(nums) + 1 else 0
