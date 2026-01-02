class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def delete_last_node(head):
    if head is None:
        return None

    if head.next is None:
        return None
    curr = head
    while curr.next.next is not None:
        curr = curr.next

    curr.next = None
    return curr.data



head = Node(10)
second = Node(20)
third = Node(30)
forth = Node(40)

head.next = second
second.next = third
third.next = forth
print(delete_last_node(head))