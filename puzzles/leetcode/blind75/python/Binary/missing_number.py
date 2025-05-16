class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # N = len(nums)
        # expected = (N * (N+1))//2
        # return expected - sum(nums)
        
        N = len(nums)
        res = 0
        for i in range(N):
            res = res ^ i ^ nums[i]
        
        res = N ^ res
        return res
