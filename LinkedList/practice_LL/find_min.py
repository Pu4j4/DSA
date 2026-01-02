class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def find_min(head):
    if head is None:
        return None
    min_val = head.data
    curr = head.next
    while curr is not None:
        if curr.data < min_val:
            min_val = curr.data
        curr = curr.next
    return min_val

head = Node(20)
second = Node(10)
third = Node(50)
forth = Node(5)

head.next = second
second.next = third
third.next =forth
print(find_min(head))