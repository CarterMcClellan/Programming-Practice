"""
The goal with this algorithm is find the kth index in what would be
the merged output array.

We are going to do this by search for a "pivot" point in the array
nums1, such that when take pivot elements from nums1 and k - pivot elements
from nums2 then we form what would the first k elements in the output 
array and take the last index

How are we going to make this logrithmic?
    Our condition is to find the point in nums1 where the largest value in
    the left half of the pivot, is smaller than the smallest value in the right
    half of the other pivot

    if this is not true because the left side of nums1 contains a value which is
    larger than the right side of nums 2, then we need to take more elements from
    nums 2 and fewer elements from nums 1

    on the opposite end if it is not true because the left side of nums2 contains
    a value which is larger than the right side of nums 1, then we need to take more
    elements from nums 1 and fewer elements from nums 2

So we can increment the pivot point which we have selected in nums1 in the manner
of binary search, where we are cutting the solution space of pivot points in half
at each iteration.

There are a couple of edge cases which we need to consider with this program
* What if the left pivot is empty, what if the right pivot is empty

An empty array merged should always be considered valid, so we choose infinitely
small and large values to satify the constraint
"""
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        n1, n2 = len(nums1), len(nums2)
        k = (n1 + n2) // 2
        l, r = 0, n1

        while l <= r:
            m1 = (r-l)//2 + l
            m2 = k - m1
            # print("left", nums1[:m1], "right", nums1[m1:])
            # print("left", nums2[:m2], "right", nums2[m2:])

            max_l1 = -float('inf') if m1 == 0 else nums1[m1-1]
            min_r1 = float('inf') if m1 == n1 else nums1[m1]
            max_l2 = -float('inf') if m2 == 0 else nums2[m2-1]
            min_r2 = float('inf') if m2 == n2 else nums2[m2]
            # print("max l1", max_l1, "min r1", min_r1, "max l2", max_l2, "min r2", min_r2)

            # if the condition is met and we have chosen the correct pivot 
            if max_l1 <= min_r2 and max_l2 <= min_r1:
                if (n1 + n2) % 2 == 0:
                    return (max(max_l1, max_l2) + min(min_r1, min_r2)) / 2
                return min(min_r1, min_r2)

            # if we are taking too much of
            # of nums1 then we want to take the pivot in
            elif max_l1 > min_r2:
                r = m1 - 1
            else:
                l = m1 + 1

