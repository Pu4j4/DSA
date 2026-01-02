# Brute force
# def rev_str(s):
#     s[:] = s[::-1]
#     print(s)
# print(rev_str(["h","e","l","l","o"]))

# optimized
# def rev_str(s):
#     n= len(s)
#     left = 0
#     right = n-1
#     while left<right:
#         s[left],s[right] = s[right], s[left]
#         left+=1
#         right-=1
#     return s
# print(rev_str(["h","e","l","l","o"]))