class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def insert_at_begin(head,data):
    new_node = Node(data)
    new_node.next = head
    head = new_node
    return head.data

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

print( insert_at_begin(head,5))