#Problem: Product of array except self  (https://leetcode.com/problems/product-of-array-except-self/description/)

#Problem statement:
#Given an integer array nums, return an array answer such that answer[i] is equal to the
# product of all the elements of nums except nums[i]

#brute force code
#for every index:
#loop entire array
#check i == j continue or skip
#multiply all elements except self

#Brute force code
def  product_self(nums):
    n = len(nums)
    res = [1] * n
    for i in range(n):
        product = 1
        for j in range(n):
            if j == i:
                continue
            product *= nums[j]
        res[i] = product
    return res

#Time: O(n^2) - nested loops      Space: O(n) - result array or O(1)

#why it's slow
#repeated calculations
#multiplies product for each product

#optimized idea
#instead of recalculating, precompute: prefix and suffix products
#create result array
#store prefix product -> res[i] = product of all elements before i
#store suffix product -> res[i] *= product of all elements after i

#optimized code
def product_self(nums):
    n = len(nums)
    res = [1] * n
    prefix = 1
    for i in range(n):
        res[i] = prefix
        prefix *= nums[i]

    suffix = 1
    for i in range(n-1,-1,-1):
        res[i] *= suffix
        suffix *= nums[i]

    return res

nums = [1,2,4,6]
print(product_self(nums))

#Time: O(n) - one pass for prefix and one pass for suffix   Space: O(n) - result array or O(1)