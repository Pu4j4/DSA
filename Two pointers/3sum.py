#Problem: Three sum (https://leetcode.com/problems/3sum/description/)

#Problem statement:
#Given an integer array nums
#return all unique triplets [nums[i],nums[j],nums[k]] such that: i!=j!=k and their sum equal to 0

#Pattern: Two pointers

#brute force idea
#using 3loops i,j,k
#calculate sum, if equal to zero->sort list of triplets and convert to tuple
#add triplets to result set and convert result set to list and return

#Brute force
def three_sum(nums):
    n = len(nums)
    result = []
    seen = set()
    for i in range(n):
        for j in range(i+1,n):
            for k in range(j+1,n):
                if nums[i]+nums[j]+nums[k]==0:
                    trip = tuple(sorted([nums[i],nums[j],nums[k]]))
                    if trip not in seen:
                        seen.add(trip)
                        result.append(list[trip])
    return result

#Time: O(n^3) - sorting takes n log n and n3 takes time more than sorting so O(n^3)  Space:O(n) - result set

#why it's slow
#using 3loops
#checking all triplets, slow for large input

#optimized idea
#instead of checking all triplets -> use one fix number i and find remaining two numbers using two pointers
#left = i+1 and right = len(nums)-1
#check if i and prev i contains duplicates
#start from left= i+1, and right = len(nums-1)  and calculate sum
#if sum < 0: move left pointer
#if sum > 0: move right pointer, if equal to zero -> add triplets as list in result
#check if duplicates exists for left and right pointers


#Optimized
def three_sum(nums):
    nums.sort()
    n = len(nums)
    result = []
    for i in range(n):
        if i>0 and nums[i] == nums[i-1]:
            continue
        left,right = i+1, n-1
        while left<right:
            curr_sum = nums[i]+nums[left]+nums[right]
            if curr_sum<0:
                left+=1
            elif curr_sum>0:
                right-=1
            else:
                result.append(list[nums[i],nums[left],nums[right]])
                left+=1
                right-=1
                while left<right and nums[left] == nums[left-1]:
                    left+=1
                while left<right and nums[right] == nums[right-1]:
                    right-=1
    return result
print(three_sum([1,-1,0,4,-1,-3]))


#Time: O(n^2) - using two loops - outer loop runs n times and inner loop two pointer runs n times
# (for sorting O(n log n)-> n2 and n3 grows much faster than n log n)
# space:O(k)- k no.of triplets   O(1) - only pointer variables used