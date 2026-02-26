#brute force
def contains_dup(nums,k):
    n = len(nums)
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] and abs(i-j) <= k:
                print(abs(i-j))
                return True
    return False




nums = [1,22,4,19,22,7]
# nums = [1,2,3,4,2]
print(contains_dup(nums,4))
