#brute force
def combinationSum(self, candidates, target):
    result = set()

    def backtrack(path, curr_sum):
        if curr_sum == target:
            result.add(tuple(sorted(path)))
            return
        if curr_sum > target:
            return

        for num in candidates:
            path.append(num)
            backtrack(path, curr_sum + num)
            path.pop()

    backtrack([], 0)
    return list(result)

#optimized
def combinationSum(self, candidates, target):
    result = []

    def backtrack(start, path, remaining):
        if remaining == 0:
            result.append(path[:])
            return

        if remaining < 0:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])  # choose
            backtrack(i, path, remaining - candidates[i])  # reuse allowed
            path.pop()  # un-choose

    backtrack(0, [], target)
    return result
