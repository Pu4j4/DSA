#brute force
from itertools import permutations
def permuteUnique(nums):
    res = set()
    for p in permutations(nums):
        res.add(p)
    return list(map(list, res))

