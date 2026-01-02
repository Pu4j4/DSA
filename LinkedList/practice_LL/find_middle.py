class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def find_middle(head):
    if head is None:
        return None

    slow = head
    fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    return slow.data


head = Node(10)
second = Node(20)
third = Node(30)
forth = Node(40)

head.next = second
second.next = third
third.next = forth
print(find_middle(head))