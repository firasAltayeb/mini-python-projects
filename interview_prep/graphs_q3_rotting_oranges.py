# You are given an m x n grid where each cell can have one of three values:
# 0 representing an empty cell, 1 representing a fresh orange or 2 representing a rotten orange.
# Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.
# If this is impossible, return -1.

from collections import deque
from typing import List


def oranges_rotting(grid: List[List[int]]) -> int:
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1
            elif grid[r][c] == 2:
                queue.append([r, c])

    minutes = 0
    while queue and fresh > 0:

        for x in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = dr + r, dc + c
                if (nr in range(rows) and nc in range(cols)
                        and grid[nr][nc] == 1):
                    queue.append([nr, nc])
                    grid[nr][nc] = 2
                    fresh -= 1

        minutes += 1

    return minutes if fresh == 0 else -1
