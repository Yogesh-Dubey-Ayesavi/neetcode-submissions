class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        rm = prices[0]
        profit = 0
        for i in range(len(prices)):
            price = prices[i]
            rm= min(price, rm)
            print(price,rm,profit)
            profit = max(profit,price - rm)
        return profit
