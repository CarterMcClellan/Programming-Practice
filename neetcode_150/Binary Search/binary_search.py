class Solution:
    def search(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            # this is easier for me to remember
            # its the length of the array then shifted over l
            m = (r-l)//2 + l

            # if the point we are looking for is
            # larger than the present value
            # then we want to shift the left window
            # to be m + 1
            if nums[m] < target:
                l = m+1
            
            # conversly if the point we are looking for is
            # smaller than the present value,
            # then we want to shift the right window to
            # be m - 1
            elif nums[m] > target:
                r = m-1

            else:
                return m

        return -1