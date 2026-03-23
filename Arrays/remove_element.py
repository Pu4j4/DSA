#Problem: Remove element  (https://leetcode.com/problems/remove-element/description/)

#Problem statement:
#Given an integer nums and integer val, remove all occurrences of val in nums in place
#return the length the array

#Pattern: Two pointers(fast and slow pointers)

#brute force idea:
#create new array
#traverse array and remove elements which are equal to val
#return length of array

#Brute force
def remove_element(nums,val):
    res = []
    for x in nums:
        if val != x:
            res.append(x)
    nums[:] = res   #copy back to original array
    return len(res)

#Time: O(n) - single traversal      Space: O(n) - extra array used

#why it's slow
#extra space used, required in place traversal

#Optimized idea
#use fast and slow pointers , k=0 which is fast pointer
#slow pointer is traversing through array
#if element not equal to val: -> assign nums[k] = nums[i] , increment k
#return k

#Optimized
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k

print(remove_element([1,3,7,2,9,13,20],7))

#Time: O(n) - single traversal   Space:O(1) - in-place modification