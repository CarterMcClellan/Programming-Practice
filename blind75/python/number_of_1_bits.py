class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count("1")
        n_ones = 0
        for i in range(32):
            val = 1 << i
            if n & val == val:
                n_ones += 1
        return n_ones
