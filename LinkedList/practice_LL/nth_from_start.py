class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def nth_from_start(head,n):
    if head is None:
        return None
    curr = head
    count = 1
    while curr is not None:
        if count == n:
            return curr.data
        count+=1
        curr = curr.next
    return None

head = Node(10)
second = Node(20)
third = Node(30)
forth = Node(40)

head.next = second
second.next = third
third.next = forth

print(nth_from_start(head,2))