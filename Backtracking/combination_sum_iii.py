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

