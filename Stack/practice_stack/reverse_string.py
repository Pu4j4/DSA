def reverse_string(s):
    my_stack = []
    for ch in s:
        my_stack.append(ch)
    reversed_s = ""
    while my_stack:
        reversed_s += my_stack.pop()
    return reversed_s


my_string = "hello"
print(reverse_string(my_string))
