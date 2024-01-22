# Given a circular integer array nums of length n, return the maximum possible sum
# of a non-empty subarray of nums. A circular array means the end of the array
# connects to the beginning of the array.
#
# A subarray may only include each element of the fixed buffer nums at most once.

def max_subarray_sum_circular(nums):
    gmax, gmin = nums[0], nums[0]
    cmax, cmin = 0, 0
    total = 0

    for n in nums:
        cmax = max(cmax + n, n)
        cmin = min(cmin + n, n)
        total += n
        gmax = max(cmax, gmax)
        gmin = min(cmin, gmin)

    return max(gmax, total - gmin) if gmax > 0 else gmax
