class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100
        profit = 0
        for i in range(len(prices)):
            min_price = min(min_price, prices[i])
            temp_profit = prices[i] - min_price
            profit = max(profit,temp_profit)
        return profit