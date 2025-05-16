class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        stack = []
        left = [0] * len(heights)
        right = [0] * len(heights)
        
        # precompute the first instance where we see a shorter
        # height left of the index
        for i in range(len(heights)):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            left[i] = stack[-1] if stack else -1
            stack.append(i)
        
        stack.clear()
        
        # precompute the first instance where we see a shorter 
        # height right of the index
        for i in range(len(heights)-1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            right[i] = stack[-1] if stack else len(heights)
            stack.append(i)
        
        max_area = 0
        for i in range(len(heights)):
            curr_height = heights[i]
            curr_area = curr_height * (right[i] - left[i] - 1)
            max_area = max(max_area, curr_area)
            
        return max_area