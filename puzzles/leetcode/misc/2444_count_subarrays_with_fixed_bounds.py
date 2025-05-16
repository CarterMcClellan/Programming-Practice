# Alright so we can trivially do this in o n^2
#
# [1, 3] # nope
# [1, 3, 5] # yep
# [1, 3, 5, 2] # yep
# [1, 3, 5, 2, 7] # nope
# [3, 5] # nope
# [3, 5, 2] # nope
# [3, 5, 2, 7] # nope
# [3, 5, 2, 7, 5] # nope
# [5, 2] # nope
#
# ... (there are no more 1s so there can be no more)
#
# ok so there are a couple basic things we are looking for
#
# sub array must contain 2 specific elements
# every other element must be between those 2 elements
#
# elements outside the range represent a break. so lets first break
# our input array into pieces that way
#
# iterate through the array and find all elements which are greater than
# maxK or less than minK, then split the array into sub arrays
#
# iterate through the array and records all indices equal to maxK
# and minK
# 
# within each of these sub arrays check to see if the element
# minK and maxK are both present. otherwise discard the subarray
#
# ok so we have a subarray which contains minK and maxK and we now have to
# figure out how to properly tally each (this needs to be a constant time
# operation).
#
# so we need to define a function helper() min_idx, max_idx, array_len
# and returns the number of sub arrays we can make, lets first
# consider some examples (this feels like it should be some fairly simple
# combinatorial thing)
#
# so we have a subarray made up entirely of "valid" indices meaning
# that there inclusion does not invalidate the subarray. but we have 
# a separate issue: the exclusion of a certain min and max k, does 
# invalidate the subarray, so the number of sub arrays is not just
# some combinatorial count given given the length of the array. it 
# also has to incorporate, how small can I make this array.
#
# [2, 1, 3, 5, 2, 3, 1, 5]
#
# wait this might be a bad example for our windowing algorithm 
# because when we remove the first one our algorithm is still valid
# lets slice it down to just
#
# [2, 1, 3, 5]
# 
# i think its actually pretty simple, keep incrementing
# l, if l is greater than curr value in min_k_inds or
# max_k_inds, then pop those inds.
#
# when either of those inds arrays gets empty, then stop counting
# and move on to the next sub array.
#
# lets write up our basic implementation
class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_k_inds, max_k_inds = [], []
        subarrays = []
        l = 0
        for idx, n in enumerate(nums):
            if minK == n:
                min_k_inds.append(idx)
            if maxK == n:
                max_k_inds.append(idx)
            if not (minK <= n <= maxK):
                subarrays.append((l, idx))
                l = idx + 1

        subarrays.append((l, idx+1))
        
        # print("subarrays", subarrays)
        # print("min k inds", min_k_inds)
        # print("max k inds", max_k_inds)
        # print("---")
        ans = 0
        for (l, r) in subarrays:
            subarray = nums[l:r]
            # print("evaluating", subarray, "l=", l, "r=", r)

            while l < r:
                if len(min_k_inds) == 0 or len(max_k_inds) == 0:
                    break

                min_k_ind, max_k_ind = min_k_inds[0], max_k_inds[0]

                # if the first occurence of either
                # the min or max k is outside the sub array
                # we need to break
                if min_k_ind >= r or max_k_ind >= r:
                    break

                # if the first occurence of either min 
                # or max k, is prior to the sub array, 
                # we need to pop until we are caught up
                if l > min_k_ind:
                    min_k_inds.pop(0)
                    continue
                
                if l > max_k_ind:
                    max_k_inds.pop(0)
                    continue

                # count all of the valid subarrays
                # the first will be from l to max(min_k_ind, max_k_ind)
                # and then there will be r - max(min_k_ind, max_k_ind) more
                first_valid = max(min_k_ind, max_k_ind)
                # print("first valid", first_valid)
                # print("adding", r-first_valid)
                ans += (r - first_valid)

                l += 1

        return ans