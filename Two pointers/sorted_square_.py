#Brute force
def sort_squares(nums):
    squared = []
    for x in nums:
        squared.append(x*x)
    return sorted(squared)
print(sort_squares([-4,-1,0,2,3]))