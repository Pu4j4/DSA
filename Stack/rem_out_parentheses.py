#brute force
# def rem_par(s):
#     result = ""
#     balance = 0
#     start = 0
#     for i in range(len(s)):
#         if s[i] == '(' :
#             balance+=1
#         else:
#             balance-=1
#         if balance == 0:
#             result += s[start+1:i]
#             start = i+1
#     return result
# print(rem_par("(())"))



#optimized
def rem_par(s):
    depth = 0
    result = []
    for ch in s:
        if ch == '(':
            if depth>0:
                result.append(ch)
            depth+=1
        else:
            depth-=1
            if depth>0:
                result.append(ch)
    return "".join(result)

print(rem_par("((()))(())"))