from typing import List

"""
Basic Idea: Convert to a hash set, 
    iterate through the list of points 
        if n-1 is in the hash set the seq len for n is whatever the prev len was plus 1

Exception to this:

If the sequence is out of order, eg something like

1, 3, 2, 4

Then you get some weirdness where

1 -> 1
3 -> 1
2 -> 1 + len(1) = 2
4 -> 1 + len(3) = 2

So you have to do a bit of weirdness here where you make sure that does
not happen by recursively visiting the guys once behind to ensure that the
sequence tally is "in order" but you don't have to actually sort. 
"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0

        unique_nums = set(nums)
        seq_len = {n: 1 for n in unique_nums}
        visited = set()

        def visit(n):
            if n-1 in unique_nums:
                if n-1 not in visited:
                    visit(n-1)
                    visited.add(n-1)
                    seq_len[n] = seq_len[n-1] + 1
                else:
                    seq_len[n] = seq_len[n-1] + 1

        for n in unique_nums:
            visit(n)
            
        return max(list(seq_len.values()))