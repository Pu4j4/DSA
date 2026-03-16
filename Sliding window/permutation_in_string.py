#Problem: Permutation in string  (https://leetcode.com/problems/permutation-in-string/description/)

#Problem statement:
#Given two strings s1 and s2, return True if s2 contains a permutation of s1 otherwise, return False

#Pattern: Sliding window + frequency count

#brute force idea
#Generate all substring of s2 of len(s2)
#sort the substring and compare with sorted s1
#if any matches return True, else False

#brute force code
def check_perms(s1,s2):
    k = len(s1)
    for i in range(len(s2)-k+1):
        substring = s2[i:i+k]
        if sorted(s1) == sorted(substring):
            return True
    return False

#Time: O(n*k log k) - sorting k elements takes k log k    Space: O(k) - stores substring

#Why its slow
#checks every substring
#sorting takes k log k

#Optimized idea
#checks lengths - if len(s1) > len(s2) ->return False
#initialize counts for s1 and s2 for 26 chars
#count frequency of s1
#Use two pointers -> left at 0 , right scanning s2
#count frequency of s2(expand window)-> window size > len(s1) -> shrink from left
#compares if counts return True if equal, otherwise false


#Optimized code
def check_perms(s1, s2):
    if len(s1) > len(s2):
        return False
    count1 = [0]*26
    count2 = [0]*26

    for ch in s1:
        count1[ord(ch)-ord('a')] += 1

    left = 0
    for right in range(len(s2)):
        count2[ord(s2[right])-ord('a')] += 1

        if right-left+1 > len(s1):
            count2[ord(s2[left])-ord('a')] -= 1
            left += 1
        if count1 == count2:
            return True
    return False

s1 = 'bg'
s2 = 'bgcolor'
print(check_perms(s1,s2))

#Time: O(n) - each character is added and removed once   Space: O(1)- freq array, max 26 array
