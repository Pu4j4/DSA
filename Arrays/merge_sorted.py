# problem: Merge sorted array (https://leetcode.com/problems/merge-sorted-array/description/)

# Problem statement:
# Given two sorted arrays nums1 and nums2, integers m(represents actual elements in nums1) and n(elements in nums2)
# nums1 has size m+n
# first m elements are valid,last n elements are 0
#merge nums2 into nums1 such that nums1 becomes one sorted array - in-place

#Pattern - Two pointers(three pointer(reverse direction) - extra pointer to place position)

#brute force idea
#traverse nums1 and add elements from m+i of nums2
#sort the nums1

#brute force
def merge_sorted(nums1,m,nums2,n):
    for i in range(n):
        nums1[m+i] = nums2[i]
    nums1.sort()
    return nums1

#Time: O((m+n) log (m+n)) - sorting n=(m+n)-n log n    Space: O(1)

#why it's slow
#sorting takes - (m+n) log (m+n) - optimize to O(m+n)

#optimized idea
#compare largest elements from both arrays
#place then at the end of array
#move backwards

#otimized
def merge_sorted(nums1,m,nums2,n):
    i = m-1
    j = n-1
    k = m+n-1
    while j>=0:
        if i>=0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i-=1
        else:
            nums1[k] = nums2[j]
            j-=1
        k-=1
    return nums1

nums1 = [1,3,4,0,0,0]
nums2 = [2,5,9]
m = 3
n = 3
print(merge_sorted(nums1,m,nums2,n))

#Time: O(m+n)- each element processed once     Space: O(1) - in-place