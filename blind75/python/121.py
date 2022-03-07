# Trick: Store the lowest price as a rolling min. 
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = 1 << 20
        max_profit = -1
        for price in prices:
            lowest_price = min(price, lowest_price)
            max_profit = max(max_profit, price - lowest_price)
        return max_profit
