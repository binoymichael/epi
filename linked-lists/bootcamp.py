from linked_list import Node


def search(node, data):
    while node:
        if node.data == data:
            return node
        node = node.next
    return None

def insert(after, node):
    node.next = after.next
    after.next = node


list = Node(1, Node(2, None))
print(search(list, 2))
print(search(list, 1))
print(search(list, 3))




