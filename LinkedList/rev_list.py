class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    curr = head

    while curr:
        nextNode = curr.next
        curr.next = prev
        prev = curr
        curr = nextNode

    return prev

head = Node(5)
second = Node(10)
third = Node(15)
forth = Node(20)

head.next = second
second.next = third
third.next = forth

print(reverse_list(head))

