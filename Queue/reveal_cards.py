from collections import deque
def deckRevealedIncreasing(deck):
    n = len(deck)
    deck.sort()
    q = deque(range(n))
    ans = [0] * n
    for card in deck:
        idx = q.popleft()
        ans[idx] = card
        if q:
            q.append(q.popleft())
    return ans