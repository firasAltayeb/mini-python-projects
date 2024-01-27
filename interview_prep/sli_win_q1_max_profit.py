# You are given an array prices where prices[i] is the price of a given stock on the ith day.
#
# You want to maximize your profit by choosing a single day to buy one stock and choosing a
# different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction else 0.

from typing import List


def max_profit(self, prices: List[int]) -> int:
    res = 0

    lowest = prices[0]
    for price in prices:
        if price < lowest:
            lowest = price
        res = max(res, price - lowest)

    # l = 0
    # for r in range(1, len(prices)):
    #     if prices[l] < prices[r]:
    #         profit = prices[r] - prices[l]
    #         res = max(res, profit)
    #     else:
    #         l = r

    return res
