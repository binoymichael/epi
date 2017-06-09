from linked_list import Node


def reversed_list(list, start, end):
    head = current = list
    for _ in range(start - 2):
        current = current.next

    left_border = current
    left = a = current.next
    b = a.next

    for _ in range(end - start):
        c = b.next
        b.next = a
        a = b
        b = c

    left.next = b
    left_border.next = a

    return head


list = Node(11, Node(3, Node(5, Node(7, Node(2)))))
print(list)
list = reversed_list(list, 2, 4)
print(list)




