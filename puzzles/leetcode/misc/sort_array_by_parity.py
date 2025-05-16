class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        # Simplest Possible Approach
        # Create 2 Arrays
        # Append each element to 1 array
        # Return conjoined result
        
        # Time Complexity: O(N)
        # Space Complexity: O(N)
        
        # Can we do better?
        # Yes, let us store only the evens
        # and the odds which need to be swapped
        # In order to make the array valid.
        # 
        # Worst case: There are the same number of
        # evens and odds, and they are in exactly the
        # wrong order.
        
        self.N = len(nums)
        self.N_evens = self.count_evens(nums)
        odd_idxs, even_idxs = self.find_evens_and_odds(nums)
        
        for odd_idx, even_idx in zip(odd_idxs, even_idxs):
            nums = self.swap(odd_idx, even_idx, nums)
        
        return nums
                
    def count_evens(self, nums: List[int]) -> int:
        num_evens = 0
        for num in nums:
            if num % 2 == 0:
                num_evens += 1
        
        return num_evens
    
    def find_evens_and_odds(self, nums: List[int]):
        odd_idxs = []
        even_idxs = []
        for idx in range(self.N_evens):
            is_odd = not (nums[idx] % 2 == 0)
            
            if is_odd:
                odd_idxs.append(idx)
        
        for idx in range(self.N_evens, self.N):
            is_even = (nums[idx] % 2 == 0)
            
            if is_even:
                even_idxs.append(idx)
        
        return odd_idxs, even_idxs
                
            
    def swap(self, idx_1, idx_2, nums):
        nums[idx_1], nums[idx_2] = nums[idx_2], nums[idx_1]
        
        return nums
