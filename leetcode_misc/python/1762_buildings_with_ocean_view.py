# ok so we are iterating through an aray
#
# if all the buildings to the right are shorter, than the building has an ocean
# view
#
# this seems fairly simply we want to construct right prefixed' max
#
# st. val[i] = max(all of values at ind > i)
class Solution:
    def findBuildings(self, heights: list[int]) -> list[int]:
        prefixed_heights = [h for h in heights]
        if len(heights) == 0:
            return []
        elif len(heights) == 1:
            return [0]
        prefixed_heights[-1] = 0
        prefixed_heights[-2] = heights[-1]
        N = len(prefixed_heights)
        for idx in range(N-2, -1, -1):
            if idx >= N-2:
                continue
            prefixed_heights[idx] = max(heights[idx+1], 
                                        prefixed_heights[idx+1])

        ans = []
        for idx in range(N):
            if prefixed_heights[idx] < heights[idx]: 
                ans.append(idx)

        return ans