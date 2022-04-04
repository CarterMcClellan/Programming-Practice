class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        # given a straight line of houses
        # find the one which is most profitable to rob
        def rob_houses(houses):
            N = len(houses)
            memo = [n for n in houses]
            
            for i in range(2, N):
                if i >= 3:
                    memo[i] = memo[i] + max(memo[i-2], memo[i-3])
                else:
                    memo[i] = memo[i] + memo[i-2]
            
            return max(memo)
        
        # eliminate the circle edge case, solve using basic
        # dp house robbing sln.
        return max(rob_houses(nums[:-1]), rob_houses(nums[1:]))
