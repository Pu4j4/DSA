# Problem: First Unique character in a string  (https://leetcode.com/problems/first-unique-character-in-a-string/description/)

# Problem statement:
# Given a string s, find the first non-repeating character in it and return its index.
# if it does not return -1

#pattern: Hashmap, frequency counting

#brute force idea
#check every character: compare with other characters, keep count = 0
#count how many times it appears
#if count == 1: return its index else -1

#brute force
def first_unique(s):
    n = len(s)
    for i in range(n):
        count = 0
        for j in range(n):
            if s[i] == s[j]:
                count += 1
        if count == 1:
            return i
    return -1
s = "bhanu"
print(first_unique(s))

#Time:  O(n^2) - nested loops   Space: O(1)


#why it's slow
#checks each and every character
#repeated comparisons


#optimized idea
#instead of checking every character, we use hashmap to store the frequency of each char
#traverse the string once and store the frequency
#traverse again with index i from 0 len(s)
#check if frequency is 1,return its index, if not -1

#optimized code
def first_unique(s):
    n = len(s)
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch,0) + 1

    for i in range(n):
        if freq[s[i]] == 1:
            return i
    return -1

s = "haha"
print(first_unique(s))

#Time: O(n)-two pass over string,O(1) lookup   space: O(1)-hashmap store max 26 characters