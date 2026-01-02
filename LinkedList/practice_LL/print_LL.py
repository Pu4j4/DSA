class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end="->")
        curr = curr.next
    print("None")

head = Node(5)
second = Node(10)
third = Node(15)
forth = Node(20)

head.next = second
second.next = third
third.next = forth

print_list(head)