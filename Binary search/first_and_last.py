# brute force
def search_range(nums,target):
    first = -1
    last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]



nums = [1,2,2,3,5,5]
print(search_range(nums, 2))
