class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0, 1, 1, 2] + [0 for _ in range(n - 3)]
        if n <= 3:
            return res[:n+1]
        
        i = 4
        while i <= n:
            for j in range(0, i):
                # print(f'C({i+j}) = C({j}) + 1')
                if i + j > n: 
                    break
                res[i + j] = res[j] + 1
            i = i + j + 1
            # print(i)
        
        return res
