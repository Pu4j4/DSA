class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def count_list(head):
    count = 0
    curr = head
    while curr is not None:
        count+=1
        curr = curr.next
    return count

head = Node(10)
second = Node(20)
third = Node(30)

head.next = second
second.next = third

print(count_list(head))