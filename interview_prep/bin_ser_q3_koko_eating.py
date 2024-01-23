# Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas.
# The guards have gone and will come back in h hours.
# Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.
# Return the minimum integer k such that all the bananas can be eaten within h hours.
import math


def min_eating_speed(piles, h):
    l, r = 1, max(piles)
    res = r

    while l <= r:
        k = (l + r) // 2

        total_time = 0
        for p in piles:
            total_time += math.ceil(float(p) / k)
        if total_time <= h:
            res = min(res, k)
            r = k - 1
        else:
            l = k + 1

    return res


banana_piles = [3, 6, 7, 11]
h = 8

print(min_eating_speed(banana_piles, h))
