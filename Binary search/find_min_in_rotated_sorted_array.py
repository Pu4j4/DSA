#Problem: Find minimum in rotated sorted  array (https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)

#Problem statement:
#Given a sorted array that has been rotated at some unknown pivot
#return the minimum element in array

#Pattern: Binary search

#brute force idea
#set minimum as first element
#compare with other elements, update min if smaller found

#brute force code
def find_min(nums):
    minimum = nums[0]
    for num in nums:
        if num < minimum:
            minimum = num
    return minimum

#Time: O(n) - check each element once   Space: O(1) - no extra space

#why it's slow
#checks each element
#need O(log n) complexity

#Optimized idea
#since array is sorted and rotated, we can eliminate half of array
#use left and right and find middle element
#if middle element > right -> search right half
#if middle element < right: keep right = mid , return left num

#Optimized code
def find_min(nums):
    left = 0
    right = len(nums)-1
    while left < right:
        mid = (left+right) // 2
        if nums[mid] > nums[right]:
            left = mid+1
        else:
            right = mid
    return nums[left]

nums = [4,5,6,1,2]
print(find_min(nums))

#Time: O(log n) - each step eliminates half array     Space: O(1)- only pointers used

