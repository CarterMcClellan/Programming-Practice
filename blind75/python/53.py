# Trick: Prefix Sum + Buy Low Sell High
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        N = len(nums)
        
        # prefix sum
        prefix_sum = [0 for _ in range(N)]
        prefix_sum[0] = nums[0]
        
        for idx in range(1, N):
            prefix_sum[idx] = prefix_sum[idx - 1] + nums[idx]
        
        # buy low sell high
        lowest = prefix_sum[0]
        max_profit = prefix_sum[0]
        for idx in range(1, N):
            max_profit = max(max_profit, prefix_sum[idx] - lowest, prefix_sum[idx])
            lowest = min(lowest, prefix_sum[idx])
        
        return max_profit
