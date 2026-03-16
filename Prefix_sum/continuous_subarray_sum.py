#Problem: Continuous subarray sum (https://leetcode.com/problems/continuous-subarray-sum/description/)

#Problem statement:
#Given an integer nums and integer k return true, if the array has continuous subarray size atleast 2
#whose sum is multiple of k otherwise return False

#Pattern: Prefix_sum

#brute force idea
#for every possible subarray:
#start from each index
#calculate sum
#check if sum%k == 0 and length >= 2

#brute force code
# def continuous_subarray(nums, k):
#     n = len(nums)
#     for i in range(n):
#         total = nums[i]
#         for j in range(i+1, n):
#             total += nums[j]
#
#             if total % k == 0:
#                 return True
#     return False

#Time: O(n^2) - checking all possible subarrays     Space: O(1)

#why it's slow
#checking all subarrays, recalculating sum again
#nested loops

#optimized idea
#keep running prefix sum
#calculate remainder = prefix_sum%k
#store remainder in remainder_map
#if remainder is seen again check size >=2 -> return True Else false

#optimized code
def continuous_subarray(nums,k):
    n = len(nums)
    remainder_map = {0:-1}
    prefix_sum = 0
    for i in range(n):
        prefix_sum += nums[i]
        remainder = prefix_sum % k

        if remainder in remainder_map:
            if i-remainder_map[remainder] >= 2:
                return True
        else:
            remainder_map[remainder] = i
    return False

nums = [12,4,7,10,9]
print(continuous_subarray(nums, 4))

#Time: O(n)-single loop through array     Space: O(n)- hashmap stores remainders

