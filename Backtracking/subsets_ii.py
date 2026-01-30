#brute force
def subsetsWithDup(self, nums):
    result = set()

    def backtrack(start, path):
        result.add(tuple(path))

        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    nums.sort()
    backtrack(0, [])
    return list(result)