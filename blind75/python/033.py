# Trick: Use the same solution to find the idx of the min of our array
# then, split the array into 2 pieces and perform a vanilla binary search
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if len(nums) <= 2:
            if target not in nums:
                return -1
            return nums.index(target)
        
        def find_pivot():
            left, right = 0, len(nums) - 1
            boundary_index = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] <= nums[-1]:
                    boundary_index = mid
                    right = mid - 1
                else:
                    left = mid + 1
            return boundary_index
        
        def binary_search(target, subarray):
            l, r = 0, len(subarray) - 1
            while l <= r:
                mid = (l + r)//2
                if subarray[mid] == target:
                    return mid
                
                elif subarray[mid] < target:
                    l = mid + 1
                
                else:
                    r = mid - 1
            
            return -1
        
        pivot = find_pivot()

        left, right = nums[:pivot], nums[pivot:]
        lhs = binary_search(target, left)
        if  lhs != -1:
            return lhs
        rhs = binary_search(target, right)
        if rhs != -1:
            return len(left) + rhs
        return -1
