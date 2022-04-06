class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:        
        if not nums:
            return 0
        
        n = len(nums)
        dp = [1] * n
        
        # originally I wanted to look at all previous subsequences
        # and increment subsequences -> giving them a 
        # smaller last value if the current value was smaller
        # the problem with this being that it means we have to maintain
        # all previously optimal subsequences... O(N^3)
        
        # instead: dp[i] = the longest subsequence we have seen at i
        # (up to and including nums[i]), thus if i < j, and nums[i] < nums[j]
        # then dp[i] < dp[j]
        
        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
                    
        return max(dp)
                        
