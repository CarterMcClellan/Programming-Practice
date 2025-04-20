from typing import List

class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            encoded_str += f"{len(s)}#{s}"

        return encoded_str

    # 4#neet4#code
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            word_len = int(s[i:j]) # i = 0, j = 1, word_len = 4
            result.append(
                s[j+1:j+1+word_len] # 2:6
            )

            i = j + 1 + word_len

        return result