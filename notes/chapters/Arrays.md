### Array Problem Types
If we want to find a (contiguous) sum which is precisely equal to something then its hashing problem. If we want to find a non-contiguous sum which is equal to or close to something, then its a left and right pointer problem. If we want to try and maximize the sum or the product, then its a dynamic programming problem.

#### Left and Right Pointers
```python
def left_and_right():
    i, j = 0, len(arr)
    while i < j:
        if case1:
            i += 1
        else:
            j -= 1
```
Leetcode examples
- [3 Sum Closest](!https://leetcode.com/problems/3sum-closest/discuss/466058/Python-Solution-or-Two-Pointers-with-explanations.)
- [3 Sum](!https://leetcode.com/problems/3sum/)
- [Subarray Product](!https://leetcode.com/problems/subarray-product-less-than-k/submissions/)

Note a couple of the modifications we are making. For example if we want unique combinations and we've sorted we can add additional logic to avoid duplicates etc...

#### Dynamic Programming
Think about recurrence relations. If we can express the current value as the product or sum of previous values, then it would be best to store those values. Definitely want to think of this if a sum is occuring
```python
def dp1d(N):
    A = [0] * N
    A[0] = A[1] = 1
    for i in range(1, len(A))
        A[i] = A[i-1] + A[i-2]
    return A[N]
```
- [Max Product](!https://leetcode.com/problems/maximum-product-subarray/)
- [Max Subarry Sum](!https://leetcode.com/problems/maximum-subarray/submissions/)

#### Dfs/ Back-Tracking
If we want to generate all possible arrays, it seems like it usually will involve some kind of clever recursion, where we branch according to all the possible cases. Note that these have *O(2^N)* complexity

```python
def solution():
    generated_values = []
    def dfs(val, path)
        if base_case: 
            generated_values.append([*path, val])
            return
        dfs(val-1, path)
        dfs(val+1, path)
    return generated_values
```

#### Binary Search
You've got a sorted list and you want to find to minimum (or some variant of this).
```python
def bin_search(nums):
    i = 0
    j = len(nums) - 1
    while i < j:
        m = (i + j) / 2
        if nums[m] > nums[j]:
            i = m + 1
        else:
            j = m
    return nums[j]
```
#### Hashing
These are all pretty simple, but they tend to involve a question like "how duplicates are there" or "whats the missing element"
```python
def hashing(nums):
    hash_table = {}
    for val in nums:
        if val in hash_table:
            hash_table[val] += 1
        else:
            hash_table[val] = 1
    return hash_table
```
They can also be pretty useful for summing. Suppose you are given an array, and a target value k. Hashing lets us build a table of the values in the array, then when iterating over the values in the array we can check to see if the (target - n) is in the hash set. Pretty simple. But if we observe that 
```python
sum(nums[i:j+1]) == k # is the same as
sum(nums[:j+1]) - sum(nums[:i]) == k
```
Then we can use hashing, not just to check for individual elements summing to k, but for contiguous chunks summing to k
- [Maxmimum Subarray Sum Equals k](!https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/discuss/177156/Python-solution)
- [Subarray Sum Equals K](!https://leetcode.com/problems/subarray-sum-equals-k/)

#### Bit Manipulation
Sometimes Bit Manipulation can save us some effort. XOR for example has the property of canceling out any two equivalent elements, and thus can be used to find the difference between 2 strings
```python
def find_difference(s, t):
    ret = 0
    for ch in s + t:
        # ord(ch) return an integer representing the Unicode code point of that character
        ret = ret ^ ord(ch)
    # chr(i) Return the string representing a character whose Unicode code point is the integer i
    return chr(ret)
```

#### Divide and Conquer
The classic peak finding question, given that we are trying to find. 