#brute force
def valid_anagram(s,t):
    if len(s) != len(t):
        return False
    return sorted(s) == sorted(t)

print(valid_anagram("anagram","nagaram"))