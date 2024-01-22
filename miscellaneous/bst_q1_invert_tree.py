class Node:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def print_tree(self):
        if self.left:
            self.left.print_tree()
        print(self.data, end=' ')
        if self.right:
            self.right.print_tree()


class Solution:
    def invert_tree(self, root):
        if root is None:
            return None

        # swap the children
        root.left, root.right = root.right, root.left

        # make 2 recursive calls
        self.invert_tree(root.left)
        self.invert_tree(root.right)
        return root


if __name__ == '__main__':
    Tree = Node(10)
    Tree.left = Node(20)
    Tree.right = Node(30)
    Tree.left.left = Node(40)
    Tree.right.right = Node(50)

    print('Initial Tree:', end=' ')
    Tree.print_tree()

    Solution().invert_tree(root=Tree)
    print('\nInverted Tree:', end=' ')

    Tree.print_tree()
