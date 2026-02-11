#brute force
def rev_str(s):
    n = len(s)
    reversed_s = ['']*n
    for i in range(n):
        reversed_s[i] = s[n-1-i]
    for i in range(n):
        s[i] = reversed_s[i]
    return s
s = ["b","h","a","n","u"]
print(rev_str(s))



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