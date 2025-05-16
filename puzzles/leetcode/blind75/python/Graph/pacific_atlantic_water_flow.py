class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # basic idea: decompose the problem into 2 parts
        # 1) Finding all tiles which can reach the pacific coastline
        # 2) Finding all tiles which can reach the atlantic coastline
        #
        # Once we know those 2 things, the answer is simply the intersection
        # of groups (1) and (2)
        self.heights = heights
        self.R, self.C = len(heights), len(heights[0])
        self.visit_mark = "#"
        self.unvisited_mark = ""
        
        self.visited_squares = [[self.unvisited_mark for _ in range(self.C)] for _ in range(self.R)]
        
        # (North, South, East, West)
        self.increments = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        # [top squares] + [left squares]
        pacific_squares = set([(0, y) for y in range(self.C)] + [(x, 0) for x in range(self.R)])
        
        # [bottom squares] + [right squares]
        atlantic_squares = set([(self.R-1, y) for y in range(self.C)] + [(x, self.C-1) for x in range(self.R)])

        for x in range(self.R):
            for y in range(self.C):
                in_pacific = self.dfs(x, y, pacific_squares)
                in_atlantic = self.dfs(x, y, atlantic_squares)
                    
                if in_pacific:
                    pacific_squares.add((x, y))
                
                if in_atlantic:
                    atlantic_squares.add((x, y))
        
        intersection = pacific_squares & atlantic_squares
        return list(list(pair for pair in intersection))
    
    def dfs(self, curr_x, curr_y, target_squares):
        # verify we have not visited this square
        if self.visited_squares[curr_x][curr_y] == self.visit_mark:
            return False

        if (curr_x, curr_y) in target_squares:
            return True

        self.visited_squares[curr_x][curr_y] = self.visit_mark
        for (d_x, d_y) in self.increments:
            next_x, next_y = curr_x+d_x, curr_y+d_y
            
            # verify in bounds
            if not(0 <= next_x < self.R and 0 <= next_y < self.C):
                continue
            
            # verify that we can move to the next square
            if not (self.heights[curr_x][curr_y] >= self.heights[next_x][next_y]):
                continue
            
            if self.dfs(next_x, next_y, target_squares):
                self.visited_squares[curr_x][curr_y] = self.unvisited_mark
                return True
            
        self.visited_squares[curr_x][curr_y] = self.unvisited_mark
        return False
