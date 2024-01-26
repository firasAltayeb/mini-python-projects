# Design a class to find the kth largest element in a stream. Note that it is the kth
# largest element in the sorted order, not the kth distinct element.
#
# The constractor initializes the object with the integer k and the stream of integers nums.
# The add functions appends the val to the stream and returns the element representing the kth largest element

import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap)
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val):
        heapq.heappush(self.minHeap, val)
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        # the default heap implementation stores min in first idx
        return self.minHeap[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
