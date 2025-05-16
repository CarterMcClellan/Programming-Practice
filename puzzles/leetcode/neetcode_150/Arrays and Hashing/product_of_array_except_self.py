from typing import List

def pivot_product(nums: List[int]) -> List[int]:
    res = [1 for _ in range(len(nums))]

    for idx, n in enumerate(nums):
        if idx == 0:
            continue

        res[idx] = res[idx-1] * nums[idx - 1]

    return res
    
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        N = len(nums)
        left_pivot = pivot_product(nums)

        reversed_array = list(reversed(nums))
        right_pivot = list(reversed(pivot_product(reversed_array)))

        ans = [0 for i in range(N)]

        for i in range(N):
            ans[i] = left_pivot[i] * right_pivot[i]

        return ans