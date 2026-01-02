#Brute force
# def four_sum(nums,target):
#     nums.sort()
#     n = len(nums)
#     res = set()
#     for  i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 for l in range(k+1,n):
#                     if nums[i]+nums[j]+nums[k]+nums[l]==target:
#                         res.add((nums[i],nums[j],nums[k],nums[l]))
#     return [list(t) for t in res]

#optimized
# def four_sum(nums,target):
#     nums.sort()
#     n = len(nums)
#     res = []
#     for i in range(n-3):
#         if i>0 and nums[i] == nums[i-1]:
#             continue
#         for j in range(i+1,n-2):
#             if j>i+1 and nums[j] == nums[j-1]:
#                 continue
#             left, right = j+1,n-1
#             while left<right:
#                 s = nums[i]+nums[j]+nums[left]+nums[right]
#                 if s<target:
#                     left+=1
#                 elif s>target:
#                     right-=1
#                 else:
#                     res.append([nums[i],nums[j],nums[left],nums[right]])
#                     left+=1
#                     right-=1
#                     while left<right and nums[left] == nums[left+1]:
#                         left+=1
#                     while left<right and nums[right] == nums[right-1]:
#                         right-=1
#     return res
#

print(four_sum([1,0,-1,0,-2,2],0))