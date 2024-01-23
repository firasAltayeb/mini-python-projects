# Given an array of integers nums, sort the array in ascending order and return it.
#
# You must solve the problem without using any built-in functions in O(nlog(n))
# time complexity and with the smallest space complexity possible.

def sort_array(nums):
    def merge(arr, s, m, e):
        left, right = arr[s:m + 1], arr[m + 1:e + 1]
        i, l, r = s, 0, 0

        while l < len(left) and r < len(right):
            if left[l] < right[r]:
                arr[i] = left[l]
                l += 1
                i += 1
            else:
                arr[i] = right[r]
                r += 1
                i += 1

        while l < len(left):
            arr[i] = left[l]
            l += 1
            i += 1
        while r < len(right):
            arr[i] = right[r]
            r += 1
            i += 1

    def merge_helper(arr, s, e):
        if s == e:
            return arr

        m = (s + e) // 2
        merge_helper(arr, s, m)
        merge_helper(arr, m + 1, e)
        merge(arr, s, m, e)

        return arr

    return merge_helper(nums, 0, len(nums) - 1)
