# Problem: Intersection of two arrays  (https://leetcode.com/problems/intersection-of-two-arrays/description/)

# Problem statement:
# Given Two integer arrays nums1 and nums2, return an array of their intersection.
# each element in the result must be unique, and you may return the result in any order

#Pattern: Hashset

#brute force idea
#compare every element in nums1 with every element in nums2
#if common elements present store them in result, if element not in result
#return the result array

#brute force code
def intersection_two_array(nums1, nums2):
    result = []
    for num in nums1:
        if num in nums2 and num not in result:
            result.append(num)
    return result


#Time: O(nxm) -checks every element in nums1 and nums2   Space: O(k)-storing intersection result

#why it's slow
#checks each and every character present in nums1 and nums2
#slow for large input


#optimized idea:
#instead of checking every element in nums2, store nums2 elements in hashset for fast lookup
#check if num in nums1 in set2, add num to result set(for unique elements) and convert set to list,return

#optimized code
def intersection_two_array(nums1,nums2):
    set2 = set(nums2)
    result = set()
    for num in nums1:
        if num in set2:
            result.add(num)
    return list(result)

nums1 = [1,2,3,4,2]
nums2 = [2,3,2]
print(intersection_two_array(nums1,nums2))

#Time: O(m+n) - set creation O(m) and lookup O(n)   Space: O(m+k) - set stores nums2 and result
