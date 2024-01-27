# Given an integer array nums and an integer k, return true if there
# are two distinct indices i and j in the array such that
# nums[i] == nums[j] and abs(i - j) <= k.


def contains_nearby_duplicate(nums, k):
    window = set()
    l = 0

    for r in range(len(nums)):
        if r - l > k:
            window.remove(nums[l])
            l += 1
        if nums[r] in window:
            return True
        window.add(nums[r])

    # dic = {}
    # for i, n in enumerate(nums):
    #     if n in dic.keys() and abs(i - dic[n]) <= k:
    #         return True
    #     dic[n] = i

    return False
