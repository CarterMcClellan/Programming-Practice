# naive implementation:
#   iterate through all possible sub arrays, 
#   then count the number of distinct elements in that sub array
#   
#   if its equal then increment

# this is o(n^2) is there a way we can do better?
#
# observation: if the sub array is valid, then its still valid when we make
# it longer
#
# idea: what if we have a map which we store the indices
# for all the elements in our array. eg.
# 
# {1: [2, 3], 5: [1], ...}
#
# then when we change a slice window, we will know what indice to include
# for it to be valid again
# 
# [1,3,1,2,2]
#
# [1,3,1,2] # pop 1, increment left but not right, because first pos 
#           # is in interval
# 
# [3,1,2]   # can't pop 3, because there is only 1 left, 
#           # therefore all sub arrays are just extensions, add them, then 
#           # break
#
# note: with this algorithm we are always incrementing from left to right
# is there ever an instance where we want left to stay fixed, and increment
# right in? I don't think so if init with the "earliest possible" sub array

class Solution:
    def countCompleteSubarrays(self, nums: list[int]) -> int:
        val_to_idx = {}
        for idx, val in enumerate(nums):
            val_to_idx[val] = val_to_idx.get(val, []) + [idx]

        # form the earliest possible sub array
        first_occ = []
        min_cnt = float('inf')
        for val, inds in val_to_idx.items():
            min_cnt = min(min_cnt, len(inds))
            first_occ.append(min(inds))

        l, r, N = min(first_occ), max(first_occ), len(nums)
        ans = 0

        while True:
            l_val = nums[l]
            inds = val_to_idx[l_val]
            # if there are multiple instances
            # of this element, then we can form multiple
            # new valid sub arrays still
            if len(inds) > 1:
                inds.pop(0)
                # we want to count all possible extensions
                # to this sub array on the rhs
                ans += (N-r)
                l += 1

                next_idx = inds[0]
                if l <= next_idx <= r:
                    # if its already in the interval, the bounds are
                    # valid and we don't have to do anything
                    continue
                else:
                    # if its outside the interval, then the right
                    # bound needs to be updated to include this point
                    r = next_idx

            # if there is exactly one instance of this element
            # left, then no more valid sub arrays can be formed without
            # it, so we can only extend to the right (count all those arrays
            # then, break)
            elif len(inds) == 1:
                n_valid_extensions = N - r
                ans += n_valid_extensions
                break

        return ans