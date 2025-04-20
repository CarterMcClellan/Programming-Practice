from typing import List, Set, Tuple
"""
This is very similar to the two integer sum solution, but we have to make a modification
- We have to support returning multiple possible solutions from the 2 sum helper
"""
class Solution:
    def two_sum_helper(self, nums: List[int], target: int) -> list[list[int]]:
        p1, p2 = 0, len(nums) - 1
        solns: Set[Tuple[int, int]]= set()
        while p1 < p2 and p1 >= 0 and p2 <= len(nums) - 1:
            current = nums[p1] + nums[p2]

            if current == target:
                solns.add((nums[p1], nums[p2]))
                p1 += 1
                continue

            if current < target:
                p1 += 1
            else:
                p2 -= 1

        return [list(s) for s in solns]

    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums = sorted(nums)
        solns = set()
        for idx, n in enumerate(nums):
            target = -n 
            remainder = nums[idx+1:]
            two_sum_solns = self.two_sum_helper(remainder, target)

            if len(two_sum_solns) > 0:
                for soln in two_sum_solns:
                    solns.add((n, soln[0], soln[1]))

        ans = [list(v) for v in solns]
        return ans