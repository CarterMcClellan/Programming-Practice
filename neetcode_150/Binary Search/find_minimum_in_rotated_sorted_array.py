"""
General thought process is it helps to draw this out

We have a couple "kind of" sorted arrays

    [6, 1, 2, 3, 4, 5]
    [3, 4, 5, 6, 1, 2]

And we want to find the min. The gut is binary search.
Rough algorithm:
    1) Split the array in half
    2) Check if the left and right halves are "ascending"
        *) if the left half is not ascending the min is over there
        *) if the right half is not ascending the min is over there
        *) if both halves are ascending, the min is the current left most point
"""
class Solution:
    def findMin(self, nums: list[int]) -> int:
        l, r = 0, len(nums)-1
        while l <= r:
            m = (r-l)//2 + l

            if (r-l) <= 3:
                return min(nums[l:r+1])

            # left half is not ascending
            # bc. left is great than right
            if nums[l] > nums[m]:
                r = m
            
            # right half is not ascending
            # bc. right is less than left
            elif nums[r] < nums[m]:
                l = m
            
            # both halves are ascending so 
            # the array is in order
            else:
                return nums[l]

        return nums[l]