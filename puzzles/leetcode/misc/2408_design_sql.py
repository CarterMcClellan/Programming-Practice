class Table:
    def __init__(self, n_columns: int):
        self.n_col = n_columns
        self.data = {}
        self.row_id = 1

    def insert(self, row: List[str]) -> bool:
        if len(row) != self.n_col:
            return False
        
        self.data[self.row_id] = row
        self.row_id += 1
        return True
    
    def rmv(self, row_id: int) -> None:
        if row_id in self.data:
            self.data.pop(row_id)

    def sel(self, row_id: int, col_id: int) -> str:
        col_id = col_id - 1 # shift left 1 for zero indexing
        if not (row_id in self.data and 0 <= col_id < self.n_col):
            return "<null>"

        r = self.data[row_id]
        return r[col_id]

    def exp(self):
        res = []
        for row_id in self.data:
            row = self.data[row_id]
            res += [str(row_id) + "," + ",".join(row)]
        return res

class SQL:

    def __init__(self, names: List[str], columns: List[int]):
        # n: table name
        # c: col name (index form)
        self.tbls = { 
            n: Table(c)
            for n, c in zip(names, columns) 
        }

    def ins(self, name: str, row: List[str]) -> bool:
        if name not in self.tbls:
            return False

        tbl = self.tbls[name]
        return tbl.insert(row)


    def rmv(self, name: str, rowId: int) -> None:
        if name not in self.tbls:
            return

        tbl = self.tbls[name]
        tbl.rmv(rowId)

    def sel(self, name: str, rowId: int, columnId: int) -> str:
        if name not in self.tbls:
            return "<null>"

        tbl = self.tbls[name]
        return tbl.sel(rowId, columnId)

    def exp(self, name: str) -> List[str]:
        if name not in self.tbls:
            return []
            
        tbl = self.tbls[name]
        return tbl.exp()


# Your SQL object will be instantiated and called as such:
# obj = SQL(names, columns)
# param_1 = obj.ins(name,row)
# obj.rmv(name,rowId)
# param_3 = obj.sel(name,rowId,columnId)
# param_4 = obj.exp(name)