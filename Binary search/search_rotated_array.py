#Problem: Search in rotated sorted array (https://leetcode.com/problems/search-in-rotated-sorted-array/description/)

#Problem statement:
#Given an integer sorted array that has been rotated at unknown pivot(position) and integer target
#return the index of target if found, otherwise return -1

#Pattern: Binary search

#brute force idea
#loop through each and every element
#if target found return index if not return -1

#brute force code
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

#Time: O(n)- checks each element     Space:O(1) - no space used

#why it's slow
#checks all elements
#slow for large input, need O(log n) complexity

#optimized idea
#even though is rotated, one half is always sorted
#checks:  if left half sorted ->check if target in left half
#else: search right half

#optimized code
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # left half sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # right half sorted
        # if nums[mid] <= nums[right]:
        else:
            if nums[mid] <= target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

nums = [4,5,6,1,2,3]
print(search(nums, 2))

#Time: O(log n) - search space halves each iteration    Space: O(1) - only pointers used