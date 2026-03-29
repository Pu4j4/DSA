# Problem: Squares of a sorted array (https://leetcode.com/problems/squares-of-a-sorted-array/description/)

#Problem statement:
# Given a sorted integer array nums in non_decreasing order(ascending order)
#return an array of the squares of each number, also sorted in ascending order

#Pattern: Two pointers(three pointers-extra pointer for place position)

#brute force idea:
#create a result array, traverse through nums
#append each squared number to result array , result the sorted result

#Brute force code
def sort_squares(nums):
    result = []
    for num in nums:
        result.append(num*num)
    return sorted(result)

print(sort_squares([-4,-1,0,2,3]))

#Time: O(n log n) - sorting takes n log n     Space: O(n) - extra result array

#why it's slow
#array is sorted , again sorting takes n log n times

#optimized idea
#larger elements comes from either left most elements or right most elements
#so we'll use two pointers left start at 0 and right at end
#set position to place largest elements
#compare elements, if larger->square the element to put at end
#move pointers and position accordingly, then return result

#Optimized code
def sorted_squares(nums):
    n = len(nums)
    result = [1]*n
    left = 0
    right = n-1
    pos = n-1 #position to put larger elements
    while left <= right:
        if abs(nums[left]) > abs(nums[right]):
            result[pos] = nums[left]*nums[left]
            left+=1
        else:
            result[pos] = nums[right]*nums[right]
            right-=1
        pos-=1
    return result

#Time: O(n) - single pass through each element    Space: O(n) - result array stores squared elements
