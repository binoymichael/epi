from linked_list import Node

def remove_kth(list, n):
    dummy = Node(-1, list)

    fast = list
    slow_pred = dummy

    for _ in range(n):
        fast = fast.next

    while fast is not None:
        fast = fast.next
        slow_pred = slow_pred.next

    slow_pred.next = slow_pred.next.next

    return dummy.next

list1 = Node(1, Node(2, Node(3, Node(4, Node(5)))))
print(list1)
list1 = remove_kth(list1, 3)
print(list1)
list1 = remove_kth(list1, 1)
print(list1)
list1 = remove_kth(list1, 3)
print(list1)
