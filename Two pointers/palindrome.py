# Problem: Valid Palindrome  (https://leetcode.com/problems/valid-palindrome/description/)

#Problem statement:
# Given a string s, determine if it is a palindrome. ignore uppercase and lowercase differences
# non-alphanumeric characters(spaces,commas,symbols) return True if it is palindrome,otherwise False
#A palindrome reads the same forward and backward

#Pattern: Two pointers

#brute force idea
# create a new string ->for each char in s: ->check if char is alphanumeric
# then convert char to lower case and add to new string
# check the string and string reverse are equal, if yes return True, otherwise false

#Brute force-1
def is_palin(s):
    cleaned_s = ""
    for ch in s:
        if ch.isalnum():
            cleaned_s += ch.lower()
    return cleaned_s == cleaned_s[::-1]


#Brute force-2
def is_palin(s):
    cleaned = "".join([ch.lower() for ch in s if ch.isalnum()])
    return  cleaned == cleaned[::-1]
print(is_palin("bhanahb"))

#Time: O(n) - cleaned string O(n),reverse O(n)  Space: O(n) - storing cleaned and reverse string

#why it's slow
#string concatenation creates new string every time ->it makes slow
#[::-1] -> creates extra copy

#optimized idea
#Use two pointers: left at start and right at end
#move left pointer until it points to alphanumeric(ignores non_alphanumeric chars from left to right)
#move right pointer until it points to alphanumeric(ignores non_alphanumeric chars from right to left)
#compare characters at left and right(in lowercase), if mismatch -> return False and move pointers
#if all comparisons pass ->it is a palindrome -> return True

#Optimized
def is_palin(s):
    left = 0
    right = len(s)-1
    while left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower() != s[right].lower():
           return False
        left+=1
        right-=1
    return True
print(is_palin("bhanahb"))

#Time: O(n) - each char visited at most once     Space: O(1)