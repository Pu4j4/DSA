# Problem:  Two Sum II - Input Array Is Sorted (https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/)

# Problem statement:
# Given a sorted array of integer nums (sorted in non_decreasing order) and an integer target.
# find two numbers such that they add up to target, return 1-based indices of two numbers

#pattern : Two pointers

#brute force idea
# loop through the nums and calculate sum
# check if sum equal to target, if yes return indices

#brute force
def two_sum_ii(numbers,target):
    n = len(numbers)
    for i in range(n):
        for j in range(n):
            if numbers[i] + numbers[j] == target:
                return [i+1,j+1]

numbers = [1,2,4,9]
print(two_sum_ii(numbers, 6))

#Time: O(n^2) - nested loops  Space: O(1)

#why it's slow
# checks all pairs, repeated comparisons

#optimized
#Use two pointers - left at start, right at end
#calculate sum and check if sum equal to target return indices
#if sum too small, left ++
#if sum to large, right--

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

#Time: O(n) - each element visited once by pointers   Space: O(1) - only Two variables used