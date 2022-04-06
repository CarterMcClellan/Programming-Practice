# Trick: Sort beforehand. Skip duplicates of value at i, j, k
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        slns = []
        N = len(nums)-1
        for i in range(0, len(nums)-2):
            j, k = i+1, N
            
            if i > 0 and nums[i] == nums[i-1]:
                continue
            while j < k:
                if nums[i] + nums[j] + nums[k] == 0:
                    slns += [[nums[i], nums[j], nums[k]]]
                    while j < k and nums[j] == nums[j+1]:
                        j += 1
                    while j < k and nums[k] == nums[k-1]:
                        k -= 1
                    j += 1; k -= 1
                             
                elif -nums[i] > nums[j] + nums[k]:
                    j += 1
                
                elif -nums[i] < nums[j] + nums[k]:
                    k -= 1
        
        return slns
