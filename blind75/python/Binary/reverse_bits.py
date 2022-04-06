class Solution:
    def reverseBits(self, n: int) -> int:
        bits = []
        for i in range(32):
            tmp = 1 << i
            if n & tmp == tmp:
                bits.append("1")
            else:
                bits.append("0")
        
        return int("".join(bits), 2)
