#brute force
from itertools import permutations

def permute(self, nums):
    res = []
    for p in permutations(nums):
        res.append(list(p))
    return res
