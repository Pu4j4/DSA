#Problem: First Bad Version  (https://leetcode.com/problems/first-bad-version/description/)

#Problem statement:
#Given an integer n representing versions from 1 to n, there is an api(function) ->isBadVersion(version)
#it returns: True ->if version is bad, False ->if version is good
#once a version becomes bad, all versions after it are also bad, find first bad version

#Pattern: Binary search

#brute force idea
#loop through n of index i from 1 to n+1
#if isBadVersion(i) -> return i

#brute force code
bad = 4
def is_badversion(version):
    return version >= bad

def bad_version(n):
    for i in range(1,n+1):
        if is_badversion(i):
            return i

n = 5
print(bad_version(n))

#Time: O(n) - checking each version one by one     Space: O(1) - no extra space

#why it's slow
#checking each version one by one
#too slow when n is very large

#optimized idea
#we notice good good good bad bad: this is sorted by condition, we're finding the boundary
#use two pointers low = 1 and high = 1
#calculate middle element, while low<=high: if mid is bad ->search left side
#if mid is good: search right side

#optimized code
def bad_version(n):
    low = 1
    high = n
    while low<=high:
        mid = (low+high) // 2
        if is_badversion(mid):
            high = mid
        else:
            low = mid+1
    return low

n = 5
print(bad_version(n))

#Time: O(log n) - search space halves every iteration      Space: O(1) - only variables used
