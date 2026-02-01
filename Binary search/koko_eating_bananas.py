#brute force
def minEatingSpeed(self, piles, h):
    maxPile = max(piles)
    for k in range(1, maxPile + 1):
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / k)

        if hours <= h:
            return k