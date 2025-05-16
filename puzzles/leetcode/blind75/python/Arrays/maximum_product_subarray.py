class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        N = len(nums)
        
        def prefix_prod(nums):
            prefix = [1 for _ in range(N)]
            prefix[0] = nums[0]
            for idx in range(1, N):
                if nums[idx]:
                    if prefix[idx-1]:
                        prefix[idx] = nums[idx] * prefix[idx - 1]
                    else:
                        prefix[idx] = nums[idx]
                else:
                    prefix[idx] = 0

            return prefix
        
        return max(prefix_prod(nums) + prefix_prod(nums[::-1]))
