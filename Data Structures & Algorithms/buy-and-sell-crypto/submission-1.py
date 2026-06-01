class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = 100
        profit = 0
        length = len(prices)
        for i in range(length):
            if min_price > prices[i]:
                min_price = prices[i]
            temp_profit = prices[i] - min_price
            if profit<temp_profit:
                profit = temp_profit
        return profit