#Problem: Range Sum Query - immutable  (https://leetcode.com/problems/range-sum-query-immutable/description/)

#Problem statement:
#Given an integer array nums, need to answer multiple queries of the form: sumrange(left,right)
#return sum of elements from index left to right(inclusive), optimize multiple queries

#Pattern: Prefix sum

#brute force idea
#for each query:
#loop from left to right anf calculate sum

#brute force code
class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):
        total = 0
        for i in range(left, right+1):
            total += self.nums[i]
        return total

#Time: O(n) - looping from left to right     Space:O(1)

#why it's slow
#each query O(n)
#we are recalculating sum repeately

#Optimized idea
#store prefix sums to answer queries in O(n)
#create prefix_sum array
#prefix[i] = sum of elements from index 0 to i-1
#formula: prefix[left, right] = prefix[right] - prefix[left]

#optimized code
class NumArray:

    def __init__(self, nums):
        self.prefix = [0]
        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):
        return self.prefix[right+1] - self.prefix[left]

obj = NumArray([1,3,5,2,6,7])
param_1 = obj.sumRange(0,2)
param_2 = obj.sumRange(2,4)
print(param_1)
print(param_2)

#Time: O(n) - direct subtraction using prefix array , O(1)-per query   Space: O(n) - Storing prefix sums