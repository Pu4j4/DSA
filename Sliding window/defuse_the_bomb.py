#Problem: Defuse the Bomb (https://leetcode.com/problems/defuse-the-bomb/description/)

#Problem statement:
#Given a circular integer array code and integer k, task is to replace every element with:
#if k>0: sum of next k elements
#if k<0: sum of previous |k| elements
#if k==0: replace with 0
#the array is circular means the end connects to the beginning

#Pattern: Sliding window(make sliding window circular)

#brute force idea
#create result array with all zeros of size n
#for each index:
#loop k times forward and backward(look at the next k or prev k elements)
#add elements one by one, store sum in result

#brute force code
def defuse_bomb(code,k):
    n = len(code)
    result = [0]*n
    if k ==0:
        return result
    for i in range(n):
        total = 0
        if k>0:
            for j in range(1,k+1):
                total+=code[(i+j)%n]
        else:
            for j in range(1, k+1):
                total+=code[(i-j)%n]
        result[i] = total
    return result

#Time: O(n*k)- loop n*k times    Space: O(n) - result array stores n elements

#why it's slow:
#for each element , loops k times -> n*k times
#nested loops, very slow

#optimized idea
#instead of recalculating sum everytime, reuse previous window sum
#case1: k>0(sum of next k)
#create window of size k ->first window: sum of elements from 1 to k
#slide the window: add next right element and remove left most element
#store sum in result
#case2: k<0(sum of prev k)
#repeat same as case1, just slide backwards
#case3: k==0
#return array of zeroes i.e return result

#optimized code
def defuse_bomb(code,k):
    n = len(code)
    result = [0]*n
    if k == 0:
        return result
    window_sum = 0
    if k > 0:
        for i in range(1,k+1):
            window_sum += code[i%n]
        for i in range(n):
            result[i] = window_sum
            window_sum -= code[(i+1)%n]
            window_sum += code[(i+k+1)%n]
    else:
        k = abs(k)
        for i in range(1, k+1):
            window_sum += code[(n-i)%n]
        for i in range(n):
            result[i] = window_sum
            window_sum -= code[(i-k+n)%n]
            window_sum += code[i%n]
    return result

code = [5,7,1,4,9]
print(defuse_bomb(code,3))

#Time: O(n) - each element added and removed once  Space: O(n) - result array stores n elements