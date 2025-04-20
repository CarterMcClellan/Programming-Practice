from collections import defaultdict
from typing import List

class Solution:

    def count_vals(self, nums: List[int]):

        counts = {}
        for n in nums:
            if n in counts:
                counts[n] += 1
            else:
                counts[n] = 1

        count_to_number = defaultdict(list)
        for number, count in counts.items():
            if count in count_to_number:
                count_to_number[count].append(number)
            else:
                count_to_number[count] = [number]

        return count_to_number
    
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count_to_number = self.count_vals(nums)

        counts = sorted(list(count_to_number.keys()), reverse=True)
        highest_counts = counts[:k]

        cnt = 0
        ans = []

        for count in highest_counts:
            to_add = count_to_number[count]
            cnt += len(to_add)
            ans.extend(to_add)

            if cnt == k:
                return ans
            

        return ans