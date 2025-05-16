"""
Basic Idea: Increment right until you have a valid substring.
Then once its valid try to compress on the left until you can't anymore,
then start shifting right again.
"""
class Solution:
    def count_characters(self, s):
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1

        return d

    def contains_characters(self, count_s, count_t):
        for k_t, v_t in count_t.items():
            if k_t not in count_s or count_s[k_t] < v_t:
                return False
        
        return True

    def minWindow(self, s: str, t: str) -> str:
        seq_found = False
        min_seq = "#" * 100
        count_t = self.count_characters(t)
        count_s = {}
        l = 0

        # "ADOBECODEBANC" returns "BAN"

        for r in range(len(s)):
            char = s[r]
            count_s[char] = count_s.get(char, 0) + 1

            while self.contains_characters(count_s, count_t):
                seq_found = True

                if len(s[l:r]) < len(min_seq):
                    min_seq = s[l:r+1]
                
                remove_char = s[l]
                count_s[remove_char] = count_s.get(remove_char, 0) - 1
                l += 1

            
        if seq_found == False:
            return ""

        return min_seq