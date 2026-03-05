# Problem: Valid Anagram (https://leetcode.com/problems/valid-anagram/description/)

# Problem Statement:
# Given two strings s and t, return True if t is an anagram of s, otherwise return False
# Anagram: Two strings are anagrams if they contain same characters with same frequency,but possibly in different order

# Pattern: Hashmap, frequency counting

#brute force idea:
# if lengths of two strings are not equal, return False
# sort the two strings and check if they're equal return True else False

#brute force code
def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(valid_anagram("anagram","nagaram"))

#Time: O(n log n) - sorting  space: O(1)

#why it's slow
#because sorting takes n*log n times

#optimized idea
#instead of sorting
#we need frequency counting, we can optimize using hashmap
# increase the frequency with s in hashmap
# decrease the frequency with t in hashmap
# if all counts is zero return True they're anagrams
# if not return False

#optimized code
def is_anagram(s,t):
    if len(s)!=len(t):
        return False
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0)+1

    for ch in t:
        if ch not in freq:
            return False
        freq[ch]-=1
        if freq[ch]<0:
            return False
    return True

#Time: O(n) - single loop,O(1) hashmap lookup   Space: O(1) - stores max 26 characters

