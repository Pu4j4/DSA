#Problem: Maximum Average Subarray I  (https://leetcode.com/problems/maximum-average-subarray-i/description/)

#Problem statement:
#Given an integer nums and integer k, find maximum average of any contiguous subarray of length k

#Pattern: Sliding window

#brute force idea
#generate all subarrays of length k, calculate if current sum
#calculate current avg of each sum and keep track of maximum average

#brute force code
def find_max_avg(nums,k):
    max_avg = float('-inf')
    for i in range(len(nums)-k+1):
        curr_sum = 0
        for j in range(i, i+k):
            curr_sum+=nums[j]
        curr_avg = curr_sum / k
        print(curr_sum,curr_avg)
        max_avg = max(max_avg,curr_avg)
    return max_avg

#Time: O(n*k) - nested loops     Space: O(1) - some variables used

#why it's slow
#recalculating sum again and again for every subarray
#using nested loops - O(n^2)
#slow for large input

#optimized idea
#calculate sum of first k elements
#Use sliding window: remove left element and add right element
#track and update maximum average

# optimized code
def find_max_avg(nums,k):
    window_sum = sum(nums[:k])
    max_sum = window_sum
    for i in range(k, len(nums)):
        window_sum = window_sum - nums[i-k] + nums[i]
        max_sum = max(max_sum, window_sum)
    return max_sum / k

print(find_max_avg([1,2,-10,29,12,8,4],4))

#Time: O(n) - each element added and removed once   Space: O(1) - some variables are used