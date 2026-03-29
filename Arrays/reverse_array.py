# Problem: Reverse an array

#Problem:
#Given an array of integer nums, reverse the array in-place
#you must modify the original array and return it

#pattern: Two pointers

#brute force idea
#create empty array result
#traverse original array from end to start
#add element to result
#traverse again ->copy elements of result into nums

#brute force code
def reverse_arr(nums):
    result = []
    for i in range(len(nums)-1,-1,-1):
        result.append(nums[i])
    for i in range(len(nums)):
        nums[i] = result[i]
    return nums

#Time: O(n) - loop through entire array once   Space:O(n) - result array created

#why it's slow
#extra space used - need to optimize space (do it in place)

#optimize idea
#use two pointers: left = 0 , right = len(nums)-1
#swap elements and move pointers inward and return nums

#optimized code
def reverse_arr(nums):
    left,right = 0, len(nums)-1
    while left<right:
        nums[left],nums[right] = nums[right], nums[left]
        left+=1
        right-=1
    return nums
nums = [1,2,3,4,5]
print(reverse_arr(nums))

#Time: O(n) - swapped each element once   Space: O(1)- in-place reverse