from binary_tree_node import BinaryTreeNode


def valid(node, lower=float('-inf'), upper=float('inf')):
    if node is None:
        return True

    if node.data > upper or node.data <= lower:
        return False

    return valid(node.left, lower, node.data) \
           and valid(node.right, node.data, upper)






tree = BinaryTreeNode(4)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.left.right = BinaryTreeNode(3)
tree.right = BinaryTreeNode(6)
tree.right.left = BinaryTreeNode(5)
tree.right.right = BinaryTreeNode(7)

print(tree)
print(tree.left)
print(tree.right)
print(valid(tree))
