#brute force
from itertools import permutations
def permuteUnique(nums):
    res = set()
    for p in permutations(nums):
        res.add(p)
    return list(map(list, res))


#Optimized
def permuteUnique(self, nums):
    nums.sort()
    res = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                continue

            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return res



