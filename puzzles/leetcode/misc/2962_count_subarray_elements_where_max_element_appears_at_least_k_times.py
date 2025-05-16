# first we determine the maximum element. then we count all the sub arrays
# which hold that element at least k times.
#
# obviously there is an o n^2 solution here where we iterate through all
# possible sub arrays.
#
# I think we can simplify the problem statement a little bit. if we filter this
# array down to
#
# [1,3,2,3,3], max = 3, k=2
# [0,1,0,1,1]
#
#
# a prefix sum also sounds useful here
# [0,1,1,2,3]
#
# observation:
# 
# 1) once we have k instances in an array we can make as many extensions as we 
#    want. so we are trying to find the smallest possible arrays where the count
#   of max elements is k
# 
# increment r until we hit k in the prefix array.
#   then increment l until nums[r] - nums[l-1] < k
#
# ok but what if we increment r and there are k elements in the
# prefix array? won't we be missing some possible valid sub arrays?
#   no we won't we will be counting all possible extensions

# nums=[1,3,2,3,3]
# k=2
# nums=[1

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_val = max(nums)
        N = len(nums)
        binarized = list(map(lambda x: int(x==max_val), nums))
        prefix_arr = [binarized[0]]
        for idx in range(1, N):
            prefix_arr.append(prefix_arr[idx-1] + binarized[idx])

        l=0
        ans=0
        for r in range(len(binarized)):    
            while True:
                if l == 0:
                    subarray_sum = prefix_arr[r]
                else:
                    subarray_sum = prefix_arr[r] - prefix_arr[l-1]
                
                if subarray_sum == k:
                    # all extension are valid so include present plus
                    # all future solns
                    ans += (N-r)
                    l += 1
                else:
                    break

        return ans