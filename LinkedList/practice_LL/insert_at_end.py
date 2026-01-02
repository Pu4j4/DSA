class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_at_end(head,data):
    new_node = Node(data)
    if head is None:
        return new_node
    curr = head
    while curr.next is not None:
        curr = curr.next
    curr.next = new_node

    return curr.next.data

head = Node(20)
second = Node(15)
third = Node(10)

head.next = second
second.next = third

print( insert_at_end(head,25))