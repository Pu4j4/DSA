#brute force
def contains_dup(nums,k):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] and abs(i-j) <= k:
                print(abs(i-j))
                return True
    return False


#optimized
def contains_dup(nums, k):
    window = set()
    for i in range(len(nums)):
        if nums[i] in window:
            return True
        window.add(nums[i])
        if len(window) >k:
            window.remove(nums[i-k])
    return False
#or
def contains_dup(nums,k):
    n = len(nums)
    index_map = {}
    for i, num in enumerate(nums):
        if num in index_map and i-index_map[num] <=k:
            return True
        index_map[num] = i
    return False

nums = [1,22,4,19,22,7]
# nums = [1,2,3,4,2]
print(contains_dup(nums,4))
