#brute force
import heapq
def top_k(nums,k):
    freq = {}
    #counting frequency
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    #sorting by frequency
    sorted_items = sorted(freq.items(), key=lambda x:x[1], reverse=True)

    #top k elements
    result = []
    for i in range(k):
        result.append(sorted_items[i][0])
    return result

#optimized
def top_k(nums,k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num,0)+1
    heap = []
    for num,count in freq.items():
        heapq.heappush(heap,(count,num))
        if len(heap) > k:
            heapq.heappop(heap)
    return [num for count,num in heap]

nums = [1,1,1,2,2,3,3,3]
k = 2
print(top_k(nums, k))
