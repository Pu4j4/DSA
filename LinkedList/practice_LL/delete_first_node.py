class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_first_node(head):
    if head is None:
        return None
    
    head = head.next
    return head.data

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third
print(delete_first_node(head))