"""
This was quite a bit harder then some of the other problems which I have encountered

I think without the prefix and suffix hint I wouldn't have gotten this, even writing a brute
force solution I kinda screwed up. 
"""
class Solution:
    def trap(self, height: list[int]) -> int:
        # prefix array
        pa = [0 for _ in range(len(height))]
        pa[0] = height[0]
        for idx in range(1, len(height)):
            h = height[idx]
            pa[idx] = max(h, pa[idx-1])

        # suffix array
        sa = [0 for _ in range(len(height))]
        sa[-1] = height[-1]
        for idx in range(len(height) - 2, -1, -1):
            h = height[idx]
            sa[idx] = max(h, sa[idx+1])

        # total
        volume = 0
        for idx in range(len(height)):
            min_height = min(pa[idx], sa[idx])
            volume += min_height - height[idx]
        return volume
                