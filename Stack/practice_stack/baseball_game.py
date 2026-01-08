def baseball(operations):
    stack = []
    for op in operations:
        if op == 'C':
            stack.pop()
        elif op == 'D':
            stack.append(2*stack[-1])
        elif op == '+':
            stack.append(stack[-1] + stack[-2])
        else:
            stack.append(op)
    return sum(stack)

print(baseball([5,2,'C','D','+']))
print(baseball([2,'C',9,3,'D','+']))