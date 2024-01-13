# Given the root of a binary search tree, and an integer k
# return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

def kth_smallest(root, k):
    """
    :type root: TreeNode
    :type k: int
    :rtype: int
    """
    stack = []
    cur = root
    n = 0

    while cur or stack:
        while cur:
            stack.append(cur)
            cur = cur.left
        cur = stack.pop()
        n += 1
        if n == k:
            return cur.val
        cur = cur.right

    # res = []

    # def inorder(root):
    #     if not root:
    #         return
    #     inorder(root.left)
    #     res.append(root.val)
    #     inorder(root.right)

    # inorder(root)

    # return res[k-1]
