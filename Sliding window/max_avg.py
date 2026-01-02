# def find_max_avg(nums,k):
#     max_avg = float('-inf')
#     for i in range(len(nums)-k+1):
#         curr_sum = 0
#         for j in range(i, i+k):
#             curr_sum+=nums[j]
#         curr_avg = curr_sum / k
#         print(curr_sum,curr_avg)
#         max_avg = max(max_avg,curr_avg)
#     return max_avg
# print(find_max_avg([1,2,-10,29,12,8,4],4))

# optimized
def find_max_avg(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
    return max_sum / k
print(find_max_avg([1,2,-10,29,12,8,4],4))