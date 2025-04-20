"""
important realization here is that if there is a tie
it does not matter which side we decement. I initially was
strung up over

[7,50000,1,1,1,7]

because there is seems like we are missing
[50000, 7] as our 2 height, but we are taking the min, so its actually worse
than the original [7, 7] pairing
"""
class Solution:
    def maxArea(self, heights: list[int]) -> int:
        i, j = 0, len(heights) - 1
        max_water = 0

        while i < j and j <= len(heights) - 1 and i >= 0:
            height_a, height_b = heights[i], heights[j]
            volume = min(height_a, height_b) * (j - i)

            max_water = max(volume, max_water)

            if height_a < height_b:
                i += 1
            else:
                j -= 1

        return max_water    