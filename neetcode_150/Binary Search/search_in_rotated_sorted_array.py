"""
The basic approach here should be to find the minimum element
once we identify that we should be able to split the left and right
hand sides into 2 sorted arrays, identify which array the target element
might be in then binary search through each because they are both sorted.
"""
class Solution:
    def get_min_idx(self, nums) -> int:
        """
        basic algorithm for finding a the minimum idx in a rotated sorted
        array
        * split the array in half
        * if the left half is not ascending, the midpoint is over there
        * if the right half is not ascending, the midpoint is over there
        * if they are both ascending, the midpoint is the left most point
        """
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r-l)//2 + l

            if r - l <= 3:
                min_val = min(nums[l:r+1])
                min_idx = nums[l:r+1].index(min_val) + l
                return min_idx

            if nums[l] > nums[m]:
                r = m
            elif nums[r] < nums[m]:
                l = m
            else:
                return l
        
        return l
    
    def bin_search(self, nums, target):
        # [1, 2], 1
        #  l, r
        #
        # m = 0
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (r-l)//2 + l

            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            
        return -1

    def search(self, nums: list[int], target: int) -> int:
        min_idx = self.get_min_idx(nums)

        left = nums[:min_idx]
        right = nums[min_idx:]

        if left and left[0] <= target <= left[-1]:
            return self.bin_search(left, target)

        right_result = self.bin_search(right, target)

        if right_result == -1:
            return -1

        return right_result + len(left)