from binary_tree_node import BinaryTreeNode


def symmetric(left, right):
    if not left and not right:
        return True
    elif left and right:
        return symmetric(left.left, right.right) \
               and symmetric(left.right, right.left)
    else:
        return False

tree = BinaryTreeNode()
tree.left = BinaryTreeNode()
tree.right = BinaryTreeNode()
tree.right.right = BinaryTreeNode()

print(symmetric(tree.left, tree.right))

