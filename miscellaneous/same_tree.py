# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
#
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.

def is_same_tree(p, q):
    """
    :type p: TreeNode
    :type q: TreeNode
    :rtype: bool
    """
    if not p and not q:
        return True
    if not p or not q or p.val != q.val:
        return False

    return (is_same_tree(p.left, q.left) and
            is_same_tree(p.right, q.right))

    # def inorder(root, temp):
    #     if not root:
    #         return root
    #     temp.append(inorder(root.left, temp))
    #     temp.append(root.val)
    #     temp.append(inorder(root.right, temp))

    # p_list = []
    # q_list = []

    # inorder(p, p_list)
    # inorder(q, q_list)

    # return p_list == q_list
