#brute force
# def buy_sell(prices):
#     n = len(prices)
#     max_profit = 0
#     for i in range(n):
#         for j in range(i+1,n):
#             profit = prices[j] - prices[i]
#             max_profit = max(max_profit,profit)
#     return max_profit


#optimized
def buy_sell(prices):
    min_price = float('inf')
    max_profit = 0
    for price in prices:
        min_price = min(price,min_price)
        profit = price - min_price
        max_profit = max(max_profit,profit)
    return max_profit
prices = [8,2,5,1,5,2]
print(buy_sell(prices))