def rem_adj_arr(arr):
    stack = []
    for num in arr:
        if stack and stack[-1] == num:
            stack.pop()
        else:
            stack.append(num)
    return stack

print(rem_adj_arr([1,2,2,1,5,9,9,5]))
print(rem_adj_arr([2,3,1,4,6,6,4,5]))