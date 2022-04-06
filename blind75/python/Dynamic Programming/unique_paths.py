class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # Lets look at a 2x2 grid first
        # 
        # In that case the robot can go (d, r) or (r, d) = 2 slns
        
        # 2x3 grid
        # 
        # (r, d, d)
        # (d, r, d)
        # (d, d, r)
        
        # Basic idea: Backfill. Number of paths == Number of paths below + Number of paths right
        
        grid = [[0 for _ in range(n)] for _ in range(m)]
        grid[-1][-1] = 1

        for r in range(m-1, -1, -1):
            for c in range(n-1, -1, -1):
                if r != m-1:
                    grid[r][c] += grid[r+1][c]
                if c != n-1:
                    grid[r][c] += grid[r][c+1]
        
        
            
        return grid[0][0]
