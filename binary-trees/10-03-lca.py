from binary_tree_node import BinaryTreeNode


def seen(node, first, second):
    if node is None:
        return None, False, False

    left_result, left_seen_first, left_seen_second = seen(node.left, first, second) if node.left else (None, False, False)
    if left_result:
        return left_result, True, True

    right_result, right_seen_first, right_seen_second = seen(node.right, first, second) if node.right else (None, False, False)
    if right_result:
        return right_result, True, True

    first_seen = left_seen_first or right_seen_first or node is first
    second_seen = left_seen_second or right_seen_second or node is second

    if first_seen and second_seen:
        return node, True, True
    else:
        return None, first_seen, second_seen


tree = BinaryTreeNode(3)
tree.left = BinaryTreeNode(2)
tree.left.left = BinaryTreeNode(1)
tree.right = BinaryTreeNode(5)
tree.right.left = BinaryTreeNode(4)
tree.right.right = BinaryTreeNode(6)

a, b, c = seen(tree, tree.left, tree.right)
print(a, b, c)
