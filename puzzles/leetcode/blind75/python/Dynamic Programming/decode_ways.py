# Key thing here is the storing strings so we don't end up exploring them
# again. In most cases it is not a big problem, but specifically for strings
# like "1111111111111111" or "1121212212121212121" we can run into trouble...
# because the cipher can branch into 2 cases here: either "1" or "11"

# Note that the memo table helps less w/ non-homogenous sequences.
# In this situation an iterative solution would be more efficient.
class Solution:
    def numDecodings(self, s: str) -> int:
        self.memo = {str(i): 1 for i in range(1, 10)}
        self.memo["0"] = 0
        
        return self.helper(s)
        
    def helper(self, s: str) -> int:
        # base cases
        if s in self.memo:
            return self.memo[s]
        
        if not s or s == "":
            return 1
        
        # invalid cases
        if s[0] == "0":
            return 0
        
        parsed_int = int(s[0:2])
        
        if parsed_int <= 26:
            res1 = self.helper(s[1:])
            res2 = self.helper(s[2:])
            
            self.memo[s] = res1 + res2
            return res1 + res2
        
        elif parsed_int >= 27:
            res = self.helper(s[1:])
            self.memo[s] = res
            
            return res     
