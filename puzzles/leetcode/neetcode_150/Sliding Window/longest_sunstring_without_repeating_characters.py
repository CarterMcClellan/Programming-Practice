"""
You start with a sliding window approach because you are trying to track a subsequence
and you want to do it on o(n) time. 

I start with l and r in the same place and increment r until I get a duplicate.
Then I need to shift l. The question is where?

My first thought is to move l all the way to r, but this overlooks potential substrings where
l's position is between its current value and r, so the most conservative increment for l
has to be until there are no more dupes.

But that's kinda tricky to implement! you need some loop where you are going to increment l
until you find the character which the right pointer is currently looking at.

but you can actually make things a bit simpler and easy to follow if you store the pointer
to the previous value of l in the hashmap
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen_characters = {}
        l, r = 0, 0
        N = len(s)
        longest_seq = 0

        while l <= r and r < N:
            if s[r] in seen_characters:
                l = max(seen_characters[s[r]] + 1, l)

            seen_characters[s[r]] = r
            longest_seq = max(longest_seq, r-l+1)
            r += 1

        return longest_seq
            