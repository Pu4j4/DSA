#Problem: Contains Duplicate ii (https://leetcode.com/problems/contains-duplicate-ii/description/)

#Problem statement:
#Given an integer array nums and integer k, return true if there are two same numbers such that the
#distance b/w their indices is at most k else return False

#Pattern: Sliding window + hashset or hashmap

#brute force idea
#compare every element with other elements
#if two elements are same and distance b/w their indices <= k (check abs(i-j) <=k) -> return True
#otherwise return False

#brute force code
def contains_dup(nums,k):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] and abs(i-j) <= k:
                return True
    return False

#Time: O(n*k) - nested loops   Space:O(1) - no extra space used

#why it's slow
#for every element, we check k elements
#nested loops -> slow for large input

#optimized idea
#instead of checking repeatedly, we maintain a sliding window of size k
#we keep last k elements in a set
#if current element already exists in set -> return True

#optimized code
def contains_dup(nums, k):
    window = set()
    for i in range(len(nums)):
        if nums[i] in window:
            return True
        window.add(nums[i])
        if len(window) >k:
            window.remove(nums[i-k])
    return False

#or

def contains_dup(nums,k):
    index_map = {}
    for i, num in enumerate(nums):
        if num in index_map and i-index_map[num] <=k:
            return True
        index_map[num] = i
    return False

nums = [1,22,4,19,12,22,7]
# nums = [1,2,3,4,2]
print(contains_dup(nums,4))

#Time: O(n) - each element added and removed once    Space: O(k) - set or hashmap stores at most k elements
