import heapq
"""
O(N*k) impl is trivial

O(N*log n) impl is less trivial, it took me a second to convince myself
that the number of times we were going to pop from the queue in any given
pass of the loop was going to be constant
"""
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        heap = [(-nums[i], i) for i in range(k)]
        heapq.heapify(heap)
        ans.append(-heap[0][0])

        for idx in range(k, len(nums)):
            val = nums[idx]
            heapq.heappush(heap, (-val, idx))

            while heap and heap[0][1] <= idx - k:
                heapq.heappop(heap)

            ans.append(-heap[0][0])

        return ans
            