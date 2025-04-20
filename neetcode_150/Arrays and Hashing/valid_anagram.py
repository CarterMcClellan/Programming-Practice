class Solution:
    def count_letters(self, s: str):
        letter_count = {}

        for character in s:
            if character in letter_count:
                letter_count[character] += 1
            else:
                letter_count[character] = 1

        return letter_count
    
    def isAnagram(self, s: str, t: str) -> bool:
        count_s = self.count_letters(s)
        count_t = self.count_letters(t)

        return count_s == count_t