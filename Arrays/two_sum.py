#brute force
# def two_sum(nums, target):
#     n = len(nums)
#     for i in range(n):
#         for j in range(i+1,n):
#             if nums[i] + nums[j] == target:
#                return [i, j]
#     return []
#
# print(two_sum([2,5,1,0,6],7))


#Optimized (using hashmap)
def two_sum(nums,target):
    seen = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in seen:
            return [seen[diff],i]
        seen[num] = i
    return []

print(two_sum([2,1,5,0,6],7))