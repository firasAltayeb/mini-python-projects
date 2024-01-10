#
# Change the array nums such that the first k elements of nums contain the unique elements
# in the order they were present in nums initially. The remaining elements of
# nums are not important as well as the size of nums.
#

def remove_duplicates(nums):
    l = 1

    for r in range(1, len(nums)):
        if nums[r] != nums[r - 1]:
            nums[l] = nums[r]
            l += 1

    return l


if __name__ == '__main__':
    arr = [1, 1, 2]

    result = remove_duplicates(arr)

    print(str(result))
