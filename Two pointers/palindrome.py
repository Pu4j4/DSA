#Brute force-1
# def is_palin(s):
#     clean = ""
#     for ch in s:
#         if ch.isalnum():
#             clean += ch.lower()
#     rev = ""
#     for ch in clean:
#         rev = ch + rev
#     return clean == rev



#Brute force-2
# def is_palin(s):
#     cleaned = "".join([ch.lower() for ch in s if ch.isalnum()])
#     reversed_s = cleaned[::-1]
#     return  cleaned == reversed_s
# print(is_palin("bhanahb"))

#Optimized
def is_palin(s):
    left = 0
    right = len(s)-1
    while left<right:
        while left<right and not s[left].isalnum():
            left+=1
        while left<right and not s[right].isalnum():
            right-=1
        if s[left].lower() != s[right].lower():
           return False
        left+=1
        right-=1
    return True
print(is_palin("bhanahb"))