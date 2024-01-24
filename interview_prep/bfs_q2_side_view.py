# Given the root of a binary tree, imagine yourself standing on the right side
# of it, return the values of the nodes you can see ordered from top to bottom.

import collections


def right_side_view(self, root):
    res = []
    queue = collections.deque([root])

    while len(queue) > 0:
        right_side = None

        for i in range(len(queue)):
            cur = queue.popleft()
            if cur:
                right_side = cur
                queue.append(cur.left)
                queue.append(cur.right)

        if right_side:
            res.append(right_side.val)

    return res

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]
