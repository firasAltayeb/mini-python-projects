# Given a root node reference of a BST and a key, delete the node with the given key in the BST.
# Return the root node reference (possibly updated) of the BST.

def find_min_node(self, root):
    while root.left:
        root = root.left
    return root


def delete_node(self, root, key):
    if not root:
        return None

    if key > root.val:
        root.right = self.delete_node(root.right, key)
    elif key < root.val:
        root.left = self.delete_node(root.left, key)
    else:
        if not root.left:
            return root.right
        elif not root.right:
            return root.left
        else:
            min_node = self.find_min_node(root.right)
            root.val = min_node.val
            root.right = self.delete_node(root.right, min_node.val)

    return root

# Input: root = [5,3,6,2,4,null,7], key = 3
# Output: [5,4,6,2,null,null,7]
