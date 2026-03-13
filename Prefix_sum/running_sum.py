#Problem: Running Sum of 1d Array  (https://leetcode.com/problems/running-sum-of-1d-array/description/)

#Problem statement:
#Given an array of integer nums, return an array running sum where
#runningsum[i] = nums[0]+nums[1]+nums[2]+...+nums[i]
#each element in output array is sum of of all previous elements including itself

#Pattern: Prefix_sum

#brute force idea
#for each index i, again for each index j till i+1
#calculate sum, append sum to result array and return result

#brute force code
def running_sum(nums):
    result = []
    for i in range(len(nums)):
        total = 0
        for j in range(i+1):
            total+=nums[j]
        result.append(total)
    return result

#Time: O(n^2) - nested loops      Space: O(n) -result array stores n elements

#why it's slow
#nested loops, each index recalculates from start
#slow for large input

#Optimized idea
#we've already calculated previous sum, so don't need to calculate sum from start again
#keep track of running sum while iterating
#formula runningsum[i] = runningsum[i-1]+runningsum[i]

#optimized code - i
def running_sum(nums):
    result = []
    total = 0
    for num in nums:
        total += num
        result.append(total)
    return result

#Time: O(n) - each element processed once    Space: O(n) - result array stores elements

#optimized code - ii -modifying same array
def running_sum(nums):
    for i in range(1, len(nums)):
        nums[i] = nums[i-1] + nums[i]
    return nums

nums = [1,13,17,20]
print(running_sum(nums))

#Time: O(n) - each element processed once    Space: O(1) - in-place