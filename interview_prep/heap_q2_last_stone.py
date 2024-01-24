# Choose the heaviest two stones int x, y with x <= y and smash them together
# the result of this smash is: both stones are destroyed if equal or the stone
# of weight x is destroyed, and the stone of weight y has new weight y - x.
#
# Return the weight of the last remaining stone. If there are no stones left, return 0.

import heapq
from typing import List


def last_stone_weight(self, stones: List[int]) -> int:
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        first = heapq.heappop(stones)
        second = heapq.heappop(stones)
        if second > first:
            heapq.heappush(stones, first - second)

    stones.append(0)
    return abs(stones[0])
