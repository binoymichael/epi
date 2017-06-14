class BinaryTreeNode:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right;

    def __repr__(self):
        return "{} <- {} -> {}".format(self.left and self.left.data,
                                       self.data, self.right and self.right.data)