# Problem: Longest substring without repeating characters (https://leetcode.com/problems/longest-substring-without-repeating-characters/description/)

# Problem statement:
# Given a string s, find the length of longest substring without repeating characters. return max length

# Pattern: Sliding window + Hashset

#brute force idea
#generate all substrings:
#for each substring: check if characters repeat,
# if no repeat -> update max length

#brute force code
def long_substring_no_repeating(s):
    n = len(s)
    max_len = 0
    for i in range(n):
        seen = set()
        for j in range(n):
            if s[j] in seen:
                break
            seen.add(s[j])
            max_len = max(max_len, j-i+1)
    return max_len

#Time: O(n^2) - nested loops    Space: O(n) - set store substring characters

#why it's slow
#it checks same characters multiple times
#nested loops
#slow for large input

#optimized idea
#use sliding window:
#instead of restarting, move window smartly
#use two pointers: left->start of window, right->end of window(moves to end)
#use set to track characters
#if no duplicate -> expand window
#if duplicate -> shrink window from left and remove duplicate
#keep updating max length

#optimized code
def long_substring_no_repeating(s):
    left = 0
    max_len = 0
    char_set = set()
    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left+=1
        char_set.add(s[right])
        max_len = max(max_len, right-left+1)
    return max_len

s = "abcab"
print(long_substring_no_repeating(s))

#Time: O(n) - each char added and removed once   Space: O(n) - set stores unique characters