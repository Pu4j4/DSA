#Problem: Find peak element (https://leetcode.com/problems/find-peak-element/description/)

#Problem statement:
#Given an integer array nums
#peak element is an element that is strictly greater than it's neighbors,return the index of any peak element

#Pattern: Binary Search

#brute force idea
#check every element and see if its greater than neighbors
#for each index:
#check nums[i] > nums[i-1]
#check nums[i] > nums[i+1]
#return index if true

#brute force code
def findpeak(nums):
    n = len(nums)
    for i in range(n):
        left = nums[i-1] if i>0 else float('-inf')
        right = nums[i+1] if i<n-1 else float('-inf')
        if nums[i] > left and nums[i] > right:
            return i

#Time: O(n) - checks every element    Space: O(1) - no extra space

#why it's slow
#checks all elements
#need O(log n)

#Optimized idea
#use two pointers left and right
#calculate mid -> nums[mid]<nums[mid+1] -> peak on right side
#if nums[mid] > nums[mid+1] ->peak on left side

#optimized code
def findpeak(nums):
    left = 0
    right = len(nums)-1
    while left<right:
        mid = (left+right) // 2
        if nums[mid] < nums[mid+1]:
            left = mid+1
        else:
            right = mid
    return left

nums = [1,2,3,1]
print(findpeak(nums))

#Time: O(log n) - eliminate half of array each step   Space: O(1) - only variables used


