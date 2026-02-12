#brute force
def two_sum_ii(numbers,target):
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]

numbers = [1,2,4,9]
print(two_sum_ii(numbers, 6))

#otimized
def two_sum_ii(numbers, target):
    left,right = 0, len(numbers)-1
    while left<right:
        curr_sum = numbers[left] + numbers[right]
        if curr_sum == target:
            return [left+1, right+1]
        elif curr_sum < target:
            left += 1
        else:
            right -= 1
    return []
numbers = [1,3,4,7,8]
print(two_sum_ii(numbers, 7))