def remove_adjacent(s):
    stack = []
    for ch in s:
        if stack and stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)

print(remove_adjacent('aabca'))
print(remove_adjacent('abcabc'))
print(remove_adjacent('abbaca'))