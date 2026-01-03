class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def delete_first_node(head):
    if head is None:
        return None
    
    head = head.next
    return head

head = Node(10)
second = Node(20)
third = Node(30)
forth = Node(40)

head.next = second
second.next = third
third.next = forth
print(delete_first_node(head))