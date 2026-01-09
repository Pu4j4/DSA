def reverse_arr(arr):
    my_stack = []
    for num in arr:
        my_stack.append(num)

    for i in range(len(arr)):
        arr[i] = my_stack.pop()
    return arr

arr = [10,50,30,90]
print(reverse_arr(arr))

