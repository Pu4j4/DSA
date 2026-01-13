#Brute force
# def remove_element(nums,val):
#     res = []
#     for x in nums:
#         if val != x:
#             res.append(x)
#     nums[:] = res
#     return len(res)
#
# print(remove_element([1,3,7,2,9],7))

#Optimized
def remove_element(nums, val):
    k = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[k] = nums[i]
            k += 1
    return k
print(remove_element([1,3,7,2,9,13,20],7))
