# Definition for a pair.
from typing import List


class Pair:
    def __init__(self, key: int, value: str):
        self.key = key
        self.value = value


# Implementation of Insertion Sort
def insertion_sort(self, pairs: List[Pair]) -> List[List[Pair]]:
    n = len(pairs)
    res = []  # To store the intermediate states of the array

    for i in range(n):
        j = i - 1

        # Move elements that are greater than key one position ahead
        while j >= 0 and pairs[j].key > pairs[j + 1].key:
            pairs[j], pairs[j + 1] = pairs[j + 1], pairs[j]
            j -= 1

        # Clone and save the entire state of the array at this point
        res.append(pairs[:])

    return res
