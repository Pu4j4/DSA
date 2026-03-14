# Problem: Maximum Number of Vowels in a Substring of Given Length (https://leetcode.com/problems/maximum-number-of-vowels-in-a-substring-of-given-length/description/)

#Problem statement:
#Given a string s and integer k, return the maximum no.of vowels in any substring of length k

#Pattern: Sliding window

#brute force idea
#Generate all substrings
#for each substring, count vowels
#update max_count

#brute force code
def max_vowels(s,k):
    n = len(s)
    vowels = 'aeiou'
    max_count = 0
    for i in range(n-k+1):
        count = 0
        for j in range(i, i+k):
            if s[j] in vowels:
                count+=1
        max_count = max(max_count, count)
    return max_count

#Time: O(n^2) - nested loops    Space: O(1) - only counters used

#why it's slow:
#inner loop runs n times, outer loop runs n times - O(n^2)
#slow for large input

#optimized idea
#instead of recounting again and again
#use sliding window to reuse prev count
#when window slides: if window size >k, remove left char, update count and add right char and update count
#update overall max_count

#optimized code
def max_vowels(s,k):
    vowels = {'a','e','i','o','u'}
    count = 0
    for i in range(k):
        if s[i] in vowels:
            count += 1
    max_count = count
    for i in range(k,len(s)):
        if s[i-k] in vowels:
            count-=1
        if s[i] in vowels:
            count+=1
        max_count = max(max_count,count)
    return max_count


s = "abcieack"
print(max_vowels(s,4))

#Time: O(n) - each element added once and removed once    Space: O(1) - some variables used
