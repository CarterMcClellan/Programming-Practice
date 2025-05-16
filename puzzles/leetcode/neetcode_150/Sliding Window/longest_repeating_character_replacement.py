class Solution:
    def num_subs_required(self, character_counts):
        """
        number of substituions = sum of all character counts
        besides the max
        """
        max_v, max_k = -1, -1
        for k, v in character_counts.items():
            if v > max_v:
                max_v = v
                max_k =k
        
        return sum([character_counts[k] for k in character_counts if k != max_k])

    def characterReplacement(self, s: str, k: int) -> int:
        """
        sliding window optimization
        - move the pointer right until the condition is violated
        - then move the pointer left until the conditon is not violated
        """
        l = 0
        ans = 0
        counts = {}
        for r in range(len(s)):
            char = s[r]
            counts[char] = counts.get(char, 0) + 1

            while self.num_subs_required(counts) > k:
                char = s[l]
                counts[char] = counts.get(char, 0) - 1
                l += 1

            ans = max(ans, r-l+1)

        return ans