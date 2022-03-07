# Trick: Compute the product of all elements which precede index i. Then compute the product of
# all elements which follow index i. Multiply the elements of these 2 lists yields the sln.
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 0 = (1 * 2 * 3)
        # 1 = (0 * 2 * 3)
        # 2 = (0 * 1 * 3)
        # 3 = (0 * 1 * 2)
        
        # 0 = ()
        # 1 = (0)
        # 2 = (0 * 1)
        # 3 = (0 * 1 * 2)
        l = [1 for _ in range(len(nums))]
        for idx in range(1, len(nums)):
            l[idx] = l[idx - 1] * nums[idx - 1]
        
        # 3 = ()
        # 2 = (3)
        # 1 = (3 * 2)
        # 0 = (3 * 2 * 1)
        r = [1 for _ in range(len(nums))]
        for idx in range(len(nums)-2, -1, -1):
            r[idx] = r[idx + 1] * nums[idx + 1]
        
        return [l_e * r_e for l_e, r_e in zip(l, r)]
