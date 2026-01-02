class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def find_max(head):
    if head is None:
        return None
    max_val = head.data
    curr = head.next

    while curr is not None:
        if curr.data > max_val:
            max_val = curr.data
        curr = curr.next
    return max_val
head = Node(30)
second = Node(50)
third = Node(10)
forth = Node(60)

head.next = second
second.next = third
third.next = forth

print(find_max(head))