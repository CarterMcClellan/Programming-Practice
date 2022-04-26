# Lets think about what we need to know about an array
# in order to find its median.

# We need to know if an array is odd or even

# if an array is odd, we want to know the exact
# middle element (of the sorted array)

# if an array is even, we want to know the average
# of the two middle elements

# idea:
# lets keep 2 heaps. 1 which represents the N/2 smallest
# elements in the array
# 
# and 1 which represents the N/2 largest_elements in the array
# 
# then the median computation should be
#   (the largest element in the small heap + the smallest element in the large heap) / 2

import heapq as hq
class MedianFinder:

    def __init__(self):
        self.small_heap = []
        self.large_heap = []
        
        # keep a count N to know 
        # if the total number of elements
        # is odd or even
        self.N = 0

    def addNum(self, num: int) -> None:
        if self.N == 0:
            hq.heappush(self.large_heap, num)
        else:
            median = self.findMedian()
            if num < median:
                hq.heappush(self.small_heap, -num)
                new_largest = -hq.heappop(self.small_heap)
                hq.heappush(self.large_heap, new_largest)
            else:
                hq.heappush(self.large_heap, num)
                new_smallest = hq.heappop(self.large_heap)
                hq.heappush(self.small_heap, -new_smallest)
        self.N += 1                

    def findMedian(self) -> float:
        # if N is odd, get the smallest value
        # in the large heap
        if self.N % 2 != 0:
            return self.large_heap[0]
        
        return (-self.small_heap[0] + self.large_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
