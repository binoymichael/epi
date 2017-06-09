from linked_list import Node


def merge(list1, list2):
    head = current = Node(-1)

    while list1 and list2:
        if list1.data < list2.data:
            current.next = list1
            list1 = list1.next
        else:
            current.next = list2
            list2 = list2.next

        current = current.next

    if list1:
        current.next = list1
    else:
        current.next = list2

    return head.next


list1 = Node(1, Node(3, Node(5)))
list2 = Node(2, Node(4, Node(6)))

print(list1)
print(list2)
print(merge(list1, list2))


