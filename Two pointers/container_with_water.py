#brute force
def container(height):
    n = len(height)
    max_area = 0
    for i in range(n):
        for j in range(i+1, n):
            width = j - i
            h = min(height[i], height[j])
            area = width * h
            max_area = max(max_area, area)
    return max_area
height = [1,8,6,2,5,4,8,3,7]
print(container(height))

#optimized
def container(height):
    max_area = 0
    left = 0
    right = len(height)
    while left<right:
         area = (right - left) * min(height[left], height[right])
         max_area = max(max_area, area)

         if height[left] < height[right]:
             left += 1
         else:
             right -= 1
    return max_area
