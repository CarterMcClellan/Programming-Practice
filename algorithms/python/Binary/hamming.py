import math
from tqdm import tqdm

def count_bits(n: int) -> int:
    """ count the number of 1s in the binary representation of n """
    if n == 0:
        return 0 # avoid log domain error

    n_ones = 0
    n_bits = math.floor(math.log2(n)) + 1
    for i in range(n_bits):
        val = 1 << i
        if n & val == val:
            n_ones += 1
    return n_ones

def count_bits_str(n: int) -> int:
    """ equivalent to the above but using strings """
    return bin(n).count("1")

if __name__ == "__main__":
    for i in tqdm(range(2**20)):
        assert count_bits(i) == count_bits_str(i), f"count_bits({i}) != count_bits_str({i})"

    print("passed")