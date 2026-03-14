#Problem: Minimum size subarray sum (https://leetcode.com/problems/minimum-size-subarray-sum/description/)

#Problem statement:
#Given an array of nums and integer target, return minimum length of continuous subarray whose sum is
#greater than or equal to target, if no such subarray exists, return 0

#Pattern: Sliding window

#brute force idea
#start from each index, keep adding elements to total and check if sum >= target
#if yes, update minimum length, return min_len or 0 if no subarray

#brute force code
def subarray_sum(nums, target):
    min_len = float('inf')
    n = len(nums)
    for i in range(n):
        total = 0
        for j in range(i,n):
            total+=nums[j]
            if total >= target:
                min_len = min(min_len, j-i+1)
    return 0 if min_len == float('inf') else min_len

#Time: O(n^2) - nested loops      Space: O(1) - no extra space

#Why it's slow
#checks all subarray
#nested loops
#slow for large input

#optimized idea
#instead of recalculating sum, use sliding window to reuse previous sum
#use two pointers: left = start of window , right = scanning window to end
#add elements to sum, when sum >= target: ->update min_len  ->shrink window from left

#optimized code
def subarray_sum(nums, target):
    min_len = float('inf')
    total = 0
    left = 0
    for right in range(len(nums)):
        total += nums[right]
        while total >= target:
            min_len = min(min_len, right-left+1)
            total-=nums[left]
            left+=1
    return 0 if min_len == float('inf') else min_len

nums = [1,2,4,2,6]
print(subarray_sum(nums,8))

#Time: O(n) - each element added and removed once   Space: O(1) - no extra space
