import heapq as hq
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Lets not use the collections.Counter class
        # Instead lets use a heap with a fixed capacity
        
        element_counts = defaultdict()
        for n in nums:
            if n in element_counts:
                element_counts[n] += 1
            else:
                element_counts[n] = 1
                
        
        heap = []
        for n, count in element_counts.items():
            if len(heap) < k:
                hq.heappush(heap, (count, n))
            
            else:
                min_count, min_n = hq.heappop(heap)
                
                if count > min_count:
                    hq.heappush(heap, (count, n))
                else:
                    hq.heappush(heap, (min_count, min_n))
        
        only_n = [n for (_, n) in heap]
        return only_n
