# Problem: Reverse string  (https://leetcode.com/problems/reverse-string/description/)

#Problem statement:
#given a character array string s, reverse string in place

#Pattern: Two pointers

#brute force idea
#create a new array
#traverse original array from end to start
#add characters to new array
#traverse again , copy characters from new array into original array

#brute force
def rev_str(s):
    n = len(s)
    reversed_s = []
    for i in range(n-1,-1,-1):
       reversed_s.append(s[i])
    for i in range(n):
        s[i] = reversed_s[i]
    return s

s = ["b","h","a","n","u"]
print(rev_str(s))

#Time: O(n) - traverse entire array one   Space:O(n) - extra array created

#why it's slow
#extra space used - need to optimize space ->O(1)


#optimized idea
#Use two pointers: left= 0, right = len(s)-1
#swap characters and move pointers inward
#return

#optimized
def rev_str(s):
    n = len(s)
    left, right = 0, n-1
    while left<right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return s
s = ["m","i","k","e"]
print(rev_str(s))

#Time: O(n) - swapped each character once    Space: O(1) - in_place reverse