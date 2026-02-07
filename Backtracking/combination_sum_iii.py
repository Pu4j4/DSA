#brute force
def combinationSum3(self, k, n):
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    res = []

    def generate(index, path):
        # when we reach the end
        if index == len(nums):
            if len(path) == k and sum(path) == n:
                res.append(path[:])
            return

        # choice 1: take nums[index]
        path.append(nums[index])
        generate(index + 1, path)
        path.pop()

        # choice 2: do NOT take nums[index]
        generate(index + 1, path)

    generate(0, [])
    return res


#optimized
def combinationSum3(self, k, n):
    res = []

    def backtrack(start, remaining_sum, remaining_k, path):
        if remaining_sum == 0 and remaining_k == 0:
            res.append(path[:])
            return

        if remaining_sum < 0 or remaining_k < 0:
            return

        for i in range(start, 10):
            path.append(i)
            backtrack(i + 1, remaining_sum - i, remaining_k - 1, path)
            path.pop()

    backtrack(1, n, k, [])
    return res
