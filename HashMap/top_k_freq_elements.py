# Problem: Top k frequent elements (https://leetcode.com/problems/top-k-frequent-elements/description/)

# Problem statement:
# Given an integer array nums and an integer k, return the top k most frequent elements.
# you may return the answer in any order

# Pattern: Hashmap(frequency counting) and Heap pattern (priority queue)

#brute force idea
#traverse through nums - count the frequency of elements using hashmap
#converts to list, sort the list by frequency
#return top k frequent elements

#brute force
import heapq
def top_k(nums,k):
    freq = {}
    #counting frequency
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    #sorting by frequency(this converts freq.items to list then sort by frequency)
    sorted_items = sorted(freq.items(), key=lambda x:x[1], reverse=True)

    #top k elements
    return [sorted_items[i][0] for i in range(k)]

#Time: O(n log n) - sorting takes n log n     Space: O(n) - hashmap stores elements

#why it's slow
# sorting takes n log n times - need better

#optimized idea
#count frequency of all elements using hashmap
#use min-heap ->stores frequency , num
#heap automatically sorts by smallest frequency
#remove the elements if len(heap) > k
#so heap stores only k most frequent elements and return the elements


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


#Time: O(n log k) - heap insertion/removal takes log k times   Space: O(n) - hashmap and heap stores elements