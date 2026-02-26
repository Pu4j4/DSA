#brute force
def search_insert(nums,target):
    for i in range(len(nums)):
        if nums[i] >= target:
            return i

nums = [1,3,4,7]
print(search_insert(nums,2))

