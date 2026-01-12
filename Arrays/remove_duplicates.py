#Brute force
# def remove_duplicates(nums):
#     s = sorted(set(nums))
#     nums[:len(nums)] = s
#     return len(s)

# print(remove_duplicates([1,3,5,5,6,7,7,8,8]))

#Optimized
def remove_duplicates(nums):
    i = 0
    for j in range(1, len(nums)):
        if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
    return i + 1
print(remove_duplicates([1,3,5,5,6,7,7]))