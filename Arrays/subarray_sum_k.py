#brute force
def subarray_sum(nums,k):
    n = len(nums)
    count = 0
    for i in range(n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum += nums[j]
            if curr_sum == k:
                count += 1
    return count
nums = [1,2,3]
k = 3
print(subarray_sum(nums,k))


