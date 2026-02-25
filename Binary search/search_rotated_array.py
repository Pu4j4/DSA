#brute force
def search(nums, target):
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

#optimized
def search(nums, target):
    left, right = 0, len(nums) - 1

    while left <= right:
        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        # left half sorted
        if nums[left] <= nums[mid]:
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # right half sorted
        # if nums[mid] <= nums[right]:
        else:
            if nums[mid] <= target < nums[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1

nums = [4,5,6,1,2,3]
print(search(nums, 2))
