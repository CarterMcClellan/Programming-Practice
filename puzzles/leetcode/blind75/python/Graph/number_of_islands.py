class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.marked_char = "#"
        self.R, self.C = len(grid), len(grid[0])
        self.grid = grid
        self.increments = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        num_islands = 0
        
        for x in range(self.R):
            for y in range(self.C):
                if self.grid[x][y] == "1":
                    num_islands += 1
                    self.mark_island(x, y)
        
        # self.print_grid()
        return num_islands
    
    def mark_island(self, x, y):
        
        if not self.in_bounds(x, y):
            return
        
        if self.is_marked(x, y):
            return
        
        if not self.is_land(x, y):
            return 
        
        self.grid[x][y] = self.marked_char
        
        for (d_x, d_y) in self.increments:
            self.mark_island(x + d_x, y + d_y)
            
                
    def in_bounds(self, x, y,):
        return 0 <= x < self.R and 0 <= y < self.C
    
    def is_marked(self, x, y):
        return self.grid[x][y] == self.marked_char
    
    def is_land(self, x, y):
        return self.grid[x][y] == "1"
    
    def print_grid(self):
        for row in self.grid:
            print(row)
