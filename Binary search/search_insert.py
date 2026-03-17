#Problem:  Search insert position (https://leetcode.com/problems/search-insert-position/description/)

#Problem statement:
##Given sorted array nums and integer target, return index if target is found, if not
#return the index where it would be inserted

#Pattern: Binary search

#brute force idea
#loop through each element index i, if element >= target return its index
#if reached end, return length

#brute force code
def search_insert(nums,target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i

#Time: O(n) - checks each element   Space: O(1) - no extra space used

#why it's slow
#check each element, n comparisons
#need O(log n) complexity

#Optimized idea
#Take two pointers: left = 0 and right = len(nums)-1
#find middle element
#compare with target: if element equal to target, return mid
#if mid is small -> search right half -> left = mid+1
#if mid is large -> search left half -> right = mid-1
#if not found, return left(because while searching left reaches end) insertion can be done in end

#optimized code
def search_insert(nums, target):
    left = 0
    right = len(nums)-1
    while left <= right:
        mid = (left+right)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid+1
        else:
            right = mid+1
    return left

nums = [1,3,4,7]
print(search_insert(nums,2))

#Time: O(log n) - each step eliminates half of array     Space: O(1) - using pointers