#brute force
def combinationSum2(candidates, target):
    from itertools import combinations
    res = set()

    n = len(candidates)
    for r in range(1, n + 1):
        for comb in combinations(candidates, r):
            if sum(comb) == target:
                res.add(tuple(sorted(comb)))

    return list(res)

