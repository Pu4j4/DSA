# brute force
def search_range(nums,target):
    first = -1
    last = -1
    for i in range(len(nums)):
        if nums[i] == target:
            if first == -1:
                first = i
            last = i
    return [first, last]


#optimized
def search_range(nums,target):
    def find_first():
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                ans = mid
                right = mid - 1
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return ans

    def find_last():
        left = 0
        right = len(nums)-1
        ans = -1
        while left<=right:
            mid = (left+right) // 2
            if nums[mid] == target:
                ans = mid
                left = mid+1
            elif nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return ans
    return [find_first(), find_last()]
nums = [1,2,2,3,5,5]
print(search_range(nums, 2))
