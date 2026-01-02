#Brute force
# def three_sum(nums):
#     n = len(nums)
#     result = []
#     seen = set()
#     for i in range(n):
#         for j in range(i+1,n):
#             for k in range(j+1,n):
#                 if nums[i]+nums[j]+nums[k]==0:
#                     trip = tuple(sorted([nums[i],nums[j],nums[k]]))
#                     if trip not in seen:
#                         seen.add(trip)
#                         result.append(list[trip])
#     return result

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
