# Given an array nums with n objects colored red, white, or blue, sort them in-place so that objects
# of the same color are adjacent, with the colors in the order red, white, and blue.
#
# We will use the integers 0, 1, and 2 to represent the color red, white, and blue, respectively.

def sort_colors(nums):
    right = len(nums) - 1
    pointer, left = 0, 0

    def swap(i, j):
        temp = nums[i]
        nums[i] = nums[j]
        nums[j] = temp

    while pointer <= right:
        if nums[pointer] == 0:
            swap(left, pointer)
            left += 1
        if nums[pointer] == 2:
            swap(right, pointer)
            right -= 1
            # cancels out line 23 - pointer shouldn't move
            pointer -= 1
        pointer += 1

    return nums
