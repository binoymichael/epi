from binary_tree_node import BinaryTreeNode

def greater_than(node, value):
    stack = []

    while node is not None:
        if value >= node.data:
            node = node.right
        else:
            stack.append(node.data)
            node = node.left

    print(stack)


tree = BinaryTreeNode(4)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.left.right = BinaryTreeNode(3)
tree.right = BinaryTreeNode(6)
tree.right.left = BinaryTreeNode(5)
tree.right.right = BinaryTreeNode(7)

print(tree)
greater_than(tree, 2)
