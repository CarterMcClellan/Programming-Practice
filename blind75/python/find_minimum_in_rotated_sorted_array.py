class Solution:
    def findMin(self, nums: List[int]) -> int:
        # draw it out
        # 
        # [3, 4, 0, 1, 2]
        # 
        
        #   * 
        # *
        #         *
        #       *
        #     *
        
        # there will always be 2 distinct parts
        # - the lhs (values > 2)
        # - the rhs (values < 2)
        # and the minimum will be the boundary
        # of those 2 parts
        
        # find boundary algorithm, described
        # here: https://algo.monster/problems/binary_search_boundary
        left, right = 0, len(nums) - 1
        boundary_index = -1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < nums[-1]:
                boundary_index = mid
                right = mid - 1
            else:
                left = mid + 1

        return nums[boundary_index]
        
