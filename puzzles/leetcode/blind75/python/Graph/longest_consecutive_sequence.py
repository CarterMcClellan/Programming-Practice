class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        # Solution:
        # For a given element, 
        #    Expand as far as you can to the right and left
        #    (order of right then left or left then right does
        #     not matter)
        
        # In the process remove those elements from the set.
        # You don't need to check them again they will be covered
        # by their children
        longest, s = 0, set(nums)
        for num in nums:
            cur_longest, j = 1, 1
            while num + j in s: 
                s.remove(num + j)
                cur_longest, j = cur_longest + 1, j + 1
            
            j = 1
            while num - j in s: 
                s.remove(num - j)
                cur_longest, j = cur_longest + 1, j + 1
            
            longest = max(longest, cur_longest)
        return longest  
