from typing import List

COL_DIM = 9
ROW_DIM = 9
N_SQUARES = 9
SQUARE_RANGES = {
    0: {
        "x": [0, 2],
        "y": [0, 2]
    },
    1: {
        "x": [3, 5],
        "y": [0, 2]
    },
    2: {
        "x": [6, 8],
        "y": [0, 2]
    },
    3: {
        "x": [0, 2],
        "y": [3, 5]
    },
    4: {
        "x": [3, 5],
        "y": [3, 5]
    },
    5: {
        "x": [6, 8],
        "y": [3, 5]
    },
    6: {
        "x": [0, 2],
        "y": [6, 8]
    },
    7: {
        "x": [3, 5],
        "y": [6, 8]
    },
    8: {
        "x": [6, 8],
        "y": [6, 8]
    },
}

class Solution:
    def _validList(self, l: List[str]) -> bool:
        only_ints = [i for i in l if i != "."]
        return len(set(only_ints)) == len(only_ints)

    def _validRow(self, board: List[List[str]], row_idx: int) -> bool:
        row = board[row_idx]
        return self._validList(row)
    
    def _validColumn(self, board: List[List[str]], col_idx: int) -> bool:
        col = []
        for row in board:
            col_val = row[col_idx]
            col.append(col_val)

        return self._validList(col)

    def _validSquare(self, board: List[List[str]], square_idx: int) -> bool:
        coords = SQUARE_RANGES[square_idx]
        [x_min, x_max] = coords["x"]
        [y_min, y_max] = coords["y"]

        vals = []
        for i in range(x_min, x_max+1):
            for j in range(y_min, y_max+1):
                vals.append(board[i][j])

        return self._validList(vals)

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        valid_cols = [self._validColumn(board, i) for i in range(COL_DIM)]
        valid_rows = [self._validRow(board, i) for i in range(ROW_DIM)]
        valid_squares = [self._validSquare(board, i) for i in range(N_SQUARES)]

        return all(valid_cols) and all(valid_rows) and all(valid_squares)