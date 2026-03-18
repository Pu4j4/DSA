#Problem: Find First and Last Position of Element in Sorted Array (https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/description/)

#Problem statement:
#Given a sorted integer nums and an integer target, return the first position and left position of target
#if target not found, return [-1,-1]

#Pattern: Binary search

#brute force idea
#initialize first and last with -1
#loop through each element of index i
#if element equal to target, check if first = -1, set first = i
#always update first then set last = i, and return [first, last]

# brute force
def search_range(nums,target):
    first = -1
    last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]

#Time:O(n) - checks each element element    Space: O(1) - only variables used

#why it's slow
#checks every element
#need O(log n) complexity

#Optimized idea
#since array is already sorted
#so instead of scanning entire array
#we use binary search twice:
#find first occurrence
#find second occurrence

#optimized
def search_range(nums,target):
    def find_first():
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def find_last():
        left = 0
        right = len(nums)-1
        ans = -1
        while left<=right:
            mid = (left+right) // 2
            if nums[mid] == target:
                ans = mid
                left = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return ans
    return [find_first(), find_last()]
nums = [1,2,2,3,5,5]
print(search_range(nums, 2))

#Time: O(log n) - each step halves search space     Space: O(1) - only pointers used