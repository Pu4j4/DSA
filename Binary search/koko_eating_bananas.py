#Problem: Koko eating bananas (https://leetcode.com/problems/koko-eating-bananas/)

#Problem statement:
#Koko loves eating bananas. There are n piles of bananas, and ith pile has piles[i] bananas
#Koko eats bananas at a speed k bananas per hour
#In one hour koko can eat at most k bananas from one pile
#Find the MINIMUM eating speed (k), so that Koko finishes all piles within h hours
#If a pile has more bananas than k, she needs multiple hours

#brute force idea
#

#brute force
import math
def koko_min_speed(piles, h):
    max_pile = max(piles)
    for k in range(1, max_pile + 1):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)

        if hours <= h:
            return k

#optimized
# def koko_min_speed(piles, h):
#     left, right = 1, max(piles)
#     ans = right
#
#     while left <= right:
#         mid = (left + right) // 2
#         hours = 0
#
#         for pile in piles:
#             hours += math.ceil(pile / mid)
#
#         if hours <= h:
#             ans = mid
#             right = mid - 1
#         else:
#             left = mid + 1
#
#     return ans

piles = [3,6,7,11]
print(koko_min_speed(piles,8))