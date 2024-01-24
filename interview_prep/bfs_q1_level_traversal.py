# Given the root of a binary tree, return the level order traversal of its nodes
# values. (i.e. from left to right, level by level).

from collections import deque


def level_order(root):
    queue = deque()
    res = []

    if root:
        queue.append(root)

    while len(queue) > 0:
        temp = []

        for i in range(len(queue)):
            cur = queue.popleft()
            temp.append(cur.val)
            if cur.left:
                queue.append(cur.left)
            if cur.right:
                queue.append(cur.right)

        res.append(temp)

    return res

# Input: root = [3,9,20,null,null,15,7]
# Output: [[3],[9,20],[15,7]]
