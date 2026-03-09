# Problem: Contains Duplicate (https://leetcode.com/problems/contains-duplicate/)

# Problem statement:
# Given an integer array nums return True iif any value appears atleast twice in the array,
# and return False if every element is distinct

#pattern: Hashset

#Brute force idea:
# for every element compare with another element using nested loops
# if it contains duplicate return true else False

#brute force
def contain_duplicate(nums):
    n = len(nums)
    for i in range(n):
        for j in range(i+1,n):
            if nums[i] == nums[j]:
                return True
    return False

print(contain_duplicate([1,3,4,2,1,2]))

# Time: O(n^2) - nested loops   space: O(1)

# Why it's slow:
#Checking every possible pair using nested loops
#repeated comparisons

# optimized idea
#instead of checking every element, we store elements in hashset
#check if element in hashset, return True if not add current element to set


#optimized (using hashset())
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1,3,4,2]))

#Time: O(n)- single loop    Space: O(n)-hashset stores n elements
