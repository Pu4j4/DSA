#Problem: Longest repeating character replacement  (https://leetcode.com/problems/longest-repeating-character-replacement/description/)

#Problem statement:
#Given string s, consisting only uppercase letters and integer k
#replace at most k characters in the string with any other uppercase letter
#return the length of longest substring that contains same letter after replacement

#Pattern: Sliding window+hashmap(frequency counting)

#brute force idea
#traverse through string, count frequency using hashmap, find most frequent character
#if (substring_length - max_frequency) ->we'll get how many characters to replace, valid if <=k else invalid
#track max_len

#brute force code
def char_replace(s,k):
    max_len = 0
    n = len(s)
    for i in range(n):
        freq = {}
        max_freq = 0
        for j in range(i,n):
            freq[s[j]] = freq.get(s[j],0)+1
            max_freq = max(max_freq, freq[s[j]])

            if (j-i+1) - max_freq <= k:
                max_len = max(max_len, (j-i+1))
    return max_len

#Time: O(n^2) - nested loops     Space: O(1) - freq_map stores max size 26

#why it's slow
#repeating checking all substrings, nested loops
#slow for large input

#Optimized idea
#create hashmap to store frequency of elements
#use two pointers left at 0 and right to expand the window
#track window_size - max_frequency and shrink window from if >k, and update freq_map
#track max_len

#optimized code
def char_replace(s,k):
    max_len = 0
    max_freq = 0
    freq = {}
    left = 0
    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right],0)+1
        max_freq = max(max_freq, freq[s[right]])

        while (right-left+1) - max_freq > k:
            freq[s[left]] -= 1
            left+=1
        max_len = max(max_len, right-left+1)
    return max_len

#Time: O(n) - single pass char added and removed once    Space: O(1) - freq_map store max size 26