import random


#
# Given an array of integer nums and an integer target,
# return indices of two numbers such that they add up
# to target
#

def find_complement_slow(nums, t):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == t:
                print(f"{i} + {j}")
                break


def find_complement(nums, t):
    comp_map = {}
    for i in range(len(nums)):
        print(f"map is {comp_map}")
        complement = t - nums[i]
        print(f"complement is {complement}")
        if complement in comp_map:
            print(f"The indices are {comp_map[complement]} + {i}")
            break
        comp_map[nums[i]] = i


if __name__ == '__main__':
    arr = [random.randint(0, 9) for _ in range(5)]
    target = 8

    find_complement(arr, target)