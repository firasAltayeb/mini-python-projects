# Given an integer array nums and an integer k, return the kth largest element in the array.
#
# Note that it is the kth largest element in the sorted order, not the kth distinct element.
#
# Can you solve it without sorting?

from typing import List


def find_kth_largest(self, nums: List[int], k: int) -> int:
    k = len(nums) - k

    def quick_select(s, e):
        pivot, p = nums[e], s
        for i in range(s, e):
            if nums[i] <= pivot:
                nums[p], nums[i] = nums[i], nums[p]
                p += 1
        nums[p], nums[e] = nums[e], nums[p]

        if p > k:
            return quick_select(s, p - 1)
        elif p < k:
            return quick_select(p + 1, e)
        else:
            return nums[p]

    return quick_select(0, len(nums) - 1)
