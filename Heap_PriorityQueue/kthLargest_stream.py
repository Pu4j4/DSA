#brute force
# def __init__(self, k, nums):
#     self.k = k
#     self.nums = nums
#
#
# def add(self, val):
#     self.nums.append(val)
#     self.nums.sort(reverse=True)
#     return self.nums[self.k - 1]


#optimized
import heapq
def __init__(self, k, nums):
    self.k = k
    self.heap = nums
    heapq.heapify(self.heap)

    while len(self.heap) > k:
        heapq.heappop(self.heap)


def add(self, val: int) -> int:
    heapq.heappush(self.heap, val)

    if len(self.heap) > self.k:
        heapq.heappop(self.heap)

    return self.heap[0]


