#Problem : Binary search (https://leetcode.com/problems/binary-search/)

#Problem statement:
#Given a sorted array integer nums in ascending order and a target value
#return the indec of target if it exists in the array , otherwise return -1

#Pattern: Binary search

#brute force idea
#loop through each element index i from o to n-1
#if target element found in array return its index else return -1

#brute force code
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

#Time: O(n) - check every element one by one   Space: O(1) - no extra space

#why it's slow:
#checks every element, n comparisons
#need O(log n) complexity

#Optimized idea
#array is sorted, we can eliminate half elements each time:
#use left and right pointers, left = 0 right = len(nums)-1
#take middle element: compare with target
#if equal -> return middle element index
#if small -> left = mid+1
#if large -> right = mid-1
#otherwise return -1

#optimized code
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

nums = [1,3,5,6,8,9]
print(search(nums,6))

#Time: O(log n)  - each halves search space     Space: O(1) - only variables used
