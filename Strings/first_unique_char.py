#brute force
def first_unique(s):
    n = len(s)
    for i in range(n):
        count = 0
        for j in range(n):
            if s[i] == s[j]:
                count += 1
        if count == 1:
            return i
    return -1
s = "bhanu"
print(first_unique(s))

