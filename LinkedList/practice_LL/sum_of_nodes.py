class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def sum_of_nodes(head):
    total = 0
    curr = head
    while curr is not None:
        total += curr.data
        curr = curr.next
    return total

head = Node(20)
second = Node(10)
third = Node(50)
forth = Node(5)

head.next = second
second.next = third
third.next =forth
print(sum_of_nodes(head))