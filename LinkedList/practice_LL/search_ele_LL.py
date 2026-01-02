class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def search_element(head,target):
    curr = head
    while curr is not None:
        if curr.data == target:
            return True
        curr = curr.next
    return False

head = Node(4)
second = Node(2)
third = Node(10)
forth = Node(18)

head.next = second
second.next = third
third.next = forth

print(search_element(head, 20))
print(search_element(head,2))