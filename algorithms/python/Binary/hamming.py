def hammingWeight(n: int) -> int:
    n_ones = 0
    for i in range(32):
        val = 1 << i
        if n & val == val:
            n_ones += 1
    return n_ones

def hammingWeight2(n: int) -> int:
    return bin(n).count("1")
