#Brute force
# def rev_vow(s):
#     vowels = set("aeiouAEIOU")
#     vowel_list = []
#     for ch in s:
#         if ch in vowels:
#             vowel_list.append(ch)
#     vowel_list.reverse()
#     result = []
#     idx = 0
#     for ch in s:
#         if ch in vowels:
#             result.append(vowel_list[idx])
#             idx+=1
#         else:
#             result.append(ch)
#     return "".join(result)
#
# print(rev_vow("hello"))


# Optimized
def rev_vow(s):
    s = list(s)
    vowels = set("aeiouAEIOU")
    left = 0
    right = len(s)-1
    while left<right:
        if s[left] not in vowels:
            left+=1
        elif s[right] not in vowels:
            right-=1
        else:
            s[left], s[right] = s[right], s[left]
            left+=1
            right-=1
    return "".join(s)
print(rev_vow("BhAnU PoOja"))
