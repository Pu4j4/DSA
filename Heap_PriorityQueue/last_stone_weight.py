#brute force
# def last_stone_weight(stones):
#     while len(stones) > 1:
#         stones.sort()
#         y = stones.pop()
#         x = stones.pop()
#         if y != x:
#             stones.append(y-x)
#     return stones[0]  if stones else 0


#optimized
import heapq
def last_stone_weight(stones):
    heap = [-s for s in stones]
    heapq.heapify(heap)

    while len(heap) > 1:
        y = -heapq.heappop(heap)
        x = -heapq.heappop(heap)

        if y != x:
            heapq.heappush(heap, -(y - x))

    return -heap[0] if heap else 0


