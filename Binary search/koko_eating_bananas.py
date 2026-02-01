#brute force
import math
def minEatingSpeed(self, piles, h):
    maxPile = max(piles)
    for k in range(1, maxPile + 1):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)

        if hours <= h:
            return k

#optimized
def minEatingSpeed(self, piles, h):
    left, right = 1, max(piles)
    ans = right

    while left <= right:
        mid = (left + right) // 2
        hours = 0

        for pile in piles:
            hours += math.ceil(pile / mid)

        if hours <= h:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans

