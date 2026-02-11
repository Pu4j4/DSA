#brute force
def two_sum_ii(numbers,target):
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]

numbers = [1,2,4,9]
print(two_sum_ii(numbers, 6))

