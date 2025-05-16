from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        val_to_index = { val: idx for idx, val in enumerate(nums)}

        for idx, n in enumerate(nums):
            target_complement = target - n

            if target_complement in val_to_index:
                complement_index = val_to_index[target_complement]

                if complement_index != idx:
                    return sorted([idx, complement_index])
                
        return [-1, -1]