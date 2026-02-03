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