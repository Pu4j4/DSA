
def valid_palin(s):
    def is_palin(left,right):
        while left<right:
            if s[left]!=s[right]:
                return False
            left+=1
            right-=1
        return True
    left, right = 0, len(s)-1
    while left<right:
        if s[left] == s[right]:
            left+=1
            right-=1
        else:
            return is_palin(left+1,right) or is_palin(left, right-1)
    return True
print(valid_palin("abcb"))