class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for idx in range(1, len(prices)):
            lowest_price = prices[idx-1]
            curr_price = prices[idx]
            max_profit = max(max_profit, curr_price - lowest_price)
            prices[idx] = min(curr_price, lowest_price)
        
        return max_profit