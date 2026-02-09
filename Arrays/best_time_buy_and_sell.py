#brute force
def buy_sell(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):
        for j in range(i+1,n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit,profit)
    return max_profit

prices = [8,3,1,2,5]
print(buy_sell(prices))