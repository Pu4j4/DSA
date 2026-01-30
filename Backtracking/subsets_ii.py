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


#Optimized
def subsetsWithDup(self, nums):
    nums.sort()
    result = []

    def backtrack(start, path):
        result.append(path[:])

        for i in range(start, len(nums)):
            if i > start and nums[i] == nums[i - 1]:
                continue

            path.append(nums[i])
            backtrack(i + 1, path)
            path.pop()

    backtrack(0, [])
    return result
