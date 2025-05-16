import math

"""
Even after seeing the expected complexity for this problem
it took me a while to see how this was a "binary search" problem

But it did make sense to start with a brute force approach and then
refine a binary search solution from that once we recognized that the values
were sorted
"""

class Solution:
    def consumption_time(self, k, piles):
        if k == 0:
            return float('inf')

        return sum([math.ceil(p_count/k) for p_count in piles])

    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        upper_bd = max(piles)
        l, r = 0, upper_bd

        result = r

        while l <= r:
            mid = (r-l)//2 + l
            time = self.consumption_time(mid, piles)

            if time <= h:
                result = mid
                r = mid - 1
            else: 
                l = mid + 1

        return result