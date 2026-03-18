#Problem: Search in 2D Matrix (https://leetcode.com/problems/search-a-2d-matrix/description/)

#Problem statement:
#Given an m*n integer matrix with the following properties:
#1.each row is sorted in ascending order
#2.the first element of each row is greater than the last element of the previous row
#given an integer target, return: True if target exists in the matrix false otherwise

#Pattern: Binary search

#brute force idea
#check every element in matrix
#if any element equals target -> return True
#otherwise return false

#brute force code
def search_matrix( matrix, target):
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False
            #or
def search_matrix(matrix, target):
    rows = len(matrix)
    cols = len(matrix[0])
    for i in range(rows):
        for j in range(cols):
            if matrix[i][j] == target:
                return True
    return False

#Time: O(m*n) - checks every element in matrix    Space:O(1) - no extra space

#why it's slow
#checks every element
#require O(log (m*n))

#optimized idea
#Since matrix is sorted
#instead of checking everything, we use binary search
#key idea: matrix behaves like sorted array

#optimized
def search_matrix(matrix, target):
    rows, cols = len(matrix), len(matrix[0])
    left, right = 0, rows * cols - 1

    while left <= right:
        mid = (left + right) // 2
        r = mid // cols
        c = mid % cols

        if matrix[r][c] == target:
            return True
        elif matrix[r][c] < target:
            left = mid + 1
        else:
            right = mid - 1

    return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
print(search_matrix(matrix, 11))
#Time: O(log (m*n)) - Binary search halves search space every step    Space: O(1) - only pointers used
