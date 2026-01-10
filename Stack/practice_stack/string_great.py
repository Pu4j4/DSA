def string_great(s):
    stack = []
    for ch in s:
        if stack and abs(ord(stack[-1])-ord(ch)) == 32:
            stack.pop()
        else:
            stack.append(ch)
    return "".join(stack)

print(string_great("leEeetcode"))
print(string_great("aBbhanuU"))