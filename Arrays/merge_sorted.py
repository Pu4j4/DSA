#brute force
def merge_sorted(nums1,m,nums2,n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort()
    return nums1



nums1 = [1,3,4,0,0,0]
nums2 = [2,5,9]
m = 3
n = 3
print(merge_sorted(nums1,m,nums2,n))
