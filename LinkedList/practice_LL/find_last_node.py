class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def find_last_node(head):
    if head is None:
        return None
    curr = head
    while curr.next is not None:
        curr = curr.next
    return curr.data

head = Node(30)
second = Node(50)
third = Node(10)
forth = Node(60)

head.next = second
second.next = third
third.next = forth

print(find_last_node(head))