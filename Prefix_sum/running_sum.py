#brute force
def running_sum(nums):
    result = []
    for i in range(len(nums)):
        total = 0
        for j in range(i+1):
            total+=nums[j]
        result.append(total)
    return result


nums = [1,13,17,20]
print(running_sum(nums))

