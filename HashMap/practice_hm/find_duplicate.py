def find_duplicate(nums):
    seen = {}
    result = []
    for num in nums:
        seen[num] = seen.get(num,0)+1

    for key in seen:
        if seen[key] > 1:
            result.append(key)
    return result
print(find_duplicate([1,2,2,3,4,7,8,9,9]))