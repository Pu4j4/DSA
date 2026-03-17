#Problem: Container with most water (https://leetcode.com/problems/container-with-most-water/description/)

#Problem statement:
#Given an array of integers height of size n
#each element represents the vertical line at index i
#find two lines such that together form a container hold max amount of water

#Pattern: Two pointers

#brute force idea
#checking all possible pairs
#traverse through nums i from 0 to n-1, traverse again j from i+1 to n-1
#for each element : calculate width = j-i ,height = min(height[i], height[j]), max_area= width*height
#find max_area of water

#brute force code
def maxarea(height):
    n = len(height)
    max_area = 0
    for i in range(n):
        for j in range(i+1,n):
            width = j - i
            h = min(height[i],height[j])
            area = width*h
            max_area = max(max_area,area)
    return max_area

#Time: O(n^2) - nested loops   Space: O(1) - no extra space used

#why it's slow
#repeated calculations , nested loops
#slow for large input

#optimized idea
#use two pointers: area = (right-left) * min(height[left],height[right])
#left = 0 and right = len(height)-1
#calculate the area
#move pointers ,repeat until left<right
#calculate max_area and return

#optimized code
def maxarea(height):
    left = 0
    right = len(height)-1
    while left<right:
        area = (right-left) * min(height[left],height[right])
        max_area = max(max_area,area)
        if height[left]<height[right]:
            left+=1
        else:
            right-=1
    return max_area

#Time: O(n) - single pass through each element    Space: O(1) - some variables used