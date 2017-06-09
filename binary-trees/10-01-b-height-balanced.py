from binary_tree_node import BinaryTreeNode


def height(node):
    if node is None:
        return True, -1

    sl, hl = height(node.left)
    sr, hr = height(node.right)

    if not sl or not sr or abs(hl - hr) > 1:
        return False, max(hl, hr) + 1

    return True, max(hl, hr) + 1



tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.left.left.left = BinaryTreeNode(0)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)

r, h = height(tree)
print(r)

