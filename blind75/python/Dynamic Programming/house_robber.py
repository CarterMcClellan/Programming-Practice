class Solution:
    def rob(self, nums: List[int]) -> int:
        # classic dp problem
        N = len(nums)
        for i in range(N):
            # can choose closest or next closest
            if i >= 3:
                nums[i] = nums[i] + max(nums[i-2], nums[i-3])
            
            # can choose neighbor
            elif i == 2:
                nums[i] = nums[i] + nums[i-2]
            
        # return most profitable    
        return max(nums)
