class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def print_list(head):
    curr = head
    while curr is not None:
        print(curr.data,end="->")
        curr = curr.next
    print("None")

def rev_list(head):
    prev = None
    curr = head

    while curr is not None:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    print("reversed list")
    print_list(prev)
    return prev

head = Node(10)
second = Node(20)
third = Node(30)
forth = Node(40)

head.next = second
second.next = third
third.next = forth

print("original list")
print_list(head)
print(rev_list(head))