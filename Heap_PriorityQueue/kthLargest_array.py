#Brute force
# def find_kth_largest(nums, k):
#     nums.sort(reverse=True)
#     return nums[k - 1]

#Optimized
import heapq
def find_kth_largest(nums, k):
    heap = []

    for num in nums:
        heapq.heappush(heap, num)
        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]