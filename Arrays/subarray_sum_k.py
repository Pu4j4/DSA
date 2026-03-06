# Problem: Subarray sum equals k (https://leetcode.com/problems/subarray-sum-equals-k/description/)

# Problem statement:
# Given an array nums and integer k, return the total no.of subarrays whose sum equals k

# Pattern: Prefix_sum + hashmap

#brute force idea
#check every possible subarray and calculate its sum
#start from each index i,extend the subarray with index j one by one
#keep each num adding to sum, if sum equals k -> increase count -> return count

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

#Time: O(n^2)- nested loops     space: O(1)

#why it's slow
#checking all subarrays, slow for large input

#optimized idea
#instead of recalculating sum every time, reuse previous sum
#prefix_sum[j] - prefix_sum[i] = k --> rearrange - prefix_sum[i] = prefix_sum[j]-k
#so check prefix_sum-k exists before
#use hashmap to store prefix sums


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


#Time: O(n) -single loop,O(1) lookup   space-O(n) - stores prefix sums