class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # First thought bfs -> (too slow) -> need O(n)
        N = len(nums)
        
        # Second thought: Lets just keep track of the furthest
        # we can jump. 
        furthest = 0
        for i in range(N):
            if i > furthest:
                return False
            
            furthest = max(furthest, i + nums[i])
        
        return True
