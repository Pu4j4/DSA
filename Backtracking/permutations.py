#brute force
def permute(self, nums):
    res = []
    for p in permutations(nums):
        res.append(list(p))
    return res


#Optimized
def permute(self, nums):
    res = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            res.append(path[:])
            return

        for i in range(len(nums)):
            if used[i]:
                continue

            used[i] = True
            path.append(nums[i])
            backtrack(path)
            path.pop()
            used[i] = False

    backtrack([])
    return res
from itertools import permutations

