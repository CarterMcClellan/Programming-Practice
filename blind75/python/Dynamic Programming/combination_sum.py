class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        
        res = []
        N = len(candidates)
        candidates = sorted(candidates)
        
        def recurse(curr, idx):
            total = sum(curr)
            if total == target:
                res.append(curr)
                
            if idx >= N:
                return 
            
            else:
                if total + candidates[idx] <= target:
                    recurse([*curr, candidates[idx]], idx)
                    recurse(curr, idx+1)
        
        recurse([], 0)
        return res
