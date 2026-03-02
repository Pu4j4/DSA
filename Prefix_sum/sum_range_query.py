#brute force
class NumArray:

    def __init__(self, nums):
        self.nums = nums

    def sumRange(self, left, right):

        total = 0

        for i in range(left, right+1):
            total += self.nums[i]

        return total


#optimized
class NumArray:

    def __init__(self, nums):

        self.prefix = [0]

        for num in nums:
            self.prefix.append(self.prefix[-1] + num)

    def sumRange(self, left, right):

        return self.prefix[right+1] - self.prefix[left]