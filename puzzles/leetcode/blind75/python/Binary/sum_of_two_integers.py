from typing import List
class Solution:
    def getSum(self, a: int, b: int) -> int:
        self.numBits = 11
        
        if a >= 0 and b >= 0:
            return self.binToInt(self.sameSign(a, b))
        
        elif a < 0 and b < 0:
            return -1*self.binToInt(self.sameSign(abs(a), abs(b)))
            
        else:
            res = self.sameSign(a, b)
            if res[0] == 0:
                return self.binToInt(res)
            res = self.invertBin(res)
            print(f"inverted {res}")
            return -1*self.binToInt(res) - 1
    
    def sameSign(self, a: int, b: int) -> int:
        aBits, bBits = self.intToBin(a), self.intToBin(b)
        print(f"{aBits}, {bBits}")
        res = [0 for _ in range(self.numBits)]
        carry = 0
        
        for idx in range(self.numBits):
            aBit, bBit = aBits[idx], bBits[idx]
            
            if aBit == 1 and bBit == 1:
                res[idx] = carry
                carry = 1
            
            elif aBit == 0 and bBit == 0:
                res[idx] = carry
                carry = 0
            
            else:
                if carry == 0:
                    res[idx] = 1
                    carry = 0
                else:
                    res[idx] = 0
                    carry = 1
        res = res[::-1]
        print(f"res {res}")
        return res
            
    def binToInt(self, a: List[int]) -> int:
        binStr = "".join([str(c) for c in a])
        return int(binStr, 2)
    
    def intToBin(self, a: int) -> List[int]:
        bits = []
        for exp in range(self.numBits):
            base = 1 << exp
            bit = int(base & a == base)
            bits.append(bit)
                
        return bits
    
    def invertBin(self, a: List[int]) -> int:
        invertedBits = [0 for _ in range(self.numBits)]
        for idx in range(self.numBits):
            if a[idx] == 0:
                invertedBits[idx] = 1
            else:
                invertedBits[idx] = 0
                
        return invertedBits
