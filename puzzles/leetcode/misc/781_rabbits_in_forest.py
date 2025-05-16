from collections import Counter
import math

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        # ok so we are trying to "pair" off all the answers
        # 
        # if 2 rabbits answered the same number they could have been
        # talking about each other
        # 
        # but what if a bunch of rabbits said 1? they can't all be talking about
        # the same rabbit. eg 5 rabbits said 1
        # 
        # 1-1, 1-1, 1 (should be 4)
        #
        # if count(answers == k) > answer:
        #  ans += (total_k / (k+1))
        #  rem = (total_k % (k+1))
        #  if rem > 0: ans += (k+1)
        # if count(answer == k) > 0:
        #  ans += (k+1)
        # 
        # return ans

        counts = Counter(answers)
        ans = 0

        for key, count in counts.items():
            if count >= key+1:
                n_groups = math.floor((count/(key+1)))
                ans += (n_groups * (key + 1))

            if count % (key+1) > 0:
                ans += (key+1)
        
        return ans
