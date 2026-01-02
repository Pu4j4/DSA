class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data, end=" -> ")
        curr = curr.next
    print("None")

def delete_by_value(head,x):
    if head is None:
        return None
    if head.next is None:
        head = head.next
        return head

    prev = None
    curr = head
    while curr is not None:
        if curr.data == x:
            prev.next = curr.next
            break
        prev = curr
        curr = curr.next
    print("Final list after deletion:")
    print_list(head)
    return head


head = Node(10)
second = Node(20)
third = Node(30)
forth = Node(40)

head.next = second
second.next = third
third.next = forth

print("Original list:")
print_list(head)
print(delete_by_value(head,20))