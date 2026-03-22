# Problem: Move zeroes (https://leetcode.com/problems/move-zeroes/description/)

# Problem statement:
#Given an integer array of nums, it contains zeroes
#move all zeroes to end of the array while maintaining relative order of non_zero elements(in-place)

#Pattern: Two pointers(fast and slow pointer)

#brute force idea
#create a result array, add non zero elements to result
#count zeroes , add zeroes at the end of result
#copy back the elements in result into original nums

#brute force code
def move_zeroes(nums):
    result = []
    for num in nums:
        if num!=0:
            result.append(num)
    zeroes = len(nums) - len(result)
    for i in range(zeroes):
        result.append(0)
    for i in range(len(nums)):
        nums[i] = result[i]
    return nums

#Time: O(n) - traverse array to collect and copy back       Space: O(n)-extra array used

#why it's slow
#extra space used - optimize space

#optimized idea
#use two pointers(fast and slow pointers)
#left - position to put non zero element
#right - scanning array
#check if current element is non_zero swap the elements
#move left pointer, return nums

#optimized code
def move_zeroes(nums):
    left = 0
    for right in range(len(nums)):
        if nums[right]!=0:
            nums[left],nums[right] = nums[right],nums[left]
            left+=1
    return nums
nums = [1,0,3,8,0,0]
print(move_zeroes(nums))

#Time: O(n) - single pass through array   Space: O(1) - in-place
