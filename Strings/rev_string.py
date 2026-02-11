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



