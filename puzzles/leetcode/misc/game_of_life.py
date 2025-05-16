class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.cardinal = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        self.diagonal = [(1, 1), (-1, -1), (1, -1), (-1, 1)]
        self.directions = self.cardinal + self.diagonal
        self.R, self.C = len(board), len(board[0])
        
        squares_to_update = []
        
        # determine squares to update
        for x in range(self.R):
            for y in range(self.C):
                is_alive = (board[x][y] == 1)
                inverse = int(not is_alive) 
                neighbors = self.get_neighbors(x, y, board)
                
                if self.should_update(is_alive, neighbors):
                    squares_to_update.append((x, y, inverse))
        
        for (x, y, new_val) in squares_to_update:
            board[x][y] = new_val
                    
    def get_neighbors(self, x, y, board):
        neighbors = []
        for (d_x, d_y) in self.directions:
            if 0 <= (x+d_x) < self.R and 0 <= (y+d_y) < self.C:
                new_x, new_y = x+d_x, y+d_y
                neighbors.append(board[new_x][new_y])
                
        return neighbors
            
    def should_update(self, is_alive, neighbors):
        living_neighbors = sum(neighbors)
        
        if is_alive:
            if living_neighbors < 2:
                return True
            
            if living_neighbors == 2 or living_neighbors == 3:
                return False
            
            if living_neighbors > 3:
                return True
        
        else:
            return living_neighbors == 3
