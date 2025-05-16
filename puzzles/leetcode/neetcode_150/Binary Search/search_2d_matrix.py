"""
This one is fairly straightforward, bin search to find the row, then bin search
to find the column.

There were 3 things I needed to understand
1) When bin search exits, the index l is the insertion point into the array
2) The index which is nearest to the target could be r or l
3) For this problem we need to check the largest value in the row when choosing the largest row
"""
class Solution:
    def bin_search(self, sorted_arr: list[int], target: int) -> bool:
        l, r = 0, len(sorted_arr)-1
        while l <= r:
            m = (r-l)//2 + l

            if sorted_arr[m] == target:
                return True
            
            elif sorted_arr[m] < target:
                l = m + 1
            
            else:
                r = m - 1
        
        return False

    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # I think the general idea here is to first find the row which it
        # could be in, then find the column which it could be in
        n_rows, n_cols = len(matrix), len(matrix[0])

        if n_rows == 0:
            return False

        if n_rows == 1:
            return self.bin_search(matrix[0], target)

        l, r = 0, n_rows-1
        while l <= r:
            m = (r-l)//2 + l

            if matrix[m][-1] == target:
                return True
            elif matrix[m][-1] < target:
                l = m + 1        
            else:
                r = m - 1

        # at this point the insertion point is l,
        # but the nearest point can be r or l (so we have
        # to check the distances)
        end_point = l if l < n_rows else r

        if abs(target - matrix[r][0]) < abs(target - matrix[end_point][0]):
            end_point = r
 
        return self.bin_search(matrix[end_point], target)