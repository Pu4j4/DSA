#brute force
def daily_temp(temps):
    n = len(temps)
    result = [0]*n
    for i in range(n):
        for j in range(i+1,n):
            if temps[j] > temps[i]:
                result[i] = j-i
                break
    return result
temps = [54,57,80,35,48,90]
print(daily_temp(temps))