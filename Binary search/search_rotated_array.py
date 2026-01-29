#brute force
def search(self, nums, target):
    for x in nums:
        if x == target:
            return True
    return False