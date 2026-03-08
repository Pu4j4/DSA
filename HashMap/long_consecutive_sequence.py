#brute force
def longestConsecutive(nums) :
    if not nums:
        return 0
    nums.sort()
    max_len = 1
    curr_len = 1

    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            if nums[i] == nums[i - 1] + 1:
                curr_len += 1
            else:
                curr_len = 1
            max_len = max(max_len, curr_len)
    return max_len



# optimized
def longestConsecutive(nums):
    max_len = 0
    num_set = set(nums)
    for num in num_set:
        if (num - 1) not in num_set:
            curr_len = 1
            while (num + curr_len) in num_set:
                curr_len += 1
            max_len = max(max_len, curr_len)
    return max_len



