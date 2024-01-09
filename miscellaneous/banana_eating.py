import math


# Return the minimum integer k such that all the bananas can be eaten within h hours.

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
