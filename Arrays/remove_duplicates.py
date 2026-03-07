# Problem: Remove Duplicates from sorted array  (https://leetcode.com/problems/remove-duplicates-from-sorted-array/description/)

#Problem statement:
#Given a sorted integer array nums, remove the duplicates in-place such that each unique element
# appears only once, return the no.of unique elements k.
#the first k elements of the array should contain unique elements

#Pattern: Two pointers(fast and slow pointer)

#brute force idea
#store the elements in nums in a set and sort the set(sorted converts set into a list)
#replace the set elements in the original nums
#return length of set because we removed duplicates

#Brute force code1
def remove_duplicates(nums):
    s = sorted(set(nums))
    nums[:] = s
    return len(s)

print(remove_duplicates([1,3,5,5,6,7,7,8,8]))

#Time: O(n log n) - sorting takes O(n log n)   Space: O(n) - set stores unique elements

#brute force idea:
#create a new array result->traverse the array nums -> append elements which are not in result
#traverse the result array -> copy back elements into nums from result
#return length of result

#brute force code2:
def remove_duplicates(nums):
    result = []
    for num in nums:
        if num not in result:
            result.append(num)
    for i in range(len(result)):
        nums[i] = result[i]
    return len(result)

#Time: O(n^2) - first loop-O(n) , checking num not in result O(n)   Space: O(n) - extra array used

#why it's slow:
#b1-sorting takes O(n log n) times
#b2 - repeated checking - O(n^2) times

#optimized idea:
#use fast and slow pointers: i and j
#j traverse through nums and check if previous element is same as current element
#then current element is kept in ith position-> i = 1 and move ith pointer after element insertion

#Optimized
def remove_duplicates(nums):
    i = 1
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i
print(remove_duplicates([1,3,5,5,6,7,7]))

#Time: O(n) - each element visited once    Space: O(1)- in place