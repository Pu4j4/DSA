# Problem : Two Sum (https://leetcode.com/problems/two-sum/)
# Platform : Leetcode

#Problem Statement
# Given an array of integers nums and integer target, return the indices of the two numbers
# such that they add up to target

#pattern: Hashmap

#brute force idea:
#check every possible pair using nested loops
#pick first number, add with all numbers
#for each pair check they're equal to target return indices


#brute force code
def two_sum(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] + nums[j] == target:
               return [i, j]
    return []

print(two_sum([2,5,1,0,6],7))

#time: O(n^2) - nested loops    space: O(1)


#why it's slow:
#checks every possible pair
#slow for large input

#optimized idea
#instead of checking all pairs, we can store elements in hashmap
#for each number: diff = target - num
#check if diff in seen return indices, if not store current number

#Optimized (using hashmap)
def two_sum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff],i]
        seen[num] = i
    return []

print(two_sum([2,1,5,0,6],7))

#time: O(n)-single loop,hashmap lookup O(1)   #space: O(n) - hashmap stores upto n elements