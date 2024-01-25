# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix.
# If there is no clear path, return -1.
# A clear path in a binary matrix is a path from the top-left cell to the bottom-right cell such that:
# All the visited cells of the path are 0.
# All the adjacent cells of the path are 8-directionally connected.

from collections import deque
from typing import List


def shortest_path_binary_matrix(self, grid: List[List[int]]) -> int:
    N = len(grid)
    q = deque([(0, 0, 1)])  # r, c, length
    visit = set((0, 0))
    direct = [[0, 1], [1, 0], [0, -1], [-1, 0],
              [1, 1], [-1, -1], [1, -1], [-1, 1]]

    while q:
        r, c, length = q.popleft()
        if (min(r, c) < 0 or max(r, c) >= N or
                grid[r][c] == 1):
            continue

        if r == N - 1 and c == N - 1:
            return length

        for dr, dc in direct:
            nr = r + dr
            nc = c + dc
            if (nr, nc) not in visit:
                q.append((nr, nc, length + 1))
                visit.add((nr, nc))

    return -1
