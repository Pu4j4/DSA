nums = [1,1,2,3,2,1]
mp = {}
for num in nums:
    if num in mp:
        mp[num] += 1
    else:
        mp[num] = 1
print(mp)