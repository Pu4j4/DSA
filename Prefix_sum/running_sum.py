#brute force
def running_sum(nums):
    result = []
    for i in range(len(nums)):
        total = 0
        for j in range(i+1):
            total+=nums[j]
        result.append(total)
    return result



#optimized - i
def running_sum(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

#optimized - ii -modifying same array
def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return nums

nums = [1,13,17,20]
print(running_sum(nums))

