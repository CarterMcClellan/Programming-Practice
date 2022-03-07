# Trick: Use a Dict. Only need to iterate once
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        values = {}
        for idx, n in enumerate(nums):
            if (target - n) in values:
                return [values[target - n], idx]
            values[n] = idx
