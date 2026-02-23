#brute force
# def max_sliding_window(nums, k):
#     n = len(nums)
#     result = []
#     for i in range(n - k + 1):
#         max_val = nums[i]
#         for j in range(i, i + k):
#             max_val = max(max_val, nums[j])
#         result.append(max_val)
#     return result


#optimized
from collections import deque
def max_sliding_window(nums, k):
    dq = deque()
    result = []
    for i in range(len(nums)):
        if dq and dq[0] <= i - k:
            dq.popleft()
        while dq and nums[dq[-1]] < nums[i]:
            dq.pop()
        dq.append(i)
        if i >= k - 1:
            result.append(nums[dq[0]])
    return result




