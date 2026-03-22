#Problem: Maximum subarray  (https://leetcode.com/problems/maximum-subarray/description/)

#Problem statement:
#Given an integer nums
#find subarray with target with largest sum and return it sum

#Pattern: Kadane's algorithm/ Dynamic programming(1D dp)

#brute force idea
#check every possible subarray and compute its sum
#start from index i
#extend the subarray with index j
#calculate subarray sum
#repeat, update max_sum (keep track of max sum)

#brute force idea
def max_subarray(nums):
    n = len(nums)
    max_sum = float('-inf')
    for i in range(0, n):
        curr_sum = 0
        for j in range(i,n):
            curr_sum +=  nums[j]
            max_sum = max(max_sum, curr_sum)
    return max_sum

#Time: O(n^2) - nested loops     Space: O(1) - some variables used

#why it's slow
#nested loops, checking every possible subarray
#repeated calculations, slow for large input

#Optimized idea
#initialize max_sum and curr_sum with first element
#for each index i from 1 to n-1 -> curr_sum -> continue with prev sum or restart with new
#Update max_sum

#Optimized code
def max_subarray(nums):
    max_sum = nums[0]
    curr_sum = nums[0]
    for i in range(1, len(nums)):
        curr_sum = max(nums[i], curr_sum+nums[i])
        max_sum = max(max_sum, curr_sum)
    return max_sum

nums = [1,-4,2,-1,9]
print(max_subarray(nums))

#Time: O(n) - single loop    Space: O(1) - some variables used