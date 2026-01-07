s = "aabbcd"
mp = {}
for ch in s:
    mp[ch] = mp.get(ch,0)+1
    #  or
        # if ch in mp:
        #     mp[ch] += 1
        # else:
        #     mp[ch] = 1
print(mp)
