def process_string(s):
    stack = []
    for ch in s:
        if ch == '#':
            if stack:
                stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)

def backspace_compare(s,t):
    return process_string(s) == process_string(t)

print(backspace_compare('ab#c', 'abc#'))
print(backspace_compare('ac#b', 'abc#'))