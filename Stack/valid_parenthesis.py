# #Brute force
# def isvalid(s):
#     prev_len = -1
#     while prev_len != len(s):
#         prev_len = len(s)
#         s = s.replace("()","").replace("[]","").replace("{}","")
#     return len(s) == 0


#optimized
def isvalid(s):
    stack = []
    match = {')':'(','}':'{',']':'['}
    for ch in s:
        if ch in match.values():
            stack.append(ch)
        else:
            if not stack:
                return False
            top = stack.pop()
            if match[ch]!=top:
                return False
    return len(stack) == 0

print(isvalid("({[]})"))
print(isvalid("()[{}]"))
print(isvalid("()[{]}"))
