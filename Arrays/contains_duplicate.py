#brute force
# def contain_duplicate(nums):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] == nums[j]:
#                 return True
#     return False
#
# print(contain_duplicate([1,3,4,2,1,2]))

#optimized (using hashset())
def contains_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

print(contains_duplicate([1,3,4,2]))