class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        N = len(intervals)
        curr = intervals[0]
        result = []
        for idx in range(1, N):
            next_ = intervals[idx]
            
            if self.disjoint(curr, next_):
                result.append(curr)
                curr = next_
                
            else:
                curr = self.merge_pair(curr, next_)
        
        result.append(curr)
        return result
    
    def merge_pair(self, interval_1: List[int], interval_2: List[int]) -> List[List[int]]:
        """ convert 2 intervals into a single interval """
        
        [s_1, e_1] = interval_1
        [s_2, e_2] = interval_2
        
        return [min(s_1, s_2), max(e_1, e_2)]
        
    
    def disjoint(self, interval_1: List[int], interval_2: List[int]) -> bool:
        """ 
        returns true if the two intervals are completely disjoint 
        """
        [s_1, e_1] = interval_1
        [s_2, e_2] = interval_2
        
        # if one interval starts after another
        # then the two are disjoint
        if s_2 > e_1 or s_1 > e_2:
            return True
        
        return False
            
