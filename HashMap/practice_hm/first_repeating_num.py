def first_repeat(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return -1
print(first_repeat([1,3,5,3,7,5,9]))