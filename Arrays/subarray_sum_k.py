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

#optimized
def subarray_sum(nums,k):
    prefix_sum = 0
    count = 0
    prefix_map = {0:1}
    for num in nums:
        prefix_sum += num
        if prefix_sum - k in prefix_map:
            count += prefix_map[prefix_sum-k]
        prefix_map[prefix_sum] = prefix_map.get(prefix_sum, 0) + 1
    return count

nums = [1,2,3,1,1,1]
k = 3
print(subarray_sum(nums,k))
