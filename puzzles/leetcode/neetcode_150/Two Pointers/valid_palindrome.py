class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphabet = set(list("abcdefghijklmnopqrstuvwxyz0123456789"))
        only_alpha = [c for c in s if c in alphabet]
        return only_alpha == list(reversed(only_alpha))