def maxArea(height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_height = min(height[l], height[r]) * (r - l)
        while l <= r:
            curr_height = min(height[l], height[r]) * (r - l)
            max_height = max(curr_height, max_height)
            if height[l] < height[r]:
                l += 1
            
            else:
                r -= 1
                
        return max_height
