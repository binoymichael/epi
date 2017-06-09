from binary_tree_node import BinaryTreeNode

def tree_traversal(tree):
    if tree.left:
        tree_traversal(tree.left)
    if tree.right:
        tree_traversal(tree.right)
    print(tree.data)

tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)
tree_traversal(tree)
