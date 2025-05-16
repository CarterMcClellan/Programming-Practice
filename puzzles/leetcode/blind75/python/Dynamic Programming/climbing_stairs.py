class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        
        n_slns = [0 for _ in range(n+1)]
        n_slns[1] = 1
        n_slns[2] = 2
        
        for i in range(3, n+1):
            n_slns[i] = n_slns[i-1] + n_slns[i-2]
            
        return n_slns[n]
