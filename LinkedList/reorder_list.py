class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
def reorder_list(head):
    if not head or not head.next:
        return
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    prev = None
    curr = slow.next
    slow.next = None
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
    first = head
    second = prev
    while second:
        temp1 = first.next
        temp2 = second.next
        first.next = second
        second.next = temp1
        first = temp1
        second = temp2

def print_list(head):
    curr = head
    while curr:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

head = Node(10)
second = Node(20)
third = Node(30)
forth = Node(40)

head.next = second
second.next = third
third.next = forth

print("Before reorder:")
print_list(head)

reorder_list(head)

print("After reorder:")
print_list(head)