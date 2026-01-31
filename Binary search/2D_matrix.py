#brute force
def searchMatrix(self, matrix, target):
    for row in matrix:
        for val in row:
            if val == target:
                return True
    return False

