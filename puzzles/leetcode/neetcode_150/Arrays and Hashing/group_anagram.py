from typing import List
from collections import defaultdict

class Solution:

    def compute_hash(self, s: str) -> str:
        s = "".join(sorted(s))

        return s
    
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        buckets = defaultdict(list)

        for s in strs:

            anagram_hash = self.compute_hash(s)

            if anagram_hash in buckets:
                buckets[anagram_hash].append(s)
            else:
                buckets[anagram_hash] = [s]

        without_keys = list(buckets.values())

        return without_keys