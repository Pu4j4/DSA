def find_the_winner(n, k):
    winner = 0
    for i in range(2, n + 1):
        winner = (winner + k) % i
    return winner + 1