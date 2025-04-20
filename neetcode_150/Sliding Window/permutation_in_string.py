alphabet = "abcdefghijklmnopqrstuvwxyz"
class Solution:
    def count(self, s: str):
        counts = {c: 0 for c in alphabet}
        for c in s:
            counts[c] = counts.get(c, 0) + 1
        return counts

    def is_permutation(self, count1, count2) -> bool:
        return count1 == count2

    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_count = self.count(s1)
        s2_count = {c: 0 for c in alphabet}
        for c in s2[:s1_len]:
            s2_count[c] = s2_count.get(c, 0) + 1

        if self.is_permutation(s1_count, s2_count):
            return True

        for r in range(s1_len, len(s2)):
            old_character = s2[r-s1_len]
            s2_count[old_character] = s2_count.get(old_character, 0) - 1

            new_character = s2[r]
            s2_count[new_character] = s2_count.get(new_character, 0) + 1

            if self.is_permutation(s1_count, s2_count):
                return True
        
        return False