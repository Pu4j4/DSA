#brute force
def top_k_frequent(nums, k):
    freq = {}
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    arr = list(freq.items())
    arr.sort(key=lambda x: x[1], reverse=True)

    return [arr[i][0] for i in range(k)]

