
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

def reverse_list(head):
    prev = None
    curr = head
    while curr is not None:
        next_temp = curr.next
        curr.next = prev
        prev = curr
        curr = next_temp
    return prev

def is_palindrome(head):
    if head is None or head.next is None:
        return True
    slow = fast = head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    second_half = reverse_list(slow)

    first = head
    second = second_half
    while second is not None:
        if first.data != second.data:
            return False
        first = first.next
        second = second.next
    return True


head = Node(10)
second = Node(20)
third = Node(10)

head.next = second
second.next = third

print(is_palindrome(head))