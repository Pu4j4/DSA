#Problem: Best time to buy and sell stock (https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/)

#Problem statement:
#Given prices, where prices[i] is the price of given stock on the ith day
#you can buy once, sell once and must buy before selling, find max profit, otherwise return 0

#Pattern: Track min so far/Greedy

#brute force ide
#Try for every possible buy day
#for each buy day, try every sell day after it, return max_profit

#brute force
def buy_sell(prices):
    n = len(prices)
    max_profit = 0
    for i in range(n):
        for j in range(i+1,n):
            profit = prices[j] - prices[i]
            max_profit = max(max_profit,profit)
    return max_profit

#Time: O(n^2) - nested loops     Space: O(1) - some varaibles

#why it's slow
#checking every possible buy and sell day , nested loops
#repeated calculations

#Optimized idea
#Initialize min price with greater value, max_profit with 0
#for each price in prices: check if price is less than min_price -> update min price with smaller price
#calculate profit -> price - min_price
#update max_profit and return

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

#Time: O(n) - tracking min_price and calculated max_profit   Space: O(1) - only some variables used
